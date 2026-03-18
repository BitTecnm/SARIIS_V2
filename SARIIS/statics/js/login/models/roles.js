export const roleRoutes = Object.freeze({
  alumno: "/alumno",
  docente: "/docente",
  admin: "/direccion",
  jefe: "/jefe-mantenimiento",
  tecnico: "/tecnico",
});

export function normalizeRole(raw) {
  return String(raw ?? "").toLowerCase().trim();
}

