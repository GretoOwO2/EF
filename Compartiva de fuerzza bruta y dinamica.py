# Sin imports externos - Solo Python básico

# ===================================================================
# 1. ALGORITMO FUERZA BRUTA
# ===================================================================

def saltos_fuerza_bruta(asientos, pos=0):
    """
    Encuentra el número mínimo de saltos usando fuerza bruta (recursión)
    
    Args:
        asientos: Lista con los valores de cada asiento
        pos: Posición actual (índice)
    
    Returns:
        Número mínimo de saltos o float('inf') si es imposible
    """
    n = len(asientos)
    
    # Caso base: si llegamos al final o más allá
    if pos >= n - 1:
        return 0
    
    # Si no podemos saltar desde esta posición
    if asientos[pos] == 0:
        return float('inf')
    
    min_saltos = float('inf')
    
    # Probar todos los saltos posibles desde esta posición
    for i in range(1, asientos[pos] + 1):
        if pos + i < n:
            saltos = saltos_fuerza_bruta(asientos, pos + i)
            min_saltos = min(min_saltos, saltos)
    
    return min_saltos + 1 if min_saltos != float('inf') else float('inf')

# ===================================================================
# 2. ALGORITMO PROGRAMACIÓN DINÁMICA
# ===================================================================

def saltos_programacion_dinamica(asientos):
    """
    Encuentra el número mínimo de saltos usando programación dinámica
    
    Args:
        asientos: Lista con los valores de cada asiento
    
    Returns:
        Número mínimo de saltos o -1 si es imposible
    """
    n = len(asientos)
    if n <= 1:
        return 0
    
    # Tabla dp donde dp[i] = mínimo número de saltos para llegar a la posición i
    dp = [float('inf')] * n
    dp[0] = 0  # Primera posición requiere 0 saltos
    
    # Llenar la tabla dp
    for i in range(n):
        if dp[i] != float('inf'):  # Si es posible llegar a la posición i
            # Explorar todos los saltos posibles desde la posición i
            for j in range(1, asientos[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
    
    return dp[n - 1] if dp[n - 1] != float('inf') else -1

# ===================================================================
# 3. ALGORITMO VORAZ (GREEDY) - SOLUCIÓN ÓPTIMA
# ===================================================================

def saltos_voraz(asientos):
    """
    Encuentra el número mínimo de saltos usando algoritmo voraz (más eficiente)
    
    Args:
        asientos: Lista con los valores de cada asiento
    
    Returns:
        Número mínimo de saltos o -1 si es imposible
    """
    n = len(asientos)
    if n <= 1:
        return 0
    
    if asientos[0] == 0:
        return -1
    
    saltos = 0
    max_alcanzable = 0
    pos_actual = 0
    
    for i in range(n):
        # Actualizar el máximo alcanzable
        max_alcanzable = max(max_alcanzable, i + asientos[i])
        
        # Si hemos llegado al final del alcance actual
        if i == pos_actual:
            saltos += 1
            pos_actual = max_alcanzable
            
            # Si podemos llegar al final
            if pos_actual >= n - 1:
                break
        
        # Si no podemos avanzar más
        if i > max_alcanzable:
            return -1
    
    return saltos

# ===================================================================
# 4. FUNCIÓN PARA OBTENER LA RUTA DE SALTOS
# ===================================================================

def obtener_ruta_saltos(asientos):
    """
    Obtiene la ruta óptima de saltos usando programación dinámica
    
    Args:
        asientos: Lista con los valores de cada asiento
    
    Returns:
        Tupla (número_saltos, ruta) donde ruta es una lista de posiciones
    """
    n = len(asientos)
    if n <= 1:
        return 0, [0] if n == 1 else []
    
    # Tabla dp y tabla para rastrear el camino
    dp = [float('inf')] * n
    parent = [-1] * n
    dp[0] = 0
    
    # Llenar las tablas
    for i in range(n):
        if dp[i] != float('inf'):
            for j in range(1, asientos[i] + 1):
                if i + j < n and dp[i] + 1 < dp[i + j]:
                    dp[i + j] = dp[i] + 1
                    parent[i + j] = i
    
    # Reconstruir la ruta
    if dp[n - 1] == float('inf'):
        return -1, []
    
    ruta = []
    pos = n - 1
    while pos != -1:
        ruta.append(pos)
        pos = parent[pos]
    
    ruta.reverse()
    return dp[n - 1], ruta

# ===================================================================
# 5. FUNCIÓN PARA COMPARAR ALGORITMOS
# ===================================================================

def comparar_algoritmos(asientos):
    """
    Compara el rendimiento de los tres algoritmos
    
    Args:
        asientos: Lista con los valores de cada asiento
    """
    print("=" * 60)
    print("COMPARACIÓN DE ALGORITMOS DEL SALTIMBANQUI")
    print("=" * 60)
    print(f"Entrada: {asientos}")
    print()
    
    # Fuerza Bruta (solo para arrays pequeños)
    if len(asientos) <= 15:
        resultado_fb = saltos_fuerza_bruta(asientos)
        print(f"1. FUERZA BRUTA:")
        print(f"   Resultado: {resultado_fb if resultado_fb != float('inf') else 'Imposible'}")
        print(f"   Complejidad: O(2^n)")
    else:
        print(f"1. FUERZA BRUTA:")
        print(f"   Resultado: No ejecutado (array muy grande)")
        print(f"   Complejidad: O(2^n)")
    
    # Programación Dinámica
    resultado_pd = saltos_programacion_dinamica(asientos)
    print(f"\n2. PROGRAMACIÓN DINÁMICA:")
    print(f"   Resultado: {resultado_pd if resultado_pd != -1 else 'Imposible'}")
    print(f"   Complejidad: O(n²)")
    
    # Algoritmo Voraz
    resultado_voraz = saltos_voraz(asientos)
    print(f"\n3. ALGORITMO VORAZ:")
    print(f"   Resultado: {resultado_voraz if resultado_voraz != -1 else 'Imposible'}")
    print(f"   Complejidad: O(n)")
    
    # Obtener ruta óptima
    num_saltos, ruta = obtener_ruta_saltos(asientos)
    print(f"\n4. RUTA ÓPTIMA:")
    if num_saltos != -1:
        print(f"   Saltos: {num_saltos}")
        print(f"   Ruta: {' -> '.join(map(str, ruta))}")
        print(f"   Distancias: {[asientos[pos] for pos in ruta[:-1]]}")
    else:
        print(f"   No hay solución posible")
    
    print("\n" + "=" * 60)

# ===================================================================
# 6. CASOS DE PRUEBA
# ===================================================================

def ejecutar_casos_prueba():
    """
    Ejecuta una serie de casos de prueba para validar los algoritmos
    """
    casos_prueba = [
        ([2, 3, 1, 1, 4], "Caso óptimo"),
        ([2, 3, 0, 1, 4], "Con obstáculo"),
        ([2, 1, 0, 4], "Caso límite"),
        ([1, 1, 1, 1], "Saltos unitarios"),
        ([4, 1, 1, 1, 1], "Salto largo inicial"),
        ([1, 2, 3], "Caso simple"),
        ([0], "Imposible desde inicio"),
        ([5], "Array de un elemento"),
        ([3, 2, 1, 0, 4], "Imposible llegar al final"),
        ([1, 0, 2], "Obstáculo intermedio"),
        ([2, 0, 1, 0, 1], "Múltiples obstáculos")
    ]
    
    print("EJECUCIÓN DE CASOS DE PRUEBA")
    print("=" * 80)
    
    for i, (asientos, descripcion) in enumerate(casos_prueba, 1):
        print(f"\nCASO {i}: {descripcion}")
        print("-" * 40)
        comparar_algoritmos(asientos)
        if i < len(casos_prueba):
            input("\nPresiona Enter para continuar...")

# ===================================================================
# 7. VISUALIZACIÓN SIMPLE (SIN MATPLOTLIB)
# ===================================================================

def visualizar_saltos_texto(asientos):
    """
    Crea una visualización textual de los saltos
    """
    num_saltos, ruta = obtener_ruta_saltos(asientos)
    
    if num_saltos == -1:
        print("No se puede visualizar: no hay solución")
        return
    
    print("\n" + "=" * 50)
    print("VISUALIZACIÓN DE LA RUTA ÓPTIMA")
    print("=" * 50)
    
    # Mostrar el array original
    print("\nArray original:")
    print("Pos: ", end="")
    for i in range(len(asientos)):
        print(f"{i:3d}", end=" ")
    print()
    print("Val: ", end="")
    for val in asientos:
        print(f"{val:3d}", end=" ")
    print()
    
    # Mostrar los saltos
    print(f"\nRuta óptima ({num_saltos} saltos):")
    for i in range(len(ruta) - 1):
        pos_actual = ruta[i]
        pos_siguiente = ruta[i + 1]
        distancia = pos_siguiente - pos_actual
        print(f"Salto {i+1}: Pos {pos_actual} -> Pos {pos_siguiente} (distancia: {distancia}, valor: {asientos[pos_actual]})")
    
    # Visualización gráfica simple
    print("\nRepresentación gráfica:")
    print("=" * (len(asientos) * 4 + 1))
    
    # Línea con valores
    print("|", end="")
    for val in asientos:
        print(f"{val:2d} ", end="|")
    print()
    
    # Línea con posiciones
    print("|", end="")
    for i in range(len(asientos)):
        print(f"{i:2d} ", end="|")
    print()
    
    # Línea mostrando la ruta
    print("|", end="")
    for i in range(len(asientos)):
        if i in ruta:
            print(" * ", end="|")
        else:
            print("   ", end="|")
    print()
    
    print("=" * (len(asientos) * 4 + 1))
    print("Leyenda: * = Posición visitada en la ruta óptima")
    print("=" * 50)

# ===================================================================
# 8. FUNCIÓN PRINCIPAL INTERACTIVA
# ===================================================================

def main():
    """
    Función principal con menú interactivo
    """
    while True:
        print("\n" + "=" * 60)
        print("PROBLEMA DEL SALTIMBANQUI")
        print("=" * 60)
        print("1. Ingresar array personalizado")
        print("2. Ejecutar casos de prueba")
        print("3. Comparar algoritmos con array aleatorio")
        print("4. Salir")
        print("-" * 60)
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            try:
                entrada = input("Ingresa los valores separados por comas: ")
                asientos = [int(x.strip()) for x in entrada.split(",")]
                comparar_algoritmos(asientos)
                
                if input("\n¿Deseas ver la visualización? (s/n): ").lower() == 's':
                    visualizar_saltos_texto(asientos)
                    
            except ValueError:
                print("Error: Ingresa solo números separados por comas")
        
        elif opcion == "2":
            ejecutar_casos_prueba()
        
        elif opcion == "3":
            # Generador simple de números pseudo-aleatorios
            n = int(input("Tamaño del array (recomendado: 10-50): "))
            asientos = []
            
            # Usar una semilla basada en input del usuario
            semilla = hash(input("Ingresa una palabra para generar el array: ")) % 1000
            
            for i in range(n):
                # Generador congruencial lineal simple
                semilla = (semilla * 1103515245 + 12345) % (2**31)
                asientos.append(semilla % 5)  # Valores entre 0-4
            
            print(f"Array generado: {asientos}")
            comparar_algoritmos(asientos)
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()