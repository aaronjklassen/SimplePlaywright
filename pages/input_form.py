from playwright.sync_api import Page, expect

class InputFormPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.name_txt = self.page.locator('#name')
        self.email_txt = self.page.locator('#inputEmail4')
        self.pass_txt = self.page.locator('#inputPassword4')
        self.company_txt = self.page.locator('#company')
        self.website_txt = self.page.locator('#websitename')
        self.country_ddl = page.locator("[name=country]")
        self.city_txt = self.page.locator('#inputCity')
        self.address_txt = self.page.locator('#inputAddress1')
        self.address2_txt = self.page.locator('#inputAddress2')
        self.state_txt = self.page.locator('#inputState')
        self.zip_txt = self.page.locator('#inputZip')
        self.submit_btn = self.page.locator('#seleniumform > div.text-right.mt-20 > button')

    def fillInForm(self, name_p: str, email_p: str, pass_p: str, company_p: str, website_p: str, country_p: str, city_p: str, address_p: str, address2_p: str, state_p: str, zip_p: str) -> None:
        expect(self.name_txt).to_be_visible()
        
        self.name_txt.fill(name_p)
        self.email_txt.fill(email_p)
        self.pass_txt.fill(pass_p)
        self.company_txt.fill(company_p)
        self.website_txt.fill(website_p)
        self.country_ddl.select_option('CA')
        self.city_txt.fill(city_p)
        self.address_txt.fill(address_p)
        self.address2_txt.fill(address2_p)
        self.state_txt.fill(state_p)
        self.zip_txt.fill(zip_p)

    def submitForm(self) -> None:
        self.submit_btn.click()
    
    def formSubmitted(self) -> bool: 
        expect(self.page.locator('.success-msg')).to_be_visible()
        return self.page.locator('.success-msg').text_content() == 'Thanks for contacting us, we will get back to you shortly.'
