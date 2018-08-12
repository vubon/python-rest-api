class ValidatorError(Exception):
    """
    Using python exception for getting error
    """
    pass


class EmptyField(ValidatorError):
    """
    Checking field is empty or not , if empty raise error
    """

    def __init__(self, field_name):
        self.field_name = field_name

    def __str__(self) -> str:
        return '{!r} field cannot be empty'.format(self.field_name)
