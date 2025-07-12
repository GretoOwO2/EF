import sys

def min_saltos(asientos):
    n = len(asientos)
    if n <= 1:
        return 0
    
    saltos = 0
    pos_actual = 0
    max_alcanzable = 0
    
    for i in range(n):
        if i > max_alcanzable:
            return -1
        
        max_alcanzable = max(max_alcanzable, i + asientos[i])
        
        if max_alcanzable >= n - 1:
            return saltos + 1
        
        if i == pos_actual:
            saltos += 1
            pos_actual = max_alcanzable
    
    return saltos

def obtener_ruta_saltos(asientos):
    n = len(asientos)
    if n <= 1:
        return [0] if n == 1 else []
    
    saltos = 0
    pos_actual = 0
    max_alcanzable = 0
    ruta = [0]
    mejor_salto = 0
    saltos_data = []
    
    for i in range(1, n):
        if i > max_alcanzable:
            return []
        
        if i + asientos[i] > max_alcanzable:
            max_alcanzable = i + asientos[i]
            mejor_salto = i
        
        if i == pos_actual or i == n-1:
            saltos += 1
            ruta.append(mejor_salto)
            saltos_data.append({
                'desde': pos_actual,
                'hacia': mejor_salto,
                'distancia': mejor_salto - pos_actual
            })
            pos_actual = max_alcanzable
            
            if max_alcanzable >= n-1:
                ruta.append(n-1)
                saltos_data.append({
                    'desde': mejor_salto,
                    'hacia': n-1,
                    'distancia': n-1 - mejor_salto
                })
                return ruta, saltos_data
    
    return [], []

def analizar_complejidad():
    print("\n" + "="*60)
    print("ANÁLISIS DE COMPLEJIDAD")
    print("="*60)
    print("• Complejidad Temporal: O(n)")
    print("• Complejidad Espacial: O(1)")
    print("• Comparación con otros enfoques:")
    print("  - Fuerza Bruta: O(2^n)")
    print("  - Programación Dinámica: O(n^2)")
    print("  - Algoritmo Voraz: O(n)")
    print("="*60)

def mostrar_demo_grafica(asientos, ruta):
    if not ruta:
        print("\nNo se puede mostrar gráfica: Ruta no disponible")
        return
    
    print("\nREPRESENTACIÓN GRÁFICA DE LA RUTA:")
    n = len(asientos)
    max_value = max(asientos)
    diagrama = []
    
    for i in range(n):
        fila = [' '] * (n + max_value + 2)
        fila[i] = '■'
        diagrama.append(fila)
    
    for i in range(len(ruta)-1):
        inicio = ruta[i]
        fin = ruta[i+1]
        for j in range(inicio, fin+1):
            if j < len(diagrama[inicio]):
                diagrama[inicio][j] = '─' if j != inicio else '■'
        diagrama[inicio][fin] = '►'
    
    for fila in diagrama:
        print(''.join(fila[:n+max_value]))
    
    print("\nLeyenda:")
    print("■ = Asiento inicial/salto")
    print("► = Destino de salto")
    print("─ = Trayectoria del salto")

def ejecutar_pruebas_detalladas():
    pruebas = [
        ([2, 3, 1, 1, 4], 2, [0, 1, 4]),
        ([1, 1, 1, 1], 3, [0, 1, 2, 3]),
        ([3, 2, 1, 0, 4], -1, []),
        ([0], 0, [0]),
        ([1, 2, 3, 4], 2, [0, 1, 3]),
        ([2, 0, 1, 1, 4], -1, []),
        ([5, 0, 0, 0, 1], 1, [0, 4]),
        ([1, 3, 1, 1, 1, 1], 3, [0, 1, 4, 5]),
        ([4, 1, 1, 3, 1, 1, 1], 2, [0, 3, 6]),
        ([2, 3, 0, 1, 2], 2, [0, 1, 4]),
        ([1, 0, 2], -1, [])
    ]
    
    print("\n" + "="*80)
    print("REPORTE DE PRUEBAS - ALGORITMO DEL SALTIMBANQUI")
    print("="*80)
    
    exitos = 0
    fallas = 0
    
    for i, (entrada, esperado_saltos, esperado_ruta) in enumerate(pruebas, 1):
        resultado_saltos = min_saltos(entrada)
        resultado_ruta = obtener_ruta_saltos(entrada)
        
        # Manejar diferentes tipos de retorno
        if isinstance(resultado_ruta, tuple):
            resultado_ruta = resultado_ruta[0]
        
        saltos_ok = resultado_saltos == esperado_saltos
        ruta_ok = resultado_ruta == esperado_ruta
        
        if saltos_ok and ruta_ok:
            estado = "ÉXITO"
            color = "\033[92m"
            exitos += 1
        else:
            estado = "FALLA"
            color = "\033[91m"
            fallas += 1
        
        print(f"\n{'='*40}")
        print(f"PRUEBA #{i}: {entrada}")
        print(f"{'='*40}")
        print(f"• Saltos: {resultado_saltos} (Esperado: {esperado_saltos})")
        print(f"• Ruta: {resultado_ruta} (Esperado: {esperado_ruta})")
        print(f"• Estado: {color}{estado}\033[0m")
        
        if saltos_ok and ruta_ok and resultado_ruta:
            mostrar_demo_grafica(entrada, resultado_ruta)
    
    print("\n" + "="*80)
    print("RESUMEN FINAL")
    print("="*80)
    print(f"Total pruebas: {len(pruebas)}")
    print(f"Pruebas exitosas: \033[92m{exitos}\033[0m")
    print(f"Pruebas fallidas: \033[91m{fallas}\033[0m")
    print(f"Tasa de éxito: {exitos/len(pruebas)*100:.2f}%")
    print("="*80)

