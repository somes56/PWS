from dataclasses import dataclass


@dataclass
class SysRunningNoHistUpsertDto:
    SysRunningNoHistID: str = ""
    CompanyID: str = ""
    AccountType: str = ""
    RollNo: int = 0
    LastYear: int = 0
    LastMonth: int = 0
    LastDay: int = 0
