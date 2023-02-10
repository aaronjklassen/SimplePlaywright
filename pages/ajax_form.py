from playwright.sync_api import Page, expect

class AjaxFormPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.name_txt = self.page.locator('#title')
        self.comment_txt = self.page.locator('#description')
        self.submit_btn = self.page.locator('#btn-submit')

    def fillInForm(self, name_p: str, comment_p: str) -> None:
        self.name_txt.fill(name_p)
        self.comment_txt.fill(comment_p)

    def submitForm(self) -> bool:
        self.submit_btn.click()
        expect(self.page.locator('#submit-control')).to_be_visible()
        testing = self.page.locator('#submit-control').text_content()
        return 'Ajax Request is Processing!' in self.page.locator('#submit-control').text_content()