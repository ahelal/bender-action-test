provider "azurerm" {
  features {}
}


data "azurerm_resource_group" "rg"{
  name     = "bender_test_rg"
}
// crreate random string prefix
resource "random_string" "random" {
  length  = 5
  special = false
  upper   = false
}

resource "azurerm_public_ip" "example" {
  name                = "example-pip-${random_string.random.result}"
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location
  allocation_method   = "Static"
  sku                 = "Basic"
  sku_tier           = "Global"

}