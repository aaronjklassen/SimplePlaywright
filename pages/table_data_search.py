from playwright.sync_api import Page, expect

class TableDataSearchPageClass:
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.filter_txt = self.page.locator('#task-table-filter')
        self.taskTable = self.page.locator('#task-table')

    def searchTable(self, searchTerm_p: str) -> None: 
        self.filter_txt.type(searchTerm_p)

    def verifySearchResult(self, searchTerm_p: str) -> bool:
        resultRows = self.taskTable.locator('tbody > tr').count()
        searchResult = None
        for i in range(resultRows):
            if str(self.taskTable.locator("tbody > tr").nth(i).get_attribute("style")) == "None":
                print(f'>>>> { self.taskTable.locator("tbody > tr").nth(i).get_attribute("style") } <<<<', end='\n')
                searchResult = self.taskTable.locator("tbody > tr").nth(i)

        searchResultText = searchResult.text_content()
        return searchTerm_p in searchResultText