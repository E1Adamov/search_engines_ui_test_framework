__doc__ = """
    This module is part of pytest's infrastructure
    It contains fixtures and hooks
"""

import logging
from typing import List
from distutils.util import strtobool

import pytest
from _pytest.fixtures import SubRequest
from _pytest.config.argparsing import Parser
from selenium.webdriver.remote.webdriver import WebDriver

from utils.browsers.driver_management import get_web_driver
from utils.enums import Browser


logger = logging.getLogger(__name__)


def pytest_addoption(parser: Parser):  # noqa
    """
    This fixture add CLI options that can be user when running tests
    """
    parser.addoption(
        "--browser",
        required=True,
        choices=Browser._member_names_,  # noqa
    )

    parser.addoption(
        "--headless",
        required=True,
        type=strtobool,
    )

    parser.addoption(
        "--browser_width",
        required=True,
        type=int,
    )

    parser.addoption(
        "--browser_height",
        required=True,
        type=int,
    )

    parser.addoption(
        "--search_string",
        required=False,
    )


@pytest.fixture
def web_drivers(request: SubRequest) -> List[WebDriver]:
    """
    This fixture instantiates web browser(s) based in the CLI parameters:
    --browser:
        >>> from utils.enums import Browser
        it can be any of the Browser enum member names
    --browser_width: integer
    --browser_height: integer
    --headless: boolean
    """
    browser_name: str = request.config.getoption("--browser")
    browser: Browser = Browser[browser_name]
    browser_quantity: int = request.param

    drivers: List[WebDriver] = []

    for instance_number in range(browser_quantity):
        logger.info(f'Instantiate browser {browser_name}, instance #{instance_number + 1}')
        web_driver: WebDriver = get_web_driver(
            browser=browser,
            width=request.config.getoption("--browser_width"),
            height=request.config.getoption("--browser_height"),
            headless=request.config.getoption("--headless"),
        )
        drivers.append(web_driver)

    yield drivers

    for driver in drivers:
        driver.quit()


@pytest.fixture(autouse=True)
def mute_noisy_loggers():
    logger_names = ["selenium", "urllib3"]
    for logger_name in logger_names:
        logger_ = logging.getLogger(logger_name)
        logger_.setLevel(level=logging.INFO)
