from datetime import datetime
from dataclasses import dataclass
from datetime import timedelta

from typing import List

import json

from Classes import Expense, Earning, LogsFilter


@dataclass
class Manager:
    expenses: List[Expense]
    earnings: List[Earning]
    home: str
    logsMenu: str
    timeRangeMenu = str
    logsFilter = LogsFilter

    def __init__(self):

        self.home = "HOME MENU\n[0:View logs] [1:Declare an expense] [2:Declare an earning] [3:Exit]"
        self.logsMenu = ("LOGS MENU\n\n"
                         "What would you like to visualize?\n"
                         "[0:Expenses] [1:Earnings] [2:Both] [3:Back]")
        self.timeRangeMenu = ("LOGS MENU\n\n"
                              "Select an option to visualize:\n"
                              "[0:Current month] [1:Previous month] [2:Current year] [3:All time] [4:Back]")


        with open ("expenses.json", "r") as file:
            raw = json.load(file)
        self.expenses = [
            Expense(
                s["amount"],
                s["day"],
                s["expenseType"],
            )
            for s in raw
        ]
        with open ("earnings.json", "r") as file:
            raw = json.load(file)
        self.earnings = [
            Earning(
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
            case "time":
                temp = self.timeRangeMenu
            case _:
                temp = "default"
        print(self.encapsule(temp))

    def printData(self,time):
        filter = self.logsFilter.name
        rightNow = datetime.now()
        year: int
        month: int
        match time:
            case "0":
                year = rightNow.year
                month = rightNow.month
            case "1":
                if rightNow.month == 1:
                    month = 12
                    year = rightNow.year-1
                else:
                    month = rightNow.month-1
                    year = rightNow.year
            case "2":
                year = rightNow
                month = 0
            case "3":
                year = 0
                month = 0
            case _:
                print("Error while printing data")
                return
        filteredExpenses: List[Expense]
        filteredEarnings: List[Earning]
        filtered = set()
        match filter:
            case "EXPENSES":
                filtered.update(self.expenses)
            case "EARNINGS":
                filtered.update(self.earnings)
            case "BOTH":
                filtered.update(self.expenses + self.earnings)
            case _:
                print("Error while printing data")
        sortedItems = sorted(filtered, key=lambda
            x: x.day)
        print(sortedItems)

    def launchTimeMenu(self):
        self.printMenu("time")
        check = True
        while check:
            action = input()
            match action:
                case "0":
                    self.printData(action)
                case "1":
                    self.printData(action)
                case "2":
                    self.printData(action)
                case "3":
                    self.printData(action)
                case "4":
                    check = False
                case _:
                    print("Invalid request")

    def launchLogs(self):
        self.printMenu("logs")
        check = True
        while check:
            action = input()
            match action:
                case "0":
                    self.logsFilter = LogsFilter.EXPENSES
                    self.launchTimeMenu()
                case "1":
                    self.logsFilter = LogsFilter.EARNINGS
                    self.launchTimeMenu()
                case "2":
                    self.logsFilter = LogsFilter.BOTH
                    self.launchTimeMenu()
                case "3":
                    check = False
                case _:
                    print("Invalid request")

    def launchHome(self):
        self.printMenu("home")
        check = True
        while check:
            action = input()
            match action:
                case "0":
                    self.launchLogs()
                case "1":
                    self.addExpense()
                case "2":
                    self.addEarning()
                case "3":
                    check = False
                case _:
                    print("Invalid request")
        print(self.encapsule("Closing..."))



    def launchProgram(self):
        print("WELCOME TO THE EXPENSES / EARNINGS TRACKER")
        self.printMenu("home")

        action = input()
        check = True
        while check:
            if action.__eq__("0"):
                self.printMenu("logs")
                checkLogs = True
                while checkLogs:
                    action = input()
                    match action:
                        case "0":
                            self.logsFilter = LogsFilter.EXPENSES
                            checkLogs = False
                        case "1":
                            self.logsFilter = LogsFilter.EARNINGS
                            checkLogs = False
                        case "2":
                            self.logsFilter = LogsFilter.BOTH
                            checkLogs = False
                        case "3":
                            checkLogs = False
                            check
                        case _:
                            print("Invalid request")

