import abc
from typing import Optional, Tuple, List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseWebUiElement(abc.ABC):
    """
        This is a base class for classes that represent one element, and multiple elements
        it wraps the selenium's WebElement and adds some extra functional on top:
        - automatic wait
        - allows to override and thus customize any WebElement's method
    """
    def __init__(
            self,
            driver: WebDriver,
            locator: Tuple[str, str],
            wait_timeout: int,
            wait_condition: ec,
            wrapped_element: Optional[WebElement] = None
    ):
        self.driver = driver
        self.locator = locator
        self.wait_timeout = wait_timeout
        self.wait_condition = wait_condition
        self.wrapped_element: WebElement | List[WebElement] = wrapped_element or self.wait_and_get_element()

    @abc.abstractmethod
    def wait_and_get_element(self) -> WebElement:
        """
        it first waits for the element, and then finds it
        """

    def wait(self) -> Optional[WebElement]:
        """
        waits for the element
        :return: whatever the wait method returns
        """
        web_driver_wait = WebDriverWait(driver=self.driver, timeout=self.wait_timeout)
        return web_driver_wait.until(
            method=self.wait_condition(locator=self.locator),
            message=f'wait for element "{self.locator}" timed out',
        )

    def __getattr__(self, item):
        return getattr(self.wrapped_element, item)
