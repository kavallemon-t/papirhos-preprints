import pandas as pd
import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


preprints = pd.read_csv(
    os.path.join(BASE_DIR, "preprints.csv"),
    dtype=str
)

autores = pd.read_csv(
    os.path.join(BASE_DIR, "autores.csv"),
    dtype=str
)

preprints_autores = pd.read_csv(
    os.path.join(BASE_DIR, "preprints_autores.csv"),
    dtype=str
)

versiones = pd.read_csv(
    os.path.join(BASE_DIR, "versiones.csv"),
    dtype=str
)


# Creamos el nombre completo de cada autor
autores["autor_fmt"] = (
    autores["nombres"].fillna("").str.strip()
    + " "
    + autores["apellidos"].fillna("").str.strip()
).str.strip()


# Unimos la tabla intermedia con la información de los autores
pa = preprints_autores.merge(
    autores[["id_autor", "autor_fmt"]],
    on="id_autor",
    how="left"
)

print("\nRELACIÓN PREPRINTS - AUTORES")
print(pa)


# Agrupamos todos los autores de cada preprint
autores_por_preprint = (
    pa.groupby("id_preprint")["autor_fmt"]
    .apply(lambda s: [x for x in s if x != ""])
    .reset_index(name="autores")
)

print("\nAUTORES AGRUPADOS")
print(autores_por_preprint)


# Añadimos los autores a la tabla principal de preprints
catalogo_preprints = preprints.merge(
    autores_por_preprint,
    on="id_preprint",
    how="left"
)

print("\nCATÁLOGO DE PREPRINTS")
print(catalogo_preprints)

# Convertimos cada fila de versiones en un diccionario
versiones["version_info"] = versiones.apply(
    lambda fila: {
        "id_version": fila["id_version"],
        "version": fila["version"],
        "fecha": fila["fecha"],
        "archivo": fila["archivo"],
        "nota_version": fila["nota_version"],
    },
    axis=1
)

# Agrupamos todas las versiones de cada preprint
versiones_por_preprint = (
    versiones.groupby("id_preprint")["version_info"]
    .apply(list)
    .reset_index(name="versiones")
)

print("\nVERSIONES AGRUPADAS")
print(versiones_por_preprint)


# Añadimos las versiones al catálogo de preprints
catalogo_preprints = catalogo_preprints.merge(
    versiones_por_preprint,
    on="id_preprint",
    how="left"
)

print("\nCATÁLOGO COMPLETO")
print(catalogo_preprints)

# Ruta donde se guardará el JSON
PROJECT_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..")
)

DATA_DIR = os.path.join(PROJECT_DIR, "docs", "data")

# Nos aseguramos de que la carpeta exista
os.makedirs(DATA_DIR, exist_ok=True)

OUTPUT_JSON = os.path.join(
    DATA_DIR,
    "preprints.json"
)


# Convertimos el catálogo a una lista de diccionarios
registros = catalogo_preprints.to_dict(orient="records")


# Guardamos el JSON
with open(OUTPUT_JSON, "w", encoding="utf-8") as archivo:
    json.dump(
        registros,
        archivo,
        ensure_ascii=False,
        indent=2
    )

print(f"\nJSON generado en: {OUTPUT_JSON}")