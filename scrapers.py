"""Module for defining scrapers"""
import abc


class BaseScraper(abc.ABC):
    """Base class for all scrapers to inherit from"""

    def __init__(self, name: str, url: str, freq: int) -> None:
        self.name = name
        self.url = url
        self.frequency = freq
        self._articles = None

    @abc.abstractmethod
    def run(self) -> None:
        """
        Method to start the scraper
        """

    @abc.abstractmethod
    def is_finished(self) -> bool:
        """
        Method to query if the scraper is finished scraping
        """
