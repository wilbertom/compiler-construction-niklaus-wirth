import pytest
from regular_language_parser import (
    IndentifierLanguageParser,
    ParsingError,
    IntegerLanguageParser,
)


def test_identifier_language_parser():
    assert IndentifierLanguageParser("abc").parse() is True
    assert IndentifierLanguageParser("h20").parse() is True
    assert IndentifierLanguageParser("helloWorld").parse() is True
    assert IndentifierLanguageParser("savingMoney").parse() is True

    with pytest.raises(ParsingError):
        IndentifierLanguageParser("123a").parse()

    with pytest.raises(ParsingError):
        IndentifierLanguageParser("hello_world").parse()

    with pytest.raises(ParsingError):
        IndentifierLanguageParser("$helloWorld").parse()

    with pytest.raises(ParsingError):
        IndentifierLanguageParser("@name").parse()


def test_integer_language_parser():
    assert IntegerLanguageParser("0").parse() is True
    assert IntegerLanguageParser("9").parse() is True
    assert IntegerLanguageParser("123").parse() is True

    with pytest.raises(ParsingError):
        IntegerLanguageParser("0.12").parse()

    with pytest.raises(ParsingError):
        IntegerLanguageParser("-2").parse()

    with pytest.raises(ParsingError):
        IntegerLanguageParser("h12").parse()
