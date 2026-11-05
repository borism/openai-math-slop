#!/usr/bin/env bash
# Two CPU lanes reproducing the MUB d=6 saved run from the shipped sources and comparing
# every output byte-for-byte with the shipped data.  Usage: bash lanes.sh <mubdir>
M=$(cd "$1" && pwd); R=$(cd "$(dirname "$0")" && pwd)/run_stage.sh
D=$M/verification/saved-run/execution/data
RES=$M/verification/saved-run/execution/results
B=$M/build
export LC_ALL=C

lane1() {  # initial C on every shipped batch
  mkdir -p "$M/lane1/batches" && cd "$M/lane1"
  for j in $(seq 0 87); do
    cp "$D/batches/f$j.bin" "batches/f$j.bin"
    bash "$R" "C.batch$j" 1800 "$B/crun" 12 4 1 .042 1 1 5000000 0 1 "batches/bad$j.bin" "batches/f$j.bin" >/dev/null
    if cmp -s "batches/bad$j.bin" "$D/batches/bad$j.bin"; then b=IDENTICAL; else b=DIFFERENT; fi
    if diff -q <(sed -E 's/ avg bins[0-9.]* balls[0-9.]* time [0-9.]*//; s/ time [0-9.]*$//' "C.batch$j.stdout") "$RES/C.batch$j.txt" >/dev/null; then s=MATCH; else s=MISMATCH; fi
    echo "C.batch$j $(cat C.batch$j.meta | cut -d' ' -f2-) bad=$b stdout=$s" >> "$M/lane1.summary"
    rm -f "batches/f$j.bin"
  done
  echo LANE1_DONE >> "$M/lane1.summary"
}

lane2() {  # B mid, B fine (with batching), cover, A0
  mkdir -p "$M/lane2/batches" && cd "$M/lane2"
  cp "$D"/coarse{0,1,2,3}.bin .
  bash "$R" Bmid 7200 "$B/brun" .07 .013 mid.bin midbad.bin - coarse0.bin coarse1.bin coarse2.bin coarse3.bin >/dev/null
  for f in mid.bin midbad.bin; do cmp -s $f "$D/$f" && echo "$f IDENTICAL" || echo "$f DIFFERENT"; done >> "$M/lane2.summary"
  diff -q <(sed -E 's/ time [0-9.]*//' Bmid.stdout) "$RES/Bmid.txt" >/dev/null && echo "Bmid stdout MATCH" >> "$M/lane2.summary" || echo "Bmid stdout MISMATCH" >> "$M/lane2.summary"
  cat Bmid.meta >> "$M/lane2.summary"
  cp "$D/mid.bin" mid.shipped.bin
  bash "$R" Bfine 7200 "$B/brun" .016 .005 fine.bin finebad.bin batches/f mid.shipped.bin >/dev/null
  for f in fine.bin finebad.bin batches/fdone.txt; do cmp -s $f "$D/$f" && echo "$f IDENTICAL" || echo "$f DIFFERENT"; done >> "$M/lane2.summary"
  nb=0; for j in $(seq 0 87); do cmp -s batches/f$j.bin "$D/batches/f$j.bin" || nb=$((nb+1)); done
  echo "batches differing: $nb of 88" >> "$M/lane2.summary"
  diff -q <(sed -E 's/ time [0-9.]*//' Bfine.stdout) "$RES/Bfine.txt" >/dev/null && echo "Bfine stdout MATCH" >> "$M/lane2.summary" || echo "Bfine stdout MISMATCH" >> "$M/lane2.summary"
  cat Bfine.meta >> "$M/lane2.summary"
  bash "$R" covrun 7200 "$B/covrun" centers.txt >/dev/null
  cmp -s centers.txt "$D/centers.txt" && echo "centers.txt IDENTICAL" >> "$M/lane2.summary" || echo "centers.txt DIFFERENT" >> "$M/lane2.summary"
  cat covrun.meta >> "$M/lane2.summary"
  cp "$D/centers.txt" centers.shipped.txt
  bash "$R" A0 10800 "$B/arun" centers.shipped.txt 0 4 coarse0.rerun.bin bad0.rerun.txt >/dev/null
  cmp -s coarse0.rerun.bin "$D/coarse0.bin" && echo "coarse0.bin IDENTICAL" >> "$M/lane2.summary" || echo "coarse0.bin DIFFERENT" >> "$M/lane2.summary"
  cmp -s bad0.rerun.txt "$D/bad0.txt" && echo "bad0.txt IDENTICAL" >> "$M/lane2.summary" || echo "bad0.txt DIFFERENT" >> "$M/lane2.summary"
  cat A0.meta >> "$M/lane2.summary"
  echo LANE2_DONE >> "$M/lane2.summary"
}

lane1 & lane2 & wait
