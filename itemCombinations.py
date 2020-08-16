import pandas

"""This program determines all item combinations based on given item components for Teamfight Tactics"""

#key numbers are based on rows in itemTable.csv, not by a list index
ITEM_KEY = {"Belt":0, "Bow":1, "Cloak":2, "Glove":3, "Rod":4, "Sword":5, "Tear":6, "Vest":7, "Spatula":8}

def makeCompletedItems(itemList):
    """
    This function takes a list of item components and returns a list of possible completed items.

    Args:
        itemList (list): list of item components

    Returns:
        completedItems (list): list of completed items
    """

    #initialize a list to contain item pairs
    itemPairList = []

    #iterate through list of item components and create each combination (pair)
    for i in range(len(itemList)):
        counter = 1
        while i + counter < len(itemList):
            itemPairList.append([itemList[i],itemList[i + counter]])
            counter += 1

    #initialize a list to hold the list of completed items
    completedItems = []

    #use pandas to initalize a table that will be used to generate completed items based on item pairs
    itemTable = pandas.read_csv("itemTable.csv")

    #i is the item pair
    for i in itemPairList:
        item1 = i[0]
        item2 = i[1]
        item2 = ITEM_KEY[item2]
        completedItems.append(itemTable[item1][item2])

    return completedItems

def cleanItemString(itemString):

    itemString = itemString.split(",")
    itemString = [i.replace(i, i.lstrip()) for i in itemString]
    itemString = [i.replace(i, i.rstrip()) for i in itemString]
    for i in itemString:
        if i.isalpha() != True:
            itemString.remove(i)

    return itemString

def removeDuplicateItems(itemString):
    itemString = list(set(itemString))
    
    return itemString
