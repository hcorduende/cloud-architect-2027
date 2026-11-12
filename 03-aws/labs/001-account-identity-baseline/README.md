# AWS Lab 001 — Account Identity Baseline

**Status:** Ready to execute — read-only checks  
**Estimated effort:** 45–60 minutes  
**Cost:** No AWS resources are created by the commands below.

## Objective
Verify which AWS identity and account context the CLI is using before attempting any deployment. This is the first safety gate for all later AWS labs.

## Prerequisites
- AWS CLI v2 installed.
- Access to a personal learning account or explicitly authorized sandbox.
- MFA enabled for the human identity.
- Do not use employer credentials for this portfolio.

## Step 1 — Confirm the active CLI context

```bash
aws --version
aws configure list
aws sts get-caller-identity
```

Review the account and ARN locally. Do not paste unredacted account IDs, principal names or credential-path details into public issues or screenshots.

## Step 2 — Inspect account alias (optional)

```bash
aws iam list-account-aliases
```

This command requires `iam:ListAccountAliases`. An account may have no alias configured.

## Step 3 — Review IAM account summary (optional)

```bash
aws iam get-account-summary
```

This command requires `iam:GetAccountSummary`. Treat the returned account metadata as internal to your own lab notes.

## Acceptance criteria
- The active identity is the intended learning identity.
- The account is the personal sandbox, not an employer or production account.
- MFA and a budget/alert are in place before any resource creation.
- You can explain the distinction between an IAM user, role and federated identity.

## Security notes
- `sts:GetCallerIdentity` is a read-only identity check.
- Do not create access keys for routine human use.
- Prefer federation/role assumption and short-lived credentials.
- Never store credentials in this repository, shell scripts or screenshots.

## Cleanup
No cloud resources are created. Sign out or remove temporary credentials from the local environment when finished, following the provider's documented credential process.

## Reflection
Record which identity type you used, what permissions were required and how you verified you were in the correct account. Redact identifiers.