# 🚀 Sistema de Gestión de Infraestructura - v1.4

Este proyecto demuestra una arquitectura de microservicios orquestada con **Docker Compose**, enfocada en la seguridad de datos, la persistencia y la automatización de entornos de base de datos.

## 📋 Novedades de la Versión 1.4

* **Seguridad de Credenciales:** Uso de archivos `.env` para gestionar variables de entorno, evitando la exposición de contraseñas.
* **Persistencia de Datos:** Configuración de volúmenes de Docker para asegurar que la información no se pierda al reiniciar.
* **Automatización de Esquemas:** Integración de scripts SQL (`v1_db_tabla.sql`) que se ejecutan automáticamente al nacer el contenedor.
* **Administración Visual:** Implementación de **Portainer** para la gestión profesional de contenedores.

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología | Función |
| :--- | :--- | :--- |
| **Orquestación** | Docker Compose | Gestión de servicios. |
| **Base de Datos** | MySQL 8.0 | Almacenamiento persistente. |
| **Servidor Web** | Nginx | Servidor de archivos estáticos. |
| **Gestión** | Portainer | Panel de control visual. |
| **Seguridad** | .env / .gitignore | Manejo de secretos. |

---

## 🚀 Instalación y Despliegue

1. **Configurar variables:**
   ```bash
   cp .env.example .env
   # Edita tus claves en el archivo .env
   
##Levantar la infraestructura:

Bash
docker compose --env-file .env up -d   

---
##Acceder a los servicios:

App Web: http://localhost:8080

Panel Portainer: https://localhost:9443
