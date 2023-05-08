from typing import List

from selenium.webdriver.remote.webelement import WebElement

from page_object.elements.base_web_ui_element import BaseWebUiElement


class WebUiElementCollection(BaseWebUiElement):
    """
    This class wraps a list of selenium's WebElement's
    """

    def wait_and_get_element(self) -> List[WebElement]:
        elements = self.wait()
        if not isinstance(elements, list):
            elements = self.driver.find_elements(*self.locator)
        return elements
