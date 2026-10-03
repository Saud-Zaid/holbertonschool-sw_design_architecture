#!/usr/bin/env python3
"""Factory pattern: extend a vehicle registry without modifying create()."""
from __future__ import annotations


class Bus:
    """Vehicle that travels on the road."""

    def mode(self) -> str:
        """Return the travel mode for a bus."""
        return "road"


class Train:
    """Vehicle that travels on rails."""

    def mode(self) -> str:
        """Return the travel mode for a train."""
        return "rails"


class Bike:
    """Vehicle that travels in a bike lane."""

    def mode(self) -> str:
        """Return the travel mode for a bike."""
        return "lane"


class Scooter:
    """Vehicle that travels in a scooter lane."""

    def mode(self) -> str:
        """Return the travel mode for a scooter."""
        return "scooter_lane"


class VehicleFactory:
    """Create vehicles by name using a registry of kinds to classes."""

    def __init__(self) -> None:
        """Initialize the factory with default vehicle mappings."""
        self._registry: dict[str, type] = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, name: str, cls: type) -> None:
        """Register a new vehicle class associated with a kind name."""
        self._registry[name] = cls

    def create(self, kind: str) -> object:
        """Instantiate and return a vehicle by its registered kind name."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind!r}")
        return self._registry[kind]()


def main() -> None:
    """Demonstrate vehicle creation via registry extension."""
    factory = VehicleFactory()

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
