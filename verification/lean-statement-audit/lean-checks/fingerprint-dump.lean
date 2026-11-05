open Lean Elab Command

def fingerprint (ci : ConstantInfo) : String :=
  let kind := match ci with
    | .defnInfo _ => "def" | .thmInfo _ => "thm" | .axiomInfo _ => "axiom"
    | .opaqueInfo _ => "opaque" | .quotInfo _ => "quot" | .inductInfo _ => "induct"
    | .ctorInfo _ => "ctor" | .recInfo _ => "rec"
  let v := match ci with
    | .defnInfo d => toString d.value.hash
    | .opaqueInfo d => toString d.value.hash
    | _ => "-"
  s!"{kind}\t{ci.levelParams}\t{ci.type.hash}\t{v}"

/-- `#dump_prefix P "out.tsv"`: fingerprints of the constants declared in every imported
module whose name starts with `P`. Columns: name, module, kind, universe params,
hash of type, hash of value (definitions only). -/
elab "#dump_prefix " p:ident out:str : command => do
  let env ← getEnv
  let mut lines : Array String := #[]
  for i in [0:env.header.moduleNames.size] do
    let mn := env.header.moduleNames[i]!
    unless p.getId.isPrefixOf mn do continue
    for n in env.header.moduleData[i]!.constNames do
      if let some ci := env.find? n then
        lines := lines.push s!"{n}\t{mn}\t{fingerprint ci}"
  IO.FS.writeFile out.getString (String.intercalate "\n" lines.toList ++ "\n")
  logInfo m!"{lines.size} constants written"
