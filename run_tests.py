# Archivo: run_tests.py

import subprocess
import sys

def run_pytest():
    """
    Ejecuta pytest en el directorio de pruebas y muestra los resultados.
    """
    try:
        print("Ejecutando pruebas con pytest...\n")
        # Ejecutar pytest con detalles y filtrado de advertencias
        subprocess.run(["pytest", "tests/", "-v", "--disable-warnings"], check=True)
        print("\n\033[92mTodas las pruebas pasaron correctamente.\033[0m")  # Texto verde
    except subprocess.CalledProcessError as e:
        print("\n\033[91mError al ejecutar las pruebas.\033[0m")  # Texto rojo
        print("Revisa el detalle arriba y corrige cualquier problema.")

def main():
    """
    Punto de entrada principal para ejecutar las pruebas.
    """
    print("========================================")
    print("  Ejecutor de pruebas - Pytest")
    print("========================================\n")
    run_pytest()

if __name__ == "__main__":
    main()
