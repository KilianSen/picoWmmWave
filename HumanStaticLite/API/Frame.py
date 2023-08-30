from HumanStaticLite.API.BaseFrame import HSL_Frame
from HumanStaticLite.API.ControlAndCommandWords import *
from HumanStaticLite.Errors import *


class Frame:
    command: SystemFunctionsCommandWords | ProductInformationCommandWords | WorkStatusCommandWords | HumanPresenceCommandWords | UARTUpgradeCommandWords
    data: bytes
    raw_frame: HSL_Frame

    def __init__(self,
                 command: SystemFunctionsCommandWords | ProductInformationCommandWords | WorkStatusCommandWords |
                                HumanPresenceCommandWords | UARTUpgradeCommandWords,
                 data: bytes,
                 raw_frame: HSL_Frame = None
                 ):

        self.command = command
        self.data = data
        self.raw_frame = raw_frame

        if raw_frame is None:
            # noinspection PyTypeChecker
            self.raw_frame = HSL_Frame(b'\x53\x59', command.CNTW.value.value, command.value, b'\x00',
                                       len(data).to_bytes(), data, None, b'\x54\x43')

    @classmethod
    def parse(cls, by: bytes):
        def autoparse_control_command(raw_control_word, raw_command_word):
            cmdw_enums = [SystemFunctionsCommandWords, ProductInformationCommandWords,
                          WorkStatusCommandWords, HumanPresenceCommandWords, UARTUpgradeCommandWords]

            for cmdwe in cmdw_enums:
                if cmdwe.CNTW.value.value != raw_control_word:
                    continue

                parsed_controlword = cmdwe.CNTW.value

                if raw_command_word not in [i.value for i in list(cmdwe.__members__.values())]:
                    continue

                parsed_commandword = cmdwe(raw_command_word)

                return parsed_controlword, parsed_commandword
            raise CouldntAutoParseControlAndCommandWord

        base = HSL_Frame.parse(by)
        _, command = autoparse_control_command(base.control_word, base.command_word)

        return cls(command, base.data, base)
