from db_advance_manager import DBAdvanceManager


#Crearemos una funcion para mostrar los resultados de una consulta

def show_results(results, message="Resultados:"):
    if results:
        print(message)
        for row in results:
            print(row)
    else:
        print("No se encontraron resultados.")
        
        
#Definiremos la funcion donde, realizaremos las consultas

def main():
  db = DBAdvanceManager("./Python_especializado/SQLite/SQLite_Avanzado/store.db")
  #db.setup_database()
  db.connect()
  print("Conectado a la base de datos store.db")
  
  print("\nIniciando consultas avanzadas...\n")
  
  
  #1. Consultas JOIN
  print("1. Consultas JOIN:")
  
  #1.1 INNER JOIN nos permite combinar filas de dos o mas tablas basadas en una relacion entre ellas
  #En este caso, combinaremos la tabla products con la tabla categories para obtener el nombre
  query_inner = """SELECT p.name AS Product, p.price, c.name AS Category, c.id AS CategoryID
                    FROM products AS p
                    INNER JOIN categories As c ON p.category_id = c.id;"""
  results_inner = db.cursor.execute(query_inner).fetchall()
  show_results(results_inner, "Resultados de INNER JOIN:")
  
  #1.2 LEFT JOIN nos permite combinar filas de dos o mas tablas, incluyendo todas las filas de la tabla izquierda y las filas coincidentes de la tabla derecha
  #En este caso, combinaremos la tabla products con la tabla categories,
  
  print("\n2. LEFT JOIN:")
  query_left = """SELECT p.name AS Product, p.price, p.stock, c.name AS Category
                    FROM products AS p
                    LEFT JOIN categories As c ON p.category_id = c.id;"""
  results_left = db.cursor.execute(query_left).fetchall()
  show_results(results_left, "Resultados de LEFT JOIN:")
  
  #3. RIGHT JOIN no es soportado directamente por SQLite, pero podemos simularlo usando LEFT JOIN
  print("\n3. RIGHT JOIN (simulado con LEFT JOIN):")
  query_right = """SELECT c.name AS Category, c.id AS CategoryID, p.name AS Product
                    FROM categories AS c
                    LEFT JOIN products As p ON c.id = p.category_id;"""
  results_right = db.cursor.execute(query_right).fetchall()
  show_results(results_right, "Resultados de RIGHT JOIN:")
  
  #4. FULL OUTER JOIN no es soportado directamente por SQLite, pero podemos simularlo usando UNION
  print("\n4. FULL OUTER JOIN (simulado con UNION):")
  query_full_outer = """SELECT p.name AS Product, c.name AS Category
                        FROM products AS p
                        LEFT JOIN categories AS c ON p.category_id = c.id
                        UNION ALL
                        SELECT p.name AS Product, c.name AS Category
                        FROM categories AS c
                        LEFT JOIN products AS p ON c.id = p.category_id;"""
  results_full_outer = db.cursor.execute(query_full_outer).fetchall()
  show_results(results_full_outer, "Resultados de FULL OUTER JOIN:")
  
  #2. ORDER BY 
  #Nos sirve para ordenar los resultados de una consulta en orden ascendente o descendente
  print("\n5. ORDER BY:")
  
  #2.1 Ordenar por precio de productos en orden descendente
  print("Ordenando productos por precio en orden descendente:")
  query_order_by = """SELECT * FROM products ORDER BY price DESC;"""
  results_order_by = db.cursor.execute(query_order_by).fetchall()
  show_results(results_order_by, "Resultados de ORDER BY:")
  
  #2.2 Ordenar por nombre de productos en orden ascendente por categoria
  print("Ordenando productos por nombre en orden ascendente por categoria:")
  query_order_by_category = """SELECT p.name AS Product, c.name AS Category
                              FROM products AS p
                              INNER JOIN categories AS c ON p.category_id = c.id
                              ORDER BY c.name ASC;"""
  results_order_by_category = db.cursor.execute(query_order_by_category).fetchall() 
  show_results(results_order_by_category, "Resultados de ORDER BY por categoria:")
  
  #2.3 Ordenar por precio de productos en orden descendente y por el precio
  query_order_by_price = """SELECT * FROM products ORDER BY price ASC;"""
  results_order_by_price = db.cursor.execute(query_order_by_price).fetchall()
  show_results(results_order_by_price, "Resultados de ORDER BY por precio:")
  
  
  #3. Filtros (Clausula WHERE)
  print("\n6. Filtros (Clausula WHERE):")
  
  
  #3.1 Filtrar por precio mayor que 10
  print("Filtrando productos por precio mayor que 10:")
  query_filter_by_price = """SELECT * FROM products WHERE price > 10;"""
  results_filter_by_price = db.cursor.execute(query_filter_by_price).fetchall()
  show_results(results_filter_by_price, "Resultados de filtros:")
  
  #3.2 Filtrar por categoria especifica
  print("Filtrando productos por categoria especifica:")
  query_filter_by_category = """SELECT p.name AS Product, c.name AS Category
                              FROM products AS p
                              INNER JOIN categories AS c ON p.category_id = c.id
                              WHERE c.name = 'Electronics';"""
  results_filter_by_category = db.cursor.execute(query_filter_by_category).fetchall()
  show_results(results_filter_by_category, "Resultados de filtros por categoria:")
  
  #3.3 Filtrar por productos de una categoria especifica y precio mayor que 20
  print("Filtrando productos de una categoria especifica y precio mayor que 20:")
  query_filter_by_category_and_price = """SELECT p.name AS Product, c.name AS Category
                              FROM products AS p
                              INNER JOIN categories AS c ON p.category_id = c.id
                              WHERE c.name = 'Electronics' AND p.price > 20;"""
  results_filter_by_category_and_price = db.cursor.execute(query_filter_by_category_and_price).fetchall() 
  show_results(results_filter_by_category_and_price, "Resultados de filtros por categoria y precio:")
  
  #3.4 Filtrar por productos de home o electronics
  print("Filtrando productos de categoria 'Home' o 'Electronics':")
  query_filter_by_home_or_electronics = """SELECT p.name AS Product, c.name AS Category
                              FROM products AS p
                              INNER JOIN categories AS c ON p.category_id = c.id
                              WHERE c.name = 'Home' OR c.name = 'Electronics';"""
  results_filter_by_home_or_electronics = db.cursor.execute(query_filter_by_home_or_electronics).fetchall() 
  show_results(results_filter_by_home_or_electronics, "Resultados de filtros por categoria:")
  
if __name__ == "__main__":
  main()