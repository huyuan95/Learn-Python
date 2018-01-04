stuff = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for inv in addedItems:
        if inv in inventory.keys():
            inventory[inv] += 1
        else:
            inventory[inv] = 1
    return inventory

inv = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
