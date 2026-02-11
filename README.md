🚀 Full-Stack DevOps Portfolio: Infraestructura Escalable y Monitoreada
Este proyecto demuestra el despliegue de una arquitectura web moderna de 3 capas utilizando Docker y Docker Compose, enfocada en la alta disponibilidad, persistencia de datos y gestión visual mediante herramientas de grado industrial.

🏗️ Arquitectura del Sistema
La infraestructura se compone de 4 servicios orquestados dinámicamente:

Proxy Inverso (Nginx): Actúa como puerta de enlace, gestionando las peticiones externas y redirigiéndolas al backend.

API Backend (FastAPI): Lógica de negocio procesada en Python, diseñada para ser ligera y rápida.

Base de Datos (MySQL 8.0): Capa de datos con persistencia mediante volúmenes locales para evitar la pérdida de información.

Panel de Control (Portainer CE): Interfaz gráfica para el monitoreo en tiempo real, gestión de logs y salud de los contenedores.

🛠️ Características Principales
Alta Disponibilidad: Configuración de políticas de restart: always para asegurar la recuperación automática ante fallos.

Persistencia Garantizada: Implementación de volúmenes de Docker para separar los datos del ciclo de vida del contenedor.

Red Aislada: Todos los servicios conviven en una red virtual privada (bridge) para mejorar la seguridad y el descubrimiento de servicios.

Seguridad de Credenciales: Gestión de variables de entorno mediante archivos .env (protegidos en .gitignore).

📊 Monitoreo y Gestión
Para este proyecto, se integró Portainer, permitiendo:

Visualización del consumo de recursos (CPU/RAM).

Acceso rápido a la consola de cada contenedor sin necesidad de SSH.

Inspección de logs para depuración rápida (Troubleshooting).

🚀 Cómo Desplegar
Solo necesitas tener instalado Docker y Docker Compose:

Clonar el repositorio:

Bash
git clone https://github.com/agarciat25/devops-aladino-fullstack.git

Levantar la infraestructura:

Bash
docker compose up -d

Acceder a los servicios:

App Web: http://localhost:8080

Panel Portainer: https://localhost:9443
