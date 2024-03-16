import pytest
from ldfghdpy import format_date, format_transaction


def test_format_date():
    date_str = '2019-07-15T11:47:40.496961'
    formatted_date = format_date(date_str)
    assert formatted_date == '15.07.2019'


def test_format_transaction():
    transaction = {'from': 'Счет 1234567890123456', 'to': 'Счет 9876543210987654'}
    formatted_transaction = format_transaction(transaction)
    assert formatted_transaction == 'Счет 1234 56** **** 3456 -> Счет **7654'


def test_format_transaction2():
    transaction = {'to': 'Счет 35737585785074382265'}
    formatted_transaction = format_transaction(transaction)
    assert formatted_transaction == 'Счет **2265'



if __name__ == '__main__':
    pytest.main()

