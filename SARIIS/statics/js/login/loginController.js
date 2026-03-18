/**
 * Login Controller
 * Maneja la lógica de autenticación del formulario
 */

class LoginController {
  constructor() {
    this.form = document.querySelector("form");
    this.btnLogin = document.getElementById("btnLogin");
    this.inputUsuario = document.getElementById("usuario");
    this.inputPassword = document.getElementById("password");
    this.btnShowPassword = document.querySelector('button[aria-label="Mostrar contraseña"]');
    this.isLoading = false;

    this.init();
  }

  init() {
    // Event listeners
    this.btnLogin.addEventListener("click", (e) => this.handleLogin(e));
    this.form.addEventListener("keypress", (e) => {
      if (e.key === "Enter") this.handleLogin(e);
    });
    this.btnShowPassword.addEventListener("click", (e) => this.togglePasswordVisibility(e));
  }

  /**
   * Alterna visibilidad de contraseña
   */
  togglePasswordVisibility(e) {
    e.preventDefault();
    const isPassword = this.inputPassword.type === "password";
    this.inputPassword.type = isPassword ? "text" : "password";

    const icon = this.btnShowPassword.querySelector("span");
    icon.textContent = isPassword ? "visibility_off" : "visibility";
  }

  /**
   * Maneja el envío del formulario de login
   */
  async handleLogin(e) {
    e.preventDefault();

    if (this.isLoading) return;

    const numeroControl = this.inputUsuario.value.trim();
    const password = this.inputPassword.value.trim();

    // Validaciones básicas
    if (!numeroControl) {
      this.showMessage("Por favor ingresa tu número de control", "error");
      this.inputUsuario.focus();
      return;
    }

    if (!password) {
      this.showMessage("Por favor ingresa tu contraseña", "error");
      this.inputPassword.focus();
      return;
    }

    await this.submitLogin(numeroControl, password);
  }

  /**
   * Envía credenciales al servidor
   */
  async submitLogin(numeroControl, password) {
    this.isLoading = true;
    this.setButtonLoading(true);

    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          numero_control: numeroControl,
          password: password,
        }),
      });

      const data = await response.json();

      if (response.ok && data.success) {
        this.showMessage("✓ Login exitoso. Redirigiendo...", "success");
        setTimeout(() => {
          window.location.href = data.redirect;
        }, 600);
      } else {
        this.showMessage(data.message || "Error en la autenticación", "error");
        this.inputPassword.value = "";
        this.inputPassword.focus();
      }
    } catch (error) {
      console.error("Error:", error);
      this.showMessage("Error de conexión. Intenta nuevamente.", "error");
    } finally {
      this.isLoading = false;
      this.setButtonLoading(false);
    }
  }

  /**
   * Muestra mensaje temporal al usuario
   */
  showMessage(message, type = "info") {
    // Eliminar mensaje anterior si existe
    const existingAlert = document.querySelector("[role='alert']");
    if (existingAlert) existingAlert.remove();

    const alertClass =
      type === "error"
        ? "bg-red-50 text-red-800 border-red-200"
        : type === "success"
          ? "bg-green-50 text-green-800 border-green-200"
          : "bg-blue-50 text-blue-800 border-blue-200";

    const alert = document.createElement("div");
    alert.setAttribute("role", "alert");
    alert.className = `p-4 mb-4 rounded-lg border ${alertClass} animate-pulse`;
    alert.textContent = message;

    this.form.insertBefore(alert, this.form.firstChild);

    if (type !== "error") {
      setTimeout(() => alert.remove(), 3000);
    }
  }

  /**
   * Cambia el estado del botón durante carga
   */
  setButtonLoading(loading) {
    if (loading) {
      this.btnLogin.disabled = true;
      this.btnLogin.innerHTML = '<span class="material-symbols-outlined animate-spin">hourglass_top</span> Verificando...';
      this.btnLogin.classList.add("opacity-70");
    } else {
      this.btnLogin.disabled = false;
      this.btnLogin.innerHTML = "INICIAR SESIÓN";
      this.btnLogin.classList.remove("opacity-70");
    }
  }
}

// Inicializar cuando el DOM esté listo
document.addEventListener("DOMContentLoaded", () => {
  new LoginController();
});
