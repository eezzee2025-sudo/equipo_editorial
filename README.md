# Bot Editorial 📝

Este repositorio contiene el **bot editorial** en Python, diseñado para automatizar procesos de revisión y canalización de contenido.

## 🚀 Funcionalidades
- Automatización de revisión de textos (`revisión_cli.py`)
- Canalización de contenido (`canalización.py`)
- Configuración adaptable (`configuración/`)
- Plantilla de variables de entorno (`.env.template`)
- Blindaje completo del `.gitignore` para proteger credenciales y archivos sensibles

## 📂 Estructura
- `configuración/` → parámetros y ajustes del bot
- `.env.template` → ejemplo de variables de entorno
- `.gitignore` → exclusión de archivos privados
- `canalización.py` → lógica de canalización
- `revisión_cli.py` → revisión desde línea de comandos

## 🔒 Seguridad
- Variables sensibles en `.env` (no versionadas)
- Archivos privados ignorados por `.gitignore`

## 📌 Próximos pasos
- Documentar flujo de trabajo editorial
- Añadir ejemplos de uso
- Integrar pruebas automáticas
