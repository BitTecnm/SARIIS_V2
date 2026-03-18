# 🏢 SARIIS - Sistema de Reportes de Incidentes y Mantenimiento ITM

**SARIIS** es una aplicación web moderna para el **Instituto Tecnológico de Minatitlán** que permite a estudiantes, docentes y personal administrativo reportar incidentes de mantenimiento en el campus de forma rápida y eficiente.

## ✨ Características Principales

### 🎯 Para Estudiantes y Docentes
- ✅ **Panel Principal Unificado** - Dashboard compartido con estadísticas y acciones rápidas
- ✅ **Crear Reportes** - Formulario intuitivo para reportar incidentes
- ✅ **Seguimiento de Reportes** - Ver todos tus reportes con filtros por estado
- ✅ **Perfil de Usuario** - Modal estilo Microsoft Teams con datos personales
- ✅ **Estado En Línea** - Indicador visual de si el usuario está activo
- ✅ **Reportes Recientes** - Últimos 2 reportes directamente en el panel

### 👔 Para Administración
- ✅ **Módulo Dirección** - Analytics y estadísticas avanzadas
- ✅ **Jefe de Mantenimiento** - Dashboard para gestionar incidentes
- ✅ **Técnicos** - Agenda de mantenimiento programado

### 🎨 Diseño y UX
- 🌓 **Tema Oscuro/Claro** - Soporte completo para ambos temas
- 📱 **Responsive Design** - Funciona perfectamente en mobile, tablet y desktop
- ✨ **Notificaciones Elegantes** - Mensajes de éxito/error con animaciones suaves
- 🎭 **Material Design** - Iconos Material Symbols integrados

---

## 📋 Estructura del Proyecto

```
FrontEnd_SARIIS/
├── app.py                          # Aplicación principal Flask
├── db.py                           # Manejo de base de datos SQLite
├── requirements.txt                # Dependencias Python
├── sariis.db                       # Base de datos (se crea automáticamente)
├── README.md                       # Este archivo
├── TEST_CREDENTIALS.md             # Credenciales de prueba
│
├── templates/
│   ├── login.html                  # Página de login
│   └── paginas/                    # Todas las interfaces unificadas
│       ├── dashboard.html          # Panel principal (estudiante + docente)
│       ├── mis_reportes.html       # Vista completa de reportes con filtros
│       ├── analytics.html          # Analytics (dirección)
│       ├── jefe_dashboard.html     # Dashboard jefe mantenimiento
│       └── agenda.html             # Agenda técnico
│
├── statics/
│   └── js/
│       └── login/
│           ├── loginController.js  # Lógica de autenticación
│           ├── main.js             # Código antiguo (no usado)
│           └── controllers/
│               └── loginController.js
│
└── .venv/                          # Entorno virtual Python
```

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- **Python 3.11+**
- **pip** (gestor de paquetes Python)
- **Git** (opcional)

