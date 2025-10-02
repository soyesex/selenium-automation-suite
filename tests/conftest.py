# tests/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    """Esta función enseña a Pytest a entender nuestros nuevos comandos."""
    parser.addoption("--browser", action="store", default="chrome", help="Elige el navegador: chrome o firefox")
    parser.addoption("--headless", action="store_true", help="Ejecuta el navegador en modo headless")

@pytest.fixture(scope="function")
def driver(request):
    """
    Esta es nuestra fixture. Creará y destruirá el driver para cada test.
    'request' es un objeto especial de Pytest que nos da acceso a la configuración.
    """
    # Leer los valores de los comandos que enseñamos a Pytest
    browser_name = request.config.getoption("browser")
    is_headless = request.config.getoption("headless")
    
    driver_instance = None

    # Configurar y lanzar el navegador elegido
    if browser_name.lower() == "chrome":
        chrome_options = ChromeOptions()
        if is_headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080") # Importante en headless
        driver_instance = webdriver.Chrome(options=chrome_options)
    
    # Aquí podríamos añadir lógica para otros navegadores como Firefox
    # elif browser_name.lower() == "firefox":
    #     ...

    # 'yield' es la clave de las fixtures. Pasa el driver_instance al test.
    # El código después del yield se ejecutará DESPUÉS de que el test termine.
    yield driver_instance
    
    # Limpieza: Cierra el navegador
    if driver_instance:
        driver_instance.quit()