import pytest
from functions import *


# generate inputs for testing divide()
def geninputs():
    inputs = [10, 2]

    for item in inputs:
        yield item


def geninputs1():
    inputs = [56, 7]

    for item in inputs:
        yield item


def gen_str_inputs():
    inputs = ['testing', 'testing1']

    for item in inputs:
        yield item


GEN = geninputs()
GEN1 = geninputs1()
GEN2 = gen_str_inputs()


# Tests for openFile()
# test to see if it works by passing in existing file
def test_openFile_exist(capsys):
    openFile("testing.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File opened."


# test to see if it purposely throws an exception when passing in non-existing file
def test_openFile_notExist(capsys):
    openFile("testin.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File open error"


# test to see if test purposely throws a TypeError exception when passing in int input
def test_openFile_intInput(capsys):
    openFile(6)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Filename should only be of string type!"


# Tests for numbers()
# ask if we are testing whole number division
@pytest.mark.parametrize("num1, num2, result", [(4, 2, 2), (10, 2, 5), (15, 5, 3), (9, 3, 3), (24, 4, 6), (5, 15, (1/3))])
def test_numbers(num1, num2, result):
    assert numbers(num1, num2) == result


def test_numbers_stringInput(capsys):
    assert numbers("hello", "hi") is None
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Type Error! Please enter an integer."


# Tests for dist()
# A(1,-2) and B(3, -2)
# A(3, 5) and B(4, 5)
@pytest.mark.parametrize("x1, y1, x2, y2, result", [(1, -2, 3, -2, 2), (3, 5, 4, 5, 1)])
def test_dist(x1, y1, x2, y2, result):
    assert dist(x1, y1, x2, y2) == result


def test_dist_stringInput(capsys):
    assert dist('hi', 1, 2, 'world') is None
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Type Error! Please enter an integer."


# Tests for isPalindrome()
def test_isPalindrome():
    assert isPalindrome("racecar") is True


def test_isNotPalindrome():
    assert isPalindrome("testing") is False


def test_isPalindrome_intInput(capsys):
    assert isPalindrome(6) is None
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Type Error! Please enter a string."


# Tests for divide()
# testing divide() with inputs 10 and 2
def test_divide(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 5.0"


# testing divide() with inputs 56 and 7
def test_divide1(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN1))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 8.0"


# testing divide() with inputs 'testing' and 'testing1'
def test_divide_str_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN2))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Please input numbers only"


# Tests for sq()
@pytest.mark.parametrize("input, result", [(81, 9), (36, 6), (121, 11)])
def test_sq(input, result):
    assert sq(input) == result


def test_sq_stringInput(capsys):
    sq('testing')
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Type Error! Please enter an integer"


def test_sq_negativeInput(capsys):
    sq(-9)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Please only input positive numbers!"


# Tests for greetUser()
# pass in name and see if it prints message correctly
def test_greetUser(capsys):
    greetUser("John", "Smith", "Adams")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program John Smith Adams\nGlad to have you!"


def test_greetUser_integer_input(capsys):
    greetUser(6, 4, 1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error: Only strings are allowed"


def test_greetUser_bool_input(capsys):
    greetUser(True, True, True)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error: Only strings are allowed"


# Tests for displayItem()
def test_displayItem(capsys):
    displayItem( ["apple", "pear", "grapes", "peach"], 2)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 2 index is grapes"
    

def test_displayItem_integers(capsys):
    displayItem( [20, 35, 50, 65], 1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 1 index is 35"


def test_displayItem_stringIndex(capsys):
    displayItem(["apple", "pear", "grapes", "peach"], "string")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Please put the right inputs"
