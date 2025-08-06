"""Functions to manage a users shopping cart items."""

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

def add_item_to_inventory(inventory, items):
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


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    return add_item_to_inventory(current_cart, items_to_add)

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return (create_inventory(notes))

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)

    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for key in aisle_mapping.keys():
        if key in cart.keys():
            cart[key] = [cart[key], aisle_mapping[key][0], aisle_mapping[key][1]]

    return dict(sorted(cart.items(), reverse=True))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key in fulfillment_cart.keys():
        quantity = store_inventory[key][0]

        if key in store_inventory.keys():
            quantity -= fulfillment_cart[key][0]
        
        if quantity <= 0: quantity = 'Out of Stock'
        
        store_inventory[key][0] = quantity

    return store_inventory