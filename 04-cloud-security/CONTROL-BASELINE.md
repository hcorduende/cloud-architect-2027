# Cloud Security Control Baseline

Use this as a design-review checklist, not as a claim of regulatory compliance.

| Domain | Baseline question | Example evidence |
|---|---|---|
| Identity | Are human and workload permissions least-privilege? | RBAC/IAM policy review |
| Authentication | Is MFA/federation used for privileged human access? | Identity configuration evidence |
| Secrets | Are credentials kept out of code, images and logs? | Secret scan and identity design |
| Network | Are ingress, egress and east-west paths explicit? | Network diagram and rule review |
| Data | Are classification, encryption and retention addressed? | Data-flow and key-management notes |
| Compute | Are images, hosts and workloads patched and hardened? | Image scan and patch evidence |
| Logging | Are security-relevant events captured and retained? | Log source inventory and sample alert |
| Detection | Are actionable alerts tied to response procedures? | Alert test and runbook |
| Recovery | Are backups protected and restores tested? | Restore-test record |
| Governance | Are policies, tags, ownership and budgets defined? | Policy and cost-control evidence |
| Supply chain | Are dependencies, actions and artifacts reviewed? | Dependency updates and CI results |

For each applicable control, record the scope, owner, implementation, test result, known exception and residual risk. A checked box without evidence is not proof.