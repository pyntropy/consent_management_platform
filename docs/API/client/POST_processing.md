

Метод предназначен для передачи в СМР атрибутов застрахованнного
по полису лица и, если необходимо, его представителя.

POST /api/v1/processing/bundle/<bundle>

В бандле выбираются согласия и


ПОЛУЧИТЬ БАНДЛ НУЖНО ПОТОМУ ЧТО ИНАЧЕ ПРИДЕТСЯ ОПРЕДЕЛЯТЬ ПО НАБОРУ ПЕРЕДАННЫХ ДАННЫХ

```json
{
  "insured": {
    "role": "self | dependent",
    "requires_representative": true,
    "personal_data": {
      "full_name": "Иванова Мария Петровна",
      "birth_date": "1985-03-20",
      "document": {
        "type": "passport_rf",
        "series": "4510",
        "number": "123456",
        "issue_date": "2010-05-20",
        "issuing_authority": "ОУФМС России по г. Москве"
      },
      "adresses": {
        "match": "true | false",
        "registration_address": "123456, г. Москва, ул. Примерная, д. 1, кв. 15",
        "actual_address": "123456, г. Москва, ул. Примерная, д. 1, кв. 15"
      },
      "contact_info": {
        "phone": "+79001234567",
        "email": "ivanov@example.com"
      }
    },
    "representative": {
      "relation": "parent | guardian | trustee",
      "personal_data": {
        "full_name": "Иванова Мария Петровна",
        "birth_date": "1985-03-20",
        "identity_document": {
          "type": "passport",
          "series": "4509",
          "number": "654321",
          "issue_date": "2000-01-01",
          "issued_by": "Отделом УФМС России по г. Москве"
        },
        "contact_info": {
          "phone": "+79007654321",
          "email": "maria@example.com",
          "address": "г. Москва, ул. Примерная, д. 1"
        }
      }
    }
```

