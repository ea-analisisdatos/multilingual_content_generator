# Archivo: run_tests.py

import subprocess

def run_pytest():
    """
    Ejecuta pytest en el directorio de pruebas y muestra los resultados.
    """
    try:
        # Ejecutar pytest y mostrar resultados en detalle
        subprocess.run(["pytest", "tests/", "-v"], check=True)
    except subprocess.CalledProcessError as e:
        print("\nError al ejecutar las pruebas.")
        print("Revisa el detalle arriba y corrige cualquier problema.")

if __name__ == "__main__":
    print("Ejecutando todas las pruebas...")
    run_pytest()
