class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.click()
        element.fill(value)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str, timeout: int = 10000) -> bool:
        try:
            self.page.locator(locator).first.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False
