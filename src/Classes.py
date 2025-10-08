import datetime
from dataclasses import dataclass
from enum import Enum

@dataclass
class ExpenseType(Enum):
    BALANCER = 0,
    FOODANDDRINKS = 1,
    CLOTHES = 2,
    VIDEOGAMES = 3,
    POKEMONTCG = 4,
    BARBER = 5,
    GAS = 6,
    BOOKS = 7,
    TRAINTICKETS = 8,
    BUSTICKETS = 9,
    FINES = 10,
    GIFTSANDFAVOURS = 11,
    PACKAGESANDLETTERS = 12,
    MOVIETHEATER = 13,
    THEATER = 14,
    EVENTS = 15,
    ATTRACTIONS = 16,
    LENDINGS = 17,
    SCHOOLSUPPLIES = 18,
    COINSJAR = 19,
    RENTALS = 20,
    PAPERS = 21,
    LOST = 22,
    STOLEN = 23,
    OTHER = 24

@dataclass
class EarningType(Enum):
    BALANCER = 0,
    RELATIVES = 1,
    WON = 2,
    WORK = 3,
    FAVOURORCOMMISSION = 4,
    FOUND = 5,
    SALES = 6,
    COINSJAR = 7,
    OTHER = 8

@dataclass
class Expense:
    amount: float
    day: datetime.date
    expenseType: ExpenseType

    def __init__(self,amount,day,expenseType):
        self.amount = amount
        self.day = day
        self.expenseType = expenseType

@dataclass
class Earning:
    amount: float
    day: datetime.date
    earningType: EarningType

    def __init__(self,amount,day,earningType):
        self.amount = amount
        self.day = day
        self.expenseType = earningType
