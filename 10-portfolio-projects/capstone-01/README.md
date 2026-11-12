# Capstone 01 — Secure Multi-Tier Cloud Platform

**Status:** Planned  
**Primary skills:** Cloud architecture, Azure/AWS, Terraform, cloud security, observability and SRE

## Problem statement
Design and build a small, secure, observable application platform that can be deployed repeatedly in a personal sandbox. The implementation must demonstrate architecture decisions and operational readiness, not just successful provisioning.

## Proposed scope
- Network segmentation with explicit ingress and egress paths.
- Private application/data tiers where supported by the selected design.
- Least-privilege workload identity and managed secrets.
- Infrastructure as code with reviewed plans.
- Centralized logs, metrics, actionable alerts and a basic runbook.
- Backup/recovery approach with a documented test.
- Cost estimate, budget controls and teardown process.

## Deliverables
1. Requirements, assumptions and non-functional requirements.
2. Architecture diagram and at least two ADRs.
3. Threat model and security control mapping.
4. Versioned Terraform implementation.
5. Deployment/validation guide and automated checks.
6. Observability dashboard or sanitized evidence.
7. Recovery/rollback test and operational runbook.
8. Cost breakdown, cleanup evidence and retrospective.

## Acceptance criteria
- A reviewer can understand the design and trade-offs.
- Deployment is reproducible from documented prerequisites.
- No secrets or production/employer information are present.
- Security controls are testable and evidence is included.
- Cost drivers and teardown steps are explicit.
- Known limitations and future improvements are documented.

## Design decision to make
Select one cloud provider for the first implementation based on the skills and exam phase active at the time. Do not attempt a dual-cloud deployment until the single-cloud baseline is stable.