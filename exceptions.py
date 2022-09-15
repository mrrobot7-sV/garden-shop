# custom exception that can be raised when the input is not a number.
class ValueNotANumberError(ValueError):
    """Raised when the input is not a number."""
    def __init__(self, message = "Error: Value is not a number."):
        self.message = message
        super().__init__(self.message)
