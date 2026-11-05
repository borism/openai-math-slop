/-- `#dump_local P "out.tsv"`: fingerprints of the constants declared in the current file whose
name starts with `P`. Same columns as `#dump_prefix`, with module `<local>`. -/
elab "#dump_local " p:ident out:str : command => do
  let env ← getEnv
  let mut lines : Array String := #[]
  for (n, ci) in env.constants.map₂.toList do
    unless p.getId.isPrefixOf n do continue
    lines := lines.push s!"{n}\t<local>\t{fingerprint ci}"
  IO.FS.writeFile out.getString (String.intercalate "\n" lines.toList ++ "\n")
  logInfo m!"{lines.size} constants written"
