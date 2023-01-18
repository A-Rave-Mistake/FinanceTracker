from entry import TrackerEntry

class EntrySort:
    def __init__(self, type: str, value: str, entries: list[TrackerEntry]):
        self.type: str = type
        self.value: str = value
        self.entries: list[TrackerEntry] = entries

        self.sort_func = self.apply_sort()

    def apply_sort(self):
        value = True if self.value == "descending" else False
        if self.type == "value":
            return (self.sort_by_value, value)

    def sort_by_value(self, entry: TrackerEntry):
        return entry.value

    def get_entries(self):
        self.entries.sort(key=self.sort_func[0], reverse=self.sort_func[1])
        return self.entries