### Paso 1: Activar Entorno Virtual

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### Paso 2: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la Aplicación
```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 🔐 Credenciales de Prueba

### Estudiantes
| Número de Control | Contraseña | Nombre | Carrera |
|---|---|---|---|
| 22230726 | 22230726 | ROBERTO DE JESÚS HERNÁNDEZ STOREY | Ingeniería en Sistemas Computacionales |
| 22230719 | 22230719 | YATZIRI JIMENEZ VALDÉS | Ingeniería en Sistemas Computacionales |
| 22230654 | 22230654 | CARLOS RAFAEL MARTINEZ HERNANDEZ | Ingeniería en Sistemas Computacionales |

### Personal Administrativo
| Número de Control | Contraseña | Nombre | Rol |
|---|---|---|---|
| 111111 | pass123 | Carlos Admin | admin |
| 654321 | pass123 | María Docente | docente |
| 222222 | pass123 | Pedro Técnico | tecnico |
| 333333 | pass123 | Juan Jefe | jefe |

---

## 🗺️ Rutas Disponibles

| Ruta | Descripción | Requiere Login | Acceso |
|---|---|---|---|
| `/` | Página de login | No | Todos |
| `/panel` | Panel principal | Sí | Estudiante, Docente |
| `/mis-reportes` | Todos los reportes del usuario | Sí | Estudiante, Docente |
| `/direccion` | Analytics y estadísticas | Sí | Admin |
| `/jefe-mantenimiento` | Dashboard jefe | Sí | Jefe |
| `/tecnico` | Agenda técnico | Sí | Técnico |
| `/logout` | Cerrar sesión | - | - |

---

## 🔌 APIs REST

### Autenticación
**POST `/api/login`**
```json
{
  "numero_control": "22230726",
  "password": "22230726"
}
```
Respuesta exitosa:
```json
{
  "success": true,
  "message": "Login exitoso",
  "redirect": "/panel"
}
```

### Reportes

**POST `/api/reportes`** - Crear nuevo reporte
```json
{
  "titulo": "Puerta rota en Edificio A",
  "area": "Infraestructura",
  "edificio": "Edificio A",
  "descripcion": "La puerta del salón 205 está rota"
}
```

**GET `/api/reportes`** - Obtener todos los reportes del usuario
Respuesta:
```json
{
  "success": true,
  "reportes": [
    {
      "id": 1,
      "titulo": "...",
      "area": "...",
      "estado": "Pendiente",
      "fecha_creacion": "2026-03-17 10:30:00"
    }
  ]
}
```

**GET `/api/reportes/recientes/2`** - Obtener los 2 reportes más recientes
Parámetro: número de reportes a traer

---

## 💾 Base de Datos

### Conexión
- **Tipo:** SQLite3
- **Archivo:** `sariis.db` (se crea automáticamente)

### Tablas

#### Usuarios (`users`)
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | ID único (PK) |
| numero_control | TEXT | Número de control (UNIQUE) |
| password | TEXT | Contraseña (almacenada) |
| nombre | TEXT | Nombre completo |
| roles | TEXT | Rol del usuario |
| correo_institucional | TEXT | Email institucional |
| carrera | TEXT | Carrera/programa |
| activo | BOOLEAN | Estado del usuario |
| created_at | TIMESTAMP | Fecha de creación |

#### Reportes (`reportes`)
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | ID único (PK) |
| user_id | INTEGER | Referencia al usuario (FK) |
| titulo | TEXT | Título del reporte |
| area | TEXT | Área afectada |
| edificio | TEXT | Edificio donde ocurre |
| descripcion | TEXT | Descripción detallada |
| estado | TEXT | Estado: Pendiente, En Proceso, Resuelto |
| fecha_creacion | TIMESTAMP | Fecha de creación |

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask 3.1.3** - Framework web Python
- **SQLite3** - Base de datos
- **Python 3.11** - Lenguaje de programación

### Frontend
- **HTML5** - Estructura
- **Tailwind CSS 4.0** - Estilos y diseño responsivo
- **JavaScript (Vanilla)** - Interactividad
- **Material Symbols** - Iconografía

### Herramientas
- **Jinja2** - Motor de plantillas
- **Git** - Control de versiones

---

## 🎯 Funcionalidades Detalladas

### 📱 Dashboard Principal (`/panel`)
- Saludo personalizado al usuario
- Acciones rápidas (Crear reporte, ver historial)
- Últimos 2 reportes creados
- Modal de perfil estilo Microsoft Teams
- Indicador de estado en línea (verde/gris)
- Formulario disponible para crear reportes

### 📊 Mis Reportes (`/mis-reportes`)
- Vista completa de todos los reportes
- Filtros por estado (Pendiente, En Proceso, Resuelto)
- Información detallada por reporte
- Búsqueda y ordenamiento

### 👤 Modal de Perfil
- Foto de perfil con indicador de estado
- Nombre y rol
- Número de control
- Carrera
- Correo institucional
- Fecha de registro
- Cierra con X, click fuera o tecla Escape

### 📢 Sistema de Notificaciones
- Mensajes flotantes en esquina superior derecha
- Colores diferenciados: Verde (éxito), Rojo (error), Azul (info)
- Animación pulse para llamar atención
- Desaparece automáticamente

---

## 🔄 Flujo de Autenticación

1. Usuario accede a `/`
2. Ingresa número de control y contraseña
3. Se valida contra la base de datos
4. Si es correcto:
   - Se guarda en sesión
   - Se redirige según rol
5. Login fallido muestra error rojo

---

## 🔒 Seguridad

⚠️ **Para Producción:**
- Cambiar `secret_key` en `app.py`
- Usar contraseñas hasheadas (bcrypt/argon2)
- Implementar HTTPS
- Validación CSRF
- Rate limiting en APIs

---

## 📝 Variables de Entorno Recomendadas

Crear archivo `.env`:
```
FLASK_ENV=development
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///sariis.db
DEBUG=False
```

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Port 5000 already in use"
```bash
python app.py --port 5001
```

### Base de datos no se crea
La BD se crea automáticamente en la primera ejecución. Si hay problema:
```bash
rm sariis.db
python app.py
```

---

## 📞 Soporte

Para reportar bugs o sugerir mejoras, contacta al equipo de desarrollo.

---

## 📄 Licencia

Proyecto desarrollado para el Instituto Tecnológico de Minatitlán.

---

## 👥 Equipo de Desarrollo

**SARIIS v2.0** - Marzo 2026
Desarrollado para TecNM Minatitlán

Si no quieres “activar” el entorno, también puedes ejecutar directo con:

```bash
.\.venv\Scripts\python app.py
```

### Si NO tienes `.venv/` (primera vez en otra PC)

```bash
py -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python app.py
```

Abre en el navegador:

- `http://127.0.0.1:5000/`

## Rutas disponibles

- `/` login
- `/alumno`
- `/docente`
- `/direccion` (admin)
- `/jefe-mantenimiento` (jefe)
- `/tecnico`
- `/logout`


## Notas

- En PowerShell, si encadenas comandos, usa `;` (por ejemplo: `comando1; comando2`). No todos los entornos aceptan `&&`.
