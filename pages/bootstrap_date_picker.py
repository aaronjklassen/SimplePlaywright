import time
from playwright.sync_api import Page, expect

class BootstrapDatePickerPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
    
    def enterBirthdate(self, date_p: str) -> None:
        self.page.locator('#birthday').fill(date_p)

    def verifyBirthday(self, date_p: str) -> bool:
        datefield = self.page.locator('#birthday').input_value()
        return datefield == date_p

    def enterDateRange(self, startDate_p: str, endDate_p: str) -> None:
        self.page.locator('#datepicker > input').nth(0).fill(startDate_p)
        self.page.locator('#datepicker > input').nth(1).fill(endDate_p)

    def verifyDateRange(self, expectedstartDate_p: str, expectedendDate_p: str) -> bool:
        dateOneCorrect = expectedstartDate_p == self.page.locator('#datepicker > input').nth(0).input_value()
        dateTwoCorrect = expectedendDate_p == self.page.locator('#datepicker > input').nth(1).input_value()

        return dateOneCorrect == dateTwoCorrect