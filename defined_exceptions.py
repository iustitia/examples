
class MyException(Exception):
    pass


class InputError(MyException):
    """
    from: https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions

    Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


raise InputError('test', 's')
