#!/usr/bin/env bash
# run_stage.sh NAME TIMEOUT_SECONDS CMD...  (run inside the rerun directory)
# Runs CMD with LC_ALL=C, records stdout, stderr, exit code, wall time and peak RSS (VmHWM).
name=$1; to=$2; shift 2
export LC_ALL=C
start=$(date +%s.%N)
timeout "$to" "$@" > "$name.stdout" 2> "$name.stderr" &
pid=$!
peak=0
while kill -0 "$pid" 2>/dev/null; do
  for c in $(pgrep -P "$pid") "$pid"; do
    h=$(awk '/VmHWM/{print $2}' /proc/$c/status 2>/dev/null)
    [ -n "$h" ] && [ "$h" -gt "$peak" ] && peak=$h
  done
  sleep 2
done
wait "$pid"; rc=$?
end=$(date +%s.%N)
printf 'name=%s exit=%s wall=%.1fs peakRSS_kB=%s\n' "$name" "$rc" "$(echo "$end - $start" | bc)" "$peak" | tee "$name.meta"
