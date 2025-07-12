class AnalizadorTexto:
  contador_analisis = 0
  
  #Inicializo mis atributos de clase
  def __init__(self, texto:str, nombre_analisis:str = "General"):
    self.texto_original = texto
    self.nombre_analisis = nombre_analisis
    AnalizadorTexto.contador_analisis += 1
    
  #Funcion para limpiar texto
  def texto_limpio(self) -> str:
    caracteres_no_deseados = ".,;:()[]-_#$@"
    limpio = ''.join(caracter for caracter in self.texto_original if caracter not in caracteres_no_deseados)
    return limpio.lower()
  
  def estadisticas_basicas(self)-> tuple:
    palabras = self.texto_limpio().split()
    if not palabras:
      return (0, "", 0)
    
    palabra_mas_larga = max(palabras, key=len)
    promedio = sum(len(p) for p in palabras) / len(palabras)
    return (len(palabras), palabra_mas_larga, round(promedio,2))
  
  def frecuencia_palabras(self) -> dict:
    palabras = self.texto_limpio().split()
    frecuencia = {}
    for palabra in palabras:
      frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia
  
  def palabras_relevantes(self, umbral: int = 3) -> list:
        """Filtra palabras con frecuencia mínima y ordena alfabéticamente"""
        frecuencias = self.frecuencia_palabras()
        return sorted(palabra for palabra, count in frecuencias.items() 
                     if count >= umbral)

def limpiar_palabra(palabra: str) -> str:
    """Limpia una palabra individual de puntuación y espacios"""
    if not isinstance(palabra, str):
        return ""
    caracteres_no_deseados = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    while palabra and palabra[0] in caracteres_no_deseados:
        palabra = palabra[1:]
    while palabra and palabra[-1] in caracteres_no_deseados:
        palabra = palabra[:-1]
    return palabra.lower()

def filtrar_por_longitud(palabras: list, condicion: callable) -> list:
    """Filtra palabras usando una función de condición de orden superior"""
    return [p for p in palabras if condicion(p)]

def eliminar_duplicados(lista: list) -> list:
    """Elimina duplicados manteniendo el orden original"""
    vista = set()
    return [x for x in lista if not (x in vista or vista.add(x))]

if __name__ == "__main__":
    # Textos de prueba
    texto1 = "El éxito no es definitivo, el fracaso no es fatídico. Lo que cuenta es el coraje para continuar."
    texto2 = "La simplicidad es la clave de la elegancia. Menos es más."
    
    # Crear instancias
    analizador1 = AnalizadorTexto(texto1, "Frase inspiradora")
    analizador2 = AnalizadorTexto(texto2, "Diseño minimalista")
    
    # Procesamiento principal
    palabras1 = analizador1.texto_limpio().split()
    largas1 = filtrar_por_longitud(palabras1, lambda p: len(p) > 5)
    unicas_ordenadas = sorted(eliminar_duplicados(largas1))
    
    # Resultados
    print("=== Análisis 1 ===")
    print(f"Texto limpio: {' '.join(palabras1[:8])}...")
    print(f"Estadísticas: {analizador1.estadisticas_basicas()}")
    print(f"Palabras relevantes (≥2): {analizador1.palabras_relevantes(2)}")
    print(f"Palabras largas (>5 letras): {unicas_ordenadas}")
    
    print("\n=== Análisis 2 ===")
    print(f"Estadísticas: {analizador2.estadisticas_basicas()}")
    print(f"Palabras relevantes: {analizador2.palabras_relevantes()}")
    
    print(f"\nTotal análisis realizados: {AnalizadorTexto.contador_analisis}")