variable "resource_group_name" {
  description = "Name of the isolated learning resource group."
  type        = string
  default     = "rg-ca27-network-lab"
}
variable "location" {
  description = "Azure region for the learning resources."
  type        = string
  default     = "eastus"
}
variable "virtual_network_name" {
  description = "Name of the lab virtual network."
  type        = string
  default     = "vnet-ca27-lab"
}
variable "vnet_address_space" {
  description = "VNet CIDR; check overlap before real use."
  type        = string
  default     = "10.20.0.0/16"
}
variable "app_subnet_prefix" {
  description = "Application subnet CIDR."
  type        = string
  default     = "10.20.1.0/24"
}
variable "data_subnet_prefix" {
  description = "Data subnet CIDR."
  type        = string
  default     = "10.20.2.0/24"
}