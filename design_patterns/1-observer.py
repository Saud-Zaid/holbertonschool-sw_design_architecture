#!/usr/bin/env python3
"""Observer pattern: add a new subscriber without modifying the publisher."""
from __future__ import annotations
from typing import Protocol


class Observer(Protocol):
    """Protocol for news observers."""

    def update(self, topic: str, data: str) -> None:
        """Receive an event notification."""
        ...


class NewsSubject:
    """Publish news events to observers filtered by subscribed topics."""

    def __init__(self) -> None:
        """Initialize the subscriber registry."""
        self._subs: dict[Observer, set[str] | None] = {}

    def subscribe(
        self, observer: Observer, topics: set[str] | None = None
    ) -> None:
        """Subscribe an observer to specified topics or all topics if None."""
        if observer in self._subs:
            return  # ignore duplicate subscribe for same instance
        self._subs[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        """Remove an observer from the subscriber registry."""
        self._subs.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        """Notify all interested observers of a topic event."""
        for observer, interests in list(self._subs.items()):
            if interests is not None and topic not in interests:
                continue
            observer.update(topic, data)


class LogObserver:
    """Observer that logs news events to stdout."""

    def update(self, topic: str, data: str) -> None:
        """Print log notification."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that sends news events by email."""

    def update(self, topic: str, data: str) -> None:
        """Print email notification."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that sends urgent news events by SMS."""

    def update(self, topic: str, data: str) -> None:
        """Print SMS notification."""
        print(f"sms:{topic}={data}")


def main() -> None:
    """Demonstrate the observer pattern with topic filtering."""
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)  # None = receives all topics
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