def exportar_resultados(asientos, saltos, ruta, saltos_data):
    if not saltos_data:
        saltos_data = []
    
    nombre_archivo = "resultado_saltimbanqui.txt"
    with open(nombre_archivo, 'w') as f:
        f.write("RESULTADOS DEL ANÁLISIS - PROBLEMA DEL SALTIMBANQUI\n")
        f.write("="*60 + "\n\n")
        f.write(f"Configuración de asientos: {asientos}\n")
        f.write(f"Número mínimo de saltos: {saltos}\n")
        
        if ruta:
            f.write(f"Ruta óptima: {' → '.join(map(str, ruta))}\n\n")
        else:
            f.write("Ruta óptima: No disponible\n\n")
        
        if saltos_data:
            f.write("DETALLE DE SALTOS:\n")
            for i, salto in enumerate(saltos_data, 1):
                f.write(f"Salto {i}: Desde asiento {salto['desde']} hasta asiento {salto['hacia']} ")
                f.write(f"(Distancia: {salto['distancia']})\n")
        
        f.write("\nANÁLISIS ALGORÍTMICO:\n")
        f.write("- Complejidad temporal: O(n)\n")
        f.write("- Complejidad espacial: O(1)\n")
        f.write("- Tipo de algoritmo: Voraz (Greedy)\n")
    
    print(f"\nResultados exportados a '{nombre_archivo}'")

def main():
    while True:
        print("\n" + "="*60)
        print("SOLUCIÓN AL PROBLEMA DEL SALTIMBANQUI")
        print("="*60)
        print("1. Ejecutar pruebas completas")
        print("2. Ingresar configuración manual")
        print("3. Ver análisis de complejidad")
        print("4. Salir")
        print("="*60)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ejecutar_pruebas_detalladas()
        elif opcion == "2":
            entrada = input("Ingrese los valores de los asientos separados por comas: ")
            try:
                asientos = list(map(int, entrada.split(',')))
                saltos = min_saltos(asientos)
                resultado = obtener_ruta_saltos(asientos)
                
                # Manejar diferentes tipos de retorno
                if isinstance(resultado, tuple):
                    ruta, saltos_data = resultado
                else:
                    ruta = resultado
                    saltos_data = []
                
                print("\n" + "="*40)
                print("RESULTADOS")
                print("="*40)
                if saltos == -1:
                    print("No existe solución para esta configuración")
                else:
                    print(f"Número mínimo de saltos: {saltos}")
                    
                    if ruta:
                        print(f"Ruta óptima: {' → '.join(map(str, ruta))}")
                        
                        if saltos_data:
                            print("\nDETALLE DE SALTOS:")
                            for i, salto in enumerate(saltos_data, 1):
                                print(f"Salto {i}: Desde asiento {salto['desde']} hasta asiento {salto['hacia']} (Distancia: {salto['distancia']})")
                        
                        mostrar_demo_grafica(asientos, ruta)
                        exportar_resultados(asientos, saltos, ruta, saltos_data)
                    else:
                        print("Ruta óptima: No disponible")
                print("="*40)
                
            except ValueError:
                print("Error: Ingrese solo números enteros separados por comas")
        elif opcion == "3":
            analizar_complejidad()
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            sys.exit()
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()