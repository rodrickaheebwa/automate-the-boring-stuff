stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    itemTotal = 0
    for i,j in inventory.items():
        print(str(j) + ' ' + i)
        itemTotal += j
    print('Total number of items: ' + str(itemTotal))

#displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1

#addToInventory(stuff, dragonLoot)
#displayInventory(stuff)
