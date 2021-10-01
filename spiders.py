"""Module for spiders"""
import abc

from tftime import Rate


class BaseSpider(abc.ABC):
    """Base class for spiders to implement"""

    def __init__(self, name, freq, url):
        self.name = name
        self.freq = freq
        self.url = url
        self._results = None
        self._rate = Rate(freq)

    @abc.abstractmethod
    def run(self):
        """Runs the spider"""

    @abc.abstractmethod
    def results(self):
        """Returns the results of the spider"""
