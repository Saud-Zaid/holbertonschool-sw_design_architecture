# UML Intro — Library Loan System

This project introduces UML (Unified Modeling Language) to represent software systems using Mermaid syntax.

## Tasks

### 0. Class Diagram (`0-class_diagram.mmd`)
Represents the structural model of the Library Loan System:
- **Classes**: `Library`, `Book`, `User`, `Loan`
- **Attributes**: Typed using Python conventions (`str`, `bool`)
- **Methods**: Representing system behaviors
- **Relationships & Multiplicities**:
  - `Library "1" *-- "0..*" Book` (Composition)
  - `Library "1" *-- "0..*" User` (Composition)
  - `Library "1" *-- "0..*" Loan` (Composition)
  - `Loan "0..*" --> "1" Book` (Directed Association)
  - `Loan "0..*" --> "1" User` (Directed Association)

### 1. Sequence Diagram (`1-sequence_diagram.mmd`)
Models the dynamic interaction flow when a user borrows a book:
1. `User->>Library: create_loan()` — The user requests the library to create a loan.
2. `Library->>Book: mark_as_unavailable()` — The library asks the book to mark itself as unavailable.
3. `create participant Loan` & `Library->>Loan: create_loan()` — The loan participant is dynamically instantiated, and the library interacts with it.
4. `Library-->>User: loan created` — The library returns confirmation to the user.
