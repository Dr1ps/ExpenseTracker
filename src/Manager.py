from dataclasses import dataclass
from typing import List

import json

from Classes import Expense, Earning


@dataclass
class Manager:
    expenses: List[Expense]
    earnings: List[Earning]

    def __init__(self):
        with open ("expenses.json", "r") as file:
            raw = json.load(file)
        expenses = [
            Expense(
                s["amount"],
                s["day"],
                s["expenseType"],
            )
            for s in raw
        ]
        with open ("earnings.json", "r") as file:
            raw = json.load(file)
        earnings = [
            Expense(
                s["amount"],
                s["day"],
                s["earningType"],
            )
            for s in raw
        ]

    def menu(self):
        a: str
        a = ("------------------------------------------"
             "[1: ")