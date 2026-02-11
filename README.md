# 🚀 Infraestructura de Microservicios: GH Imports

### 📝 Descripción del Proyecto
Este repositorio contiene la arquitectura de microservicios diseñada para modernizar el sistema de ventas de GH Imports. Se migró de un entorno monolítico en Ubuntu 16 a una infraestructura orquestada y escalable en **Ubuntu 24.04 LTS** utilizando **Docker**.

### 🏗️ Arquitectura del Sistema
El proyecto implementa una arquitectura de tres capas aisladas mediante una red interna tipo `bridge`:

* **Servidor Web / Proxy Inverso:** Gestionado con **Nginx**, encargado de recibir las peticiones externas y redirigirlas al backend.
* **Lógica de Negocio (Backend):** Desarrollado con **FastAPI**, procesando las solicitudes y comunicándose con la base de datos.
* **Persistencia de Datos:** Base de datos **MySQL 5.7** con volúmenes persistentes para asegurar la integridad de la información.

### 🛠️ Desafíos Técnicos Resueltos (Troubleshooting)
Como parte del proceso de trazabilidad y despliegue, se resolvieron los siguientes obstáculos críticos:

* **Corrección de Sintaxis YAML:** Se depuraron errores de tipo `KeyError: 'ContainerConfig'` y errores de indentación en el archivo `docker-compose.yml`, ajustando correctamente los contextos de construcción para los contenedores.
* **Gestión de Permisos en Linux:** Resolución de errores de tipo `Permission denied` al configurar los archivos de Nginx mediante el uso correcto de privilegios de superusuario (`sudo`).
* **Configuración de Proxy Inverso:** Implementación de reglas de `proxy_pass` para conectar el flujo de red entre el puerto 80 externo y el puerto 8000 interno de la API, logrando un estado **HTTP 200 OK**.

### ⚙️ Instrucciones de Despliegue
1. Clonar este repositorio.
2. Crear un archivo `.env` basado en el archivo `.env.example` incluido.
3. Ejecutar el comando de orquestación:
   ```bash
   docker-compose up -d --build
   
4. Verificar el funcionamiento en: http://localhost
