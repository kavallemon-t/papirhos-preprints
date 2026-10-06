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

    # Portada: puede existir o estar vacía
    portada = (
        preprint.get("portada") or ""
    ).strip()

    autores = preprint.get("autores", [])
    versiones = preprint.get("versiones", [])

    # Para las citas usamos comas
    autores_texto = ", ".join(autores)

    # Para el encabezado visual usamos puntos medios
    autores_header = " · ".join(autores)


    # Ordenamos las versiones de la más reciente
    # a la más antigua
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


    # =====================================================
    # PORTADA DE LA FICHA
    # =====================================================

    if portada:

        portada_ficha = f"""
            <div class="preprint-detail-cover">

                <img
                    src="../../portadas_preprints/{portada}"
                    alt="Portada de {titulo}"
                    loading="lazy">

            </div>
        """

    else:

        portada_ficha = f"""
            <div
                class="preprint-detail-cover
                       preprint-detail-cover-placeholder">

                <span>
                    {id_preprint}
                </span>

                <small>
                    Preprint
                </small>

            </div>
        """


    # =====================================================
    # INFORMACIÓN RÁPIDA DE LA VERSIÓN ACTUAL
    # =====================================================

    if version_actual:

        version_header = (
            f'v{version_actual["version"]} actual'
        )

        fecha_header = version_actual["fecha"]

        boton_pdf_header = f"""
            <a
                href="../../archivos_preprints/{version_actual["archivo"]}"
                class="md-button md-button--primary">

                Ver PDF

            </a>
        """

    else:

        version_header = "Sin versión"
        fecha_header = "Sin fecha"
        boton_pdf_header = ""


    # =====================================================
    # ENCABEZADO VISUAL DE LA FICHA
    # =====================================================

    contenido = f"""---
title: "{id_preprint}"
---

<section class="preprint-detail-hero">

    {portada_ficha}


    <div class="preprint-detail-main">

        <p class="preprint-detail-eyebrow">
            Preprint · {id_preprint}
        </p>


        <h1>
            {titulo}
        </h1>


        <p class="preprint-detail-authors">
            {autores_header}
        </p>


        <div class="preprint-detail-version">

            <span class="preprint-version-badge">
                {version_header}
            </span>

            <span class="preprint-detail-date">
                {fecha_header}
            </span>

        </div>


        <div class="preprint-detail-actions">

            {boton_pdf_header}

            <a
                href="../"
                class="md-button preprint-secondary-button">

                Volver a Preprints

            </a>

        </div>

    </div>

</section>


<section class="libro-seccion libro-resumen preprint-resumen">

    <h2>
        Resumen
    </h2>

    <p>
        {resumen}
    </p>

</section>

"""


    # =====================================================
    # INFORMACIÓN DE LA VERSIÓN ACTUAL
    # =====================================================

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


        # =================================================
        # VERSIÓN ACTUAL
        # =================================================

        contenido += f"""
<section class="libro-seccion preprint-version-section">

    <h2>
        Versión actual
    </h2>


    <div class="preprint-current-version-card">

        <div class="preprint-current-version-header">

            <div>

                <p class="preprint-current-version-label">
                    Versión vigente
                </p>


                <div class="preprint-current-version-number">

                    <span class="preprint-version-badge">
                        v{version_actual["version"]}
                    </span>

                    <span class="preprint-current-version-date">
                        {version_actual["fecha"]}
                    </span>

                </div>

            </div>


            <a
                href="../../archivos_preprints/{version_actual["archivo"]}"
                class="md-button md-button--primary">

                Ver PDF

            </a>

        </div>


        <div class="preprint-current-version-change">

            <span class="preprint-version-meta-label">
                Cambios en esta versión
            </span>

            <p>
                {version_actual.get("nota_version") or "Sin nota de cambios."}
            </p>

        </div>

    </div>

</section>


<section class="libro-seccion preprint-citation-section">

    <h2>
        Cómo citar
    </h2>


    <div class="citation-box citation-box-featured">

        <div class="citation-box-main">

            <p
                id="{id_cita_actual}"
                class="citation-text">

                {cita}

            </p>

        </div>


        <button
            type="button"
            class="citation-copy-button"
            data-target="{id_cita_actual}">

            Copiar cita

        </button>

    </div>


    <details class="preprint-bibtex-details">

        <summary>
            BibTeX
        </summary>


        <div class="preprint-bibtex-content">

            <textarea
                id="{id_bibtex_actual}"
                rows="7"
                cols="80"
                class="verbatim preprint-bibtex-area">{bibtex}</textarea>


            <button
                type="button"
                class="bibtex-copy-button"
                data-target="{id_bibtex_actual}">

                Copiar BibTeX

            </button>

        </div>

    </details>

</section>

"""


    # =====================================================
    # HISTORIAL DE VERSIONES
    # =====================================================

    contenido += """
<section class="libro-seccion preprint-history-section">

    <h2>
        Historial de versiones
    </h2>


    <p class="preprint-history-intro">
        Consulta las versiones anteriores de este preprint,
        sus fechas de publicación y los cambios realizados.
    </p>


    <div class="preprint-history-list">

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


        # Indicamos visualmente cuál es la versión actual
        es_actual = (
            version_actual
            and version["version"] == version_actual["version"]
        )

        etiqueta_actual = (
            '<span class="preprint-history-current">Actual</span>'
            if es_actual
            else ""
        )


        nota_version = (
            version.get("nota_version")
            or "Sin nota de cambios."
        )


        contenido += f"""
        <article class="preprint-history-card">

            <div class="preprint-history-card-header">

                <div class="preprint-history-version">

                    <span class="preprint-history-number">
                        v{version["version"]}
                    </span>

                    {etiqueta_actual}

                </div>


                <span class="preprint-history-date">
                    {version["fecha"]}
                </span>

            </div>


            <div class="preprint-history-card-body">

                <div class="preprint-history-change">

                    <span class="preprint-version-meta-label">
                        Cambios
                    </span>

                    <p>
                        {nota_version}
                    </p>

                </div>


                <a
                    href="../../archivos_preprints/{version["archivo"]}"
                    class="md-button preprint-secondary-button">

                    Ver PDF

                </a>

            </div>


            <details class="preprint-history-details">

                <summary>
                    Citación y BibTeX
                </summary>


                <div class="preprint-history-citation-content">

                    <div class="citation-box">

                        <div class="citation-box-main">

                            <p
                                id="{id_cita_version}"
                                class="citation-text">

                                {cita_version}

                            </p>

                        </div>


                        <button
                            type="button"
                            class="citation-copy-button"
                            data-target="{id_cita_version}">

                            Copiar cita

                        </button>

                    </div>


                    <div class="preprint-history-bibtex">

                        <p class="preprint-history-bibtex-title">
                            BibTeX
                        </p>


                        <textarea
                            id="{id_bibtex_version}"
                            rows="7"
                            cols="80"
                            class="verbatim preprint-bibtex-area">{bibtex_version}</textarea>


                        <button
                            type="button"
                            class="bibtex-copy-button"
                            data-target="{id_bibtex_version}">

                            Copiar BibTeX

                        </button>

                    </div>

                </div>

            </details>

        </article>

