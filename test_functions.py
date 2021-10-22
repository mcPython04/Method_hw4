import pytest
from functions import *


def geninputs():
    inputs = [10, 2]

    for item in inputs:
        yield item


GEN = geninputs()


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


# ask if we are testing whole number division
@pytest.mark.parametrize("num1, num2, result", [(4, 2, 2), (10, 2, 5), (15, 5, 3), (9, 3, 3), (24, 4, 6), (5, 15, (1/3))])
def test_numbers(num1, num2, result):
    assert numbers(num1, num2) == result



def test_numbers_stringInput(capsys):
    assert numbers("hello", "hi") is None
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Type Error! Please enter an integer."


# A(1,-2) and B(3, -2)
# A(3, 5) and B(4, 5)
@pytest.mark.parametrize("x1, y1, x2, y2, result", [(1, -2, 3, -2, 2), (3, 5, 4, 5, 1)])
def test_dist(x1, y1, x2, y2, result):
    assert dist(x1, y1, x2, y2) == result


def test_isPalindrome():
    assert isPalindrome("racecar") is True


def test_isNotPalindrome():
    assert isPalindrome("testing") is False


def test_divide(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 5.0"


def test_sq():
    assert sq(81) == 9


# pass in name and see if it prints message correctly
def test_greetUser(capsys):
    greetUser("Meng", "Xiang", "Chen")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program Meng Xiang Chen\nGlad to have you!"
    
def test_displayItem(capsys):
    displayItem( ["apple", "pear", "grapes", "peach"], 2)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 2 index is grapes"


