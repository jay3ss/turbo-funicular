"""Module for defining feeds"""
import abc


class BaseFeed(abc.ABC):
    """Base class for feeds to inherit from"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._scraper = None
        self._parsers = None

    @abc.abstractmethod
    def subscribe(self) -> bool:
        """
        Method to subscribe to the feed
        """

    @abc.abstractmethod
    def unsubscribe(self) -> bool:
        """
        Method to unsubscribe from the feed
        """

    @abc.abstractmethod
    def run(self):
        """
        Method to start the feed
        """

    @property
    @abc.abstractmethod
    def feed(self):
        """
        Returns the results from the feed
        """
