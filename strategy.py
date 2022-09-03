from __future__ import annotations
from abc import ABC, abstractmethod
import json


class RenderDocumentContext:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def format(self, title: str, body: str) -> None:
        result = self._strategy.render(title, body)
        print(result)


class Strategy(ABC):
    @abstractmethod
    def render(self, title: str, body: str):
        pass


class MarkdownFromat(Strategy):
    def render(self, title: str, body: str):
        return "# %s \n %s" % (title, body)


class JSONFormat(Strategy):
    def render(self, title: str, body: str):
        return json.dumps({
            "title": title,
            "body": body
        })


class HTMLFormat(Strategy):
    def render(self, title: str, body: str):
        return "<html>\n<h1>%s</h1>\n<p>%s</p>\n</html>" % (title, body)


context = RenderDocumentContext(MarkdownFromat())
context.format("Mi titulo", "Mi cuerpo")

context = RenderDocumentContext(JSONFormat())
context.format("Mi titulo", "Mi cuerpo")

context = RenderDocumentContext(HTMLFormat())
context.format("Mi titulo", "Mi cuerpo")
