import sender_stand_request


# Función para obtener el cuerpo de solicitud de un kit
def get_kit_body(name):
    return {"name": name}


# Función para obtener el token de un nuevo usuario
def get_new_user_token():
    return sender_stand_request.get_new_user_token()


# Pruebas positivas
def positive_assert(kit_name):
    auth_token = get_new_user_token()
    response = sender_stand_request.create_kit(auth_token, kit_name)
    assert response.status_code == 201
    assert response.json()["name"] == kit_name


# Pruebas negativas (código de respuesta 400)
def negative_assert_code_400(kit_name):
    auth_token = get_new_user_token()
    response = sender_stand_request.create_kit(auth_token, kit_name)
    assert response.status_code == 400


# Prueba 1: El número permitido de caracteres es 1
def test_kit_name_with_one_character():
    positive_assert("a")


# Prueba 2: El número permitido de caracteres es 511
def test_kit_name_with_511_characters():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert(name)


# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_kit_name_with_zero_characters():
    negative_assert_code_400("")


# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_kit_name_with_512_characters():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_code_400(name)


# Prueba 5: Se permiten caracteres especiales
def test_kit_name_with_special_characters():
    positive_assert("\"№%@\",\"")


# Prueba 6: Se permiten espacios
def test_kit_name_with_spaces():
    positive_assert(" A Aaa ")


# Prueba 7: Se permiten números
def test_kit_name_with_numbers():
    positive_assert("123")


# Prueba 8: El parámetro no se pasa en la solicitud
def test_kit_name_parameter_not_passed():
    negative_assert_code_400({})


# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_kit_name_with_number_type_parameter():
    negative_assert_code_400(123)
