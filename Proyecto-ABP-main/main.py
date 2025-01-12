import flet as ft

from views.main_view import main
from models.client_model import crear_tabla_clientes
from models.table_model import crear_tabla_mesas
from models.reserve_model import crear_tabla_reservas

from services.crud_operations import insertar_mesas_json

from services.mongo_service import get_db

if __name__ == "__main__":
    
    db = get_db()
    crear_tabla_clientes(db)
    crear_tabla_mesas(db)
    crear_tabla_reservas(db)

    insertar_mesas_json(db)
    
    ft.app(target= lambda page: main(page, db), view=ft.AppView.WEB_BROWSER, assets_dir="assets")