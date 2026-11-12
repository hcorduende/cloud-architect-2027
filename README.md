# Cloud Architect 2027 — Learning & Engineering Portfolio

A hands-on, evidence-driven program to grow into cloud architecture across **Azure, AWS, cloud security, platform engineering, Kubernetes, automation and AI engineering**.

> **Cadence:** 12 focused hours/week · **Start:** 1 December 2026 · **Status:** Building

## North star
Design, implement, secure and operate cloud platforms. Demonstrate architectural judgment through reproducible labs, infrastructure as code, automation, diagrams, decision records and end-to-end projects.

This repository is the public technical evidence. Private career planning and task execution stay in the companion Notion and Trello workspaces.

## Learning tracks

| Track | Focus | Evidence |
|---|---|---|
| Cloud architecture | Well-Architected design, trade-offs, resilience and cost | ADRs, diagrams, case studies |
| Azure | Administration, governance, networking and monitoring | CLI and Terraform labs |
| AWS | IAM, VPC, compute, storage and observability | Secure AWS labs |
| Cloud security | Identity, posture, network, data and detection | Threat models and control notes |
| DevOps & platform | Terraform, CI/CD and automation | IaC modules and pipelines |
| Kubernetes / CKA | Workloads, networking, storage, RBAC and troubleshooting | Versioned hands-on labs |
| Python | Automation, APIs, testing and tools | Tested utilities |
| AI engineering | Grounded apps, agents, evaluation and safety | Prototypes and architecture notes |
| Observability / SRE | SLIs, SLOs, telemetry and incident response | Dashboards and runbooks |

## Certification direction
- **AZ-104:** target exam window — late December 2026.
- **AWS Certified AI Practitioner:** target — January 2027.
- **Microsoft AI-103, CKA and cloud-security certification(s):** mandatory program outcomes; sequence and exam windows are managed in the learning roadmap.
- Architecture, AWS and Terraform credentials will support demonstrated skills, not replace hands-on evidence.

Revalidate exam names, versions and objectives with the issuing vendor before booking.

## Repository map
| Path | Purpose |
|---|---|
| `01-cloud-architecture/` | Patterns, diagrams, ADRs and case studies |
| `02-azure/` | Azure administration and architecture labs |
| `03-aws/` | AWS labs, starting with account safety and IAM |
| `04-cloud-security/` | Security principles, threat models and controls |
| `05-devops-platform/` | Terraform, CI/CD and platform engineering |
| `06-kubernetes-cka/` | Kubernetes administration and CKA preparation |
| `07-python-engineering/` | Python fundamentals and cloud automation |
| `08-ai-engineering/` | AI applications, retrieval, agents and evaluation |
| `09-observability-sre/` | Monitoring, SRE, alerting and incident response |
| `10-portfolio-projects/` | End-to-end capstones |
| `11-runbooks/` | Operational procedures |
| `12-learning-journal/` | Weekly evidence and reflections |

## First milestones
1. Establish a safe development workflow and complete the first Azure networking lab.
2. Learn Python by shipping a tested CIDR/subnet-overlap validator.
3. Reproduce the Azure network lab with Terraform and validate its plan.
4. Add identity, security, monitoring and cost controls.
5. Progress through AWS, Kubernetes and capstones in dependency order.

## Engineering rules
- Every lab records prerequisites, tested versions, architecture, validation, security, cost and cleanup.
- Use sandbox accounts and least-privilege permissions. Review changes before applying them.
- Never commit secrets, private keys, state files, customer data or employer-confidential information.
- Use synthetic examples and generic architectures in this public portfolio.
- A topic is complete only with reproducible evidence: code, tests, sanitized output, diagram or documented decision.

## Start here
- [Engineering standards](docs/ENGINEERING-STANDARDS.md)
- [Contribution workflow](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Lab template](docs/templates/LAB-TEMPLATE.md)
- [ADR template](docs/templates/ADR-TEMPLATE.md)
- [Azure Lab 001](02-azure/labs/001-resource-group-and-vnet/README.md)

Planned work is marked as planned; no lab is called validated until it has actually been executed.

*Educational portfolio. Review and adapt all examples before use in real environments.*