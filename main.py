#-------------------------------------------------------
# Importación de las librerías necesarias
#-------------------------------------------------------

# Importar la libreria flet
import flet as ft

#-------------------------------------------------------
# Importación de las funciones necesarias
#-------------------------------------------------------

from views.main_view import main

from models.client_model import crear_tabla_clientes
from models.table_model import crear_tabla_mesas
from models.reserve_model import crear_tabla_reservas

from services.crud_operations import insertar_mesas_json
from services.mongo_service import get_db

# -------------------------------------------------------
# Funcion principal del programa
# -------------------------------------------------------
if __name__ == "__main__":
    
    # Obtener la base de datos
    db = get_db()

    # Crear las colecciones
    crear_tabla_clientes(db)
    crear_tabla_mesas(db)
    crear_tabla_reservas(db)

    # Insertar los datos de las mesas
    insertar_mesas_json(db)
    
    # Ejecutar la app flet con la vista web y la carpeta de assets indicada
    ft.app(target= lambda page: main(page, db), view=ft.AppView.WEB_BROWSER, assets_dir="assets")