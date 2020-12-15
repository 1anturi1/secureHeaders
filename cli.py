
from lib.utils.util import load_env_config
from lib.scanner.headers import Headers
import os

load_env_config()
def main():
    print("-------------------------------------------------------------------")
    print("Bienvenido a la herramienta de escaneo de encabezados de seguridad.")
    print("Basado en el proyecto 'OWASP security headers' (https://wiki.owasp.org/index.php/OWASP_Secure_Headers_Project)")
    print("-------------------------------------------------------------------")
    print("Por favor ingrese la URL del sitio al cuál desea realizar el escaneo")
    print("Para un sitio web desplegado en un dominio, el formato debe ser como el siguiente: facebook.com ")
    print("Para un sitio web desplegado localmente, el formato debe ser como el siguiente: 127.0.0.1:8000 ")
    url = str(input())
    threads_number = os.getenv('THREAD_NUMBER')
    Headers().run(url,int(threads_number))

if __name__ == '__main__':
    main()