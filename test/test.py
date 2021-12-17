from unittest import TestCase, main

from project.team import Team


class Test(TestCase):
    def setUp(self) -> None:
        self.team = Team("Test")

    def test_initialization(self):
        self.team.members = {}

        self.assertEqual("Test", self.team.name)
        self.assertDictEqual({}, self.team.members)

    def test_raises_when_name_contains_symbol(self):
        with self.assertRaises(ValueError) as context:
            self.team.name = ""

        self.assertEqual("Test", self.team.name)
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.team.name = "@"

        self.assertEqual("Test", self.team.name)
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member_when_member_not_in_members(self):
        self.team.members = {}
        dict = {"Peter": 1}
        result = self.team.add_member(**dict)

        self.assertEqual({"Peter": 1}, self.team.members)
        self.assertEqual("Successfully added: Peter", result)

        self.team.members = {"Peter": 2}
        dict = {"Dimitar": 1, "Georgi": 3}
        result = self.team.add_member(**dict)

        self.assertEqual({"Peter": 2, "Dimitar": 1, "Georgi": 3}, self.team.members)
        self.assertEqual("Successfully added: Dimitar, Georgi", result)

    def test_add_members_when_member_in_members(self):
        self.team.members = {"Peter": 2}
        dict = {"Peter": 3}
        self.team.add_member(**dict)

        self.assertEqual({"Peter": 2}, self.team.members)

    def test_remove_member_when_member_in_members(self):
        self.team.members = {"Peter": 2}
        result = self.team.remove_member("Peter")

        self.assertEqual({}, self.team.members)
        self.assertEqual("Member Peter removed", result)

    def test_remove_member_when_member_not_in_members(self):
        self.team.members = {}
        result = self.team.remove_member("Peter")

        self.assertEqual({}, self.team.members)
        self.assertEqual("Member with name Peter does not exist", result)

        self.team.members = {"Peter": 2}
        result = self.team.remove_member("Dimitar")

        self.assertEqual({"Peter": 2}, self.team.members)
        self.assertEqual("Member with name Dimitar does not exist", result)

    def test_add_(self):
        self.another_team = Team("Another")
        self.another_team.members = {}
        dict = {"Georgi": 1}
        self.another_team.add_member(**self.team.members)
        self.another_team.add_member(**dict)
        result = self.team.__add__(self.another_team)

        self.assertEqual("TestAnother", result.name)
        self.assertEqual({"Georgi": 1}, result.members)

    def test_gt_(self):
        self.another_team = Team("Another")
        self.another_team.members = {}
        dict = {"Georgi": 1}
        self.another_team.add_member(**self.team.members)
        self.another_team.add_member(**dict)
        result = self.team.__gt__(self.another_team)

        self.assertEqual(False, result)

        self.team.members = {"Peter": 1, "Georgi": 2}
        result = self.team.__gt__(self.another_team)

        self.assertEqual(True, result)

    def test_len_(self):
        self.assertEqual(0, self.team.__len__())

        self.team.members = {"Peter": 1}
        result = self.team.__len__()

        self.assertEqual(1, result)

    def test_str_(self):
        self.team.members = {"Aleks": 1, "Borislav": 2, "Dimitar": 3}
        expected = "Team name: Test\nMember: Dimitar - 3-years old\nMember: Borislav - 2-years old\nMember: Aleks - 1-years old"
        actual = self.team.__str__()

        self.assertEqual(expected, actual)

        self.team.members = {"Aleks": 1, "Borislav": 2, "Dimitar": 2}
        expected = "Team name: Test\nMember: Borislav - 2-years old\nMember: Dimitar - 2-years old\nMember: Aleks - 1-years old"
        actual = self.team.__str__()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()