"""


    contenido += """
    </div>

</section>

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


        <div class="preprints-search">

            <label
                for="preprints-search-input"
                class="preprints-search-label">
                Buscar preprints
            </label>

            <div class="preprints-search-box">

                <input
                    type="search"
                    id="preprints-search-input"
                    placeholder="Buscar por título, autor, identificador o palabra clave..."
                    autocomplete="off">

            </div>

            <p
                id="preprints-results-count"
                class="preprints-results-count">
            </p>

            <div class="preprints-advanced-link">
                <a href="../explorar/">
                    Búsqueda avanzada →
                </a>
            </div>

        </div>


        <div
            id="preprints-no-results"
            class="preprints-no-results"
            hidden>

            <strong>
                No se encontraron preprints.
            </strong>

            <span>
                Intenta con otro título, autor,
                identificador o palabra clave.
            </span>

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


                        <div class="preprint-summary-wrapper">

                            <p class="preprint-summary preprint-summary-collapsed">
                                {resumen}
                            </p>

                            <button
                                type="button"
                                class="preprint-summary-toggle">
                                Ver más
                            </button>

                        </div>

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

# =========================================================
# BUSCADOR Y RESÚMENES EXPANDIBLES
# =========================================================

contenido_indice += """
<script>

(() => {

    const input = document.getElementById(
        "preprints-search-input"
    );

    const cards = Array.from(
        document.querySelectorAll(".preprint-card")
    );

    const count = document.getElementById(
        "preprints-results-count"
    );

    const noResults = document.getElementById(
        "preprints-no-results"
    );


    // =====================================================
    // RESÚMENES EXPANDIBLES
    // =====================================================

    function actualizarBotonesResumenes() {

        const wrappers =
            document.querySelectorAll(
                ".preprint-summary-wrapper"
            );


        wrappers.forEach((wrapper) => {

            const resumen =
                wrapper.querySelector(
                    ".preprint-summary"
                );

            const boton =
                wrapper.querySelector(
                    ".preprint-summary-toggle"
                );


            if (!resumen || !boton) {
                return;
            }


            /*
             * Guardamos el estado actual del resumen.
             */

            const estabaCerrado =
                resumen.classList.contains(
                    "preprint-summary-collapsed"
                );


            /*
             * Medimos cuánto ocupa cuando está
             * reducido a cuatro líneas.
             */

            resumen.classList.add(
                "preprint-summary-collapsed"
            );

            const alturaReducida =
                resumen.getBoundingClientRect().height;


            /*
             * Quitamos temporalmente el límite
             * para medir la altura completa.
             */

            resumen.classList.remove(
                "preprint-summary-collapsed"
            );

            const alturaCompleta =
                resumen.getBoundingClientRect().height;


            /*
             * Restauramos el estado que tenía.
             */

            if (estabaCerrado) {

                resumen.classList.add(
                    "preprint-summary-collapsed"
                );

            }


            /*
             * Si el texto completo cabe dentro
             * de las cuatro líneas, no necesitamos
             * mostrar el botón.
             */

            if (
                alturaCompleta <=
                alturaReducida + 2
            ) {

                boton.hidden = true;

            } else {

                boton.hidden = false;

            }

        });

    }


    const botonesResumen =
        document.querySelectorAll(
            ".preprint-summary-toggle"
        );


    botonesResumen.forEach((boton) => {

        boton.addEventListener(
            "click",
            () => {

                const wrapper =
                    boton.closest(
                        ".preprint-summary-wrapper"
                    );


                if (!wrapper) {
                    return;
                }


                const resumen =
                    wrapper.querySelector(
                        ".preprint-summary"
                    );


                if (!resumen) {
                    return;
                }


                const estaCerrado =
                    resumen.classList.contains(
                        "preprint-summary-collapsed"
                    );


                if (estaCerrado) {

                    resumen.classList.remove(
                        "preprint-summary-collapsed"
                    );

                    boton.textContent =
                        "Ver menos";

                } else {

                    resumen.classList.add(
                        "preprint-summary-collapsed"
                    );

                    boton.textContent =
                        "Ver más";

                }

            }
        );

    });


    /*
     * Esperamos a que el navegador haya calculado
     * correctamente tamaños y tipografías antes
     * de decidir qué resúmenes necesitan botón.
     */

    requestAnimationFrame(
        actualizarBotonesResumenes
    );


    if (
        document.fonts &&
        document.fonts.ready
    ) {

        document.fonts.ready.then(
            actualizarBotonesResumenes
        );

    }


    // =====================================================
    // BUSCADOR
    // =====================================================

    function normalizar(texto) {

        return texto
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\\u0300-\\u036f]/g, "")
            .trim();

    }


    function actualizarContador(visibles) {

        if (!count) return;


        if (visibles === 1) {

            count.textContent =
                "1 preprint encontrado";

        } else {

            count.textContent =
                `${visibles} preprints encontrados`;

        }

    }


    function filtrarPreprints() {

        const consulta = normalizar(
            input.value
        );

        let visibles = 0;


        cards.forEach((card) => {

            const contenido = normalizar(
                card.textContent
            );

            const coincide =
                consulta === "" ||
                contenido.includes(consulta);


            card.hidden = !coincide;


            if (coincide) {
                visibles += 1;
            }

        });


        actualizarContador(visibles);


        if (noResults) {

            noResults.hidden =
                visibles !== 0;

        }

    }


    // =====================================================
    // EVENTOS DEL BUSCADOR
    // =====================================================

    if (input) {

        input.addEventListener(
            "input",
            filtrarPreprints
        );

    }


    actualizarContador(
        cards.length
    );

})();

</script>
"""


# =========================================================
# GUARDAMOS LA PÁGINA PRINCIPAL
# =========================================================

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