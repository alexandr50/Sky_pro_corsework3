import unittest
from scripts import utils

RESULT_LIST = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07 06:17', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 560813069, 'state': 'CANCELED', 'date': '2019-12-03 04:27', 'operationAmount': {'amount': '17628.50', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 1796816785869527', 'to': 'Visa Classic 7699855375169288'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19 09:22', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13 17:38', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}]



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
        self.assertEqual(utils.sorted_func_for_date('tests/data/test.json'), RESULT_LIST)


if __name__ == '__main__':
    unittest.main()