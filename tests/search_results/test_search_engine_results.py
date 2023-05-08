from typing import List

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.pages.bing.bing_home_page import BingBrowserHomePage
from page_object.pages.google.google_home_page import GoogleBrowserHomePage
from tests.conftest import logger
from utils.parallelization.run_in_threads import run_in_threads
from utils.parallelization.thread_parameters import ThreadParameters


class TestSearchEngineResults:
    """
    This test suite contains test cases related to search engines test results validation
    """

    @pytest.mark.parametrize("web_drivers", [2], indirect=True)
    def test_two_search_engines_return_10_valid_results(
            self,
            request: pytest.FixtureRequest,
            web_drivers: List[WebDriver],
    ):
        """
        1. run 2 browser processes based on the <--browser> name passed in the CLI parameters
        2. clear cookies in both
        3. Perform the following actions for Google and Bing:
            - open te home page
            - search for the <--search_string> passed in the CLI parameters
            - parse search results
                - paginate to the next page and repeat until results count == 10
        4. Validate each search result for both Google and Bing by making sure
            that at least any search result attribute contains the <--search_string>
        """

        logger.info("Clear browser cookies")
        for driver in web_drivers:
            driver.delete_all_cookies()

        driver_1, driver_2 = web_drivers

        logger.info("Open Google home page")
        google_home_page = GoogleBrowserHomePage(driver=driver_1)

        logger.info("Open Bing home page")
        bing_home_page = BingBrowserHomePage(driver=driver_2)

        search_string = request.config.getoption("--search_string")
        kwargs = {"query": search_string, "quantity": 10}

        google_results, bing_results = run_in_threads(
            ThreadParameters(target=google_home_page.get_parsed_search_results, kwargs=kwargs),
            ThreadParameters(target=bing_home_page.get_parsed_search_results, kwargs=kwargs),
        )

        logger.info(f'Google parsed search results: {google_results}')
        logger.info(f'Bing parsed search results: {bing_results}')

        for google_result in google_results:
            logger.info(f'Google results: make sure at least one attribute contains "{search_string}": {google_result}')
            msg = f'Search result {google_result} does not contain search string "{search_string}"'
            assert any(search_string.lower() in attribute.lower() for attribute in google_result.__dict__.values()), msg

        for bing_result in bing_results:
            logger.info(f'Bing results: make sure at least one attribute contains "{search_string}": {bing_result}')
            msg = f'Search result {bing_result} does not contain search string "{search_string}"'
            assert any(search_string.lower() in attribute.lower() for attribute in bing_result.__dict__.values()), msg
