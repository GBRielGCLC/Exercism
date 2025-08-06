"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    dict_array = []

    for item in items:
        counter = items.count(item)
        index_tuple = tuple([item, counter])

        if index_tuple not in dict_array: dict_array.append(index_tuple)

    return dict(dict_array)

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    items_dict = create_inventory(items)

    for key, value in items_dict.items():
        if key in inventory.keys():
            inventory[key] += value
        else:
            inventory[key] = value

    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory.keys() and inventory[item] > 0:
            inventory[item] -= 1

    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory.keys(): inventory.pop(item)

    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    inventory_array = []

    for key, value in inventory.items():
        if value > 0:
            inventory_array.append(tuple([key, value]))

    return inventory_array