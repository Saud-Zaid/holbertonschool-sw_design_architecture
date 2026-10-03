# Design Patterns

This directory contains implementations of foundational software design patterns from the Gang of Four catalog.

## Tasks

### 0. Factory — Extending a registry (`0-factory.py`)
Demonstrates the Factory (creational) design pattern using a registry dictionary to map vehicle kind names to their classes. New vehicle types (e.g., `Scooter`) can be registered from the outside via `register_kind()` without modifying the core creation logic (`create()`), upholding the Open/Closed Principle.
