import time
from playwright.sync_api import Page, expect

class SelectBoxPageClass:
    def __init__(self, page: Page) -> None:
        self.page = page

    def selectSingleDropdown(self, select_p: str) -> None:
        self.page.locator('#select-demo').select_option(select_p)
        time.sleep(100)
        expect(self.page.locator('.selected-value')).to_be_visible()
    
    def singleDropdownVerify(self, expected_p: str) -> None:
        actual = self.page.locator('.selected-value').text_content()
        return expected_p in actual
    
    def selectMultipleDropdown(self) -> None:
        expect(self.page.locator('#multi-select')).to_be_visible
        self.page.locator('#multi-select').select_option(['California', 'Florida', 'Ohio', 'Washington'])

    def selectMultipleFirstSelected(self) -> bool:
        expect(self.page.locator('#printMe')).to_be_visible()
        self.page.locator('#printMe').click()
        expect(self.page.locator('.genderbutton')).to_be_visible()
        return self.page.locator('.genderbutton').text_content() == 'California'

    