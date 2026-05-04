# orders-rest-api-python

**API REST para gestión de pedidos — SENA ADSO**

## 🚀 Stack Tecnológico

- **Lenguaje:** Python 3.14
- **Framework Web:** FastAPI
- **ORM:** SQLAlchemy (Síncrono)
- **Base de Datos:** SQLite
- **Servidor ASGI:** Uvicorn

## 📋 Requisitos Previos

Asegúrate de tener instalado en tu sistema:
- Python 3.11 o superior
- pip (Administrador de paquetes de Python)
- Git

## 🛠️ Instrucciones de Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/alejo8933/orders-rest-api-python.git
   cd orders-rest-api-python
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv env
   # En Windows:
   env\Scripts\activate
   # En Linux/Mac:
   source env/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   Crea un archivo `.env` en la raíz del proyecto y agrega la siguiente línea:
   ```env
   DATABASE_URL=sqlite:///./orders.db
   ```

5. **Poblar la base de datos (Seed)**
   ```bash
   python seed.py
   ```

6. **Iniciar el servidor**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

## 🌐 Endpoints Disponibles

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/api/v1/health` | Verifica el estado de la API |
| `GET` | `/api/v1/orders` | Obtiene lista paginada de pedidos |
| `POST` | `/api/v1/orders` | Crea un nuevo pedido |
| `GET` | `/api/v1/orders/{orderId}` | Obtiene detalles de un pedido específico |
| `PUT` | `/api/v1/orders/{orderId}` | Reemplaza un pedido por completo |
| `PATCH` | `/api/v1/orders/{orderId}` | Actualiza parcialmente un pedido |
| `DELETE` | `/api/v1/orders/{orderId}` | Elimina un pedido |
| `GET` | `/api/v1/orders/{orderId}/items` | Obtiene los items de un pedido |
| `POST` | `/api/v1/orders/{orderId}/items` | Agrega un item al pedido |
| `PATCH` | `/api/v1/orders/{orderId}/items/{itemId}` | Actualiza un item del pedido |
| `DELETE` | `/api/v1/orders/{orderId}/items/{itemId}` | Elimina un item del pedido |
| `GET` | `/api/v1/products` | Obtiene lista paginada de productos |
| `GET` | `/api/v1/products/{productId}` | Obtiene detalles de un producto |
| `GET` | `/api/v1/customers` | Obtiene lista paginada de clientes |
| `POST` | `/api/v1/customers` | Crea un nuevo cliente |
| `PATCH` | `/api/v1/customers/{customerId}` | Actualiza parcialmente un cliente |
| `GET` | `/api/v1/customers/{customerId}` | Obtiene detalles de un cliente |

## 📖 Documentación

Una vez que el servidor esté en ejecución, puedes acceder a la documentación interactiva provista por Swagger UI en:
[http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)

## 🧪 Pruebas

Para ejecutar las pruebas automatizadas del proyecto, asegúrate de estar en el entorno virtual y ejecuta:
```bash
pytest tests/ -v
```

## 📁 Estructura del Proyecto

```text
orders-api/
├── app/
│   ├── models/         # Modelos de SQLAlchemy
│   ├── schemas/        # Esquemas de validación de Pydantic
│   ├── repositories/   # Lógica de acceso a datos
│   ├── services/       # Reglas de negocio
│   ├── routers/        # Controladores y endpoints de FastAPI
│   ├── utils/          # Utilidades (paginación, manejo de errores)
│   ├── database.py     # Configuración de base de datos
│   └── main.py         # Archivo principal de FastAPI
├── tests/              # Pruebas unitarias
├── seed.py             # Script para poblar la base de datos
├── requirements.txt    # Dependencias del proyecto
├── .env                # Variables de entorno (no versionado)
└── .gitignore          # Archivos excluidos de Git
```

## ✒️ Autor

- **alejo8933**
