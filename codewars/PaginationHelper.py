import math


class PaginationHelper:
    items_per_page = 0
    collection = []

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if not 0 <= page_index <= len(self.collection) // self.items_per_page:
            return -1
        return min(self.items_per_page * (page_index + 1), len(self.collection)) - \
               max(0, self.items_per_page * page_index)

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if not 0 <= item_index < len(self.collection):
            return -1
        return item_index // self.items_per_page
