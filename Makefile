# Primeros dos comendos: Sirven para iniciar y eliminar un contendor de postgres:12-alpine

StartContainerPostgrest12:
	docker run --name postgres12 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:12-alpine

DeleteContainerPostgrest12:
	docker stop postgres12; docker rm postgres12

# Primer comando: Creamos una base de datos llamada prueba dentro del contendor postgres:12-alpine
# Segundo comando: Elimina la base de datos prueba

CreateDB:
	docker exec -it postgres12 createdb --username=root --owner=root prueba

DropDB:
	docker exec -it postgres12 dropdb prueba

# Primer comando: Sirve para crear la migración.
# Los dos siguientes para migrar (up) y para eliminar la migración (down)

CreateMigration:
	migrate create -ext sql -dir db/migration -seq init_schema

# Fueron para hacer pruebas. sin utilizar Django
MigrationUp:
	migrate -path db/migration -database "postgresql://root:secret@localhost:5432/prueba?sslmode=disable" -verbose up

MigrationDown:
	migrate -path db/migration -database "postgresql://root:secret@localhost:5432/prueba?sslmode=disable" -verbose down

# Comando para hacer migrate a Django una vez encendido el servicio backpython del docker 
MigrateDjango:
	docker exec -it backpython python3 /project/manage.py migrate

RunServer:
	docker exec backpython python3 /project/manage.py runserver 0:8000

.PHONY: StartContainerPostgrest12 DeleteContainerPostgrest12 CreateDB DropDB CreateMigration MigrationUp MigrationDown MigrateDjango RunServer