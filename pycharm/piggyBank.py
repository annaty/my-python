class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        
    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        if self.cents + deposit_cents > 99:
            sum = (self.cents + deposit_cents) / 100
            self.dollars += int(sum)

            self.cents = int(round((sum - int(sum))*100))

        elif self.cents + deposit_cents <= 99:
            self.cents += deposit_cents

piggy = PiggyBank(1, 1)
piggy.add_money(500, 500)
print(piggy.dollars)
print(piggy.cents)