import sys
import string


class ParsingError(Exception):
    pass


class ParsingFinsihed(ParsingError):
    pass


class ParsingLogicError(ParsingError):
    pass


class ParsingLogicShouldNotOccurError(ParsingLogicError):
    pass


class RegularLanguageParser:
    def __init__(self, source_code, stderr=sys.stderr):
        self._source_code = source_code
        self.stderr = stderr

        self._position = 0
        self.symbol = None

    def parse(self):
        raise NotImplementedError

    def next(self):
        if self._position == len(self._source_code):
            raise ParsingFinsihed
        else:
            self.symbol = self._source_code[self._position]
            self._position += 1

    def error(self):
        message = f"Symbol does not belong to the language: {self.symbol}"
        raise ParsingError(message)


class IndentifierLanguageParser(RegularLanguageParser):
    letters = string.ascii_letters
    digits = string.digits

    def parse(self):
        self.next()

        try:
            if self.symbol in self.letters:
                self.next()
            else:
                self.error()

            while self.symbol in (self.letters + self.digits):
                if self.symbol in self.letters:
                    self.next()
                elif self.symbol in self.digits:
                    self.next()
                else:
                    raise ParsingLogicShouldNotOccurError("bad branch")

            self.error()

            return True
        except ParsingFinsihed:
            return True


class IntegerLanguageParser(RegularLanguageParser):
    digits = string.digits

    def parse(self):
        self.next()

        try:
            if self.symbol in self.digits:
                self.next()
            else:
                self.error()

            while self.symbol in (self.digits):
                self.next()

            self.error()

        except ParsingFinsihed:
            return True
