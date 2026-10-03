# Design Patterns

This directory contains implementations of foundational software design patterns from the Gang of Four catalog.

## Tasks

### 0. Factory — Extending a registry (`0-factory.py`)
Demonstrates the Factory (creational) design pattern using a registry dictionary to map vehicle kind names to their classes. New vehicle types (e.g., `Scooter`) can be registered from the outside via `register_kind()` without modifying the core creation logic (`create()`), upholding the Open/Closed Principle.

### 1. Observer — Adding a new subscriber (`1-observer.py`)
Demonstrates the Observer (behavioral) design pattern. `NewsSubject` publishes events to observers based on topic subscriptions without knowing concrete listener implementations. Implements `SmsObserver` subscribed exclusively to the `"breaking"` topic.

### 2. Decorator — Adding a new wrapper (`2-decorator.py`)
Demonstrates the Decorator (structural) design pattern. Implements `CaramelDecorator`, wrapping any `Beverage` object to dynamically add toppings and calculate costs through object composition, avoiding subclass explosion.
