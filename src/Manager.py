from dataclasses import dataclass

from typing import List

import json

from Classes import Expense, Earning


@dataclass
class Manager:
    expenses: List[Expense]
    earnings: List[Earning]
    home: str
    logsMenu: str

    def __init__(self):

        self.home = "HOME MENU\n[0:View logs] [1:Declare an expense] [2:Declare an earning]"
        self.logsMenu = ("LOGS MENU\n\n"
                         "What would you like to visualize?\n"
                         "[0:Expenses] [1:Earnings] [2:Both]")

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

    def encapsule(self,data):
        toPrint  = "-------------------------------------------------------------"
        toPrint = toPrint + "\n" + data
        return toPrint

    def printMenu(self,typeOfMenu):
        temp: str
        match typeOfMenu:
            case "home":
                temp = self.home
            case "logs":
                temp = self.logsMenu
            case _:
                temp = "default"
        print(self.encapsule(temp))

