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
