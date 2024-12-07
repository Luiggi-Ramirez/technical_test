import pytest
import requests


class TestUnitTodoList:
    BASE_URL = "http://127.0.0.1:8000"

    @pytest.mark.unit
    def test_create_task(self):
        payload = {
            "id": 4,
            "title": "tarea 4",
            "description": "tarea 4",
            "completed": False,
        }
        response = requests.post(url=f"{self.BASE_URL}/tasks/", json=payload)
        # se testea el codigo de la response
        assert response.status_code == 201

    @pytest.mark.unit
    def test_create_repeated_task(self):
        payload = {
            "id": 4,
            "title": "tarea 4",
            "description": "tarea 4",
            "completed": False,
        }
        requests.post(url=f"{self.BASE_URL}/tasks/", json=payload)
        response_2 = requests.post(url=f"{self.BASE_URL}/tasks/", json=payload)
        # se testea la respuesta en la creacion
        assert response_2.status_code == 400

    @pytest.mark.unit
    def test_get_tasks(self):
        response = requests.get(url=f"{self.BASE_URL}/tasks/")
        # se testea la respuesta al obtener la data
        assert response.status_code == 200

    @pytest.mark.unit
    def test_get_task(self):
        response = requests.get(url=f"{self.BASE_URL}/tasks/2/")
        # se testea la respuesta al obtener la data
        assert response.status_code == 200

    @pytest.mark.unit
    def test_task_not_found(self):
        response = requests.get(url=f"{self.BASE_URL}/tasks/100/")
        # se testea la respuesta al obtener la data
        assert response.status_code == 404

    @pytest.mark.unit
    def test_update_task(self):
        payload = {
            "id": 1,
            "title": "Tarea 1",
            "description": "Tarea 1",
            "completed": True,
        }
        response = requests.put(url=f"{self.BASE_URL}/tasks/1/", json=payload)
        # se testea si la actualizacion fue exitosa
        assert response.status_code == 200

    @pytest.mark.unit
    def test_delete_task_success(self):
        response = requests.delete(url=f"{self.BASE_URL}/tasks/3/")
        # se testea si la eliminacion fue exitosa
        assert response.status_code == 204
        assert response.text == ""

    @pytest.mark.unit
    def test_delete_task_not_found(self):
        # se testea que la data ya no exista
        response = requests.get(url=f"{self.BASE_URL}/tasks/3/")
        assert response.status_code == 404
