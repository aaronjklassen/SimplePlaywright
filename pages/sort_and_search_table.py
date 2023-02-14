from playwright.sync_api import Page, expect

class SearchSortTablePageClass:

    def __init__(self, page: Page) -> None:
        self.page = page