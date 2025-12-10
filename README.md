# Catálogo Virtual de Repuestos Médicos y Estéticos

Este proyecto es un catálogo virtual interactivo para gestionar y visualizar repuestos de equipos médicos y estéticos. Está diseñado para ser ligero, rápido y fácil de desplegar en cualquier servidor estático como GitHub Pages.

## Características Principales

*   **Gestión de Inventario (CRUD):**
    *   **Crear:** Agregue nuevos repuestos con nombre, equipo, cantidad y foto.
    *   **Leer:** Visualice todos los repuestos en una cuadrícula moderna con búsqueda y filtros.
    *   **Actualizar:** Edite la información de cualquier repuesto existente.
    *   **Eliminar:** Borre repuestos obsoletos.
*   **Intercambio de Imágenes (Drag & Drop):** Arrastre y suelte tarjetas para intercambiar imágenes rápidamente entre productos.
*   **Persistencia de Datos:** Todos los cambios se guardan automáticamente en el navegador (LocalStorage), por lo que no se pierden al recargar la página.
*   **Base de Datos JSON:** Los datos iniciales se cargan desde un archivo `data.json`, facilitando la actualización masiva.
*   **Diseño Responsivo:** Funciona perfectamente en computadoras, tablets y móviles.

## Estructura del Proyecto

*   `catalogo_repuestos.html`: El archivo principal de la aplicación.
*   `data.json`: Contiene la base de datos inicial de repuestos.
*   `images/`: Carpeta que almacena las imágenes de los repuestos.

## Cómo Desplegar en GitHub Pages

1.  **Subir a GitHub:**
    *   Cree un nuevo repositorio en GitHub.
    *   Suba todos los archivos de este proyecto (`catalogo_repuestos.html`, `data.json`, carpeta `images/`, etc.) a ese repositorio.
    *   Asegúrese de renombrar `catalogo_repuestos.html` a `index.html` para que sea la página principal por defecto.

2.  **Activar GitHub Pages:**
    *   Vaya a la pestaña **Settings** (Configuración) de su repositorio.
    *   Busque la sección **Pages** en el menú lateral izquierdo.
    *   En **Source**, seleccione la rama `main` (o `master`) y la carpeta `/root`.
    *   Haga clic en **Save**.

3.  **¡Listo!**
    *   GitHub le proporcionará un enlace (ej. `https://usuario.github.io/nombre-repo/`).
    *   Cualquier persona con ese enlace podrá ver y utilizar el catálogo desde cualquier lugar.

## Uso Local

Simplemente abra el archivo `catalogo_repuestos.html` (o `index.html`) en su navegador web favorito (Chrome, Edge, Firefox).

## Notas Importantes

*   **Persistencia:** Los cambios realizados por el usuario (nuevos productos, ediciones) se guardan en el **navegador del usuario**. Si abre el catálogo en otra computadora, verá los datos originales del archivo `data.json`.
*   **Imágenes:** Al subir nuevas imágenes desde la web, estas se guardan en el navegador. Para agregar imágenes permanentes para todos los usuarios, debe agregarlas a la carpeta `images/` y actualizar el archivo `data.json` antes de subir los cambios a GitHub.