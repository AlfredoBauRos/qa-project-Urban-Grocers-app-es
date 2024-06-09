# Proyecto de Pruebas positivas y negativas para la Creación de kits

Este proyecto consta de pruebas automatizadas para verificar la funcionalidad de creación de kits en una aplicación.
## Requisitos

- `Python 3.6 o superior`
- `pytest`
- `requests`

## Instalación

1. Clona el repositorio en tu máquina local:

   ```sh
   git clone <URL_del_repositorio>
   cd <nombre_del_repositorio>

## Crea un entorno virtual
* -inicia PyCharm.
* -Selecciona "New Project" para crear un nuevo proyecto.
* -Selecciona la configuración del proyecto.
* -Lenguaje. Selecciona Pure Python en el menú de la izquierda.
* -Identifica la ruta de tu proyecto: El nombre del último directorio es el nombre de tu proyecto.
* -Selecciona "New Virtualenv using" (Nuevo uso de Virtualenv) y luego elige Virtualenv en la lista desplegable.

## Instalar los paquetes

    pip install pytest requests


## Estructura del Proyecto

* data.py: Contiene datos utilizados en las pruebas, como encabezados de solicitud y cuerpos de usuario.
* configuration.py: Define la configuración de la aplicación, incluyendo la URL del servicio y las rutas de API.
* sender_stand_request.py: Contiene funciones para enviar solicitudes HTTP al servicio de la aplicación.
* create_kit_name_kit_test.py: Contiene las pruebas de creación de kit.
## Ejecución de Pruebas

    pytest create_kit_name_kit_test.py

ejecuta todas las pruebas, utiliza el siguiente comando en la terminal:

## Descripción de las Pruebas
Pruebas Positivas

Prueba 1: Verifica que se pueda crear un kit con un solo carácter.

    def test_kit_name_with_one_character():
    positive_assert("a")



Prueba 2: Verifica que se pueda crear un kit con 511 caracteres.

    def test_kit_name_with_511_characters():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert(name)



## Pruebas Negativas


Prueba 3: Verifica que no se pueda crear un kit sin nombre (0 caracteres).

    def test_kit_name_with_zero_characters():
    negative_assert_code_400("")


Prueba 4: Verifica que no se pueda crear un kit con más de 512 caracteres.

    def test_kit_name_with_512_characters():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_code_400(name)


Prueba 5: Verifica que se permitan caracteres especiales en el nombre del kit.

    def test_kit_name_with_special_characters():
    positive_assert("\"№%@\",")


Prueba 6: Verifica que se permitan espacios en el nombre del kit

    def test_kit_name_with_spaces():
    positive_assert(" A Aaa ")


Prueba 7: Verifica que se permitan números en el nombre del kit.

    def test_kit_name_with_numbers():
    positive_assert("123")


Prueba 8: Verifica que no se pueda crear un kit si el parámetro del nombre no se pasa en la solicitud.

    def test_kit_name_parameter_not_passed():
    negative_assert_code_400({})


Prueba 9: Verifica que no se pueda crear un kit si se pasa un tipo de parámetro incorrecto para el nombre.

    def test_kit_name_with_number_type_parameter():
    negative_assert_code_400(123)



