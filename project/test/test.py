from unittest import TestCase, main
from project.pet_shop import PetShop


class Test(TestCase):
    def setUp(self) -> None:
        self.petshop = PetShop("Shop")

    def test_initialization(self):
        self.assertEqual("Shop", self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_add_food_raises_when_quantity_is_equal_or_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            self.petshop.add_food("test", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.petshop.add_food("test", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_if_name_not_food(self):
        self.petshop.food = {}
        result = self.petshop.add_food("test", 1)

        self.assertEqual({"test": 1}, self.petshop.food)
        self.assertEqual(f"Successfully added 1.00 grams of test.", result)

        self.petshop.food = {"test2": 2}
        result = self.petshop.add_food("test3", 5)

        self.assertEqual({"test2": 2, "test3": 5}, self.petshop.food)
        self.assertEqual(f"Successfully added 5.00 grams of test3.", result)

    def test_add_pet_successfully(self):
        self.petshop.pets = []
        result = self.petshop.add_pet("dog")

        self.assertEqual(["dog"], self.petshop.pets)
        self.assertEqual("Successfully added dog.", result)

        self.petshop.pets = ["cat"]
        result = self.petshop.add_pet("chicken")

        self.assertEqual(["cat", "chicken"], self.petshop.pets)
        self.assertEqual("Successfully added chicken.", result)

    def test_add_pet_when_exists(self):
        self.petshop.pets = ["cat"]
        with self.assertRaises(Exception) as context:
            self.petshop.add_pet("cat")

        self.assertEqual(["cat"], self.petshop.pets)
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_feed_pet_raises_when_pet_not_in_pets(self):
        self.petshop.pets = []
        self.petshop.food = {}
        with self.assertRaises(Exception) as context:
            self.petshop.feed_pet("lunch", "dog")

        self.assertEqual("Please insert a valid pet name", str(context.exception))
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_feet_pet_when_food_not_in_foods(self):
        self.petshop.pets = ["dog"]
        self.petshop.food = {}
        result = self.petshop.feed_pet("lunch", "dog")

        self.assertEqual({}, self.petshop.food)
        self.assertEqual(["dog"], self.petshop.pets)
        self.assertEqual('You do not have lunch', result)

        self.petshop.pets = ["dog", "cat"]
        self.petshop.food = {"chicken": 2}
        result = self.petshop.feed_pet("chrisp", "cat")

        self.assertEqual({"chicken": 2}, self.petshop.food)
        self.assertEqual(["dog", "cat"], self.petshop.pets)
        self.assertEqual('You do not have chrisp', result)

    def test_feed_pet_when_food_food_is_less_than_100(self):
        self.petshop.pets = ["dog"]
        self.petshop.food = {"chicken": 49}
        result = self.petshop.feed_pet("chicken", "dog")

        self.assertEqual({"chicken": 1049.00}, self.petshop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_successfully(self):
        self.petshop.pets = ["dog"]
        self.petshop.food = {"chicken": 101}
        result = self.petshop.feed_pet("chicken", "dog")

        self.assertEqual({"chicken": 1}, self.petshop.food)
        self.assertEqual("dog was successfully fed", result)

    def test_repr(self):
        self.petshop.pets = ["cat", "dog", "chicken"]
        self.assertEqual(f'Shop Shop:\nPets: cat, dog, chicken', repr(self.petshop))


if __name__ == "__main__":
    main()