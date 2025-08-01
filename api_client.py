import nvdlib
import os
import requests
from dotenv import load_dotenv

def test_api_connection():
    """
    Función mejorada para probar la conexión con la API de la NVD.
    """
    load_dotenv()
    api_key = os.getenv("NVD_API_KEY")

    try:
        # Petición simple a un CVE conocido para validar la conexión y la API key.
        test_cve_id = "CVE-2007-0001"
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={test_cve_id}"
        headers = {"apiKey": api_key} if api_key else {}
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Lanza una excepción si la respuesta no es 200 OK

        # Verificamos si el CVE de prueba se encuentra en la respuesta.
        data = response.json()
        if data and "vulnerabilities" in data:
            print("---")
            print("✅ Conexión con la API de la NVD establecida correctamente.")
            print(f"👉 Código de respuesta: {response.status_code} (OK)")
            print("---")
            return True
        else:
            print("---")
            print("❌ Error: La API respondió, pero no se encontró el CVE de prueba.")
            print("---")
            return False

    except requests.exceptions.HTTPError as e:
        print("---")
        print(f"❌ Error HTTP al conectar con la API: {e}")
        print("---")
        return False
    except requests.exceptions.RequestException as e:
        print("---")
        print(f"❌ Error de red o conexión al conectar con la API: {e}")
        print("---")
        return False