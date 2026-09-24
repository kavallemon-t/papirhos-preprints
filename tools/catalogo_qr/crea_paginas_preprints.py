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


# =========================================================
# GENERAMOS UNA FICHA PARA CADA PREPRINT
# =========================================================

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


# =========================================================
# GENERAMOS LA PÁGINA PRINCIPAL DE PREPRINTS
# =========================================================

contenido_indice = """
<div class="preprints-page">

    <section class="preprints-hero">

        <p class="preprints-eyebrow">
            Repositorio académico
        </p>

        <h1>Preprints</h1>

        <p class="preprints-lead">
            Consulta prepublicaciones y materiales académicos disponibles
            antes de su publicación editorial definitiva.
        </p>

        <p class="preprints-description">
            Cada trabajo puede contar con distintas versiones a medida que
            se realizan correcciones o actualizaciones.
        </p>

    </section>


    <section class="preprints-list">

        <div class="preprints-list-header">

            <div>

                <p class="preprints-section-label">
                    Papirhos Preprints
                </p>

                <h2>
                    Prepublicaciones recientes
                </h2>

            </div>

        </div>

"""


for preprint in preprints:

    id_preprint = preprint["id_preprint"]
    titulo = preprint["titulo"]
    resumen = preprint["resumen"]

    # Portada: puede existir o estar vacía
    portada = (
        preprint.get("portada") or ""
    ).strip()

    autores = preprint.get("autores", [])
    versiones = preprint.get("versiones", [])

    autores_texto = " · ".join(autores)


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


    # Información de la versión actual
    if version_actual:

        numero_version = version_actual["version"]
        fecha_actual = version_actual["fecha"]
        archivo_actual = version_actual["archivo"]

        texto_versiones = (
            f"{len(versiones)} versión"
            if len(versiones) == 1
            else f"{len(versiones)} versiones"
        )

        boton_pdf = (
            f'<a href="../archivos_preprints/{archivo_actual}" '
            f'class="md-button preprint-secondary-button">'
            f'Ver PDF</a>'
        )

    else:

        numero_version = "—"
        fecha_actual = "Sin versión disponible"
        texto_versiones = "Sin versiones"
        boton_pdf = ""


    # Generamos la portada o un placeholder
    if portada:

        bloque_portada = f"""
            <div class="preprint-cover">

                <img
                    src="../portadas_preprints/{portada}"
                    alt="Portada de {titulo}"
                    loading="lazy">

            </div>
        """

    else:

        bloque_portada = f"""
            <div class="preprint-cover preprint-cover-placeholder">

                <span>
                    {id_preprint}
                </span>

                <small>
                    Preprint
                </small>

            </div>
        """


    # Generamos la tarjeta
    contenido_indice += f"""
        <article class="preprint-card">

            <div class="preprint-card-layout">

                {bloque_portada}


                <div class="preprint-card-main">


                    <div class="preprint-card-top">

                        <span class="preprint-id">
                            {id_preprint}
                        </span>

                        <span class="preprint-date">
                            Actualizado {fecha_actual}
                        </span>

                    </div>


                    <div class="preprint-card-content">

                        <h3 class="preprint-title">

                            <a href="{id_preprint}/">
                                {titulo}
                            </a>

                        </h3>


                        <p class="preprint-authors">
                            {autores_texto}
                        </p>


                        <p class="preprint-summary">
                            {resumen}
                        </p>

                    </div>


                    <div class="preprint-card-footer">

                        <div class="preprint-version-info">

                            <span class="preprint-version-badge">
                                v{numero_version}
                            </span>

                            <span class="preprint-version-count">
                                {texto_versiones}
                            </span>

                        </div>


                        <div class="preprint-actions">

                            <a
                                href="{id_preprint}/"
                                class="md-button md-button--primary">
                                Ver ficha
                            </a>

                            {boton_pdf}

                        </div>

                    </div>


                </div>

            </div>

        </article>
"""


# Cerramos las secciones principales
contenido_indice += """
    </section>

</div>
"""


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