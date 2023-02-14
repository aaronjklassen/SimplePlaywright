import time
from playwright.sync_api import Page, expect

class TableDataSearchPageClass:
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_txt = self.page.locator('#task-table-filter')
        self.taskTable = self.page.locator('#task-table')
        self.filteredTaskTable = self.page.locator('.table-responsive').nth(1)

    def searchTable(self, searchTerm_p: str) -> None: 
        self.search_txt.type(searchTerm_p)

    def verifySearchResult(self, searchTerm_p: str) -> bool:
        resultRows = self.taskTable.locator('tbody > tr').count()
        searchResult = None
        time.sleep(100/1000)
        for i in range(resultRows):
            if str(self.taskTable.locator("tbody > tr").nth(i).get_attribute("style")) == "None":
                searchResult = self.taskTable.locator("tbody > tr").nth(i)
        searchResultText = searchResult.text_content()
        return searchTerm_p in searchResultText

    def filterTable(self, filterColumn_p: str, filterTerm_p: str) -> bool:
        filterButton = self.page.locator('.btn-filter')
        filterFields = {
            'user id' : self.page.locator('.filters > th').nth(0).locator('input'),
            'task' : self.page.locator('.filters > th').nth(1).locator('input'),
            'name' : self.page.locator('.filters > th').nth(2).locator('input'),
            'progress' : self.page.locator('.filters > th').nth(3).locator('input')
        }
        expect(filterFields[filterColumn_p]).to_be_visible()
        filterButton.click()
        expect(filterFields[filterColumn_p]).to_be_enabled()
        filterFields[filterColumn_p].type(filterTerm_p)

    def verifyFilter(self, filterColumn_p: str, filterTerm_p: str) -> bool:
        tableRowsCount = self.filteredTaskTable.locator('tbody > tr').count()
        filteredresult = None
        columns = {
            'user id'  : 0,
            'task'     : 1,
            'name'     : 2,
            'progress' : 3
        }

        for i in range (tableRowsCount):
            print(f'>>> { self.filteredTaskTable.locator("tbody > tr").nth(i).get_attribute("style") } <<<')
            if str(self.filteredTaskTable.locator('tbody > tr').nth(i).get_attribute('style')) == "None":
                filteredResult = self.filteredTaskTable.locator('tbody > tr').nth(i)        
        filteredTerm = filteredResult.locator('td').nth(columns[filterColumn_p]).text_content()

        return filteredTerm == filterTerm_p