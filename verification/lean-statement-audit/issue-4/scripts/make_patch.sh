#!/usr/bin/env bash
# make_patch.sh ORIG NEW_OUT PATCH_OUT : relabel "(Lean)" -> "(Lean: partial)" for the 21 families of issue 4.
set -e
orig=$1; new=$2; out=$3
cp "$orig" "$new"
for n in 009 033 126 152 159 191 194 206 222 229 230 260 261 266 269 272 280 281 323 367 371; do
  c=$(grep -c "(\[Lean\](lean/docs/$n.md))" "$new")
  [ "$c" = 1 ] || { echo "family $n: expected 1 link, found $c" >&2; exit 1; }
  sed -i "s|(\[Lean\](lean/docs/$n.md))|([Lean: partial](lean/docs/$n.md))|" "$new"
done
diff -u --label a/CONTENTS.md --label b/CONTENTS.md "$orig" "$new" > "$out" || true
