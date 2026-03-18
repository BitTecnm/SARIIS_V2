import { normalizeRole, roleRoutes } from "../models/roles.js";

function getById(id) {
  const el = document.getElementById(id);
  if (!el) throw new Error(`No se encontró el elemento #${id}`);
  return el;
}

export function initLogin() {
  const btnLogin = getById("btnLogin");
  const inputUsuario = getById("usuario");

  btnLogin.addEventListener("click", () => {
    const role = normalizeRole(inputUsuario.value);
    const destination = roleRoutes[role];
    if (!destination) {
      alert("Escribe: alumno, docente, jefe, tecnico o admin para probar el avance.");
      return;
    }
    window.location.href = destination;
  });
}

