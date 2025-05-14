from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def fetch_html(self) -> str:
        pass

    @abstractmethod
    def parse_products(self) -> list:
        pass