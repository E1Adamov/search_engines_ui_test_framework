from __future__ import annotations

from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement

from page_object.elements.base_web_ui_element import BaseWebUiElement


class WebUiElement(BaseWebUiElement):
    """
    This class wraps selenium's WebElement
    """

    def wait_and_get_element(self) -> WebElement:
        element = self.wait()
        if not isinstance(element, WebElement):
            element = self.driver.find_element(*self.locator)
        return element

    def element(self, locator: tuple[str, str]) -> WebUiElement:
        try:
            element = self.wrapped_element.find_element(*locator)
        except StaleElementReferenceException:
            self.wrapped_element = self.wait_and_get_element()
            element = self.wrapped_element.find_element(*locator)

        return WebUiElement(
            driver=self.driver,
            locator=locator,
            wait_timeout=self.wait_timeout,
            wait_condition=self.wait_condition,
            wrapped_element=element,

        )

    def elements(self, locator: tuple[str, str]) -> list[WebUiElement]:
        selenium_elements = self.wrapped_element.find_elements(*locator)
        elements = [
            WebUiElement(
                driver=self.driver,
                locator=locator,
                wait_condition=self.wait_condition,
                wait_timeout=self.wait_timeout,
                wrapped_element=selenium_element,
            )
            for selenium_element in selenium_elements
        ]
        return elements
