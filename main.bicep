param storageAccountName string = 'staccnmadsfi672345hsd'

module stacc 'storageAccount.bicep' = [for i in range(0, 1): {
  name: 'stacc_${i}'
  scope: resourceGroup()
  params: {
    storageAccountName: storageAccountName
  }
}]
