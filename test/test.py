from unittest import TestCase, main

from project.team import Team

class Test(TestCase):
    def setUp(self) -> None:
        self.team = Team("Testov")
        self.team.members = {}
        self.another_team = Team("another")
        self.another_team.members = {"Peter": 1}

    def test_initialization(self):
        self.assertEqual("Testov", self.team.name)
        self.assertDictEqual({}, self.team.members)

    def test_name_raises_when_name_is_empty(self):
        with self.assertRaises(ValueError) as context:
            self.team.name = ""
            raise ValueError("Team Name can contain only letters!")

        self.assertEqual("Team Name can contain only letters!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.team.name = "@"
            raise ValueError("Team Name can contain only letters!")

    def test_add_member_if_member_does_not_exist(self):
        dict = {"Peter": 1}
        result = self.team.add_member(**dict)
        self.assertEqual({"Peter": 1}, self.team.members)
        self.assertEqual("Successfully added: Peter", result)
        dict_2 = {"Georgi": 5}
        result_2 = self.team.add_member(**dict_2)
        self.assertEqual({"Peter": 1, "Georgi": 5}, self.team.members)
        self.assertEqual("Successfully added: Georgi", result_2)


    def test_remove_member_when_does_not_exist(self):
        result = self.team.remove_member("Peter")
        self.assertEqual("Member with name Peter does not exist", result)
        self.assertEqual({}, self.team.members)

        self.team.members = {"Peter": 1, "Georgi": 2}
        result = self.team.remove_member("Krasimir")
        self.assertEqual({"Peter": 1, "Georgi": 2}, self.team.members)
        self.assertEqual("Member with name Krasimir does not exist", result)

    def test_remove_successfully(self):
        self.team.members = {"Peter": 5, "Georgi": 4}
        result = self.team.remove_member("Peter")
        self.assertEqual({"Georgi": 4}, self.team.members)
        self.assertEqual("Member Peter removed", result)

    def test_other(self):
        self.team.__gt__(self.another_team)
        self.assertFalse(self.team.members, self.another_team.members)
        dict = {"Dimitur": 1, "Peter": 2}
        self.team.add_member(**dict)
        self.team.__gt__(self.another_team)
        self.assertTrue(self.team.members, self.another_team.members)

    def test_len(self):
        self.assertEqual(0, self.team.__len__())
        dict = {"Peter": 1}
        self.team.add_member(**dict)
        self.assertEqual(1, self.team.__len__())

    def test_add(self):
        team = Team("Testov")
        another_team = Team("another")
        another_dict = {"Georgi": 1}
        another_team.add_member(**another_dict)
        dict = {"Anastas": 1, "Peter": 2}
        team.add_member(**dict)
        expected = "Team name: Testovanother\nMember: Peter - 2-years old\nMember: Anastas - 1-years old\nMember: Georgi - 1-years old"
        actual = team.__add__(another_team).__str__()
        self.assertEqual(expected, actual)


    def test_str_(self):
        self.team.members = {"Anastas": 1, "Peter": 2, "Georgi": 3}
        expected = "Team name: Testov\nMember: Georgi - 3-years old\nMember: Peter - 2-years old\nMember: Anastas - 1-years old"
        actual = self.team.__str__()

if __name__ == "__main__":
    main()