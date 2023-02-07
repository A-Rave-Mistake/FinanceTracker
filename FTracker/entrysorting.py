from entry import TrackerEntry

class EntrySort:
    def __init__(self, type: str, value: str, entries: list[TrackerEntry]):
        """
        Desc:
            Object used for quickly sorting entries within a container widget
        Args:
            type::str
                Value by which the entries will be sorted.
                Possible values: 'wallet', 'name', 'value', 'category', 'type' or 'date'
            value::str
                Sorting order.
                Possible Values: 'none', 'ascending' or 'descending'
        """

        self.type: str = type
        self.value: str = value
        self.entries: list[TrackerEntry] = entries

        self.sort_func = self.apply_sort()

    def apply_sort(self):
        value = True if self.value == "descending" else False

        if self.type == "value":
            return (self.sort_by_value, value)
        if self.type == "name":
            return (self.sort_by_name, value)
        if self.type == "type":
            return (self.sort_by_type, value)
        if self.type == "wallet":
            return (self.sort_by_wallet, value)
        if self.type == "category":
            return (self.sort_by_category, value)
        if self.type == "date":
            return (self.sort_by_date, value)

    def sort_by_value(self, entry: TrackerEntry):
        return entry.value

    def sort_by_name(self, entry: TrackerEntry):
        return entry.name

    def sort_by_wallet(self, entry: TrackerEntry):
        return entry.wallet

    def sort_by_type(self, entry: TrackerEntry):
        return entry.type

    def sort_by_category(self, entry: TrackerEntry):
        return entry.category

    def sort_by_date(self, entry: TrackerEntry):
        return entry.date

    def get_entries(self):
        self.entries.sort(key=self.sort_func[0], reverse=self.sort_func[1])
        return self.entries