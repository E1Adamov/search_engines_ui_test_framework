import abc

from selenium.webdriver.remote.webdriver import WebDriver

from page_object.pages.base_page import BaseWebPage


class BaseWebPageWithAcceptCookies(BaseWebPage, abc.ABC):
    """
    this is the base class for web pages that require cookies acceptance
    """

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.accept_cookies()

    @abc.abstractmethod
    def accept_cookies(self) -> str:
        """
        :return: accept cookies if necessary
        """
        raise NotImplementedError
