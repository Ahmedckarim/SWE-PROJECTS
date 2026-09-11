import json
import csv
from datetime import date


class Expense:
    def __init__(self, description, amount,category, expense_date=None ):
        self.description = description
        self.amount = amount
        self.category = category

        if expense_date:
            self.date = expense_date
        else:
            self.date = str(date.today())


    def to_dic(self):
        return{
            "description": self.description,
            "amount":  self.amount,
            "category": self.category,
            "date": self.date

        }

