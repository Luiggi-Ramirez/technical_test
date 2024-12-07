import pytest
from fastapi.testclient import TestClient
from todo_list.main import app


class TestIntegrationTodoList:
    client = TestClient(app)
    tasks = [
        {"id": 1, "title": "tarea 1", "description": "tarea 1", "completed": False},
        {"id": 2, "title": "tarea 2", "description": "tarea 2", "completed": False},
        {"id": 3, "title": "tarea 3", "description": "tarea 3", "completed": False},
    ]

    @pytest.mark.integration
    def test_create_task(self):
        payload = {
            "id": 5,
            "title": "tarea 5",
            "description": "tarea 5",
            "completed": False,
        }
        # se crea el recurso
        response = self.client.post(url="/tasks/", json=payload)
        data = response.json()
        # se testea que la creacion del recurso sea corrrecta
        assert response.status_code == 201
        # se testea el estado de la response
        assert data["id"] == 5
        assert data["title"] == "tarea 5"
        assert data["description"] == "tarea 5"
        assert data["completed"] is False
        # se testea que no se añada data con id repetido
        response_2 = self.client.post(url="/tasks/", json=payload)
        assert response_2.status_code == 400
        # se testea que la task se haya añadidio a la lista
        response = self.client.get(url="/tasks/5/")
        assert response.status_code == 200

    @pytest.mark.integration
    def test_get_tasks(self):
        response = self.client.get(url="/tasks/")
        assert response.status_code == 200
        data = response.json()
        # se testea si la respuesta es una instancia de tipo list
        assert isinstance(data, list)
        # se testea si la response contiene data
        assert len(data) > 0

    @pytest.mark.integration
    def test_get_task(self):
        payload = {
            "id": 6,
            "title": "tarea 6",
            "description": "tarea 6",
            "completed": False,
        }
        # creamos una nueva task
        response = self.client.post(url="/tasks/", json=payload)
        # obtenemos la task
        response = self.client.get(url="/tasks/6/")
        # se testea que la data existe
        assert response.status_code == 200
        data = response.json()
        # se testea que la data sea la esperada
        assert data["id"] == 6
        assert data["title"] == "tarea 6"
        assert data["description"] == "tarea 6"
        assert data["completed"] is False
        # se testea la busqueda de una task quw no existe
        response = self.client.get(url="/tasks/20/")
        assert response.status_code == 404

    @pytest.mark.integration
    def test_update_task(self):
        payload = {
            "id": 1,
            "title": "tarea 1",
            "description": "tarea 1",
            "completed": True,
        }
        # actualizamos un recurso existente
        response = self.client.put(url="/tasks/1/", json=payload)
        data = response.json()
        # se testea que la actualización sea exitosa
        assert response.status_code == 200
        # se testea que se haya actualizado con la data esperada
        assert data["id"] == 1
        assert data["title"] == "tarea 1"
        assert data["description"] == "tarea 1"
        assert data["completed"] is True
        # se obtiene el recurso
        response_get = self.client.get(url="/tasks/1/")
        data_get = response_get.json()
        # se testea que el cambio se haya aplicado en el recurso
        assert data_get["completed"] is True
        # actualizamos un recurso inexistente
        response = self.client.put(url="/tasks/100/", json=payload)
        # se testea que la actualización falle por no encontrar el recurso
        assert response.status_code == 404

    @pytest.mark.integration
    def test_delete_task(self):
        # eliminamos el recurso
        response = self.client.delete(url="/tasks/5/")
        # verificamos que la eliminación a sido correcta
        assert response.status_code == 204
        assert response.text == ""
        # verificamos que el recurso ya no se encuentra
        response = self.client.get(url="/tasks/5/")
        assert response.status_code == 404
