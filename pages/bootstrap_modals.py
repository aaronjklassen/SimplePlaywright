from playwright.sync_api import Page, expect

class BootstrapModalPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page

    def openSingleModal(self) -> None:
        self.page.locator(r'#__next > section.mt-50 > div > div > div.w-8\/12.smtablet\:w-full > div:nth-child(2) > button').click()
        expect(self.page.locator('#myModal').nth(0)).to_be_visible()
    
    def verifySingleModalOpen(self) -> bool:
        modalTitle = self.page.locator('.modal-title').nth(0).text_content()
        return modalTitle == 'Modal Title'

    def openMultipleModals(self) -> None:
        self.page.locator(r'#__next > section.mt-50 > div > div > div.w-8\/12.smtablet\:w-full > div:nth-child(3) > button').click()
        expect(self.page.locator('#myMultiModal')).to_be_visible()
        expect(self.page.locator('#myMultiModal > div > div > div.modal-body > button')).to_be_visible()
        self.page.locator('#myMultiModal > div > div > div.modal-body > button').click()
        expect(self.page.locator('#mySecondModal')).to_be_visible()

    def verifyMultipleModalsOpen(self) -> bool:
        modal2title = self.page.locator('#mySecondModal > div > div > div.modal-header > h4').text_content()
        return modal2title == 'Modal 2'
