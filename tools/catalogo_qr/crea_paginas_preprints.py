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

SITE_URL = "https://kavallemon-t.github.io/papirhos-preprints"

# Nos aseguramos de que exista la carpeta de salida
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Leemos los datos de los preprints
with open(JSON_PATH, "r", encoding="utf-8") as archivo:
    preprints = json.load(archivo)


# Generamos una ficha para cada preprint
for preprint in preprints:

    id_preprint = preprint["id_preprint"]
    url_preprint = f"{SITE_URL}/preprints/{id_preprint}/"
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
    version_actual = (
        versiones_ordenadas[0]
        if versiones_ordenadas
        else None
    )


    contenido = f"""# {titulo}

**Autores:** {autores_texto}

**Identificador:** `{id_preprint}`

---

## Resumen

{resumen}

"""


    # Información de la versión actual
    if version_actual:

        # Obtenemos el año a partir de la fecha
        anio_actual = version_actual["fecha"][:4]


        # Creamos la cita de la versión actual
        cita = (
            f"{autores_texto}. "
            f"({anio_actual}). "
            f"{titulo}. "
            f"Papirhos Preprints, "
            f"{id_preprint}, "
            f"v{version_actual['version']}. "
            f"{url_preprint}"
        )


        # Preparamos los autores para BibTeX
        autores_bibtex = " and ".join(autores)


        # Creamos el BibTeX de la versión actual
        bibtex = f"""@misc{{{id_preprint}v{version_actual["version"]},
  author = {{{autores_bibtex}}},
  title = {{{titulo}}},
  year = {{{anio_actual}}},
  note = {{Papirhos Preprints: {id_preprint}, v{version_actual["version"]}}},
  url = {{{url_preprint}}}
}}"""


        # IDs únicos para los botones
        id_cita_actual = f"cita-actual-{id_preprint}"
        id_bibtex_actual = f"bibtex-actual-{id_preprint}"


        contenido += f"""## Versión actual

**v{version_actual["version"]}**

**Fecha:** {version_actual["fecha"]}

**Cambios:** {version_actual["nota_version"]}

[Ver PDF](../archivos_preprints/{version_actual["archivo"]})

## Cómo citar

<div class="citation-box">

<blockquote id="{id_cita_actual}">
{cita}
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="{id_cita_actual}">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="{id_bibtex_actual}"
    rows="7"
    cols="80"
    class="verbatim">{bibtex}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="{id_bibtex_actual}">
    Copiar BibTeX
</button>

</details>

"""


    # Historial de versiones
    contenido += """## Historial de versiones

"""


    for version in versiones_ordenadas:

        # Obtenemos el año de esta versión
        anio_version = version["fecha"][:4]


        # Creamos la cita específica de esta versión
        cita_version = (
            f"{autores_texto}. "
            f"({anio_version}). "
            f"{titulo}. "
            f"Papirhos Preprints, "
            f"{id_preprint}, "
            f"v{version['version']}. "
            f"{url_preprint}"
        )


        # Creamos el BibTeX específico de esta versión
        autores_bibtex = " and ".join(autores)

        bibtex_version = f"""@misc{{{id_preprint}v{version["version"]},
  author = {{{autores_bibtex}}},
  title = {{{titulo}}},
  year = {{{anio_version}}},
  note = {{Papirhos Preprints: {id_preprint}, v{version["version"]}}},
  url = {{{url_preprint}}}
}}"""


        # IDs únicos para esta versión
        id_cita_version = (
            f"cita-{id_preprint}-v{version['version']}"
        )

        id_bibtex_version = (
            f"bibtex-{id_preprint}-v{version['version']}"
        )


        contenido += f"""### v{version["version"]}

- **Fecha:** {version["fecha"]}
- **Cambios:** {version["nota_version"]}
- [Ver PDF](../archivos_preprints/{version["archivo"]})

**Cómo citar esta versión**

<div class="citation-box">

<blockquote id="{id_cita_version}">
{cita_version}
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="{id_cita_version}">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="{id_bibtex_version}"
    rows="7"
    cols="80"
    class="verbatim">{bibtex_version}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="{id_bibtex_version}">
    Copiar BibTeX
</button>

</details>

"""


    # JavaScript para copiar citas y BibTeX
    contenido += """
<script>
(() => {

    const botonesBibtex =
        document.querySelectorAll(".bibtex-copy-button");

    botonesBibtex.forEach((boton) => {

        boton.addEventListener("click", () => {

            const textarea = document.getElementById(
                boton.dataset.target
            );

            if (!textarea) return;

            navigator.clipboard.writeText(
                textarea.value
            ).then(() => {

                const textoOriginal = boton.textContent;

                boton.textContent = "Copiado";
                boton.classList.add("copied");

                setTimeout(() => {
                    boton.textContent = textoOriginal;
                    boton.classList.remove("copied");
                }, 1500);

            });

        });

    });


    const botonesCita =
        document.querySelectorAll(".citation-copy-button");

    botonesCita.forEach((boton) => {

        boton.addEventListener("click", () => {

            const cita = document.getElementById(
                boton.dataset.target
            );

            if (!cita) return;

            navigator.clipboard.writeText(
                cita.innerText.trim()
            ).then(() => {

                const textoOriginal = boton.textContent;

                boton.textContent = "Copiado";
                boton.classList.add("copied");

                setTimeout(() => {
                    boton.textContent = textoOriginal;
                    boton.classList.remove("copied");
                }, 1500);

            });

        });

    });

})();
</script>
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