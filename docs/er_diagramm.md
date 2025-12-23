 ```mermaid
  erDiagram
    Bundle ||--o{ BundleConsents: "Содержит"
    BundleConsents }|--|{ Consents: "Одно или несколько согласий в разных сборках"

    Consents ||--o{ Documents: "Одно согласие может б"
 
    Consents {
        id UUID "id согласия."
    }
 ```