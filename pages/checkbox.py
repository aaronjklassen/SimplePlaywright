from playwright.sync_api import Page, expect

class CheckboxDemoPageClass:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.singleCheckDemo_box = self.page.locator('#isAgeSelected')
        self.multicheck_btn = self.page.locator('#box')


    def singleCheck(self) -> None:
        expect(self.singleCheckDemo_box).to_be_visible()
        self.singleCheckDemo_box.click()
        expect(self.page.locator('#txtAge')).to_be_visible()

    def verifyIsChecked(self) -> bool:
        expected = self.page.locator('#txtAge').text_content()
        return expected == 'Success - Check box is checked'

    def multiCheck(self) -> None:
        expect(self.multicheck_btn).to_be_visible()
        self.multicheck_btn.click()
        expect(self.page.locator('#ex1-check1')).to_be_checked()
        expect(self.page.locator('#ex1-check2')).to_be_checked()
        expect(self.page.locator('#ex1-check3').nth(0)).to_be_checked()
        expect(self.page.locator('#ex1-check3').nth(1)).to_be_checked()

    def buttonChanged(self) -> bool:
        expect(self.multicheck_btn).to_be_visible()
        checkButtonText = self.multicheck_btn.get_attribute('value')
        return checkButtonText == 'uncheck all'
