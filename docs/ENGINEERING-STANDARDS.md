# Engineering Standards

## Documentation
Every lab includes context, objectives, prerequisites, architecture, deployment, validation, cleanup, security, cost and troubleshooting.

## Infrastructure as Code
- Pin provider versions and document tested versions.
- Use variables for environment-specific settings.
- Treat state as sensitive; never commit state files or real variable values.
- Run `terraform fmt -check` and `terraform validate`.
- Review plans before apply; document destroy steps.

## Python
- State the Python version tested.
- Use a virtual environment, type hints and tests.
- Never hardcode credentials. Validate input and handle failures explicitly.

## Kubernetes
- Explain resource scope and impact before applying manifests.
- Set resource requests/limits where appropriate.
- Use namespaces, RBAC and network policies in secure examples.
- Keep secrets out of committed manifests.
- Include rollout, health-check and rollback validation.

## Architecture reviews
Assess security, reliability, performance, cost, operational excellence and sustainability. State assumptions and trade-offs.