from enum import Enum


class ControlWords(Enum):
    HeartbeatPacketIdentification: bytes = b'\x01'
    ProductInformation: bytes = b'\x02'
    UARTUpgrade: bytes = b'\x03'
    OperationStatus: bytes = b'\x05'
    HumanPresence: bytes = b'\x80'
    UnderlyingOpenFunctionInformation: bytes = b'\x08'


class SystemFunctionsCommandWords(Enum):
    HeartbeatQuery: bytes = b'\x01'
    ModuleReset: bytes = b'\x02'

    ControlWordBackpoint: ControlWords = ControlWords.HeartbeatPacketIdentification


class ProductInformationCommandWords(Enum):
    ProductModelQuery: bytes = b'\xA1'
    ProductIdQuery: bytes = b'\xA2'
    HardwareModelQuery: bytes = b'\xA3'
    FirmwareVersionQuery: bytes = b'\xA4'

    ControlWordBackpoint: ControlWords = ControlWords.ProductInformation


class WorkStatusCommandWords(Enum):
    InitializationCompletedQuery: bytes = b'\x01'
    SceneSettings: bytes = b'\x07'
    SensitivitySetting: bytes = b'\x08'
    InitializationStatusInquiry: bytes = b'\x81'
    SceneSettingsInquiry: bytes = b'\x87'
    SensitivitySettingInquiry: bytes = b'\x88'

    MotionSpeedInquiry: bytes = b"\x85"  # WHY THE HECK ARE U HERE ?? All similar functions are at
    # ControlWordBackpoint 0x08

    # Custom Mode Setting
    CustomModeSetting: bytes = b'\x09'
    EndOfCustomModeSettings: bytes = b'\x0A'
    CustomModeQuery: bytes = b'\x89'

    ControlWordBackpoint: ControlWords = ControlWords.OperationStatus


class HumanPresenceCommandWords(Enum):
    ActiveReportingOfPresence: bytes = b'\x01'
    ActiveReportingOfMotion: bytes = b'\x02'
    ActiveReportingOfBodyMotionParameter: bytes = b'\x03'
    NoPersonTimeoutSetting: bytes = b'\x0A'
    ActiveReportingOfProximity: bytes = b'\x0B'

    PresenceInformationInquiry: bytes = b'\x81'
    MotionInformationInquiry: bytes = b'\x82'
    BodyMovementInquiryParameterInquiry: bytes = b'\x83'
    NoPersonTimeoutStateInquiry: bytes = b'\x8A'
    ProximityInquiry: bytes = b'\x8B'

    ControlWordBackpoint: ControlWords = ControlWords.HumanPresence


class UARTUpgradeCommandWords(Enum):
    StartUARTUpgrade: bytes = b"01"
    UpgradePackageTransmission: bytes = b"\x02"
    EndingTheUARTUpgrade: bytes = b"\x03"

    ControlWordBackpoint: ControlWords = ControlWords.UARTUpgrade


class UnderlyingOpenFunctionInformationCommandWords(Enum):
    UnderlyingOpenFunctionInformationOutputSwitch: bytes = b"\x00"
    UnderlyingOpenFunctionInformationOutputSwitchInquiry: bytes = b"\x80"

    ReportingOfSensorInformation: bytes = b"\x01"
    ExistenceEnergyValueInquiry: bytes = b"\x81"
    MotionEnergyValueInquiry: bytes = b"\x82"
    StaticDistanceInquiry: bytes = b"\x83"
    MotionDistanceInquiry: bytes = b"\x84"

    # Underlying open parameter setting
    ExistenceJudgmentThresholdSettings: bytes = b"\x08"
    MotionTriggerThresholdSettings: bytes = b"\x09"
    ExistencePerceptionBoundarySettings: bytes = b"\x0A"
    MotionTriggerBoundarySetting: bytes = b"\x0B"
    MotionTriggerTimeSetting: bytes = b"\x0C"
    MotionToStillTimeSetting: bytes = b"\x0D"
    TimeForEnteringNoPersonStateSetting: bytes = b"\x0E"

    # Underlying open parameter inquiry
    ExistenceJudgmentThresholdInquiry: bytes = b"\x88"
    MotionTriggerThresholdInquiry: bytes = b"\x89"
    ExistencePerceptionBoundaryInquiry: bytes = b"\x8A"
    MotionTriggerBoundaryInquiry: bytes = b"\x8B"
    MotionTriggerTimeInquiry: bytes = b"\x8C"
    MotionToStillTimeInquiry: bytes = b"\x8D"
    TimeForEnteringNoPersonStateInquiry: bytes = b"\x8E"

    ControlWordBackpoint: ControlWords = ControlWords.UnderlyingOpenFunctionInformation
