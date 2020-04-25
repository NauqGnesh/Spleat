import sys
import math

class Person(Food):
    overpaid = []
    owe = []
    oweString = []

    def __init__(self, name = "unkown", moneyOwed = "0", moneyPaid = "0", overpay = "0", percentDebt = "0", numPerson = "0"):
        self.__name = name
        self.__moneyOwed = moneyOwed
        self.__moneyPaid = moneyPaid
        self.__overpay = overpay
        self.__percentDebt = percentDebt
        self.__numPerson += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def moneyPaid(self):
        return self.__moneyPaid
    
    @moneyPaid.setter
    def moneyPaid(self, pay):
        self.__moneyPaid = pay
    
    @property
    def moneyOwed(self):
        return moneyOwed

    @moneyOwed.setter
    def moneyOwed(self, owe):
        self.__moneyOwed = owe

    @property
    def percentDebt(self):
        return self.__percentDebt

    @percentDebt.setter
    def percentDebt(self, debt):
        self.__percentDebt = debt
    
    @property 
    def numPerson(self):
        return self.__numPerson

    @numPerson.setter
    def numPerson(self, num):
        self.__numPerson = num

    @property
    def overpay(self):
        return self.__overpay
    
    @overPay.setter
    def overpay(self, over):
        self.__overpay = over

    @property 
    def calculation(array, tax):
        overpaySum = 0

        for x in len(array):
            foodPrice = array[x].getPrice / array[x].numPerson

            if(array[x].moneyPaid > foodPrice):
                array[x].overpay(array[x].moneyPaid - foodPrice)

                overpaySum += array[x].overpay
                overpaid.append(array[x])
            else:
                array[x].moneyOwed(foodPrice - array[x].moneyPaid())
                owe.append(array[x])

        for j in len(owe):
            percentDebt = owe[j].moneyOwed/overpaySum

            for k in len(overpaid):
                owe[x].moneyOwed(percentDebt * overpaid[x].overpay + (percentDebt * overpaid[x].overpaid * tax))
                oweString.append(owe[j].name + " owes " + overpaid[k].name() + ": $" + owe[j].moneyOwed())

            

                
