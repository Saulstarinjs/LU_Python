from django.db import models


class Deposit(models.Model):

    deposit = models.FloatField()
    term = models.IntegerField()
    rate = models.FloatField()

    def interest(self):
        new_deposit = self.deposit

        for i in range(self.term):
            new_deposit = new_deposit * (1 + self.rate)

        interest = new_deposit - self.deposit

        return float(interest)
