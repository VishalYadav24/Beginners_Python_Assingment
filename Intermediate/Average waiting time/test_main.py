import pytest

from main import calculate_least_waiting_time

def test_calculate_least_waiting_time():
    sample_order_count = 4
    sample_order_details = ['0', '1', '2', '5', '3', '6', '8', '9']