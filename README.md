# Flask Products Backend

A simple **RESTful API** built with **Flask** for managing products. Supports **CRUD operations** and stores data in a JSON file.

---

## Features

- Create new products ✅
- Retrieve all products ✅
- Retrieve a product by ID ✅
- Update products ✅
- Delete products ✅
- Data stored locally in `products.json`
- Ready for deployment on **Railway** or similar platforms 🌍

---

## Tech Stack

- Python 3.12  
- Flask  
- JSON file storage  

---

## API Endpoints

| Method | Endpoint                  | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/`                       | Check API status                |
| GET    | `/products`               | Get all products                |
| GET    | `/products/<id>`          | Get a product by ID             |
| POST   | `/products`               | Create a new product            |
| PUT    | `/products/<id>`          | Update a product by ID          |
| DELETE | `/products/<id>`          | Delete a product by ID          |

---

## Example Requests

### Get all products
```bash
curl https://YOUR_RAILWAY_URL/products
```

### Create a new product
```bash
curl -X POST https://YOUR_RAILWAY_URL/products \
-H "Content-Type: application/json" \
-d '{"name":"Laptop","price":50000,"category":"Electronics","stock":10}'
```

### Update a product
```bash
curl -X PUT https://YOUR_RAILWAY_URL/products/1 \
-H "Content-Type: application/json" \
-d '{"price":48000,"stock":8}'
```

### Delete a product
```bash
curl -X DELETE https://YOUR_RAILWAY_URL/products/1
```

---

## Run Locally

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate environment:
- Windows (PowerShell):
```powershell
venv\Scripts\Activate.ps1
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install flask
```

4. Run the app:
```bash
python app.py
```

---

## Notes

- Flask runs on `0.0.0.0` and listens to Railway’s port automatically  
- Data is stored in `products.json`  
- API is simple, lightweight, and **perfect for practice or portfolio projects**
