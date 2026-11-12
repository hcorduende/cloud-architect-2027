# Python Lab 001 — CIDR Network Plan Validator

**Status:** Implemented; local execution and CI validation pending · **Effort:** 1–2 hours

## Goal
Build a small utility that catches overlapping IPv4/IPv6 ranges before creating cloud VNets or VPCs.

## Run
```bash
python --version
python -m unittest -v
python network_plan.py 10.20.0.0/16 10.20.1.0/24 10.30.0.0/16
python network_plan.py --strict 10.20.1.0/24 10.20.1.128/25
```

The final command should return exit code 1 because the ranges overlap. Invalid CIDR input returns exit code 2.

## Concepts
Functions, type hints, `ipaddress`, collections, exceptions, CLI arguments, exit codes and unit testing with `unittest`.

## Limitations
This checks overlap only. It does not know provider-reserved ranges, routing, peering/transit constraints or existing cloud networks. Verify address plans in the target environment.