


class CException(Exception):
    """
    Class des exceptions
    """

    def __init__(self, numException = 0, descException =""):
        Exception.__init__(self, numException)
        self.iNumException = numException
        self.sDescException = descException

    
