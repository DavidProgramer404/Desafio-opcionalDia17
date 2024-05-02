import requests

# Requerimiento 1: Obtener toda la información de los usuarios
users_url = 'https://reqres.in/api/users'
response = requests.get(users_url)

if response.status_code // 100 != 2:
    print("Error al obtener los usuarios:", response.status_code)
else:
    users_data = response.json()
    print("Usuarios:")
    print(users_data)

# Requerimiento 2: Crear un usuario llamado Ignacio con trabajo Profesor
new_user_data = {
    "name": "Ignacio",
    "job": "Profesor"
}

response = requests.post(users_url, json=new_user_data)

if response.status_code // 100 != 2:
    print("Error al crear el usuario:", response.status_code)
else:
    created_user = response.json()
    print("Usuario creado:")
    print(created_user)

# Requerimiento 3: Actualizar un usuario llamado morpheus con residence igual a zion
user_id_to_update = 2  # Asignar el ID del usuario morpheus
update_data = {
    "residence": "zion"
}

update_url = f"{users_url}/{user_id_to_update}"
response = requests.put(update_url, json=update_data)

if response.status_code // 100 != 2:
    print("Error al actualizar el usuario:", response.status_code)
else:
    updated_user = response.json()
    print("Usuario actualizado:")
    print(updated_user)

# Requerimiento 4: Eliminar un usuario llamado Tracey
user_id_to_delete = 7  # Asignar el ID del usuario Tracey
delete_url = f"{users_url}/{user_id_to_delete}"
response = requests.delete(delete_url)

print("Código de respuesta al eliminar el usuario Tracey:", response.status_code)
