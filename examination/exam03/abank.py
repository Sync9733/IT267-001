from bank import Bank
class Abank(Bank):
    def __init__(self, bankname: str,loanamount:int,loanyear:int,lonerate:float) -> None:
        super().__init__(bankname)
        self.__loanamount = loanamount
        self.__loanyear = loanyear
        self.__loanrate = lonerate
        self.interest = 0
        self.monthlypay = 0

    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def location(self,value):
        self.__loanamount = value

    @property
    def loanrate(self):
        return self.__loanrate
    @loanrate.setter
    def location(self,value):
        self.__loanrate = value

    @property
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def location(self,value):
        self.__loanyear = value

    def flat_rate(self):
        super().flat_rate()
        self.interest = self.loanamount*(self.loanrate/100)*self.loanyear
        self.monthlypay = (self.loanamount+self.interest)/24

    def display_interest(self):
        self.flat_rate()
        print(f'****** {self.bankname} Loan Info ******')
        print(f'Loan : {self.loanamount:,.2f} baht')
        print(f'Rate : {self.loanrate:.2f}%')
        print(f'Year : {self.loanyear}')
        print(f'-- Interest --')
        print(f'Interest : {self.interest:,.2f} baht')
        print(f'Monthly Repayment {self.monthlypay:,.2f} baht')
