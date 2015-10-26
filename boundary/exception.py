class APIError(Exception):
    """Base exception class for pulse exceptions"""


class APIConnectionError(APIError):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Error connecting to Boundary API: %s" % self.error


class APIResponseError(APIError):
    def __init__(self, status_code, error):
        self.status_code = status_code
        self.error = error

    def __str__(self):
        return "Error response from Boundary API (%d): %s" % (self.status_code, self.error)
