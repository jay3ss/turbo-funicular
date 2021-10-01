"""Module for defining feeds"""
import abc


class BaseFeed(abc.ABC):
    """Base class for feeds to inherit from"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._spider = None
        self._articles = None

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
