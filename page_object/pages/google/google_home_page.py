from __future__ import annotations

from typing import List

from selenium.webdriver.common.by import By

from page_object.elements.web_ui_element import WebUiElement
from page_object.pages.base_page_with_accept_cookies import BaseWebPageWithAcceptCookies
from page_object.pages.base_search_page import BaseSearchPage


class GoogleBrowserHomePage(BaseWebPageWithAcceptCookies, BaseSearchPage):
    """
    This class represents the Google Search engine home page
    """

    locators = dict(
        search_input=(By.CSS_SELECTOR, "textarea[name=q]"),
        accept_cookies_button=(By.XPATH, '(//div[@role="none"])[last()]'),
        search_result_container=(By.XPATH, '//div[@id="rso"]/div[.//em and .//h3]'),
        search_result_title=(By.XPATH, './/h3'),
        search_result_description=(By.XPATH, './/em/ancestor::div[1]'),
        page_number=(By.CSS_SELECTOR, 'a[aria-label="Page {page_number}"]'),
    )

    def get_url(self) -> str:
        return "https://www.google.com/?hl=en"

    def accept_cookies(self) -> GoogleBrowserHomePage:
        accept_cookies_button = self.element(locator=self.locators["accept_cookies_button"])
        accept_cookies_button.click()
        return self

    def navigate_to_page_number(self, page_number: int) -> GoogleBrowserHomePage:
        locator_value = self.locators["page_number"][-1].format(page_number=page_number)
        page_number_element = self.element(locator=(self.locators["page_number"][0], locator_value))
        page_number_element.click()
        return self

    def get_search_input(self) -> WebUiElement:
        return self.element(locator=self.locators["search_input"])

    def get_search_result_container_elements(self) -> List[WebUiElement]:
        return self.elements(locator=self.locators["search_result_container"])

    def _get_search_result_title(self, container: WebUiElement) -> str:
        return container.element(locator=self.locators["search_result_title"]).text

    def _get_description(self, container: WebUiElement) -> str:
        return container.element(locator=self.locators["search_result_description"]).text
