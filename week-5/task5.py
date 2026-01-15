class BankAccount:
    def __init__(self, vladelec, balans):
        self.__vladelec = vladelec
        self.__balans = balans

    def popolnit(self, summa):
        if summa > 0:
            self.__balans = self.__balans + summa
        else:
            print("Summa popolneniya dolzhna byt polozhitelnoy")

    def snyat(self, summa):
        if summa <= self.__balans:
            self.__balans = self.__balans - summa
        else:
            print("Nedostatochno sredstv")

    def poluchit_balans(self):
        return self.__balans


vladelec = input("Vvedite imya vladelca: ")
nachalniy_balans = int(input("Vvedite nachalniy balans: "))

schet = BankAccount(vladelec, nachalniy_balans)

summa_popolneniya = int(input("Vvedite summu popolneniya: "))
schet.popolnit(summa_popolneniya)

summa_snyatiya = int(input("Vvedite summu snyatiya: "))
schet.snyat(summa_snyatiya)

print("Tekushiy balans:", schet.poluchit_balans())
