import csv
import os
import shutil
import unicodedata


# =========================================================
# RUTAS DEL PROYECTO
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_DIR = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        ".."
    )
)


# =========================================================
# ARCHIVOS DE ORIGEN
# =========================================================

LIBROS_CSV = os.path.join(
    BASE_DIR,
    "libros.csv"
)

LIBROS_AUTORES_CSV = os.path.join(
    BASE_DIR,
    "libros_autores.csv"
)


PDFS_ORIGEN = os.path.join(
    PROJECT_DIR,
    "docs",
    "assets",
    "pdfs_src"
)

PORTADAS_ORIGEN = os.path.join(
    PROJECT_DIR,
    "docs",
    "assets",
    "covers"
)


# =========================================================
# ARCHIVOS DE DESTINO
# =========================================================

PREPRINTS_CSV = os.path.join(
    BASE_DIR,
    "preprints.csv"
)

PREPRINTS_AUTORES_CSV = os.path.join(
    BASE_DIR,
    "preprints_autores.csv"
)

VERSIONES_CSV = os.path.join(
    BASE_DIR,
    "versiones.csv"
)


PDFS_DESTINO = os.path.join(
    PROJECT_DIR,
    "docs",
    "archivos_preprints"
)

PORTADAS_DESTINO = os.path.join(
    PROJECT_DIR,
    "docs",
    "portadas_preprints"
)

FICHAS_DESTINO = os.path.join(
    PROJECT_DIR,
    "docs",
    "preprints"
)


# =========================================================
# CONFIGURACIÓN DE ESTA PRIMERA CARGA
# =========================================================

# Esta fecha representa la incorporación inicial
# de estos archivos a Papirhos Preprints.
#
# NO estamos diciendo que sea la fecha de publicación
# original del libro.
FECHA_VERSION_INICIAL = "2026-09-29"


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================

