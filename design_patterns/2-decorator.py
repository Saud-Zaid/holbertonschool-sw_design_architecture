#!/usr/bin/env python3
"""Decorator pattern: add new toppings by wrapping beverage objects."""
from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract base class representing a beverage."""

    @abstractmethod
    def cost(self) -> int:
        """Return the cost of the beverage."""
        ...

    @abstractmethod
    def description(self) -> str:
        """Return the description of the beverage."""
        ...


class Coffee(Beverage):
    """Concrete beverage representing plain coffee."""

    def cost(self) -> int:
        """Return the base cost of coffee."""
        return 50

    def description(self) -> str:
        """Return the base description of coffee."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator that adds milk to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize the decorator with an inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Return beverage cost with milk added."""
        return self._inner.cost() + 10

    def description(self) -> str:
        """Return beverage description with milk added."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator that adds sugar to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize the decorator with an inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Return beverage cost with sugar added."""
        return self._inner.cost() + 5

    def description(self) -> str:
        """Return beverage description with sugar added."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator that adds caramel to a beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initialize the decorator with an inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        """Return beverage cost with caramel added."""
        return self._inner.cost() + 15

    def description(self) -> str:
        """Return beverage description with caramel added."""
        return self._inner.description() + " + caramel"


def main() -> None:
    """Demonstrate beverage decoration and cost calculation."""
    cup1 = MilkDecorator(Coffee())
    print(cup1.description(), cup1.cost())

    cup2 = MilkDecorator(SugarDecorator(Coffee()))
    print(cup2.description(), cup2.cost())

    cup3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(cup3.description(), cup3.cost())


if __name__ == "__main__":
    main()
