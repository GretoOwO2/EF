Algoritmo Saltimbanqui_ProgramacionDinamica
    Dimension asientos[100]
    Dimension dp[100]
    Definir n, resultado, i, j Como Entero
    Escribir "=== ALGORITMO PROGRAMACI�N DIN�MICA ==="
    Escribir "�Cu�ntos asientos?"
    Leer n
    
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Valor en asiento ", i, ":"
        Leer asientos[i]
    FinPara
    
    resultado <- SaltosPD(asientos, n, dp)
    Si resultado >= 9999 Entonces
        Escribir "No se puede llegar al final."
    Sino
        Escribir "Saltos m�nimos (Programaci�n Din�mica): ", resultado
    FinSi
FinAlgoritmo

// Funci�n de programaci�n din�mica
Funcion saltos <- SaltosPD(arr, n, dp)
    Definir i, j Como Entero
    
    // Inicializar tabla dp con valores infinitos
    Para i <- 1 Hasta n Con Paso 1 Hacer
        dp[i] <- 9999
    FinPara
    
    // Caso base: primera posici�n requiere 0 saltos
    dp[1] <- 0
    
    // Llenar la tabla dp
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Si dp[i] < 9999 Entonces  // Si es posible llegar a la posici�n i
            // Explorar todos los saltos posibles desde la posici�n i
            Para j <- 1 Hasta arr[i] Con Paso 1 Hacer
                Si i + j <= n Entonces
                    // Actualizar el m�nimo n�mero de saltos para llegar a i+j
                    Si dp[i] + 1 < dp[i + j] Entonces
                        dp[i + j] <- dp[i] + 1
                    FinSi
                FinSi
            FinPara
        FinSi
    FinPara
    
    // Retornar el resultado para la �ltima posici�n
    saltos <- dp[n]
FinFuncion
