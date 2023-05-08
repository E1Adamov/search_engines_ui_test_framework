from __future__ import annotations

import abc
from typing import List


from page_object.dataclasses.search_result import SearchResult
from page_object.elements.web_ui_element import WebUiElement
from tests.conftest import logger


class BaseSearchPage(abc.ABC):
    """
    This is the base class for the search engines search pages
    """

    @abc.abstractmethod
    def get_search_input(self) -> WebUiElement:
        """
        :return: the search string input element
        """

    @abc.abstractmethod
    def get_search_result_container_elements(self) -> [List[WebUiElement]]:
        """
        :return: list of the elements that contain search results
        """

    @abc.abstractmethod
    def _get_search_result_title(self, container: WebUiElement) -> str:
        """
        find the link text from the search result container
        """

    @abc.abstractmethod
    def _get_description(self, container: WebUiElement) -> str:
        """
        find the description from the search result container
        """

    @abc.abstractmethod
    def navigate_to_page_number(self, page_number: int) -> BaseSearchPage:
        """
        navigates to the search results page <page_number>
        """

    def get_parsed_search_results(self, query: str, quantity: int, page_limit: int = 3) -> List[SearchResult]:
        logger.info(f'{self.__class__.__name__}: search for "{query}" and get parsed results, quantity: {quantity}')
        search_input = self.get_search_input()

        logger.info(f'Input text "{query}" into the search text input')
        search_input.send_keys(query)

        logger.info(f'{self.__class__.__name__}: press ENTER')
        search_input.submit()

        logger.info(f'Read and parse search results for {self.__class__.__name__}')
        result_containers: [List[WebUiElement]] = self.get_search_result_container_elements()

        pages_parsed = 1
        while len(result_containers) < quantity and pages_parsed < page_limit:
            pages_parsed += 1
            logger.info(f"Navigate to search results page {pages_parsed}")
            self.navigate_to_page_number(page_number=pages_parsed)
            new_result_containers = self.get_search_result_container_elements()
            result_containers.extend(new_result_containers)

        result_containers = result_containers[:quantity]

        results = []

        for result_container in result_containers:
            title = self._get_search_result_title(container=result_container)
            logger.debug(f'{self.__class__.__name__}: Find description for search result with title"{title}"')
            description = self._get_description(container=result_container)
            result: SearchResult = SearchResult(title=title,  description=description)
            results.append(result)

        return results
