#Mini Proyecto: API de Gestión de Libros con Flask

#Objetivo: Crear una API RESTful para gestionar libros usando Flask, SQLite, Blueprints y retornando JSON.

#Requisitos:
#1. Usar Flask y SQLite3
#2. Organizar el código con Blueprints
#3. Solo endpoints JSON (sin vistas HTML)
#4. Base de datos SQLite con una tabla "libros"
#5. Implementar operaciones CRUD básicas

#Estructura de la tabla `libros`:

""" CREATE TABLE libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    anio_publicacion INTEGER
); """

#Endpoints a implementar:
""" | Método | Ruta           | Función                     |
|--------|----------------|----------------------------|
| GET    | /libros        | Obtener todos los libros    |
| GET    | /libros/<int:id> | Obtener un libro por ID     |
| POST   | /libros        | Agregar nuevo libro        |
| PATCH  | /libros/<int:id> | Actualizar libro existente  |
| DELETE | /libros/<int:id> | Eliminar libro             | """

#Especificaciones:
""" 1. GET /libros: Devuelve lista completa de libros en JSON
2. GET /libros/<id>: Devuelve un libro específico (404 si no existe)
3. POST /libros: Crea nuevo libro con datos JSON (validar campos)
4. PATCH /libros/<id>: Actualiza libro existente (responder 404 si no existe)
5. DELETE /libros/<id>: Elimina un libro (responder 404 si no existe)
 """
 
#Estructura de proyecto sugerida:

""" proyecto_libros/
├── app.py
├── database.py
└── libros/
    └── libros_bp.py """

#Pasos básicos:
""" 1. Configurar entorno Flask
2. Crear Blueprint para rutas de libros
3. Implementar funciones de conexión a SQLite
4. Programar los endpoints CRUD
5. Probar con Insomnia """

#Entrega:
""" - Código completo en GitHub
- Script SQL para crear la tabla
- Colección Postman/curl para probar los endpoints """

#Consejos para novatos:
""" 1. Usar "sqlite3.Row" para obtener diccionarios
2. Validar existencia de campos en JSON
3. Manejar errores con códigos HTTP apropiados
4. Cerrar conexiones a BD correctamente
5. Usar "jsonify" para todas las respuestas """

#Ejemplo de respuesta GET /libros:
[
    {
        "id": 1,
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "anio_publicacion": 1943
    }
]