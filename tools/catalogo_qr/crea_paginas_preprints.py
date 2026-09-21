import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..")
)

JSON_PATH = os.path.join(
    PROJECT_DIR,
    "docs",
    "data",
    "preprints.json"
)

OUTPUT_DIR = os.path.join(
    PROJECT_DIR,
    "docs",
    "preprints"
)


# Nos aseguramos de que exista la carpeta de salida
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Leemos los datos de los preprints
with open(JSON_PATH, "r", encoding="utf-8") as archivo:
    preprints = json.load(archivo)


for preprint in preprints:

    id_preprint = preprint["id_preprint"]
    titulo = preprint["titulo"]
    resumen = preprint["resumen"]

    autores = preprint.get("autores", [])
    versiones = preprint.get("versiones", [])

    autores_texto = ", ".join(autores)


    # Ordenamos las versiones de la más reciente a la más antigua
    versiones_ordenadas = sorted(
        versiones,
        key=lambda v: int(v["version"]),
        reverse=True
    )


    # Obtenemos la versión más reciente
    version_actual = versiones_ordenadas[0] if versiones_ordenadas else None


    contenido = f"""# {titulo}

**Autores:** {autores_texto}

**Identificador:** `{id_preprint}`

---

## Resumen

{resumen}

"""


    # Información de la versión actual
    if version_actual:
        contenido += f"""## Versión actual

**v{version_actual["version"]}**

**Fecha:** {version_actual["fecha"]}

**Archivo:** `{version_actual["archivo"]}`

**Cambios:** {version_actual["nota_version"]}

"""


    # Historial de versiones
    contenido += """## Historial de versiones

"""

    for version in versiones_ordenadas:

        contenido += f"""### v{version["version"]}

- **Fecha:** {version["fecha"]}
- **Archivo:** `{version["archivo"]}`
- **Cambios:** {version["nota_version"]}

"""


    # Guardamos la ficha
    OUTPUT_PATH = os.path.join(
        OUTPUT_DIR,
        f"{id_preprint}.md"
    )

    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(contenido)


    print(f"Ficha generada: {OUTPUT_PATH}")

# Generamos la página principal de preprints
contenido_indice = """# Preprints

Consulta las prepublicaciones y materiales académicos disponibles antes de su publicación editorial definitiva.

Los documentos pueden contar con distintas versiones a medida que se realizan correcciones o actualizaciones.

---

## Prepublicaciones disponibles

"""


for preprint in preprints:

    id_preprint = preprint["id_preprint"]
    titulo = preprint["titulo"]
    resumen = preprint["resumen"]

    autores = preprint.get("autores", [])
    versiones = preprint.get("versiones", [])

    autores_texto = ", ".join(autores)

    # Buscamos la versión más reciente
    versiones_ordenadas = sorted(
        versiones,
        key=lambda v: int(v["version"]),
        reverse=True
    )

    version_actual = (
        versiones_ordenadas[0]
        if versiones_ordenadas
        else None
    )


    contenido_indice += f"""### {titulo}

**Autores:** {autores_texto}

{resumen}

"""

    if version_actual:
        contenido_indice += (
            f"**Versión actual:** "
            f"v{version_actual['version']} "
            f"— {version_actual['fecha']}\n\n"
        )

    contenido_indice += (
        f"[Ver ficha](preprints/{id_preprint}.md)\n\n"
        "---\n\n"
    )


# Guardamos la página principal
INDICE_PATH = os.path.join(
    PROJECT_DIR,
    "docs",
    "preprints.md"
)

with open(
    INDICE_PATH,
    "w",
    encoding="utf-8"
) as archivo:
    archivo.write(contenido_indice)

print(f"Índice de preprints generado: {INDICE_PATH}")