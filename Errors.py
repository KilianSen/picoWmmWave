class NotAFrameError(AssertionError):
    message = "Not a frame"


class FrameChecksumError(AssertionError):
    message = "Frame checksum is invalid!"


class CouldntAutoParseControlAndCommandWord(AssertionError):
    ...
