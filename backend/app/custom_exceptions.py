class CustomJwtException(Exception):
    """Exception raised for jwt error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)