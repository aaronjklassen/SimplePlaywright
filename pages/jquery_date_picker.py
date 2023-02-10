from playwright.sync_api import Page, expect

class JQueryDatePickerPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page

    def enterDates(self, startDate_p: str, endDate_p: str) -> None:
        self.page.locator('#from').fill(startDate_p)
        self.page.locator('#to').fill(endDate_p)

    def verifyDates(self, startDate_p: str, endDate_p: str) -> bool:
        expectedOne = self.page.locator('#from').input_value() == startDate_p
        expectedTwo = self.page.locator('#to').input_value() == endDate_p

        return expectedOne == expectedTwo

