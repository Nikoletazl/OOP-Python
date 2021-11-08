class Shop:
    _small_shop_capacity = 10

    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}

    # @staticmethod
    # def _can_add_item(items_count, capacity):
    #     return items_count < capacity - 1

    def _can_add_item(self):
        return self.items_count < self.capacity - 1

    def add_item(self, item):
        if not self._can_add_item():
            return f"Not enough capacity in the shop"
        if item not in self.items:
            self.items[item] = 0

        self.items[item] += 1
        self.items_count += 1
        return f"{item} added to the shop"

    def remove_item(self, item, amount):
        if not self._can_remove_amount_of_item(item, amount):
            return f"Cannot remove {amount} {item}"
        self.items[item] -= amount
        self.items_count -= amount
        return f"{amount} {item} removed from the shop"

    def _can_remove_amount_of_item(self, item, amount):
        return item in self.items and self.items[item] >= amount

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, cls._small_shop_capacity)


import unittest

class ShopTests(unittest.TestCase):
    def setUp(self):
        self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)

    def test_add_item_success(self):
        result = self.fresh_shop.add_item("Bananas")
        self.assertEqual(self.fresh_shop.items["Bananas"], 1)
        self.assertEqual(result, "Bananas added to the shop")

    def test_remove_item_success(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Bananas", 1)
        self.assertEqual(result, "1 Bananas removed from the shop")

    def test_remove_item_unsuccessful(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Tomatoes", 2)
        self.assertEqual(result, "Cannot remove 2 Tomatoes")

    def test_repr(self):
        self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")


if __name__ == "__main__":
    unittest.main()