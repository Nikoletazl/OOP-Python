from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student_card = StudentReportCard("Test", 12)

    def test_initializing_all_attributes(self):
        self.assertEqual("Test", self.student_card.student_name)
        self.assertEqual(12, self.student_card.school_year)
        self.assertDictEqual({}, self.student_card.grades_by_subject)

    def test_initializing_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_initializing_invalid_school_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        self.student_card.school_year = 1
        self.assertEqual(1, self.student_card.school_year)

    def test_add_grade(self):
        self.assertDictEqual({}, self.student_card.grades_by_subject)
        result = self.student_card.add_grade("TestSubject", 5)
        self.assertEqual({"TestSubject": [5]}, self.student_card.grades_by_subject)
        self.assertIsNone(result)

        self.student_card.add_grade("Subject1", 5)
        self.assertEqual({"TestSubject": [5], "Subject1": [5]}, self.student_card.grades_by_subject)

    def test_add_grade_subject_in_grades_by_subjects(self):
        self.student_card.grades_by_subject = {"TestSubject": [5]}
        self.student_card.add_grade("TestSubject", 6)
        self.assertDictEqual({"TestSubject": [5, 6]}, self.student_card.grades_by_subject)

    def test_report_for_average_grade_by_subject_no_subjects_found(self):
        self.assertDictEqual({}, self.student_card.grades_by_subject)
        result = self.student_card.average_grade_by_subject()
        self.assertEqual("", result)

    def test_average_grade_by_subject(self):
        self.student_card.grades_by_subject = {"TestSubject": [5, 3, 4], "TestSubject2": [5, 5]}
        result = self.student_card.average_grade_by_subject()

        self.assertEqual("TestSubject: 4.00\nTestSubject2: 5.00", result)

    def test_average_grade_for_all_subjects(self):
        self.student_card.grades_by_subject = {"TestSubject": [5, 3, 4], "TestSubject2": [5, 5]}
        result = self.student_card.average_grade_for_all_subjects()

        self.assertEqual("Average Grade: 4.40", result)

    def test_repr_representation(self):
        self.student_card.grades_by_subject = {"TestSubject": [5, 3, 4], "TestSubject2": [5, 5]}

        self.assertEqual(f"Name: Test\nYear: 10\n----------\nTestSubject: 4.00"
                         f"\nTestSubject2: 5.00\n----------\nAverage Grade: 4.40", repr(self.student_card))


if __name__ == "__main__":
    main()