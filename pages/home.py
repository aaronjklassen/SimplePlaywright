from playwright.sync_api import Page, expect

class HomePageClass:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.inputForms = {
            'Simple Form Demo' : self.page.get_by_text('Simple Form Demo'),
            'Checkbox Demo' : self.page.get_by_text('Checkbox Demo'),
            'Radio Buttons Demo' : self.page.get_by_text('Radio Buttons Demo'),
            'Select Dropdown List' : self.page.get_by_text('Select Dropdown List'),
            'Input Form Submit' : self.page.get_by_text('Input Form Submit'),
            'Ajax Form Submit' : self.page.get_by_text('Ajax Form Submit'),
            'JQuery Select dropdown' : self.page.get_by_text('JQuery Select dropdown')
        }
        self.alertsAndModals = {
            'Bootstrap Alerts'   : self.page.get_by_text('Bootstrap Alerts'),
            'Bootstrap Modals'   : self.page.get_by_text('Bootstrap Modals'),
            'Window Popup Modal' : self.page.get_by_text('Window Popup Modal'),
            'Progress Bar Modal' : self.page.get_by_text('Progress Bar Modal'),
            'Javascript Alerts'  : self.page.get_by_text('Javascript Alerts'),
            'File Download'      : self.page.get_by_text('File Download')
        }

        self.datePickers = {
            'Bootstrap Date Picker' : self.page.get_by_text('Bootstrap Date Picker'),
            'JQuery Date Picker'    : self.page.get_by_text('JQuery Date Picker')
        }
        
        self.tables = {
            'Table Pagination' : self.page.get_by_text('Table Pagination'),
            'Table Data Search' : self.page.get_by_text('Table Data Search'),
            'Table Filter' : self.page.get_by_text('Table Filter'),
            'Table Sort & Search' : self.page.get_by_text('Table Sort & Search'),
            'Table Data Download' : self.page.get_by_text('Table Data Download'),
        }

    def selectInputFormDemo(self, demo_p: str) -> None:
        self.inputForms[demo_p].click()
    
    def selectAlertsAndModalsDemo(self, demo_p: str) -> None: 
        self.alertsAndModals[demo_p].click()

    def selectDatePickerDemo(self, demo_p: str) -> None:
        self.datePickers[demo_p].click()
    
    def selectTableDemo(self, demo_p: str) -> None:
        self.tables[demo_p].click()