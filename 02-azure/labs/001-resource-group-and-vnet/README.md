# Lab 001 — Resource Group and Virtual Network

**Status:** Ready to execute — not yet validated  
**Track:** Azure / AZ-104 · **Effort:** 1.5–2 hours

## Objective
Create an isolated resource group, virtual network and two subnets using Azure CLI, inspect the configuration and remove all resources.

## Prerequisites
- Azure subscription dedicated to learning.
- Azure CLI installed and authenticated with `az login`.
- Contributor rights scoped to the sandbox.
- A budget/alert configured before deploying billable resources.

## Deploy
Check the selected subscription first:

```bash
az account show --output table
az group create --name rg-ca27-network-lab --location eastus
az network vnet create \
  --resource-group rg-ca27-network-lab \
  --name vnet-ca27-lab \
  --address-prefixes 10.20.0.0/16 \
  --subnet-name snet-app \
  --subnet-prefixes 10.20.1.0/24
az network vnet subnet create \
  --resource-group rg-ca27-network-lab \
  --vnet-name vnet-ca27-lab \
  --name snet-data \
  --address-prefixes 10.20.2.0/24
```

## Validate
```bash
az network vnet show -g rg-ca27-network-lab -n vnet-ca27-lab --output json
az network vnet subnet list -g rg-ca27-network-lab --vnet-name vnet-ca27-lab --output table
```

Expected: one VNet with `10.20.0.0/16` and two non-overlapping /24 subnets.

## Security and design notes
- CIDRs are examples; check for overlap before using them in a real environment.
- No public IP or inbound rule is created.
- A subnet alone is not a complete security boundary; apply NSGs, routing and private connectivity as required.
- Do not commit subscription IDs or tenant details.

## Cleanup
```bash
az group delete --name rg-ca27-network-lab --yes --no-wait
az group exists --name rg-ca27-network-lab
```

The final command should eventually return `false`. Document region/quota issues and why subnet boundaries alone do not provide complete isolation.