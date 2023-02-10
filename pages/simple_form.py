from playwright.sync_api import Page, expect

class SimpleFormPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.user_message_first_txt = self.page.locator('#user-message').nth(0)
        self.user_message_first_submit = self.page.locator('#showInput')
        self.two_input_first_txt = self.page.locator('#sum1')
        self.two_input_second_txt = self.page.locator('#sum2')
        self.user_message_output = self.page.locator('#message')

    def fillSingleInputAndSubmit(self, text_p: str) -> None:
        self.user_message_first_txt.fill(text_p)
        self.user_message_first_submit.click()

    def fillTwoInputAndSubmit(self, field_one_txt: str, field_two_txt: str) -> None:
        self.two_input_first_txt.fill(field_one_txt)
        self.two_input_second_txt.fill(field_two_txt)
        self.page.locator('#gettotal > button').click()

    def verifySingleOutput(self, expectedText_p: str) -> bool:
        actualText = self.user_message_output.text_content()
        return expectedText_p == actualText

    def verifyTwoInputSum(self, expected_p: str) -> str:
        expect(self.page.locator('#addmessage')).to_be_visible()
        actual = self.page.locator('#addmessage').text_content()
        return expected_p == actual