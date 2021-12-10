from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class Test(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 5)

    def test_initialization(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(5, self.paint_factory.capacity)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertDictEqual(self.paint_factory.products, self.paint_factory.ingredients)

    def test_add_ingredient_raises_when_ingredient_not_valid(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient("orange", 1)

        self.assertEqual(f"Ingredient of type {'orange'} not allowed in {self.paint_factory.__class__.__name__}", str(context.exception))

    def test_add_ingredient_raises_when_product_quantity_is_not_valid(self):
        result = self.assertFalse(self.paint_factory.can_add(6))
        self.assertEqual(None, result)

        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient("white", 6)

        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_ingredient_successfully(self):
        self.paint_factory.ingredients = {}
        self.assertTrue(self.paint_factory.can_add(1))

        self.paint_factory.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.paint_factory.ingredients)

        self.paint_factory.add_ingredient("white", 1)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_remove_ingredient_raises_when_ingredient_is_not_in_the_factory(self):
        self.paint_factory.ingredients = {}
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient("pink", 1)

        self.assertEqual(repr("No such ingredient in the factory"), str(context.exception))
        self.assertEqual({}, self.paint_factory.ingredients)

        self.paint_factory.add_ingredient("white", 1)
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient("pink", 1)

        self.assertEqual(repr("No such ingredient in the factory"), str(context.exception))
        self.assertEqual({"white": 1}, self.paint_factory.ingredients)


    def test_remove_ingredient_raises_when_quantity_is_less_than_0(self):
        self.paint_factory.ingredients = {"white": 2, "green": 1}
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient("white", 3)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_ingredient_successfully(self):
        self.paint_factory.ingredients = {"white": 2, "green": 1}
        self.paint_factory.remove_ingredient("white", 1)
        self.assertEqual({"white": 1, "green": 1}, self.paint_factory.ingredients)

    def test_repr(self):
        self.paint_factory.ingredients = {"white": 2, "green": 1}
        expected = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\nwhite: 2\ngreen: 1\n"
        actual = self.paint_factory.__repr__()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()




