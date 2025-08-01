
# VulnScanCLI
Una herramienta de línea de comandos (CLI) escrita en Python que escanea tu sistema operativo en busca de software instalado y verifica si tienen vulnerabilidades conocidas (CVEs) a través de la Base de Datos Nacional de Vulnerabilidades (NVD) del NIST.

---

## 🚀 Características (En Desarrollo)

- **Escaneo de Software:** Detecta automáticamente los programas instalados en el sistema.
- **Búsqueda de Vulnerabilidades (CVE):** Se conecta a la API de la NVD para obtener información sobre CVEs.
- **Resultados Visuales:** Muestra las vulnerabilidades encontradas con un formato claro y con colores en la terminal.

---

## 🛠️ Requisitos de Instalación

Asegúrate de tener Python 3.8 o superior instalado.

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TRristan/VulnScanCLI.git](https://github.com/TRristan/VulnScanCLI.git)
    cd VulnScanCLI
    ```

2.  **Crea un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    _Nota: Todavía no tienes este archivo, pero es una buena práctica. Más adelante puedes crearlo con `pip freeze > requirements.txt`_

4.  **Configura tu API Key (Opcional):**
    Crea un archivo llamado **`.env`** en la carpeta raíz del proyecto y añade tu clave de la NVD para evitar limitaciones de peticiones.
    ```
    NVD_API_KEY=tu_clave_aqui
    ```

---


✍️ Contribuciones
Este proyecto es un trabajo personal y está en constante desarrollo. Si quieres contribuir, no dudes en abrir un issue o enviar un pull request.

