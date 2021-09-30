"""Module for scrapers"""
import abc


class BaseScraper(abc.ABC):
    """Base class for scrapers to implement"""

    def __init__(self, name, freq, url):
        self.name = name
        self.freq = freq
        self.url = url
        self._results = None

    @abc.abstractmethod
    def run(self):
        """Runs the scraper"""

    @abc.abstractmethod
    def results(self):
        """Returns the results of the scraper"""
