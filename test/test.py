from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTests(TestCase):
    VALID_NAME = "Pet Shop"
    FOOD_NAME = "test food"
    PET_NAME = "Petsy"

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.VALID_NAME)

    def test_init_expect_to_set_correct_values(self):
        ps = PetShop(self.VALID_NAME)
        self.assertEqual(self.VALID_NAME, self.pet_shop.name)
        self.assertListEqual([], self.pet_shop.pets)
        self.assertDictEqual({}, self.pet_shop.food)

    def test_add_food__when_quantity_is_negative__expect_to_throw(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food(self.FOOD_NAME, -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food__when_name_not_in_pet_shop_expect_to_add_it(self):
        self.pet_shop.add_food(self.FOOD_NAME, 10)
        self.pet_shop.add_food("another", 15)

        self.assertEqual(10, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual(15, self.pet_shop.food["another"])

    def test_add_food__when_food_in_pet_shop_expect_to_increase_by_quantity(self):
        self.pet_shop.add_food(self.FOOD_NAME, 10)
        self.pet_shop.add_food(self.FOOD_NAME, 15)
        self.pet_shop.add_food("another", 15)

        self.assertEqual(25, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual(15, self.pet_shop.food["another"])

    def test_add_food_when_food_not_in_petshop__expect_correct_message(self):
        quantity = 10
        result = self.pet_shop.add_food(self.FOOD_NAME, quantity)

        self.assertEqual(f"Successfully added {quantity:.2f} grams of {self.FOOD_NAME}.", result)

    def test_add_pet_when_pet_not_in_petshop_expect_to_add_it(self):
        result = self.pet_shop.add_pet(self.PET_NAME)

        self.assertListEqual([self.PET_NAME], self.pet_shop.pets)
        self.assertEqual(f"Successfully added {self.PET_NAME}.", result)

    def test_add_pet_when_pet_in_petshop_expect_to_raise(self):
        result = self.pet_shop.add_pet(self.PET_NAME)

        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet(self.PET_NAME)

        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_feed_pet_when_pet_not_in_petshop_expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)

        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet_when_food_not_in_petshop_expect_to_return_correct_message(self):
        self.pet_shop.add_pet(self.PET_NAME)

        result = self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)

        self.assertEqual(f"You do not have {self.FOOD_NAME}", result)

    def test_feed_pet_when_food_is_99_expect_to_increase_by_1000_and_correct_message(self):
        self.pet_shop.add_pet(self.PET_NAME)
        self.pet_shop.add_food(self.FOOD_NAME, 99)

        result = self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)

        self.assertEqual(99 + 1000, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_when_food_is_101_expect_to_decrease_by_100_and_correct_message(self):
        self.pet_shop.add_pet(self.PET_NAME)
        self.pet_shop.add_food(self.FOOD_NAME, 101)

        result = self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)

        self.assertEqual(101 - 100, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual\
            (f"{self.PET_NAME} was successfully fed", result)

    def test_repr_when_no_pets_expect_correct_result(self):
        expected = f"""Shop {self.VALID_NAME}:
Pets: """

        actual = repr(self.pet_shop)

        self.assertEqual(expected, actual)

    def test_repr_when_single_pet_expect_correct_result(self):
        self.pet_shop.add_pet(self.PET_NAME)
        expected = f"""Shop {self.VALID_NAME}:
Pets: {self.PET_NAME}"""

        actual = repr(self.pet_shop)

        self.assertEqual(expected, actual)

    def test_repr_when_multiple_pets_expect_correct_result(self):
        another_pet_name = self.PET_NAME + "2"
        self.pet_shop.add_pet(self.PET_NAME)
        self.pet_shop.add_pet(another_pet_name)

        expected = f"""Shop {self.VALID_NAME}:
Pets: {self.PET_NAME}, {another_pet_name}"""

        actual = repr(self.pet_shop)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
