from pathlib import Path
from playwright.sync_api import Page
import pytest
import pytest_html
from pytest_html import extras
from pages.home import HomePageClass
from pages.simple_form import SimpleFormPageClass
from pages.checkbox import CheckboxDemoPageClass
from pages.radio_button import RadioButtonPageClass
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

url = 'https://www.lambdatest.com/selenium-playground/'

@pytest.fixture(autouse=True)
def setup(page: Page) -> None:
    page.goto(url)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("reports/screenshots/")
            screenshot_dir.mkdir(exist_ok=True)
            screenshotFolder = str(item.nodeid).replace('/', '-').replace('_', '-').replace('.', '-').replace('::', '-').replace('[', '-').replace(']', '').replace(' ', '-')
            print(f' >>>> reports/screenshots/{ screenshotFolder.lower() }/test-failed-1.png <<<<< ', end='\n')
            screen_file = f'screenshots/{ screenshotFolder.lower() }/test-failed-1.png' 
            page.screenshot(path=screen_file)

        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra

@pytest.fixture
def home_page(page: Page) -> HomePageClass:
    return HomePageClass(page)

@pytest.fixture
def simple_form_page(page: Page) -> SimpleFormPageClass:
    return SimpleFormPageClass(page)

@pytest.fixture
def checkbox_page(page: Page) -> CheckboxDemoPageClass:
    return CheckboxDemoPageClass(page)

@pytest.fixture
def radio_button_page(page: Page) -> RadioButtonPageClass:
    return RadioButtonPageClass(page)

@pytest.fixture
def select_boxes_page(page: Page) -> SelectBoxPageClass:
    return SelectBoxPageClass(page)

@pytest.fixture
def input_form_page(page: Page) -> InputFormPageClass:
    return InputFormPageClass(page)

@pytest.fixture
def ajax_form_page(page: Page) -> AjaxFormPageClass:
    return AjaxFormPageClass(page)

@pytest.fixture
def jquery_dropdown_page(page: Page) -> JqueryDropdownPageClass:
    return JqueryDropdownPageClass(page)

@pytest.fixture
def bootstrap_alerts_page(page: Page) -> BootstrapAlertsPageClass:
    return BootstrapAlertsPageClass(page)

@pytest.fixture
def bootstrap_modal_page(page: Page) -> BootstrapModalPageClass:
    return BootstrapModalPageClass(page)

@pytest.fixture
def bootstrap_date_picker_page(page: Page) -> BootstrapDatePickerPageClass:
    return BootstrapDatePickerPageClass(page)

@pytest.fixture
def jquery_date_picker_page(page: Page) -> JQueryDatePickerPageClass:
    return JQueryDatePickerPageClass(page)

@pytest.fixture
def table_pagination_page(page: Page) -> TablePaginationDemoPage:
    return TablePaginationDemoPage(page)

@pytest.fixture
def table_data_search(page: Page) -> TableDataSearchPageClass:
    return TableDataSearchPageClass(page)