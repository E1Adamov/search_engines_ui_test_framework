import abc
from typing import Dict, Tuple, List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec

from configuration import config
from page_object.elements.web_ui_element import WebUiElement
from page_object.elements.web_ui_element_collection import WebUiElementCollection


class BaseWebPage(abc.ABC):
    """
    This is the base class for all the web page classes
    """
    locators: Dict[str, Tuple[str, str]] = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.get_url()
        self.validate_locators()
        self.driver.get(self.url)

    @abc.abstractmethod
    def get_url(self) -> str:
        """
        :return: the url of this page
        """
        raise NotImplementedError

    @classmethod
    def validate_locators(cls):
        for locator_name, locator in cls.locators.items():
            msg = f'locator {locator_name} in class {cls.__name__} must be a tuple of <By>, and the <selector value>'
            assert isinstance(locator, tuple), msg
            assert len(locator) == 2, msg

    def element(
            self,
            locator: Tuple[str, str],
            condition=ec.presence_of_element_located,
            timeout=config.WAIT_10,
    ) -> WebUiElement:
        return WebUiElement(
            driver=self.driver,
            locator=locator,
            wait_condition=condition,
            wait_timeout=timeout,
        )

    def elements(
            self,
            locator: Tuple[str, str],
            condition=ec.presence_of_element_located,
            timeout=config.WAIT_10,
    ) -> List[WebUiElement]:
        elements_collection = WebUiElementCollection(
            driver=self.driver,
            locator=locator,
            wait_condition=condition,
            wait_timeout=timeout,
        )
        elements = [
            WebUiElement(
                driver=self.driver,
                locator=locator,
                wait_condition=condition,
                wait_timeout=timeout,
                wrapped_element=element,
            )
            for element in elements_collection.wrapped_element
        ]
        return elements
