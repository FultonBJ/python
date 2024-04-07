```mermaid
classDiagram
class Context
Context 0-- Strategy :uses
class StrategyHello {
    <<abstract>>
    +execute()
}
Strategy <|-- ConcreateStrategy1
Strategy <|-- ConcreateStrategy2
ConcreateStrategy1: +execute()
ConcreateStrategy2: +execute()
```

# Bridge pattern

```mermaid
classDiagram
class Abstraction {
    <<abstract>>
}
RefinedAbstraction1 --|> Abstraction
RefinedAbstraction2 ==|> Abstraction
class Implemntation {
    <<abstract>>
    +implementation()
}
Abstraction o-- Implementation :uses
ConcreteImplementation <|-- ConcreteImplementation1
ConcreteImplementation <|-- ConcreteImplementation2
```