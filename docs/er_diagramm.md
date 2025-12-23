 ```mermaid
  erDiagram
    Bundle ||--o{ BundleConsent: "Содержит"
    BundleChains }|--|{ Chains: "Содержит"

    Chains ||--|| ConsentsChain: "Имеет"
    ConsentsChain ||--|{ Consents: "Указывает на"
 
    Consents {
        id UUID "id согласия."
        previous_id UUID "id предыдущей версии согласия."
    }
 ```