from enum import Enum


class ControlWords(Enum):
    HeartbeatPacketIdentification: bytes = b'\x01'
    ProductInformation: bytes = b'\x02'
    UARTUrgrade: bytes = b'\x03'
    OperationStatus: bytes = b'\x05'
    HumanPresence: bytes = b'\x80'


class SystemFunctionsCommandWords(Enum):
    HeartbeatQuery: bytes = b'\x01'
    ModuleReset: bytes = b'\x02'

    CNTW: ControlWords = ControlWords.HeartbeatPacketIdentification


class ProductInformationCommandWords(Enum):
    ProductModelQuery: bytes = b'\xA1'
    ProductIdQuery: bytes = b'\xA2'
    HardwareModelQuery: bytes = b'\xA3'
    FirmwareVersionQuery: bytes = b'\xA4'

    CNTW: ControlWords = ControlWords.ProductInformation


class WorkStatusCommandWords(Enum):
    InitializationCompletedQuerry: bytes = b'\x01'
    SceneSettings: bytes = b'\x07'
    SensitivitySetting: bytes = b'\x08'
    InitializationStatusInquiry: bytes = b'\x81'
    SceneSettingsInquiry: bytes = b'\x87'
    SensitivitySettingInquiry: bytes = b'\x88'

    CNTW: ControlWords = ControlWords.OperationStatus


class HumanPresenceCommandWords(Enum):
    ActiveReportingOfPresence: bytes = b'\x01'
    ActiveReportingOfMotion: bytes = b'\x02'
    ActiveReportingOfBodyMotionParameter: bytes = b'\x03'
    NoPersonTimeoutSetting: bytes = b'\x0A'
    ActiveReportingOfProximity: bytes = b'\x0B'

    PresenceInforamtionInquiry: bytes = b'\x81'
    MotionInforamtionInquiry: bytes = b'\x82'
    BodyMovementInquiryParameterInquiry: bytes = b'\x83'
    NoPersonTimeoutStateInquiry: bytes = b'\x8A'
    ProximityInquiry: bytes = b'\x8B'

    CNTW: ControlWords = ControlWords.HumanPresence


class UARTUpgradeCommandWords(Enum):
    NOT_SUPPORTED: bytes = b'\x00'

    CNTW: ControlWords = ControlWords.UARTUrgrade
