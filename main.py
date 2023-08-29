import utime
from machine import UART


# # 0x01 - heartbeat packet identification, 0x02 - product information, 0x03 - UART upgrade, 0x05 - operation status,
# 0x80 - human presence

class HSL_Frame:
    @staticmethod
    def calculate_csk(hsl_frame):
        def calculate_checksum(header, control_word, command_word, length_identifierh, length_identifier, data):
            # Convert all inputs to integer
            header = int(header, 16)
            control_word = int(control_word, 16)
            command_word = int(command_word, 16)
            length_identifierh = int(length_identifierh, 16)
            length_identifier = int(length_identifier, 16)
            data = [int(d, 16) for d in data]

            # Perform the sum operation
            total = header + control_word + command_word + length_identifierh + length_identifier + sum(data)

            # Extract the lower eight bits
            checksum = total & 0xFF

            return checksum
        return calculate_checksum(hsl_frame.FrameHeader,hsl_frame.ControlWord, hsl_frame.CommandWord, hsl_frame.LengthH, hsl_frame.LengthL, hsl_frame.Data)

    FrameHeader: bytes = b"\x53\x59"
    ControlWord: bytes
    CommandWord: bytes
    LengthH: bytes
    LengthL: bytes
    Data: bytes
    Checksum: bytes
    EndOfFrame: bytes = b'\x54\x43'

    def __init__(self, control, comand, lenght_h, lenght_l, data):
        self.ControlWord = control
        self.CommandWord = comand
        self.LengthH = lenght_h
        self.LengthL = lenght_l
        self.Data = data

        self.Checksum = self.calculate_csk(self)





class HumanStaticLite:
    uart = UART

    def __init__(self, UART_Interface: UART):
        self.uart = UART_Interface
