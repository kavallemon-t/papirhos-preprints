## Básicos de MkDocs

- `mkdocs serve`: inicia un servidor local para visualizar los cambios del sitio antes de publicarlos.
- `mkdocs build --clean`: genera el sitio completo y permite comprobar que no existan errores de construcción.
- `mkdocs gh-deploy`: construye el sitio y publica la versión actual en GitHub Pages.

## Generación de datos y páginas

En `tools/catalogo_qr/` se encuentran los archivos de datos y los scripts de Python utilizados para generar la información del sitio.

Las principales bases de datos son:

- `preprints.csv`: contiene la información general de cada preprint, como identificador, título, colección, serie y portada.
- `resumenes.csv`: contiene el resumen correspondiente a cada preprint.
- `autores.csv`: contiene la información de los autores.
- `preprints_autores.csv`: relaciona cada preprint con uno o más autores.
- `versiones.csv`: contiene las distintas versiones de cada preprint, incluyendo fecha, archivo PDF y nota de versión.

### crea_preprints.py

Lee las bases de datos de `tools/catalogo_qr/` y combina la información correspondiente a cada preprint.

Entre otras cosas:

- Relaciona los preprints con sus autores.
- Añade el resumen correspondiente a cada preprint.
- Agrupa las distintas versiones de cada preprint.
- Genera el archivo:

```text
docs/data/preprints.json

## Flujo para actualizar y revisar cambios

Cuando se modifica información de los preprints y se quiere revisar cómo quedó el sitio, se deben ejecutar los siguientes comandos desde la carpeta principal del proyecto.

### Si se modificaron los datos de los preprints

Por ejemplo:

- `preprints.csv`
- `resumenes.csv`
- `autores.csv`
- `preprints_autores.csv`
- `versiones.csv`
- se añadió o cambió una portada
- se añadió o cambió un PDF

Ejecutar:

```powershell
python tools/catalogo_qr/crea_preprints.py
python tools/catalogo_qr/crea_paginas_preprints.py
mkdocs serve