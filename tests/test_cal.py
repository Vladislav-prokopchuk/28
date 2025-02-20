import sys
import os

# Додаємо батьківську директорію до шляху
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import Calculator  # Тепер імпорт працюватиме

import pytest


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    calc.result_display.setText("1 + 1")
    calc.on_button_click()
    assert calc.result_display.text() == "2"


def test_subtraction(calc):
    calc.result_display.setText("5 - 3")
    calc.on_button_click()
    assert calc.result_display.text() == "2"


def test_multiplication(calc):
    calc.result_display.setText("3 * 4")
    calc.on_button_click()
    assert calc.result_display.text() == "12"


def test_division(calc):
    calc.result_display.setText("10 / 2")
    calc.on_button_click()
    assert calc.result_display.text() == "5.0"


def test_integer_division(calc):
    calc.result_display.setText("10 // 3")
    calc.on_button_click()
    assert calc.result_display.text() == "3"


def test_modulus(calc):
    calc.result_display.setText("10 % 3")
    calc.on_button_click()
    assert calc.result_display.text() == "1"
