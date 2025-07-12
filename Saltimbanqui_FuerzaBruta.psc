Algoritmo Saltimbanqui_ProgramacionDinamica
    Dimension asientos[100]
    Dimension dp[100]
    Definir n, resultado, i, j Como Entero
    Escribir "=== ALGORITMO PROGRAMACIÓN DINÁMICA ==="
    Escribir "¿Cuántos asientos?"
    Leer n
    
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Valor en asiento ", i, ":"
        Leer asientos[i]
    FinPara
    
    resultado <- SaltosPD(asientos, n, dp)
    Si resultado >= 9999 Entonces
        Escribir "No se puede llegar al final."
    Sino
        Escribir "Saltos mínimos (Programación Dinámica): ", resultado
    FinSi
FinAlgoritmo

// Función de programación dinámica
Funcion saltos <- SaltosPD(arr, n, dp)
    Definir i, j Como Entero
    
    // Inicializar tabla dp con valores infinitos
    Para i <- 1 Hasta n Con Paso 1 Hacer
        dp[i] <- 9999
    FinPara
    
    // Caso base: primera posición requiere 0 saltos
    dp[1] <- 0
    
    // Llenar la tabla dp
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Si dp[i] < 9999 Entonces  // Si es posible llegar a la posición i
            // Explorar todos los saltos posibles desde la posición i
            Para j <- 1 Hasta arr[i] Con Paso 1 Hacer
                Si i + j <= n Entonces
                    // Actualizar el mínimo número de saltos para llegar a i+j
                    Si dp[i] + 1 < dp[i + j] Entonces
                        dp[i + j] <- dp[i] + 1
                    FinSi
                FinSi
            FinPara
        FinSi
    FinPara
    
    // Retornar el resultado para la última posición
    saltos <- dp[n]
FinFuncion
