from unittest import TestCase, main
from project.movie import Movie


class Test(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Test", 2000, 10)

    def test_initialization(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertListEqual([], self.movie.actors)

    def test_raises_when_year_is_not_valid(self):
        with self.assertRaises(ValueError) as context:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(context.exception))
        self.assertEqual(2000, self.movie.year)

    def test_raises_when_name_is_empty(self):
        with self.assertRaises(ValueError) as context:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(context.exception))
        self.assertEqual("Test", self.movie.name)

    def test_add_actor_successfully(self):
        self.movie.actors = []
        self.movie.add_actor("Testov")

        self.assertEqual(["Testov"], self.movie.actors)

    def test_add_actor_when_is_already_added(self):
        self.movie.actors = ["Test1", "Test2", "Test3"]
        result = self.movie.add_actor("Test2")

        self.assertEqual("Test2 is already added in the list of actors!", result)
        self.assertEqual(["Test1", "Test2", "Test3"], self.movie.actors)

    def test_gt(self):
        other_movie = Movie("Test2", 2001, 11)
        result = self.movie.__gt__(other_movie)

        self.assertEqual('"Test2" is better than "Test"', result)

        other_movie.rating = 9
        result = self.movie.__gt__(other_movie)

        self.assertEqual('"Test" is better than "Test2"', result)

    def test_repr(self):
        self.movie.actors = ["Test1", "Test2", "Test3"]
        expected = "Name: Test\n" \
               "Year of Release: 2000\n" \
               "Rating: 10.00\n" \
               "Cast: Test1, Test2, Test3"

        actual = self.movie.__repr__()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
