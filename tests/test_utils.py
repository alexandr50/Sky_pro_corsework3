import unittest
from scripts import utils
from .data.result_data import result_list


class TestUtils(unittest.TestCase):
    def test_get_correct_date_for_sort(self):
        self.assertEqual(utils.get_correct_date_for_sort('2019-08-26T10:50:58.294041'), '2019-08-26 10:50')
        self.assertEqual(utils.get_correct_date_for_sort(''), '')

    def test_correct_date_for_output(self):
        self.assertEqual(utils.correct_date_for_output('2019-08-26 10:50'), '26.08.2019')
        self.assertEqual(utils.correct_date_for_output('2018-08-26'), '26.08.2018')

    def test_get_correct_bill(self):
        self.assertEqual(utils.get_correct_bill("Счет 41421565395219882431"), "Счет **2431")
        self.assertEqual(utils.get_correct_bill("Visa Platinum 8990922113665229"), "Visa Platinum **5229")

    def test_correct_number_card(self):
        self.assertEqual(utils.correct_number_card("Visa Classic 6831982476737658"), "Visa Classic 6831 98** **** 7658")
        self.assertEqual(utils.correct_number_card(None), "")

    def test_sorted_func_for_date(self):
        self.assertEqual(utils.sorted_func_for_date('tests/data/test.json'), result_list)


if __name__ == '__main__':
    unittest.main()