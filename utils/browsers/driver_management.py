import os.path

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from root import ROOT_PATH
from utils.enums import Browser


def get_web_driver(browser: Browser, width: int, height: int, headless: bool) -> WebDriver:
    """
    Instantiates the web driver
    :param browser: browser type
    :param width: browser window width
    :param height: browser window height
    :param headless: specifies if the browser should be headless
    :return:
    """
    driver_getter_map = {
        Browser.chrome: __get_chrome,
        Browser.firefox: __get_firefox,
    }
    driver_getter = driver_getter_map[browser]
    driver_path = os.path.join(ROOT_PATH, "web_drivers")
    driver = driver_getter(path=driver_path, headless=headless)
    driver.set_window_size(width=width, height=height)
    return driver


def __get_chrome(path: str, headless: bool) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')

    executable_path = ChromeDriverManager(path=path).install()
    service = ChromeService(executable_path=executable_path)

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def __get_firefox(path: str, headless: bool) -> webdriver.Firefox:
    options = webdriver.FirefoxOptions()
    options.headless = headless

    executable_path = GeckoDriverManager(path=path).install()
    service = FirefoxService(executable_path=executable_path)

    driver = webdriver.Firefox(service=service, options=options)
    return driver
