import pytest
from functions import *


def geninputs():
    inputs = [10, 2]

    for item in inputs:
        yield item


GEN = geninputs()


def test_openFile(capsys):
    openFile("testing.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File opened."


def test_numbers():
    assert numbers(4, 2) == 2


# A(1,-2) and B(3, -2)
def test_dist():
    assert dist(1, -2, 3, -2) == 2


def test_isPalindrome():
    assert isPalindrome("testing") == False
    assert isPalindrome("racecar") == True


def test_divide(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 5.0"


def test_sq():
    assert sq(81) == 9
