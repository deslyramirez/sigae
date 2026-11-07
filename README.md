# SIGAE - Sistema Integrado de Gestión de Ayuda en Emergencias

Sistema del Gobierno Regional de Piura para el Fenómeno del Niño 2026-2027.
Gestiona la ayuda humanitaria, el estado de los albergues y las alertas tempranas.

## Ramas (GitFlow)
- `main`: solo versiones aprobadas que están en producción (Biblioteca Maestra).
- `develop`: integración de cambios para pruebas (Biblioteca de Integración).
- `feature/*`, `hotfix/*`: trabajo de cada cambio (Biblioteca de Trabajo).

## Cómo correr las pruebas
```
python -m pytest -q
```
