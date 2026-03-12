# Yonathan Sosa | Data Science & Automation Portfolio

Este proyecto es una aplicación web profesional desarrollada con **Flask** para mostrar un portafolio especializado en Análisis de Datos, Inteligencia Artificial y Automatización.

## 🚀 Características

- **Diseño Moderno:** Interfaz oscura, minimalista y profesional utilizando Google Fonts (Plus Jakarta Sans).
- **Sección de Contacto Optimizada:** Formulario simplificado (solo email) y tarjeta de contacto profesional para correo directo.
- **Portafolio Interactivo:** Enlaces directos a reportes de Power BI y proyectos en GitHub.
- **Backend Robusto:** Gestión de contactos mediante una base de datos SQLite y exportación automática a Excel.
- **Diseño Responsivo:** Totalmente compatible con dispositivos móviles y tablets.
- **Botón de WhatsApp:** Acceso directo para comunicación inmediata.

## 🛠️ Stack Tecnológico

- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript.
- **Backend:** Python 3.x con Flask.
- **Base de Datos:** SQLite.
- **Librerías de Datos:** Pandas, Openpyxl (para manejo de Excel).

## 📋 Pasos para la Configuración e Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Requisitos Previos
Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

### 2. Clonar o Descargar el Proyecto
Ubícate en la carpeta donde tienes los archivos:
`C:\Users\ADMIN\Desktop\PAGINA WEB`

### 3. Crear un Entorno Virtual (Opcional pero recomendado)
Abre una terminal en la carpeta del proyecto y ejecuta:
```bash
python -m venv venv
```
Actívalo:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 4. Instalar Dependencias
Instala las librerías necesarias utilizando el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Ejecutar la Aplicación
Inicia el servidor de desarrollo de Flask:
```bash
python app.py
```
La aplicación estará disponible en tu navegador en la dirección: `http://127.0.0.1:5000`

## 📁 Estructura del Proyecto

- `app.py`: Servidor principal y lógica de rutas.
- `database.db`: Base de Datos SQLite (se crea automáticamente al iniciar).
- `contactos.xlsx`: Archivo Excel donde se guardan los leads (se crea automáticamente).
- `templates/`: Carpeta con los archivos HTML (index.html).
- `static/`: Carpeta con estilos CSS, scripts JS e imágenes/certificados PDF.
- `requirements.txt`: Lista de librerías de Python necesarias.

## 📧 Gestión de Contactos
Cada vez que un usuario ingresa su correo en la sección de contacto:
1. Se guarda en la tabla `contactos` de `database.db`.
2. Se añade una nueva fila al archivo `contactos.xlsx` para facilitar su seguimiento comercial.

---
*Desarrollado para potenciar la marca personal de Yonathan Sosa.*
