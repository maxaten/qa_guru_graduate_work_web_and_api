import allure
from jsonschema.validators import validate
from utils.helper import load_json_schema


class TestReqresApi:

    @allure.tag('api')
    @allure.title('Создание пользователя')
    def test_create_user(self, reqres):
        name = 'Olga'
        job = 'Manager'
        schema = load_json_schema('post_create_user.json')

        response = reqres.post(
            url='/api/users',
            json={
                'name': name,
                'job': job
            })

        assert response.status_code == 201
        validate(instance=response.json(), schema=schema)
        assert response.json()["name"] == name
        assert response.json()["job"] == job

    @allure.tag('api')
    @allure.title('Обновление данных пользователя')
    def test_update_user(self, reqres):
        name = 'Ololosha'
        job = 'President'
        schema = load_json_schema('put_update_user.json')

        response = reqres.put(
            url='/api/users/2',
            json={
                "name": name,
                "job": job
            }
        )

        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)
        assert response.json()["name"] == name
        assert response.json()["job"] == job

    @allure.tag('api')
    @allure.title('Регистрация пользователя')
    def test_register_user(self, reqres):
        email = 'eve.holt@reqres.in'
        password = 'pistol'
        schema = load_json_schema('post_register_user.json')

        response = reqres.post(
            url='/api/register',
            json={
                "email": email,
                "password": password
            }
        )

        validate(instance=response.json(), schema=schema)
        assert response.status_code == 200

    @allure.tag('api')
    @allure.title('Удаление пользователя')
    def test_delete_user(self, reqres):
        delete_user = reqres.delete("/api/users/2")

        assert delete_user.status_code == 204

    @allure.tag('api')
    @allure.title('Обновление некоторых данных клиента')
    def test_patch_user(self, reqres):
        name = 'morpheus'
        job = 'zion resident'
        schema = load_json_schema('patch_user.json')

        response = reqres.patch(
            url='/api/users/2',
            json={
                "name": name,
                "job": job
            }
        )

        validate(response.json(), schema=schema)
        assert response.status_code == 200
        assert response.json()['name'] == name
        assert response.json()['job'] == job

    @allure.tag('api')
    @allure.title('Загрузка страницы пользователей с задержкой')
    def test_delayed_response(self, reqres):
        delay = 3
        per_page = 6
        page = 1
        schema = load_json_schema('get_delay_response.json')

        response = reqres.get(
            url='/api/users',
            params={'delay': delay}
        )

        validate(response.json(), schema=schema)
        assert response.status_code == 200
        assert response.json()['per_page'] == per_page
        assert response.json()['page'] == page

    @allure.tag('api')
    @allure.title('Успешная авторизация пользователя')
    def test_login_user(self, reqres):
        email = 'eve.holt@reqres.in'
        password = 'cityslicka'
        schema = load_json_schema('post_login_user.json')

        response = reqres.post(
            url='/api/login',
            json={
                "email": email,
                "password": password
            }
        )

        validate(response.json(), schema=schema)
        assert response.status_code == 200

    @allure.tag('api')
    @allure.title('Неуспешная авторизация пользователя')
    def test_user_login_unsuccessful(self, reqres):
        email = 'peter@klaven'
        text_error = 'Missing password'
        schema = load_json_schema('post_user_login_unsuccessful.json')

        response = reqres.post(
            url='/api/login',
            json={
                'email': email
            }
        )

        validate(response.json(), schema=schema)
        assert response.status_code == 400
        assert response.json()['error'] == text_error

    @allure.tag('api')
    @allure.title('Неуспешная регистрация пользователя')
    def test_register_unsuccessful_user(self, reqres):
        email = 'sydney@fife'
        text_error = 'Missing password'
        schema = load_json_schema('post_unregister_user.json')

        response = reqres.post(
            url='/api/register',
            json={
                "email": email
            }
        )

        validate(response.json(), schema=schema)
        assert response.status_code == 400
        assert response.json()['error'] == text_error
