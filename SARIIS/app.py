from __future__ import annotations

from flask import Flask, redirect, render_template, url_for, request, session, jsonify
from functools import wraps
from db import init_db, verify_login, crear_reporte, obtener_reportes_usuario


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="statics",
        static_url_path="/statics",
    )
    app.secret_key = "sariis-secret-key-2026"  # Cambiar en producción

    # Inicializar BD
    init_db()

    # Decorador para proteger rutas
    def require_login(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user_id" not in session:
                return redirect(url_for("login"))
            return f(*args, **kwargs)
        return decorated_function

    @app.get("/")
    def login():
        if "user_id" in session:
            # Si ya está logueado, ir al dashboard según rol
            redirect_url = get_redirect_url(session.get("rol", "Estudiante"))
            return redirect(redirect_url)
        return render_template("login.html")

    # Función para mapear rol a ruta
    def get_redirect_url(rol):
        role_routes = {
            "Estudiante": "/panel",
            "docente": "/panel",
            "admin": "/direccion",
            "tecnico": "/tecnico",
            "jefe": "/jefe-mantenimiento",
        }
        return role_routes.get(rol, "/panel")

    @app.post("/api/login")
    def api_login():
        """API para autenticar usuario"""
        data = request.get_json()
        numero_control = data.get("numero_control", "").strip()
        password = data.get("password", "").strip()

        if not numero_control or not password:
            return jsonify({"success": False, "message": "Credenciales inválidas"}), 400

        user = verify_login(numero_control, password)
        if user:
            session["user_id"] = user["id"]
            session["numero_control"] = user["numero_control"]
            session["nombre"] = user["nombre"]
            session["rol"] = user["roles"]
            session["carrera"] = user["carrera"]
            session["correo_institucional"] = user["correo_institucional"]
            session["created_at"] = user["created_at"]
            redirect_url = get_redirect_url(user["roles"])
            return jsonify({
                "success": True,
                "message": "Login exitoso",
                "redirect": redirect_url
            })
        
        return jsonify({"success": False, "message": "Número de control o contraseña incorrectos"}), 401

    @app.get("/panel")
    @require_login
    def panel():
        return render_template("paginas/dashboard.html", user=dict(session))

    @app.get("/mis-reportes")
    @require_login
    def mis_reportes():
        """Página para ver todos los reportes del usuario"""
        return render_template("paginas/mis_reportes.html", user=dict(session))

    @app.get("/direccion")
    @require_login
    def direccion():
        return render_template("paginas/analytics.html")

    @app.get("/jefe-mantenimiento")
    @require_login
    def jefe_mantenimiento():
        return render_template("paginas/jefe_dashboard.html")

    @app.get("/tecnico")
    @require_login
    def tecnico():
        return render_template("paginas/agenda.html")

    @app.get("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))

    @app.post("/api/reportes")
    @require_login
    def crear_nuevo_reporte():
        """Endpoint para crear un nuevo reporte"""
        data = request.get_json()
        titulo = data.get("titulo", "").strip()
        area = data.get("area", "").strip() or None
        edificio = data.get("edificio", "").strip() or None
        descripcion = data.get("descripcion", "").strip() or None

        if not titulo:
            return jsonify({"success": False, "message": "El título es obligatorio"}), 400

        try:
            reporte_id = crear_reporte(
                session["user_id"], titulo, area, edificio, descripcion
            )
            return jsonify({
                "success": True,
                "message": "Reporte creado exitosamente",
                "reporte_id": reporte_id
            }), 201
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 500

    @app.get("/api/reportes")
    @require_login
    def obtener_mis_reportes():
        """Obtiene los reportes del usuario logueado"""
        reportes = obtener_reportes_usuario(session["user_id"])
        return jsonify({"success": True, "reportes": reportes})

    @app.get("/api/reportes/recientes/<int:limite>")
    @require_login
    def obtener_reportes_recientes(limite):
        """Obtiene los últimos N reportes del usuario"""
        reportes = obtener_reportes_usuario(session["user_id"])
        return jsonify({"success": True, "reportes": reportes[:limite]})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

