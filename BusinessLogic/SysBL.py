from datetime import datetime
from django.utils import timezone
from DataAccess.MasterRepo import masterRepo
from Master.dtos import SysRunningNoHistUpsertDto


class sysBL:
    def GenerateRunningNo(SysCompanyID, AccountType):
        rtn = None
        SysCompanyDto = None
        SysRunningNoHistDto = None
        TodayDto = datetime.now(tz=timezone.utc)
        Year2LastDigit = abs(TodayDto.year) % 100
        NoHistDto = SysRunningNoHistUpsertDto()

        AccountPrefix = ""

        try:
            AccountPrefix = (
                "I"
                if AccountType == "IN"
                else "C"
                if AccountType == "CN"
                else "D"
                if AccountType == "DN"
                else "E"
                if AccountType == "EN"
                else "S"
            )

            SysCompanyDto = masterRepo.LoadSysCompany(SysCompanyID)

            SysRunningNoHistDto = masterRepo.LoadSysRunningNoHist(
                SysCompanyID, AccountType, Year2LastDigit, TodayDto.month, TodayDto.day
            )

            NoHistDto.SysRunningNoHistID = (
                None if SysRunningNoHistDto == None else str(SysRunningNoHistDto.ID)
            )
            NoHistDto.CompanyID = str(SysCompanyID)
            NoHistDto.AccountType = AccountType
            NoHistDto.RollNo = (
                SysRunningNoHistDto.RollNo + 1 if SysRunningNoHistDto != None else 1
            )
            NoHistDto.LastYear = Year2LastDigit
            NoHistDto.LastMonth = TodayDto.month
            NoHistDto.LastDay = TodayDto.day

            masterRepo.UpsertSysRunningNoHist(NoHistDto)

            rtn = (
                AccountPrefix
                + SysCompanyDto.Code
                + str(Year2LastDigit)
                + str(TodayDto.month).zfill(2)
                + str(TodayDto.day).zfill(2)
                + str(NoHistDto.RollNo).zfill(3)
            )

        except Exception as e:
            print(e)

        return rtn

    def ConvertToWords(self, Numb: str):
        Val = ""
        WholeNo = Numb
        Points = ""
        AndStr = ""
        PointStr = ""
        EndStr = "ONLY"

        DecimalPlace = Numb.index(".")

        if DecimalPlace > 0:
            WholeNo = Numb[0:DecimalPlace]
            Points = Numb[DecimalPlace + 1 :]

            if int(Points) > 0:
                AndStr = "AND SEN "
                PointStr = self.ConvertDecimals(self, Points)

        Val = (
            self.ConvertWholeNumber(self, WholeNo)
            + " "
            + AndStr
            + PointStr
            + " "
            + EndStr
        )

        return Val

    def ConvertWholeNumber(self, Number: str):
        Word = ""
        BeginsZero = False
        IsDone = False
        DblAmt = float(Number)

        if DblAmt > 0:
            BeginsZero = Number.startswith("0")
            NumDigits = len(Number)
            Pos = 0
            Place = ""

            if NumDigits == 1:
                Word = self.Ones(self, Number)
                IsDone = True
            elif NumDigits == 2:
                Word = self.Tens(self, Number)
                IsDone = True
            elif NumDigits == 3:
                Pos = (NumDigits % 3) + 1
                Place = " HUNDRED "
            elif NumDigits == 4 or NumDigits == 5 or NumDigits == 6:
                Pos = (NumDigits % 4) + 1
                Place = " THOUSAND "
            elif NumDigits == 7 or NumDigits == 8 or NumDigits == 9:
                Pos = (NumDigits % 7) + 1
                Place = " MILLION "
            elif NumDigits == 10 or NumDigits == 11 or NumDigits == 12:
                Pos = (NumDigits % 10) + 1
                Place = " BILLION "
            else:
                IsDone = True

            if IsDone == False:
                if Number[0:Pos] != "0" and Number[Pos:] != "0":
                    Word = (
                        self.ConvertWholeNumber(self, Number[0:Pos])
                        + Place
                        + self.ConvertWholeNumber(self, Number[Pos:])
                    )
                else:
                    Word = self.ConvertWholeNumber(
                        self, Number[0:Pos]
                    ) + self.ConvertWholeNumber(self, Number[Pos:])

            if Word.strip() == Place.strip():
                Word = ""

        return Word.strip()

    def Ones(self, Number: str):
        Name = ""
        No = int(Number)

        if No == 1:
            Name = "ONE"
        elif No == 2:
            Name = "TWO"
        elif No == 3:
            Name = "THREE"
        elif No == 4:
            Name = "FOUR"
        elif No == 5:
            Name = "FIVE"
        elif No == 6:
            Name = "SIX"
        elif No == 7:
            Name = "SEVEN"
        elif No == 8:
            Name = "EIGHT"
        elif No == 9:
            Name = "NINE"

        return Name

    def Tens(self, Number: str):
        Name = ""
        No = int(Number)

        if No == 10:
            Name = "TEN"
        elif No == 11:
            Name = "ELEVEN"
        elif No == 12:
            Name = "TWELVE"
        elif No == 13:
            Name = "THIRTEEN"
        elif No == 14:
            Name = "FOURTEEN"
        elif No == 15:
            Name = "FIFTEEN"
        elif No == 16:
            Name = "SIXTEEN"
        elif No == 17:
            Name = "SEVENTEEN"
        elif No == 18:
            Name = "EIGHTEEN"
        elif No == 19:
            Name = "NINETEEN"
        elif No == 20:
            Name = "TWENTY"
        elif No == 30:
            Name = "THIRTY"
        elif No == 40:
            Name = "FORTY"
        elif No == 50:
            Name = "FIFTY"
        elif No == 60:
            Name = "SIXTY"
        elif No == 70:
            Name = "SEVENTY"
        elif No == 80:
            Name = "EIGHTY"
        elif No == 90:
            Name = "NINETY"
        else:
            if No > 0:
                Name = (
                    self.Tens(self, Number[0:1] + "0")
                    + " "
                    + self.Ones(self, Number[1:])
                )

        return Name

    def ConvertDecimals(self, Number: str):
        Cd = ""
        Cd = self.ConvertWholeNumber(self, Number)
        return Cd
