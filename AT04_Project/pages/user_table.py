from typing import List, Optional
from playwright.sync_api import Locator
from core.base_page import BasePage

class UserTable(BasePage):
     # ===== LOCATORS =====
    def table(self) -> Locator:
        return self.page.locator("table")
    
    def rows(self) -> Locator:
        return self.table().locator("tbody tr")

    def spinner(self) -> Optional[Locator]:
        """ Override nếu project có loading/spinner """
        return self.page.locator(".oxd-loading-spinner")
    
    def next_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Go to next page")

    def prev_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Go to previous page")
    
     # ===== WAITS =====
    def wait_table_ready(self):
        """
        Table ready = có row + spinner biến mất
        """
        self.rows().first.wait_for(state="visible")

        if self.spinner():
            try:
                self.spinner().wait_for(state="hidden", timeout=5000)
            except:
                pass  # spinner không tồn tại → ignore

    # ===== CORE ACTIONS =====
    def get_cell_text(self, row: int, col: int) -> str:
        """
        Get text of a specific cell
        """
        self.wait_table_ready()

        return (
            self.rows()
            .nth(row)
            .locator("td")
            .nth(col)
            .inner_text()
            .strip()
        )
    
    def get_row_values(self, row: int) -> List[str]:
        """
        Get all values of a row
        """
        self.wait_table_ready()

        cells = self.rows().nth(row).locator("td")
        return [
            cells.nth(i).inner_text().strip()
            for i in range(cells.count())
        ]
    
    def get_column_values(self, col: int) -> List[str]:
        """
        Get all values of a column
        """
        self.wait_table_ready()

        values = []
        rows = self.rows()

        for i in range(rows.count()):
            values.append(
                rows.nth(i)
                .locator("td")
                .nth(col)
                .inner_text()
                .strip()
            )
        return values
    
    # ===== SEARCH / ASSERT =====
    def is_value_exist_in_column(self, col: int, expected: str) -> bool:
        """
        Check value exist in column (current page)
        """
        column_values = self.get_column_values(col)
        return any(expected == value for value in column_values)
    
    def find_row_index_by_column_value(self, col: int, expected: str) -> Optional[int]:
        """
        Return row index if found, else None
        """
        rows = self.rows()

        for i in range(rows.count()):
            cell_text = (
                rows.nth(i)
                .locator("td")
                .nth(col)
                .inner_text()
                .strip()
            )
            if cell_text == expected:
                return i
        return None

    # ===== PAGINATION =====
    def go_next_page(self):
        if self.next_btn().is_enabled():
            self.next_btn().click()
            self.wait_table_ready()

    def go_prev_page(self):
        if self.prev_btn().is_enabled():
            self.prev_btn().click()
            self.wait_table_ready()