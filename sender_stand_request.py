import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def get_new_user_token():
    response = post_new_user(data.user_body.copy())
    response_json = response.json()
    return response_json.get("authToken")


def create_kit(auth_Token, kit_name):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_Token}"
    kit_body = {"name": kit_name}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)


if __name__ == "__main__":
    response = post_new_user(data.user_body)
    print(response.status_code)
    print(response.json())
