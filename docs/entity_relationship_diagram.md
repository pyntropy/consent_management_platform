```mermaid
classDiagram

    class ConsentBundleTemplate {
        UUID id – id пакета согласий
        date created_at
        date updated_at
        UUID created_by
        UUID updated_by
        boll is_deleted 
        ———
        str title — название пакета
        float version — версия пакета
        List products
        List consents
    }
    

    
    class ConsentTemplate {
        +uuid id
    }
    
    class DataSet{
        +uuid id
    }

    ConsentBundleTemplate "1" o-- "0..*" Consent