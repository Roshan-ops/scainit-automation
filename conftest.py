# import os
# import pytest
# from playwright.sync_api import sync_playwright
# from utils.config import Config

# os.makedirs("screenshots", exist_ok=True)
# os.makedirs("reports", exist_ok=True)
# os.makedirs("traces", exist_ok=True)

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=Config.HEADLESS)
#         yield browser
#         browser.close()

# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context(viewport={"width": 1440, "height": 900})
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#     yield page
#     context.tracing.stop(path="traces/trace.zip")
#     context.close()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         page = item.funcargs.get("page")
#         if page:
#             page.screenshot(path=f"screenshots/{item.name}.png", full_page=True)


import os
import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("traces", exist_ok=True)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path="traces/trace.zip")
    context.close()