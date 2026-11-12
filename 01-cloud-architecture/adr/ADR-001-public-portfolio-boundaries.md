# ADR-001: Keep the public portfolio isolated from employer environments

- **Status:** Accepted
- **Date:** 2026-11-12
- **Decision owners:** Portfolio owner

## Context
The portfolio demonstrates infrastructure, cloud security and platform engineering skills. Practical workplace experience may inform learning goals, but real employer environments can contain sensitive topology, identities, security controls, operational data and business information.

## Decision
All public examples will use synthetic names, sample CIDRs, disposable sandbox accounts and generic architecture. No employer credentials, identifiers, screenshots, internal runbooks, customer data, proprietary diagrams or confidential configurations will be committed.

## Options considered
1. Publish sanitized reproductions of workplace systems — rejected because sanitization can miss sensitive details and publication rights may be unclear.
2. Build equivalent generic labs in isolated personal sandboxes — accepted; demonstrates transferable skills without exposing employer information.

## Consequences
- Portfolio evidence is safe to share and reproduce.
- Some operational context must be generalized.
- Workplace learning requires separate authorization and must not be copied into this repository.
- Every lab documents its environment and data limitations.

## Follow-up
Review this boundary before adding screenshots, logs, architecture diagrams or case studies.