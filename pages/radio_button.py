from playwright.sync_api import Page, expect

class RadioButtonPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.genderRadios = {
            'Male'   : self.page.locator('.mr-10').nth(2),  
            'Female' : self.page.locator('.mr-10').nth(3),
            'Other'  : self.page.locator('.mr-10').nth(4),
        }
        self.ageRadios = {
            '0 to 5' : self.page.locator('.mr-10').nth(5),
            '5 to 15' : self.page.locator('.mr-10').nth(6),
            '15 to 50' : self.page.locator('.mr-10').nth(7),
        }

    def selectDemoRadio(self, mOrF_p: str) -> None:
        expect(self.page.locator('.mr-10').nth(0)).to_be_visible()
        radios = {
            'Male'   : self.page.locator('.mr-10').nth(0),
            'Female' : self.page.locator('.mr-10').nth(1)
        }

        radios[mOrF_p].click()
        self.page.locator('#buttoncheck').click()
        expect(self.page.locator('.radiobutton')).to_be_visible()

    def verifyRadioChecked(self, mOrF_p: str) -> bool:
        expected = f"Radio button '{ mOrF_p }' is checked"
        actual = self.page.locator('.radiobutton').text_content()
        return actual == expected

    def selectMultipleRadios(self, gender_p: str, age_p: str) -> None:
        expect(self.page.get_by_role('button', name="Get Values")).to_be_visible()
        
        self.genderRadios[gender_p].click()
        self.ageRadios[age_p].click()

        self.page.get_by_role('button', name="Get Values").click()

    def verifyRadiosChecked(self, gender_p: str, age_p: str) -> bool:
        expect(self.page.locator('.genderbutton')).to_be_visible()
        expect(self.page.locator('.groupradiobutton')).to_be_visible()

        expectedGenderText = gender_p
        actualGenderText = self.page.locator('.genderbutton').text_content()
        expectedAgeText = age_p
        actualAgeText = self.page.locator('.groupradiobutton').text_content().replace('-', 'to')

        genderCorrect = expectedGenderText == actualGenderText
        ageCorrect = expectedAgeText == actualAgeText

        return genderCorrect == ageCorrect