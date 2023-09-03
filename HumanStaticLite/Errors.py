class NotAFrameError(AssertionError):
    def __init__(self):
        message: str = "The provided data does not start with the frame header!"
        super().__init__(message)


class FrameChecksumError(AssertionError):
    def __init__(self, cks1: str = None, cks2: str = None):
        message: str = "Frame checksum is invalid"
        if cks1 is not None and cks2 is not None:
            message += '\n                    ' + f'Expected: {cks1} == {cks2}'
        super().__init__(message)


class FailedAutoParseControlAndCommandWord(AssertionError):
    def __init__(self, raw_control_word=None, raw_command_word=None):
        message = "Failed to parse control and command word"

        if raw_command_word is not None and raw_control_word is not None:
            message += f": Control word {raw_control_word}, Command word {raw_command_word}"

        super().__init__(message)
