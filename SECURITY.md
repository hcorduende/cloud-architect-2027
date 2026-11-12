# Security Policy

This is a public educational repository. Never add real credentials, production data, customer information or employer-confidential material.

For a vulnerability in this repository, do not publish exploit details in an issue. Contact the repository owner privately through GitHub's security reporting mechanism.

## Required safeguards
- Use least-privilege identities and short-lived credentials.
- Prefer managed identities/OIDC and cloud secret managers over static secrets.
- Keep state files and local variable files out of version control.
- Review infrastructure plans before applying changes.
- Destroy paid lab resources after validation.
- Use synthetic examples and sanitized evidence.