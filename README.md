# 🚀 Gestor de Tareas Web: Organiza tu Productividad con Facilidad

---

## Descripción del Proyecto

Este proyecto es una **aplicación web de gestión de tareas** robusta y fácil de usar, diseñada para ayudar a los usuarios a mantenerse organizados y aumentar su productividad. Permite crear, organizar y gestionar tareas pendientes de manera eficiente, ofreciendo una experiencia de usuario intuitiva y fluida.

Desarrollada con un enfoque en la funcionalidad **CRUD (Crear, Leer, Actualizar, Eliminar)**, esta aplicación proporciona todas las herramientas necesarias para un control completo sobre las tareas. Ya sea para uso personal o para un pequeño equipo, esta solución web simplifica la gestión de la carga de trabajo y asegura que nada se quede sin hacer.

---

## Características Principales

* **Creación de Tareas:** Agrega nuevas tareas con descripciones detalladas de forma rápida y sencilla.
* **Visualización de Tareas:** Accede a una lista clara y organizada de todas tus tareas pendientes.
* **Edición y Actualización:** Modifica cualquier detalle de una tarea existente, como su descripción o estado.
* **Marcado como Completado:** Marca tareas como finalizadas para llevar un registro de tu progreso.
* **Eliminación de Tareas:** Remueve tareas que ya no son relevantes con un solo clic.
* **Funcionalidad CRUD Completa:** Implementación sólida de las operaciones básicas de base de datos para una gestión de datos eficiente.

---

## Tecnologías Utilizadas

Este proyecto fue construido utilizando las siguientes tecnologías clave:

* **Frontend:**
    * **HTML5**
    * **Bootstrap 5** (para un diseño responsivo y moderno)
* **Backend:**
    * **Django** (Framework web de Python)
    * **Python**
* **Base de Datos:**
    * **SQLite** (ideal para desarrollo y pequeños proyectos)

---

## Cómo Ejecutar el Proyecto

Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/tu-usuario/nombre-de-tu-repositorio.git](https://github.com/tu-usuario/nombre-de-tu-repositorio.git)
    cd nombre-de-tu-repositorio
    ```

2.  **Configurar el Backend (Django):**

    * **Crear un entorno virtual (recomendado):**
        ```bash
        python -m venv venv
        source venv/bin/activate  # En Linux/macOS
        # venv\Scripts\activate   # En Windows
        ```
    * **Instalar dependencias:**
        ```bash
        pip install -r requirements.txt # Asegúrate de tener un archivo requirements.txt con tus dependencias de Django (ej: pip freeze > requirements.txt)
        ```
    * **Configurar variables de entorno:**
        Crea un archivo `.env` en la raíz de tu proyecto (junto a `manage.py`) y añade tu `SECRET_KEY` de Django y cualquier otra configuración necesaria.

        ```
        # .env
        DJANGO_SECRET_KEY=tu_super_secret_key_generada_aqui
        ```
        **Recuerda:** Asegúrate de que `.env` esté incluido en tu `.gitignore` para evitar que se suba al repositorio.
    * **Aplicar migraciones de la base de datos:**
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

3.  **Iniciar la Aplicación:**

    * **Ejecutar el servidor de desarrollo de Django:**
        ```bash
        python manage.py runserver
        ```

4.  **Acceder a la Aplicación:**

    Abre tu navegador y ve a `http://localhost:8000/` (el puerto predeterminado de Django).

---

## Aprendizajes y Retos

Este proyecto me permitió consolidar mis conocimientos en **Django y Python**, así como en el diseño de interfaces con **Bootstrap 5**. Enfrenté el reto de optimizar las operaciones **CRUD** para una experiencia de usuario fluida y de integrar las distintas capas de la aplicación de manera eficiente.

---

## Próximas Mejoras (Roadmap)

Tengo varias ideas para futuras mejoras y funcionalidades:

* **Autenticación de Usuarios:** Implementar un sistema de registro e inicio de sesión para que cada usuario tenga sus propias tareas.
* **Priorización de Tareas:** Añadir la opción de asignar diferentes niveles de prioridad a las tareas.
* **Categorías/Etiquetas:** Permitir clasificar las tareas con categorías o etiquetas personalizadas.
* **Notificaciones:** Integrar notificaciones para recordatorios de tareas o fechas límite.
* **Mejoras en UI/UX:** Continuar refinando la interfaz de usuario para una experiencia aún más intuitiva.

---

## Contacto

¡Me encantaría conectar y discutir este proyecto o futuras oportunidades!

* **Nombre:** Santiago Boada
* **LinkedIn:** [Santiago Boada Rivas](https://www.linkedin.com/in/santiago-boada-rivas-6b4a392a4/)
* **Correo Electrónico:** [zarvi.developer@gmail.com](mailto:zarvi.developer@gmail.com)

---
