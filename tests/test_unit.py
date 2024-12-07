import pytest
from fastapi.testclient import TestClient
from todo_list.main import app


class TestUnitTodoList:
    client = TestClient(app)
    tasks = [
        {"id": 1, "title": "tarea 1", "description": "tarea 1", "completed": False},
        {"id": 2, "title": "tarea 2", "description": "tarea 2", "completed": False},
        {"id": 3, "title": "tarea 3", "description": "tarea 3", "completed": False},
    ]

    @pytest.mark.unit
    def test_create_task(self):
        payload = {
            "id": 4,
            "title": "tarea 4",
            "description": "tarea 4",
            "completed": False,
        }
        response = self.client.post(url="/tasks/", json=payload)
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
        self.client.post(url="/tasks/", json=payload)
        response_2 = self.client.post(url="/tasks/", json=payload)
        # se testea la respuesta en la creacion
        assert response_2.status_code == 400

    @pytest.mark.unit
    def test_get_tasks(self):
        response = self.client.get(url="/tasks/")
        # se testea la respuesta al obtener la data
        assert response.status_code == 200

    @pytest.mark.unit
    def test_get_task(self):
        response = self.client.get(url="/tasks/2/")
        # se testea la respuesta al obtener la data
        assert response.status_code == 200

    @pytest.mark.unit
    def test_task_not_found(self):
        response = self.client.get(url="/tasks/100/")
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
        response = self.client.put(url="/tasks/1/", json=payload)
        # se testea si la actualizacion fue exitosa
        assert response.status_code == 200

    @pytest.mark.unit
    def test_delete_task_success(self):
        response = self.client.delete(url="/tasks/3/")
        # se testea si la eliminacion fue exitosa
        assert response.status_code == 204
        assert response.text == ""

    @pytest.mark.unit
    def test_delete_task_not_found(self):
        # se testea que la data ya no exista
        response = self.client.get(url="/tasks/3/")
        assert response.status_code == 404
