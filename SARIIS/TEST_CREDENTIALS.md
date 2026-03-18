# Datos de Prueba - Login SARIIS

## Credenciales de Prueba

### Estudiantes

| Número de Control | Contraseña | Nombre | Rol | Correo | Carrera |
|---|---|---|---|---|---|
| 22230726 | 22230726 | ROBERTO DE JESÚS HERNÁNDEZ STOREY | Estudiante | L22230726@minatitlan.tecnm.mx | Ingeniería en Sistemas Computacionales (En Línea) |
| 22230719 | 22230719 | YATZIRI JIMENEZ VALDÉS | Estudiante | L22230719@minatitlan.tecnm.mx | Ingeniería en Sistemas Computacionales (En Línea) |
| 22230654 | 22230654 | CARLOS RAFAEL MARTINEZ HERNANDEZ | Estudiante | L22230654@minatitlan.tecnm.mx | Ingeniería en Sistemas Computacionales (En Línea) |

### Otros

| Número de Control | Contraseña | Nombre | Rol |
|---|---|---|---|
| 111111 | pass123 | Carlos Admin | admin |
| 654321 | pass123 | María Docente | docente |
| 222222 | pass123 | Pedro Técnico | tecnico |

## Rutas Disponibles

- `/` - Login
- `/panel` - **Panel Principal (Estudiante + Docente)** ← Ambos ven esta página
- `/mis-reportes` - Ver todos tus reportes con filtros
- `/direccion` - Analytics Dirección (requiere login como admin)
- `/jefe-mantenimiento` - Dashboard Jefe Mantenimiento (requiere login como jefe)
- `/tecnico` - Agenda Técnico (requiere login como tecnico)
- `/logout` - Salir

## Redirecciones después de Login

- **Estudiante** → `/panel` (página principal)
- **Docente** → `/panel` (página principal)
- **Admin** → `/direccion`
- **Técnico** → `/tecnico`
- **Jefe** → `/jefe-mantenimiento`

## APIs Disponibles

- `POST /api/reportes` - Crear nuevo reporte
- `GET /api/reportes` - Obtener todos los reportes del usuario
- `GET /api/reportes/recientes/2` - Obtener los 2 reportes más recientes del usuario

## Base de Datos

- **Archivo**: `sariis.db` (SQLite)
- **Se crea automáticamente** en la primera ejecución
- **Tabla**: `users` con campos: id, numero_control, password, nombre, roles, activo, created_at
