?# Guía Completa: Cómo Publicar y Actualizar tu Catálogo en Internet (Gratis)

Esta guía te enseñará cómo poner tu catálogo en internet usando **GitHub Pages** para que cualquier persona pueda verlo desde su celular o computadora. También aprenderás el "ciclo de actualización" para mantenerlo al día.

---

## Parte 1: Publicar por Primera Vez

### Paso 1: Crear una cuenta en GitHub
1.  Ve a [github.com](https://github.com/) y crea una cuenta gratuita (si no tienes una).

### Paso 2: Crear un Repositorio
1.  Inicia sesión y haz clic en el botón **"+"** en la esquina superior derecha -> **New repository**.
2.  **Repository name:** Escribe un nombre simple, por ejemplo: `catalogo-repuestos`.
3.  Asegúrate de que esté marcado como **Public**.
4.  Haz clic en **Create repository**.

### Paso 3: Subir tus Archivos
1.  En la pantalla siguiente, busca el enlace que dice **"uploading an existing file"**.
2.  Arrastra y suelta los siguientes archivos y carpetas de tu proyecto:
    *   `index.html` (El archivo principal del catálogo).
    *   `data.json` (Tu base de datos de repuestos).
    *   La carpeta `images` completa (con todas las fotos).
3.  Espera a que se carguen todos los archivos.
4.  En el cuadro "Commit changes", escribe "Versión inicial" y haz clic en el botón verde **Commit changes**.

### Paso 4: Activar tu Página Web
1.  En tu repositorio, ve a la pestaña **Settings** (arriba a la derecha, icono de engranaje).
2.  En el menú de la izquierda, busca y haz clic en **Pages**.
3.  En la sección **Build and deployment** > **Branch**, selecciona `main` (o `master`) y asegúrate que la carpeta sea `/(root)`.
4.  Haz clic en **Save**.
5.  Espera unos minutos (1-3 min). Refresca la página hasta que veas un mensaje arriba que dice: **"Your site is live at..."** seguido de un enlace.
6.  ¡Ese es el enlace de tu catálogo! Compártelo con quien quieras.

---

## Parte 2: Cómo Actualizar tu Catálogo (El Ciclo de Trabajo)

Como esta es una página web "estática" (sin base de datos en la nube), los cambios que haces en el navegador **NO** se guardan automáticamente en internet. Debes seguir este proceso:

### 1. Edita en tu Computadora
1.  Abre el archivo `index.html` en tu computadora.
2.  Haz todos los cambios que necesites:
    *   Agrega nuevos repuestos.
    *   Cambia precios o cantidades.
    *   Sube nuevas fotos.
    *   Marca prioridades.

### 2. Guarda los Cambios
1.  Cuando termines de editar, haz clic en el botón verde **"Guardar JSON"** en la barra superior del catálogo.
2.  Esto descargará un archivo llamado `data.json` a tu carpeta de Descargas.

### 3. Actualiza GitHub (Internet)
1.  Ve a tu repositorio en GitHub (el que creaste en la Parte 1).
2.  Haz clic en **Add file** > **Upload files**.
3.  Arrastra el archivo `data.json` que acabas de descargar.
    *   **Importante:** Si agregaste **NUEVAS FOTOS** desde tu computadora, esas fotos se guardaron temporalmente en tu navegador. Para que se vean en internet, debes subir también los archivos de imagen originales a la carpeta `images` en GitHub o asegurarte de que el `data.json` tenga las imágenes incrustadas (el sistema actual ya las incrusta automáticamente para facilitar esto).
4.  Escribe un mensaje como "Actualización de inventario" y haz clic en **Commit changes**.

¡Listo! En unos minutos, tu página web pública se actualizará con la nueva información.

---

## Resumen del Flujo de Trabajo

1.  **Abres** el catálogo local en tu PC.
2.  **Haces cambios** (agregar, editar, borrar).
3.  **Descargas** el `data.json` con el botón verde.
4.  **Subes** ese archivo a GitHub.

¡Así de fácil mantienes tu catálogo actualizado para todo el mundo!