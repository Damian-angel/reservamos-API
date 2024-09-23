# Reservamos API -Code Challenge
## Este proyecto es una API que permite a los usuarios comparar el pronóstico del clima para los próximos 7 días en diferentes destinos ofrecidos por Reservamos, utilizando la API de OpenWeather y las coordenadas de las ciudades obtenidas de la API de Reservamos.

Requisitos Previos

Python 3.6.6 (preferentemente 3.6 o superior)
Git (para clonar el repositorio)
Virtualenv (para manejar el entorno virtual)
OpenWeather API Key 
Instrucciones para correr el proyecto en local
1. Clonar el repositorio
Primero, clona el repositorio de este proyecto en tu máquina local:


```js
git clone https://github.com/Damian-angel/reservamos-API.git

```
2. Crear y activar el entorno virtual
Para mantener el proyecto aislado de las dependencias globales, crea un entorno virtual:



# Crear un entorno virtual
```py
python -m venv venv
```
# Activar el entorno virtual
En Windows
```
venv\Scripts\activate
```
En macOS o Linux
```
source venv/bin/activate
```
3. Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias que están listadas en el archivo requirements.txt:
```
pip install -r requirements.txt
```
4. Configurar las variables de entorno
El proyecto utiliza la clave API de OpenWeather, la cual debe estar configurada como una variable de entorno. Para ello, sigue los siguientes pasos:

Crea un archivo .env en la raíz del proyecto.
reemplazar "api key" con tu clave API de OpenWeather.
Agrega tu clave API en el archivo .env de la siguiente manera:
```
OPENWEATHER_API_KEY= " api key "
```

5. Aplicar las migraciones de la base de datos
Ejecuta las migraciones para configurar la base de datos del proyecto:

```

python manage.py migrate
```
6. Ejecutar el servidor localmente
Para levantar el servidor de desarrollo localmente, ejecuta:

```
python manage.py runserver
```
El servidor de Django se iniciará en http://127.0.0.1:8000/, donde podrás acceder a la API.

7. Probar la API
Con el servidor corriendo, puedes realizar solicitudes a la API. Por ejemplo, puedes buscar el pronóstico del clima para una ciudad específica (ejemplo queretaro):

```
GET http://127.0.0.1:8000/api/weather?city=queretaro

```
Este endpoint devolverá el pronóstico del clima para los próximos 7 días, con las temperaturas máximas y mínimas por cada día.