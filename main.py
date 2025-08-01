from api_client import test_api_connection

def main():
    print("Iniciando prueba de conexión con la API de la NVD...")
    if not test_api_connection():
        print("El programa no puede continuar sin conexión a la API.")
        return # Termina el programa si la conexión falla

    # Si llegamos aquí, la conexión es exitosa y el programa puede continuar
    print("Comenzando el escaneo de vulnerabilidades...")
    # ... (El resto de tu lógica de escaneo)

if __name__ == "__main__":
    main()