from typing import NewType

import FT_Time
from category import Category


DATE = NewType(('date'), tuple[str, str or int])


# Represents a single value entry that is either classified as 'expense' or 'income'
class TrackerEntry:
    def __init__(self, name: str,
                 type: str,
                 category: str,
                 value: float,
                 currency: str,
                 wallet: str,
                 date):
        '''
        Args:
            name::str
                Name of entry as typed by the user
            category::str
                Category name
            type::str
                Equal to either 'Income' or 'Expense'
            value::float
                Amount of specified currency
            currency::str
                Currency
            wallet::str
                Name of the wallet this entry belongs to
            date::FT_Time.now = time.localtime()
                Date of entry creation
        '''

        self.name: str = name
        self.type: str = type
        self.category = category
        self.value: float = value
        self.currency: str = currency
        self.wallet: str = wallet
        self.date = date



# Holds all entries of a single type (income or expense)
# Also holds all entries of children objects (see DateEntry class)
class EntryContainer:
    def __init__(self):
        self.entries: list[TrackerEntry] = []
        self.categories: list[Category] = []

    def add_entry(self, item: TrackerEntry) -> list[TrackerEntry]:
        self.entries.append(item)
        return self.entries

    def add_category(self, kwargs):
        if self.category_exists(kwargs.get('name')):
            return None
        else:
            new_category = Category(self, kwargs.get('name'), kwargs.get('color'), kwargs.get('type'))
            self.categories.append(new_category)
            print(f"{kwargs['name']} [{kwargs['type']}]")
            return new_category

    def category_exists(self, name: str) -> bool:
        if name in [vars(cat)['name'] for cat in self.categories]:
            return True
        else:
            return False

    def get_total(self) -> float:
        return sum([entry.value for entry in self.entries])



# Represents a single date object (month, week, day) that contains income and expense related to that period
class DateEntry:
    def __init__(self, date: DATE, parent = None):
        '''
        Args:
            name::DATE - tuple(str, str or int)
                First value is a string equal to: 'day', 'month' or 'year'
                Second value can be a str or int, and either represents day, year as int or month's name as a str
           parent::dict
                 DateEntry object of higher order in terms of date
                 ex. a DateEntry instance of param date[0] == 'day' will have a DateEntry parent with date[0] == 'month'
                 ex2. a DateEntry instance with param 'year' won't have any parent as it is of highest order
        '''

        self.date: DATE = date
        self.parent: DateEntry = parent

        # Contains all date units of lesser order
        # (ex. a 'year' Date Entry will have children of 'month' type Date Entries)
        self.children: list[DateEntry] = []

        # Contains entries of all children that belong to this object
        self.expenseList = EntryContainer()
        self.incomeList = EntryContainer()



    # ---- Functions ---- #

    # Add new entry to the DateEntry object of current year
    # Also tell the correct child element (month) to do the same
    def add_entry(self, kwargs):
        if not all([kwargs.get('name'), kwargs.get('category'), kwargs.get('type'), kwargs.get('value'), kwargs.get('currency')]):
            return tuple(False)

        if kwargs.get('type').lower() == "expense":
            new_entry = TrackerEntry(name=kwargs.get('name'),
                                     type=kwargs.get('type'),
                                     category=kwargs.get('category'),
                                     value=kwargs.get('value'),
                                     currency=kwargs.get('currency'),
                                     wallet=kwargs.get('wallet'),
                                     date=FT_Time.now)
            self.expenseList.add_entry(new_entry)
            self.add_entry_to_children(kwargs)
            return (True, new_entry)

        elif kwargs.get('type').lower() == "income":
            new_entry = TrackerEntry(name=kwargs.get('name'),
                                     type=kwargs.get('type'),
                                     category=kwargs.get('category'),
                                     value=kwargs.get('value'),
                                     currency=kwargs.get('currency'),
                                     wallet=kwargs.get('wallet'),
                                     date=FT_Time.now)
            self.incomeList.add_entry(new_entry)
            self.add_entry_to_children(kwargs)
            return (True, new_entry)

        else:
            return tuple(False)

    # Each time a new entry is added, all children of this DateEntry object will do the same
    # Order: DateEntry(year) -> DateEntry(month) -> DateEntry(day)
    def add_entry_to_children(self, entry):
        if len(self.children) == 0:
            return

        if self.date[0] == "year":
            # Add entry to current month
            self.children[FT_Time.now.tm_mon-1].add_entry(entry)
        elif self.date[0] == "month":
            # Add entry to the current day
            self.children[FT_Time.now.tm_mday-1].add_entry(entry)
        else:
            return

    # Get a total sum of all expenses
    def get_total_expenses(self) -> float:
        return self.expenseList.get_total()

    # Get a total sum of all income
    def get_total_income(self) -> float:
        return self.incomeList.get_total()

    def get_all_entries(self) -> list[TrackerEntry]:
        return self.incomeList.entries + self.expenseList.entries

    # Should only be used if the instance of DataEntry is of 'year' type
    def create_months(self, months):
        self.children = [DateEntry(DATE(("month", month)), parent=self) for month in months]

    # Should only be used if the instance of DataEntry is of 'month' type
    def create_days(self, length: int):
        self.children = [DateEntry(DATE(("day", day)), parent=self) for day in range(1, length+1)]