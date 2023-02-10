import pytest
from playwright.sync_api import Page, expect
from pages.home import HomePageClass
from pages.radio_button import RadioButtonPageClass
from pages.simple_form import SimpleFormPageClass
from pages.checkbox import CheckboxDemoPageClass
from pages.select_boxes import SelectBoxPageClass
from pages.input_form import InputFormPageClass
from pages.ajax_form import AjaxFormPageClass
from pages.jquery_dropdown import JqueryDropdownPageClass
from pages.bootstrap_alerts import BootstrapAlertsPageClass
from pages.bootstrap_modals import BootstrapModalPageClass
from pages.bootstrap_date_picker import BootstrapDatePickerPageClass
from pages.jquery_date_picker import JQueryDatePickerPageClass
from pages.table_pagination import TablePaginationDemoPage
from pages.table_data_search import TableDataSearchPageClass


# def test_simple_form_one_input_demo(page: Page, home_page: HomePageClass, simple_form_page: SimpleFormPageClass) -> None:
#     expect(page).to_have_title('Selenium Grid Online | Run Selenium Test On Cloud')
#     home_page.selectInputFormDemo('Simple Form Demo')
#     simple_form_page.fillSingleInputAndSubmit('Testing Simple Form')
#     assert simple_form_page.verifySingleOutput('Testing Simple Form')

# def test_simple_form_two_input_demo(page: Page, home_page: HomePageClass, simple_form_page: SimpleFormPageClass) -> None:
#     home_page.selectInputFormDemo('Simple Form Demo')
#     simple_form_page.fillTwoInputAndSubmit('10', '25')
#     assert simple_form_page.verifyTwoInputSum('35')

# def test_checkbox_one_demo(page: Page, home_page: HomePageClass, checkbox_page: CheckboxDemoPageClass) -> None:
#     home_page.selectInputFormDemo('Checkbox Demo')
#     checkbox_page.singleCheck()
#     assert checkbox_page.verifyIsChecked()

# def test_multi_checkbox_demo(page: Page, home_page: HomePageClass, checkbox_page: CheckboxDemoPageClass) -> None:
#     home_page.selectInputFormDemo('Checkbox Demo')
#     checkbox_page.multiCheck()
#     assert checkbox_page.buttonChanged()

# def test_radio_button_first_demo(page: Page, home_page: HomePageClass, radio_button_page: RadioButtonPageClass) -> None:
#     home_page.selectInputFormDemo('Radio Buttons Demo')
#     radio_button_page.selectDemoRadio('Female')
#     assert radio_button_page.verifyRadioChecked('Female')

# def test_radio_button_second_demo(page: Page, home_page: HomePageClass, radio_button_page: RadioButtonPageClass) -> None:
#     home_page.selectInputFormDemo('Radio Buttons Demo')
#     radio_button_page.selectMultipleRadios('Male', '5 to 15')
#     assert radio_button_page.verifyRadiosChecked('Male', '5 to 15')

# def test_select_boxes_first_demo(page: Page, home_page: HomePageClass, select_boxes_page: SelectBoxPageClass) -> None:
#     home_page.selectInputFormDemo('Select Dropdown List')
#     select_boxes_page.selectSingleDropdown('Thursday')
#     assert select_boxes_page.singleDropdownVerify('Thursday')

# def test_multiple_select_boxes_first_demo(page: Page, home_page: HomePageClass, select_boxes_page: SelectBoxPageClass) -> None:
#     home_page.selectInputFormDemo('Select Dropdown List')
#     select_boxes_page.selectMultipleDropdown()
#     assert select_boxes_page.selectMultipleFirstSelected()

# def test_input_form_submit_demo(page: Page, home_page: HomePageClass, input_form_page: InputFormPageClass) -> None:
#     home_page.selectInputFormDemo('Input Form Submit')
#     input_form_page.fillInForm('FirstLast NameName', 'email@email.com', 'password', 'acme inc', 'acme.com', 'Canada', 'charlottetown', '1 main st', 'address 2', 'PEI', 'C1C1C9')
#     input_form_page.submitForm()
#     assert input_form_page.formSubmitted()

# def test_ajax_form_submit_demo(page: Page, home_page: HomePageClass, ajax_form_page: AjaxFormPageClass) -> None:
#     home_page.selectInputFormDemo('Ajax Form Submit')
#     ajax_form_page.fillInForm('Name', 'Comment')
#     assert ajax_form_page.submitForm()

