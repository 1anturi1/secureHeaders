# USO PRÁCTICO DE ENCABEZADOS HTTP PARA MEJORAR LA SEGURIDAD EN EL PROTOCOLO

Basado en: OWASP SecureHeaders Project  

Proyecto de grado Andrés Iván Anturi Figueroa

Asesora: Sandra Julieta Rueda Rodríguez, Ph.D.

Universidad de Los Andes

Facultad de Ingeniería

Departamento de Ingeniería de Sistemas y Computación


## Dependencias 

- Microsoft C++ Build Tools 14.0
- Python 3.6

## Pasos para la instalación:
1.	Descargar el proyecto disponible en: https://github.com/1anturi1/secureHeaders
2.	Ubicarse desde la consola de comandos en el proyecto. 
3.	(Opcional) Instalar entorno virtual: pip install virtualenv
4.	(Opcional) Crear entorno virtual localmente: virtualenv [nombre_entorno]
5.	(Opcional) Activar entorno virtual:
 - Mac OS/Linux:
 - source [nombre_entorno]/bin/actívate
 - Windows:
 - [nombre_entorno]\Scripts\activate
6.	Instalar las dependencias con: 
 - a.	pip install -r requirements.txt
 - b.	pip3 install python-dotenv
 - c.	python -m pip install gevent
 - d.	pip install beautifulsoup4
 - e.	pip install requests
 - f.	pip install lxml
7.	Ejecutar la aplicación desde la consola utilizando alguno de los siguientes comandos:
 - a.	cli.py
 - b.	py cli.py
 - c.	python cli.py
8.	Ingresar la dirección del sitio web que desea escanear con el formato indicado. Omita el protocolo y el www si es el caso, como en el siguiente ejemplo: https://www.amazon.com solo se debe ingresar el “amazon.com”. Si el sitio que desea escanear se encuentra desplegado localmente o en una IP distinta, ingrese la dirección con el siguiente formato: 127.0.0.1:8080
