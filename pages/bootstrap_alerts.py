import time
from playwright.sync_api import Page, expect

class BootstrapAlertsPageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.buttons = {
            'Autoclosable Success Message' : self.page.get_by_role('button', name='Autoclosable Success Message'),
            'Normal Success Message' : self.page.get_by_role('button', name='Normal Success Message'),
            'Autoclosable Info Message' : self.page.get_by_role('button', name='Autoclosable Info Message'),
            'Normal Info Message' : self.page.get_by_role('button', name='Normal Info Message'),
            'Autoclosable Warning Message' : self.page.get_by_role('button', name='Autoclosable Warning Message'),
            'Normal Warning Message' : self.page.get_by_role('button', name='Normal Warning Message'),
            'Autoclosable Danger Message' : self.page.get_by_role('button', name='Autoclosable Danger Message'),
            'Normal Danger Message' : self.page.get_by_role('button', name='Normal Danger Message'),
        }
    
    def testSuccessMessages(self, successMessage_p: str) -> None:
        expect(self.page.locator('.alert-success-auto')).not_to_be_visible()
        time.sleep(350/1000)
        self.buttons[successMessage_p].click()

    def alertDisplayed(self, autoOrNormal_p: str, alertType_p: str) -> None:
        autoalerts = {
            'success' : self.page.locator('.alert-success-auto'),
            'info' : self.page.locator('.alert-info-auto'),
            'warning' : self.page.locator('.alert-warning-auto'),
            'danger' : self.page.locator('.alert-danger-auto'),
        }
        manualalerts = {
            'success' : self.page.locator('.alert-success-manual'),
            'info' : self.page.locator('.alert-info-manual'),
            'warning' : self.page.locator('.alert-warning-manual'),
            'danger' : self.page.locator('.alert-danger-manual'),
        }

        beforeAlert = self.page.locator('div.alert').count()
        
        if autoOrNormal_p == 'auto':
            expect(autoalerts[alertType_p]).to_be_visible()
            time.sleep(6)
            expect(autoalerts[alertType_p]).not_to_be_visible()
        elif autoOrNormal_p == 'normal':
            expect(manualalerts[alertType_p]).to_be_visible()
            manualalerts[alertType_p].locator('.close').click()
            expect(manualalerts[alertType_p]).not_to_be_visible()



        afterAlert = self.page.locator('div.alert').count()
        print(f' >>>>> After Alert: {str(afterAlert)} <<<<< ', end='\n')

        return afterAlert == (beforeAlert - 1)