import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Modo headless - necesario para CI/CD
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()


# CAPTURA DE SCREENSHOTS

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{report.nodeid.replace('::', '_')}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\n Screenshot guardado: {file_path}\n")

            # Adjuntar al HTML si pytest-html está presente
            if pytest_html and hasattr(report, "extra"):
                screenshot_rel = os.path.relpath(file_path, os.getcwd())
                html = (
                    f'<div><img src="{screenshot_rel}" '
                    f'style="width:600px;border:1px solid #ccc;" '
                    f'alt="screenshot"></div>'
                )
                report.extra.append(pytest_html.extras.html(html))



# MANEJO DE pytest-html 

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


