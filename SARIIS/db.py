"""
Manejo de Base de Datos SQLite para SARIIS
"""
import sqlite3
import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "sariis.db"


def get_db():
    """Retorna conexión a la BD"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Inicializa la base de datos con las tablas"""
    conn = get_db()
    cursor = conn.cursor()

    # Tabla de usuarios/estudiantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_control TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            nombre TEXT NOT NULL,
            roles TEXT NOT NULL,
            correo_institucional TEXT UNIQUE,
            carrera TEXT,
            activo BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabla de reportes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reportes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            area TEXT,
            edificio TEXT,
            descripcion TEXT,
            estado TEXT DEFAULT 'Pendiente',
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Insertar datos de prueba si no existen
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        test_users = [
            ("22230726", "22230726", "ROBERTO DE JESÚS HERNÁNDEZ STOREY", "Estudiante", "L22230726@minatitlan.tecnm.mx", "Ingeniería en Sistemas Computacionales (En Línea)"),
            ("22230719", "22230719", "YATZIRI JIMENEZ VALDÉS", "Estudiante", "L22230719@minatitlan.tecnm.mx", "Ingeniería en Sistemas Computacionales (En Línea)"),
            ("22230654", "22230654", "CARLOS RAFAEL MARTINEZ HERNANDEZ", "Estudiante", "L22230654@minatitlan.tecnm.mx", "Ingeniería en Sistemas Computacionales (En Línea)"),
            ("111111", "pass123", "Carlos Admin", "admin", None, None),
            ("654321", "pass123", "María Docente", "docente", None, None),
            ("222222", "pass123", "Pedro Técnico", "tecnico", None, None),
        ]
        for num_control, pwd, nombre, rol, correo, carrera in test_users:
            cursor.execute(
                "INSERT INTO users (numero_control, password, nombre, roles, correo_institucional, carrera) VALUES (?, ?, ?, ?, ?, ?)",
                (num_control, pwd, nombre, rol, correo, carrera),
            )

    conn.commit()
    conn.close()


def get_user_by_numero_control(numero_control: str):
    """Obtiene un usuario por número de control"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE numero_control = ? AND activo = 1",
        (numero_control,),
    )
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None


def verify_login(numero_control: str, password: str):
    """Verifica credenciales de login"""
    user = get_user_by_numero_control(numero_control)
    if user and user["password"] == password:
        return user
    return None


def crear_reporte(user_id: int, titulo: str, area: str = None, edificio: str = None, descripcion: str = None):
    """Crea un nuevo reporte"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO reportes (user_id, titulo, area, edificio, descripcion) 
           VALUES (?, ?, ?, ?, ?)""",
        (user_id, titulo, area, edificio, descripcion),
    )
    conn.commit()
    reporte_id = cursor.lastrowid
    conn.close()
    return reporte_id


def obtener_reportes_usuario(user_id: int):
    """Obtiene todos los reportes de un usuario"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM reportes WHERE user_id = ? ORDER BY fecha_creacion DESC""",
        (user_id,),
    )
    reportes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return reportes


if __name__ == "__main__":
    init_db()
    print("BD inicializada correctamente")
