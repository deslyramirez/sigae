# Plan de Gestión de la Configuración - SIGAE

## Comité de Control de Cambios (CCB)
| Rol | Integrante | Por qué |
|---|---|---|
| Presidente | Gestor de Configuración | Administra el repositorio y verifica que el cambio se haga como se aprobó |
| Miembro | Líder de Proyecto | Ve el impacto en el cronograma y en el equipo de 12 ingenieros |
| Miembro | Arquitecto / Líder técnico | Ve el impacto técnico en los módulos |
| Miembro | Representante de QA | Define las pruebas de regresión |
| Miembro | Representante de INDECI / Gobierno Regional | Prioriza según cómo avanza el evento climático |

Para cambios internos se reúne el CCB técnico (Gestor de Configuración, Líder técnico y QA).

## Ventana de cambio
- Cambios normales: sábados de 02:00 a 04:00, con respaldo previo y plan de rollback.
- Cambios de emergencia: en cualquier horario, con aprobación del CCB por emergencia.
- Despliegue gradual, monitoreo de 24 a 48 horas y aviso a los usuarios antes y después.

## Reglas del repositorio
- Una rama por cambio: `feature/SCR-XXXX` o `hotfix/SCR-XXXX`.
- Formato de commit: `<tipo>(<alcance>): <descripción>` y en el pie `SCR-XXXX`.
- Prohibido hacer commit directo en `main` o `develop` (ver `.githooks/pre-commit`).
- Cada versión liberada se etiqueta con un tag.
