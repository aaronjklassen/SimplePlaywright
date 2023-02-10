import time
from playwright.sync_api import Page, expect

class TablePaginationDemoPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.rows_ddl = self.page.locator('#maxRows')
        self.table_tbl = self.page.locator('#table-id')
        self.table_pagination = self.page.locator('.pagination_sp')

    def adjustTableRowNumber(self, rows_p: int) -> None:
        # rows = self.page.locator()
        self.rows_ddl.select_option(value=str(rows_p))

    def tableRowsDisplayed(self, rows_p: int) -> bool:
        tableRowsCount  = self.page.locator('#table-id > tbody > tr').count()
        tableRows = []
        visibleRows = []
        for i in range(tableRowsCount):
            tableRows.append(self.page.locator('#table-id > tbody > tr').nth(i))
        
        for row in tableRows:
            test = row.get_attribute("style")
            if test == "display: none;":
                continue
            else:
                visibleRows.append(row)
            
        return rows_p == len(visibleRows)

    def tablePageSwitch(self, page_p: int) -> None:
        expect(self.page.locator('.pagination-container')).to_be_visible()
        time.sleep(350/1000)
        self.page.locator('.pagination-container').get_by_text(str(page_p)).click()
    
    def tablePageSwitchNextOrPrev(self, nextOrPrev_p: str) -> None:
        expect(self.page.locator('.pagination-container')).to_be_visible()
        prev = self.page.locator('.pagination-container').get_by_text('<')
        next = self.page.locator('.pagination-container').get_by_text('>')

        if nextOrPrev_p == 'prev':
            prev.click()
        elif nextOrPrev_p == 'next':
            next.click()

    def verifyTablePageSelected(self, page_p: int) -> bool:
        expect(self.page.locator('.pagination-container')).to_be_visible()
        tablePages = []
        time.sleep(350/1000)
        activePage = self.page.locator('.pagination-container').locator('.active')

        return activePage.text_content().strip() == str(page_p)