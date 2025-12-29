# Сформировать согласие пользователя



```mermaid
sequenceDiagram
    participant c as Канал
    participant cmp as CMP
    
    Note over c, cmp: 
    c ->> cmp: POST /process
        
```



```json
{
  "userId":
  "bundleId":
  userData{
    "id": 12345,
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "preferences": {
      "theme": "dark",
      "notifications": true
    }
  },
  "status": "active"
}
```