provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "rg"{
  name     = "bender_test_rg"
}

resource "random_string" "random" {
  length  = 5
  special = false
  upper   = false
}

variable "postgresql_host" {
  type = string
  default = "psqlbender"
}

resource "azurerm_postgresql_flexible_server" "example" {
  name                          = "${var.postgresql_host}-${random_string.random.result}"
  resource_group_name           = data.azurerm_resource_group.rg.name
  location                      = data.azurerm_resource_group.rg.location
  version                       = "12"
  public_network_access_enabled = true
  administrator_login           = "psqladmin"
  administrator_password        = "${var.postgresql_host}${random_string.random.result}123"
  zone                          = "1"
  storage_mb   = 32768
  storage_tier = "P30"
  sku_name   = "GP_Standard_D4s_v3"
}
