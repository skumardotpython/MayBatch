class NetworkError(RuntimeError):

    def __init__(self, args):
        self.args = str(args)


try:
    raise NetworkError("Network Error Occurred")
except NetworkError as e:
    print(e)