# def test_jquery_dropdown_demo(page: Page, home_page: HomePageClass, jquery_dropdown_page: JqueryDropdownPageClass) -> None:
#     home_page.selectInputFormDemo('JQuery Select dropdown')
#     jquery_dropdown_page.searchBoxTest('Denmark')
#     assert jquery_dropdown_page.verifySearchBoxValue('Denmark')

# def test_bootstrap_auto_alert_demo(page: Page, home_page: HomePageClass, bootstrap_alerts_page: BootstrapAlertsPageClass) -> None:
#     home_page.selectAlertsAndModalsDemo('Bootstrap Alerts')
#     bootstrap_alerts_page.testSuccessMessages('Autoclosable Success Message')
#     assert bootstrap_alerts_page.alertDisplayed('auto', 'success')

# def test_bootstrap_manual_alert_demo(page: Page, home_page: HomePageClass, bootstrap_alerts_page: BootstrapAlertsPageClass) -> None:
#     home_page.selectAlertsAndModalsDemo('Bootstrap Alerts')
#     bootstrap_alerts_page.testSuccessMessages('Normal Success Message')
#     assert bootstrap_alerts_page.alertDisplayed('normal', 'success')

# def test_bootstrap_single_modal_demo(page: Page, home_page: HomePageClass, bootstrap_modal_page: BootstrapModalPageClass) -> None:
#     home_page.selectAlertsAndModalsDemo('Bootstrap Modals')
#     bootstrap_modal_page.openSingleModal()
#     assert bootstrap_modal_page.verifySingleModalOpen()

# def test_bootstrap_multiple_modal_demo(page: Page, home_page: HomePageClass, bootstrap_modal_page: BootstrapAlertsPageClass) -> None:
#     home_page.selectAlertsAndModalsDemo('Bootstrap Modals')
#     bootstrap_modal_page.openMultipleModals()
#     assert bootstrap_modal_page.verifyMultipleModalsOpen()

# def test_bootstrap_date_picker_demo(page: Page, home_page: HomePageClass, bootstrap_date_picker_page: BootstrapDatePickerPageClass) -> None:
#     home_page.selectDatePickerDemo('Bootstrap Date Picker')
#     bootstrap_date_picker_page.enterBirthdate('1992-04-19')
#     assert bootstrap_date_picker_page.verifyBirthday('1992-04-19')

# def test_bootstrap_date_range_picker_demo(page: Page, home_page: HomePageClass, bootstrap_date_picker_page: BootstrapAlertsPageClass) -> None:
#     home_page.selectDatePickerDemo('Bootstrap Date Picker')
#     bootstrap_date_picker_page.enterDateRange('2023-01-01', '2023-01-31')
#     assert bootstrap_date_picker_page.verifyDateRange('2023-01-01', '2023-01-31')

# def test_jquery_date_picker(page: Page, home_page: HomePageClass, jquery_date_picker_page: JQueryDatePickerPageClass) -> None:
#     home_page.selectDatePickerDemo('JQuery Date Picker')
#     jquery_date_picker_page.enterDates('02/14/2023', '02/17/2023')
#     assert jquery_date_picker_page.verifyDates('02/14/2023', '02/17/2023')

# def test_table_row_change(page: Page, home_page: HomePageClass, table_pagination_page: TablePaginationDemoPage) -> None:
#     home_page.selectTableDemo('Table Pagination')
#     table_pagination_page.adjustTableRowNumber(20)
#     assert table_pagination_page.tableRowsDisplayed(20)

# def test_table_page_change(page: Page, home_page: HomePageClass, table_pagination_page: TablePaginationDemoPage) -> None:
#     home_page.selectTableDemo('Table Pagination')
#     table_pagination_page.tablePageSwitch(3)
#     assert table_pagination_page.verifyTablePageSelected(3)

# def test_table_page_change_prev(page: Page, home_page: HomePageClass, table_pagination_page: TablePaginationDemoPage) -> None:
#     home_page.selectTableDemo('Table Pagination')
#     table_pagination_page.tablePageSwitchNextOrPrev('next')
#     assert table_pagination_page.verifyTablePageSelected(2)

# def test_table_page_change_next(page: Page, home_page: HomePageClass, table_pagination_page: TablePaginationDemoPage) -> None:
#     home_page.selectTableDemo('Table Pagination')
#     table_pagination_page.tablePageSwitch(2)
#     table_pagination_page.tablePageSwitchNextOrPrev('prev')
#     assert table_pagination_page.verifyTablePageSelected(1)

def test_table_data_search(page: Page, home_page: HomePageClass, table_data_search: TableDataSearchPageClass) -> None:
    home_page.selectTableDemo('Table Data Search')
    table_data_search.searchTable('Landing Page')
    assert table_data_search.verifySearchResult('Landing Page')