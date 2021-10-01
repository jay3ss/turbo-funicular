"""Module for article class"""
from datetime import datetime
from typing import List


class Article:
    """Class to model an article"""

    def __init__(
        self,
        title: str,
        url: str,
        img: str,
        categories: List,
        keywords: List,
        authors: List,
        published_on: datetime,
        updated_on: datetime,
    ) -> None:
        self.title = title
        self.url = url
        self.img = img
        self.categories = categories
        self.keywords = keywords
        self.authors = authors
        self.published_on = published_on
        self.updated_on = updated_on
