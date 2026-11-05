#!/usr/bin/env bash
# Resume of lanes.sh after the container restart (~03:25 UTC Nov 5): lane1 batches 57..87; lane2 covrun + A0.
# Identical commands and comparisons to lanes.sh; partial outputs of the interrupted invocations are deleted first.
M=$(cd "$1" && pwd); R=$(cd "$(dirname "$0")" && pwd)/run_stage.sh
D=$M/verification/saved-run/execution/data
RES=$M/verification/saved-run/execution/results
B=$M/build
export LC_ALL=C
lane1() {
  cd "$M/lane1"; rm -f batches/f57.bin batches/bad57.bin C.batch57.*
  for j in $(seq 57 87); do
    cp "$D/batches/f$j.bin" "batches/f$j.bin"
    bash "$R" "C.batch$j" 1800 "$B/crun" 12 4 1 .042 1 1 5000000 0 1 "batches/bad$j.bin" "batches/f$j.bin" >/dev/null
    if cmp -s "batches/bad$j.bin" "$D/batches/bad$j.bin"; then b=IDENTICAL; else b=DIFFERENT; fi
    if diff -q <(sed -E 's/ avg bins[0-9.]* balls[0-9.]* time [0-9.]*//; s/ time [0-9.]*$//' "C.batch$j.stdout") "$RES/C.batch$j.txt" >/dev/null; then s=MATCH; else s=MISMATCH; fi
    echo "C.batch$j $(cat C.batch$j.meta | cut -d' ' -f2-) bad=$b stdout=$s" >> "$M/lane1.summary"
    rm -f "batches/f$j.bin"
  done
  echo LANE1_DONE >> "$M/lane1.summary"
}
lane2() {
  cd "$M/lane2"; rm -f centers.txt covrun.*
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
