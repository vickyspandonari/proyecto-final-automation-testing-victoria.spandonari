import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()


# CAPTURAR SCREENSHOTS Y AGREGARLOS AL REPORTE HTML

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Solo capturar en la fase "call" (ejecución del test)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # Crear carpeta screenshots
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Nombre del archivo con timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{report.nodeid.replace('::', '_')}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            # Capturar screenshot
            driver.save_screenshot(file_path)

            # Imprimir ruta en consola
            print(f"\n Screenshot guardado: {file_path}\n")

            
            # Insertar la imagen en el HTML report
            
            if hasattr(report, "extra"):
                # Ruta relativa para que el HTML pueda mostrar la imagen
                screenshot_path_relative = os.path.relpath(
                    file_path, os.getcwd()
                )

                html = (
                    f'<div><img src="{screenshot_path_relative}" '
                    f'style="width:600px;border:1px solid #ccc;" '
                    f'alt="screenshot"></div>'
                )
                report.extra.append(pytest_html.extras.html(html))



# NECESARIO PARA QUE pytest-html FUNCIONE CON EL HOOK

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
