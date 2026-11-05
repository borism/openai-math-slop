#!/usr/bin/env python3
"""Validate a formalization.yaml against the v0.4 JSON schema (draft-07).
Usage: python3 -I validate_yaml.py SCHEMA_v0.4.json FILE.yaml"""
import json, sys
import yaml, jsonschema
schema = json.load(open(sys.argv[1]))
doc = yaml.safe_load(open(sys.argv[2], encoding="utf-8"))
errs = sorted(jsonschema.Draft7Validator(schema).iter_errors(doc), key=lambda e: list(e.path))
for e in errs[:20]:
    print("ERROR", list(e.path), e.message[:200])
srcs = doc["sources"]
tagged = [s for s in srcs if "relationship" in s]
print(f"sources={len(srcs)} annotated={len(tagged)} errors={len(errs)}")
for s in tagged:
    print(" ", s["relationship"], "|", s["title"])
