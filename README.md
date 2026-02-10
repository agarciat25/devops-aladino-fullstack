# 🚀 Portafolio de Microservicios: FastAPI + Nginx + Docker

¡Bienvenido a mi proyecto de infraestructura! Este repositorio demuestra la implementación de una arquitectura escalable utilizando contenedores para separar la lógica de negocio del servidor web.

## 🏗️ Arquitectura del Sistema
El proyecto está orquestado mediante **Docker Compose** y consta de dos servicios principales:
* **Backend**: Una API REST construida con **FastAPI** corriendo en un entorno virtual aislado.
* **Frontend/Proxy**: Un servidor **Nginx** que actúa como Proxy Inverso, gestionando el tráfico estático y redirigiendo las consultas a la API.

## 🛠️ Desafíos Técnicos Superados
Durante el desarrollo, se aplicaron habilidades de **Troubleshooting** de nivel avanzado:
* **Gestión de Volúmenes**: Resolución de conflictos de montaje de archivos vs directorios en contenedores.
* **Administración de Linux**: Configuración de repositorios oficiales de Docker y actualización de plugins para evitar errores de compatibilidad (`KeyError: ContainerConfig`).
* **Optimización de Repositorios**: Limpieza de entornos virtuales (`venv`) y estandarización mediante `.gitignore` y `requirements.txt`.

## 🚀 Cómo ejecutar el proyecto
1. Clonar el repositorio.
2. Asegurarse de tener instalado el **Docker Compose Plugin** moderno.
3. Ejecutar el comando:
   ```bash
   docker compose up -d --build
