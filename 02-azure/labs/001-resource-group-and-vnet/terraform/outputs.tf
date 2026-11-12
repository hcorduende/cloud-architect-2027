output "resource_group_name" {
  description = "Created resource group."
  value       = azurerm_resource_group.lab.name
}
output "virtual_network_id" {
  description = "Resource ID of the virtual network."
  value       = azurerm_virtual_network.lab.id
}
output "subnet_ids" {
  description = "Application and data subnet IDs."
  value = {
    app  = azurerm_subnet.app.id
    data = azurerm_subnet.data.id
  }
}