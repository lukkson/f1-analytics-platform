class F1ApiException(Exception):
    pass


class F1ApiConnectionException(F1ApiException):
    pass


class F1ApiNotFoundException(F1ApiException):
    pass
