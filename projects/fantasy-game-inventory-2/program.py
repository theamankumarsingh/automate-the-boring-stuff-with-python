def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print(v,k)
        item_total+=v
    print("Total number of items: "+str(item_total))
def addToInventory(inventory,addedItems):
    for x in addedItems:
        try:
            inventory[x]+=1
        except:
            inventory[x]=1
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)