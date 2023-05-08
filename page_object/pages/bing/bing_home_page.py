from __future__ import annotations

from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from page_object.elements.web_ui_element import WebUiElement
from page_object.pages.base_page_with_accept_cookies import BaseWebPageWithAcceptCookies
from page_object.pages.base_search_page import BaseSearchPage


class BingBrowserHomePage(BaseWebPageWithAcceptCookies, BaseSearchPage):
    """
    This class represents the Bing Search engine home page
    """

    locators = dict(
        search_input=(By.CSS_SELECTOR, "#sb_form_q"),
        accept_cookies_button=(By.CSS_SELECTOR, '#bnp_btn_accept'),
        search_result_container=(By.CSS_SELECTOR, 'ol#b_results li.b_algo'),
        search_result_title=(By.CSS_SELECTOR, 'h2'),
        search_result_description_1=(By.CSS_SELECTOR, 'p'),
        search_result_description_2=(By.CSS_SELECTOR, '.tab-content'),
        search_result_description_3=(By.CSS_SELECTOR, '.sa_uc'),
        page_number=(By.XPATH, '//nav[@role="navigation"]//a[text()="{page_number}"]'),

    )

    def get_url(self) -> str:
        return "https://www.bing.com/"

    def accept_cookies(self) -> BingBrowserHomePage:
        accept_cookies_button = self.element(locator=self.locators["accept_cookies_button"])
        accept_cookies_button.click()
        return self

    def navigate_to_page_number(self, page_number: int) -> BingBrowserHomePage:
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
        for num in range(3):
            locator_name = f"search_result_description_{num + 1}"
            locator = self.locators[locator_name]
            try:
                description_element = container.element(locator=locator)
            except NoSuchElementException:
                pass
            else:
                return description_element.text
        raise LookupError(f'')

