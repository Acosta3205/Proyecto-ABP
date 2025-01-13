# Proyecto-ABP
Este proyecto es una aplicación web desarrollaba en Flet y que utiliza MongoDB como base de datos principal.

El archivo principal para ejecutar la aplicación es main.py


Requisitos previos:

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.12 o superior
- MongoDB
- Biblioteca Flet: pip install flet
- Biblioteca Pymongo: pip install pymongo dnspython

Configurar la conexión a MongoDB:

Primero, crea una base de datos llamada Restaurante en MongoDB

Luego, accede al archivo config.py que se encuentra en el directorio utils y modifica la variable mongo_uri estableciendo en ella la dirección de tu servidor de MongoDB

Ejecutar la aplicación:

Para ejecutar la aplicación bastará con ejecutar el archivo main.py encontrado en la raiz del proyecto.

Estructura del proyecto:

.
├── assets/                 # Recursos gráficos
│   └── images/             # Imágenes utilizadas en la aplicación
├── models/                 # Modelos de datos
│   ├── client_model.py     # Modelo para clientes
│   ├── reserve_model.py    # Modelo para reservas
│   └── table_model.py      # Modelo para mesas
├── services/               # Lógica de conexión y operaciones
│   ├── crud_operations.py  # Operaciones CRUD
│   ├── mongo_service.py    # Conexión a MongoDB
│   └── querys.py           # Consultas y operaciones específicas
├── utils/                  # Utilidades y configuraciones
│   ├── config.py           # Configuración del proyecto
│   └── validators.py       # Validadores de datos
├── views/                  # Interfaces de usuario
│   ├── main_view.py        # Vista principal
│   ├── second_view.py      # Segunda vista (Crear Reserva)
│   ├── third_view.py       # Tercera vista (Modificar Reserva)
│   ├── fourth_view.py      # Cuarta vista (Eliminar Reserva)
│   ├── fifth_view.py       # Quinta vista (Crear Reserva)
│   └── sixth_view.py       # Sexta vista (Modificar Reserva)
├── main.py                 # Archivo principal para ejecutar la aplicación
└── README.md               # Documentación del proyecto