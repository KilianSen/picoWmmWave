from HumanStaticLite.Errors import *


class HSL_Frame:
    frame_header: bytes
    control_word: bytes
    command_word: bytes
    length_h: bytes  # INFO: always 0x00 in datasheet
    length_l: bytes
    data: bytes
    checksum: bytes
    end_of_frame: bytes

    @property
    def length_identifier(self) -> bytes:
        return b''.join([self.length_h, self.length_l])

    @length_identifier.setter
    def length_identifier(self, value: bytes):
        self.length_h = value[0:1:]
        self.length_l = value[1::]

    def __init__(self, frame_header: bytes, control_word: bytes, command_word: bytes, length_h: bytes, length_l: bytes,
                 data: bytes, checksum: bytes, end_of_frame: bytes):
        self.frame_header: bytes = frame_header
        self.control_word: bytes = control_word
        self.command_word: bytes = command_word
        self.length_h: bytes = length_h  # INFO: always 0x00 in datasheet
        self.length_l: bytes = length_l
        self.data: bytes = data
        self.checksum: bytes = checksum
        if checksum is None:
            self.checksum = HSL_Frame.calculate_checksums(self).to_bytes()
        self.end_of_frame: bytes = end_of_frame

    @classmethod
    def calculate_checksums(cls, frame):
        frame: cls = frame
        full_frame = frame.frame_header + frame.control_word + frame.command_word + frame.length_identifier + frame.data
        checksum = sum(full_frame) & 0xFF  # only lower 8 bit
        return checksum

    @classmethod
    def parse(cls, by: bytes):
        frame_header = by[0:2]
        control_word = by[2:3]
        command_word = by[3:4]

        length_h = by[4:5]
        length_l = by[5:6]

        data = by[6:len(by) - 3]

        checksum = by[len(by) - 3:len(by) - 2]
        end_of_frame = by[len(by) - 2:len(by)]

        if frame_header != b'\x53\x59':
            raise NotAFrameError

        prototype = cls(frame_header, control_word, command_word, length_h, length_l, data, checksum, end_of_frame)
        if checksum != cls.calculate_checksums(prototype).to_bytes():
            raise FrameChecksumError
        return prototype
