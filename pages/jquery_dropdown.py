from playwright.sync_api import Page, expect

class JqueryDropdownPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.ddSearchBox_ddl = self.page.get_by_role('combobox').nth(0)
    
    def searchBoxTest(self, country_p: str) -> None:
        expect(self.ddSearchBox_ddl).to_be_visible()
        self.ddSearchBox_ddl.click()
        self.page.get_by_role('textbox').nth(1).fill(country_p)
        self.page.get_by_role('treeitem', name=country_p).click()

    def verifySearchBoxValue(self, country_p: str) -> bool:
        expect(self.ddSearchBox_ddl).to_be_visible()
        expected = self.page.locator('#select2-country-container').get_attribute('title')
        return expected == country_p

    def selectMultipleValues(self) -> bool:
        expect(self.page.get_by_role('combobox').nth(1)).to_be_visible()
        self.page.get_by_role('combobox').nth(1).click()
        self.page.locator('.select2-search__field').fill('Arkansas')
        self.page.keyboard.press("Enter")