def leer_csv(ruta):

    with open(
        ruta,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as archivo:

        return list(
            csv.DictReader(archivo)
        )


def escribir_csv(
    ruta,
    columnas,
    filas
):

    with open(
        ruta,
        "w",
        encoding="utf-8",
        newline=""
    ) as archivo:

        writer = csv.DictWriter(
            archivo,
            fieldnames=columnas
        )

        writer.writeheader()
        writer.writerows(filas)


def normalizar_texto(texto):

    texto = str(texto or "").strip()

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto.lower()


def preparar_resumen(resumen):

    """
    Algunos resúmenes del catálogo actual son
    únicamente textos provisionales de prueba.

    No queremos mostrarlos como si fueran
    resúmenes académicos reales.
    """

    texto = str(resumen or "").strip()

    normalizado = normalizar_texto(texto)


    valores_provisionales = {
        "resumen proximamente",
        "resumen 2",
        "resumen 3",
        "resumen 5",
        "resuemn 6",
    }


    if (
        not texto
        or normalizado in valores_provisionales
    ):

        return "Resumen no disponible por el momento."


    return texto


def buscar_portada(id_preprint):

    extensiones = [
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    ]


    for extension in extensiones:

        nombre = (
            f"{id_preprint}{extension}"
        )

        ruta = os.path.join(
            PORTADAS_ORIGEN,
            nombre
        )


        if os.path.isfile(ruta):

            return nombre


    return ""


# =========================================================
# PREPARAMOS CARPETAS
# =========================================================

os.makedirs(
    PDFS_DESTINO,
    exist_ok=True
)

os.makedirs(
    PORTADAS_DESTINO,
    exist_ok=True
)

os.makedirs(
    FICHAS_DESTINO,
    exist_ok=True
)


# =========================================================
# LEEMOS LA INFORMACIÓN EXISTENTE
# =========================================================

libros = leer_csv(
    LIBROS_CSV
)

libros_autores = leer_csv(
    LIBROS_AUTORES_CSV
)


# =========================================================
# TABLAS NUEVAS
# =========================================================

preprints_nuevos = []

versiones_nuevas = []

ids_migrados = set()


# =========================================================
# MIGRAMOS LOS REGISTROS QUE TIENEN PDF
# =========================================================

for libro in libros:

    id_preprint = (
        libro.get("id_libro", "")
        .strip()
    )


    if not id_preprint:

        continue


    pdf_origen = os.path.join(
        PDFS_ORIGEN,
        f"{id_preprint}.pdf"
    )


    # Solamente incorporamos materiales
    # para los que realmente tenemos PDF.
    if not os.path.isfile(pdf_origen):

        print(
            f"ADVERTENCIA: "
            f"{id_preprint} no tiene PDF. "
            f"No se migrará."
        )

        continue


    # =====================================================
    # PORTADA
    # =====================================================

    portada = buscar_portada(
        id_preprint
    )


    if portada:

        portada_origen = os.path.join(
            PORTADAS_ORIGEN,
            portada
        )

        portada_destino = os.path.join(
            PORTADAS_DESTINO,
            portada
        )


        shutil.copy2(
            portada_origen,
            portada_destino
        )


    # =====================================================
    # PDF — PRIMERA VERSIÓN
    # =====================================================

    archivo_version = (
        f"{id_preprint}-v1.pdf"
    )


    pdf_destino = os.path.join(
        PDFS_DESTINO,
        archivo_version
    )


    shutil.copy2(
        pdf_origen,
        pdf_destino
    )


    # =====================================================
    # REGISTRO DEL PREPRINT
    # =====================================================

    preprints_nuevos.append(
        {
            "id_preprint": id_preprint,

            "titulo":
                libro.get(
                    "titulo",
                    ""
                ).strip(),

            "coleccion":
                libro.get(
                    "coleccion",
                    ""
                ).strip(),

            "serie":
                libro.get(
                    "serie",
                    ""
                ).strip(),

            "num_serie":
                libro.get(
                    "num_serie",
                    ""
                ).strip(),

            "resumen":
                preparar_resumen(
                    libro.get(
                        "resumen",
                        ""
                    )
                ),

            # No conservamos aquí estados editoriales
            # como "Publicado" o "Físico".
            #
            # Dentro de Papirhos Preprints estos
            # materiales están disponibles/activos.
            "estado": "Activo",

            "portada": portada,
        }
    )


    # =====================================================
    # PRIMERA VERSIÓN
    # =====================================================

    versiones_nuevas.append(
        {
            "id_version":
                f"{id_preprint}-v1",

            "id_preprint":
                id_preprint,

            "version":
                "1",

            "fecha":
                FECHA_VERSION_INICIAL,

            "archivo":
                archivo_version,

            "nota_version":
                (
                    "Primera versión disponible "
                    "en Papirhos Preprints."
                ),
        }
    )


    ids_migrados.add(
        id_preprint
    )


    print(
        f"Migrado: {id_preprint}"
    )


# =========================================================
# RELACIÓN PREPRINTS - AUTORES
# =========================================================

preprints_autores_nuevos = []


for relacion in libros_autores:

    id_libro = (
        relacion.get(
            "id_libro",
            ""
        ).strip()
    )

    id_autor = (
        relacion.get(
            "id_autor",
            ""
        ).strip()
    )


    if id_libro not in ids_migrados:

        continue


    if not id_autor:

        continue


    preprints_autores_nuevos.append(
        {
            "id_preprint":
                id_libro,

            "id_autor":
                id_autor,
        }
    )


# =========================================================
# ESCRIBIMOS LAS TRES TABLAS DE PREPRINTS
# =========================================================

escribir_csv(
    PREPRINTS_CSV,
    [
        "id_preprint",
        "titulo",
        "coleccion",
        "serie",
        "num_serie",
        "resumen",
        "estado",
        "portada",
    ],
    preprints_nuevos
)


escribir_csv(
    PREPRINTS_AUTORES_CSV,
    [
        "id_preprint",
        "id_autor",
    ],
    preprints_autores_nuevos
)


escribir_csv(
    VERSIONES_CSV,
    [
        "id_version",
        "id_preprint",
        "version",
        "fecha",
        "archivo",
        "nota_version",
    ],
    versiones_nuevas
)


# =========================================================
# ELIMINAMOS LAS FICHAS DE PRUEBA ANTIGUAS
# =========================================================

ids_prueba = [
    "pap-pre-001",
    "pap-pre-002",
]


for id_prueba in ids_prueba:

    ficha = os.path.join(
        FICHAS_DESTINO,
        f"{id_prueba}.md"
    )


    if os.path.isfile(ficha):

        os.remove(ficha)

        print(
            f"Ficha de prueba eliminada: "
            f"{id_prueba}.md"
        )


    # Eliminamos posibles PDFs de prueba.
    if os.path.isdir(PDFS_DESTINO):

        for nombre in os.listdir(
            PDFS_DESTINO
        ):

            if nombre.startswith(
                id_prueba
            ):

                ruta = os.path.join(
                    PDFS_DESTINO,
                    nombre
                )

                if os.path.isfile(ruta):

                    os.remove(ruta)


    # Eliminamos posibles portadas de prueba.
    if os.path.isdir(PORTADAS_DESTINO):

        for nombre in os.listdir(
            PORTADAS_DESTINO
        ):

            if nombre.startswith(
                id_prueba
            ):

                ruta = os.path.join(
                    PORTADAS_DESTINO,
                    nombre
                )

                if os.path.isfile(ruta):

                    os.remove(ruta)


# =========================================================
# RESUMEN
# =========================================================

print()
print("=" * 55)
print("MIGRACIÓN TERMINADA")
print("=" * 55)

print(
    f"Preprints migrados: "
    f"{len(preprints_nuevos)}"
)

print(
    f"Relaciones autor-preprint: "
    f"{len(preprints_autores_nuevos)}"
)

print(
    f"Versiones creadas: "
    f"{len(versiones_nuevas)}"
)

print()
print(
    "Ahora ejecuta crea_preprints.py "
    "y crea_paginas_preprints.py."
)