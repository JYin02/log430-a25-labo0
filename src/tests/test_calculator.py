"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from src.calculator import Calculator

my_calculator = Calculator()

def test_app():
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    assert my_calculator.addition(5, 3) == 8

def test_subtraction():
    assert my_calculator.subtraction(5, 3) == 2

def test_multiplication():
    assert my_calculator.multiplication(2, 3) == 6

def test_division():
    assert my_calculator.division(6, 3) == 2
    assert my_calculator.division(5, 0) == "Erreur : division par zéro"
