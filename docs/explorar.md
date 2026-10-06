<section class="catalogo-hero catalogo-hero-busqueda">
    <p class="catalogo-eyebrow">Explorar</p>
    <h1>Búsqueda avanzada</h1>

    <p>
        Combina distintos criterios para localizar prepublicaciones
        por título, autor, colección, serie o fecha de actualización.
    </p>
</section>


<div id="filtros">

    <label>
        Colección:
        <select id="f-coleccion">
            <option value="">Todas</option>
        </select>
    </label>


    <label>
        Serie:
        <select id="f-serie">
            <option value="">Todas</option>
        </select>
    </label>


    <label>
        Año de actualización:
        <select id="f-anio">
            <option value="">Todos</option>
        </select>
    </label>


    <label>
        Autor:
        <input
            id="f-autor"
            type="text"
            placeholder="Ej. Brasselet">
    </label>


    <label>
        Título:
        <input
            id="f-titulo"
            type="text"
            placeholder="Buscar por título">
    </label>


    <label>
        Palabra clave:
        <input
            id="f-palabra"
            type="text"
            placeholder="ID, resumen, autor...">
    </label>


    <label>
        Ordenar por:
        <select id="f-order">
            <option value="fecha-desc">
                Más recientes
            </option>

            <option value="fecha-asc">
                Más antiguos
            </option>

            <option value="titulo-asc">
                Título (A → Z)
            </option>

            <option value="titulo-desc">
                Título (Z → A)
            </option>
        </select>
    </label>


    <button
        id="btn-clear"
        type="button"
        class="md-button">
        Limpiar filtros
    </button>

</div>


<div class="busqueda-resultados-header">
    <span id="contador"></span>
</div>


<div id="resultados"></div>


<script>

(async function () {

    /*
     * Calculamos la raíz del sitio a partir de la página actual.
     *
     * Ejemplos:
     *
     * Local:
     * /papirhos-preprints/explorar/
     *          ↓
     * /papirhos-preprints/
     *
     * GitHub Pages:
     * /papirhos-preprints/explorar/
     *          ↓
     * /papirhos-preprints/
     */
    const BASE = new URL(
        "../",
        window.location.href
    ).href;


    // Leemos la base de datos de preprints.
    const respuesta = await fetch(
        `${BASE}data/preprints.json`
    );


    // Si el archivo no pudo cargarse,
    // mostramos un error claro en la consola.
    if (!respuesta.ok) {

        throw new Error(
            `No se pudo cargar preprints.json: ${respuesta.status}`
        );

    }


    const preprints =
        await respuesta.json();


    // Verificamos que el JSON tenga la estructura esperada.
    if (!Array.isArray(preprints)) {

        throw new Error(
            "preprints.json no contiene una lista válida."
        );

    }


    // Atajo para querySelector.
    const $ = (selector) =>
        document.querySelector(selector);


    // Quitamos duplicados y valores vacíos.
    const unique = (lista) =>
        Array.from(
            new Set(
                lista.filter(Boolean)
            )
        );


    // Normalizamos texto para que las búsquedas
    // no dependan de mayúsculas ni acentos.
    const normalizarTexto = (texto) =>

        String(texto || "")
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .toLowerCase()
            .trim();


    // Ordenamos las versiones de un preprint.
    function versionesOrdenadas(preprint) {

        return [...(preprint.versiones || [])]
            .sort(
                (a, b) =>
                    Number(b.version) -
                    Number(a.version)
            );

    }


    // Obtenemos la versión más reciente.
    function versionActual(preprint) {

        const versiones =
            versionesOrdenadas(preprint);

        return versiones.length
            ? versiones[0]
            : null;

    }


    // Obtenemos el año de la actualización más reciente.
    function anioActualizacion(preprint) {

        const version =
            versionActual(preprint);

        if (!version || !version.fecha) {
            return "";
        }

        return String(version.fecha)
            .slice(0, 4);

    }


    // Referencias a los controles.
    const selColeccion = $("#f-coleccion");
    const selSerie = $("#f-serie");
    const selAnio = $("#f-anio");

    const inpAutor = $("#f-autor");
    const inpTitulo = $("#f-titulo");
    const inpPalabra = $("#f-palabra");

    const selOrder = $("#f-order");

    const contador = $("#contador");
    const contenedor = $("#resultados");

    const btnClear = $("#btn-clear");


// =====================================================
// RESÚMENES EXPANDIBLES
// =====================================================

function actualizarBotonesResumenes() {

    const wrappers =
        contenedor.querySelectorAll(
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
         * Comprobamos si realmente existe texto
         * oculto por el límite de cuatro líneas.
         *
         * Si todo el resumen ya cabe, ocultamos
         * el botón Ver más.
         */
        if (
            resumen.scrollHeight <=
            resumen.clientHeight + 2
        ) {

            boton.hidden = true;

        } else {

            boton.hidden = false;

        }

    });

}


contenedor.addEventListener(
    "click",
    (event) => {

        const boton =
            event.target.closest(
                ".preprint-summary-toggle"
            );


        if (!boton) {
            return;
        }


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

    // =====================================================
    // LLENAMOS LOS SELECTS
    // =====================================================

    unique(
        preprints.map(
            preprint => preprint.coleccion
        )
    )
        .sort()
        .forEach(
            coleccion => {

                selColeccion.insertAdjacentHTML(
                    "beforeend",
                    `<option>${coleccion}</option>`
                );

            }
        );


    unique(
        preprints.map(
            preprint => preprint.serie
        )
    )
        .sort()
        .forEach(
            serie => {

                selSerie.insertAdjacentHTML(
                    "beforeend",
                    `<option>${serie}</option>`
                );

            }
        );


    unique(
        preprints.map(
            preprint =>
                anioActualizacion(preprint)
        )
    )
        .sort(
            (a, b) =>
                Number(b) - Number(a)
        )
        .forEach(
            anio => {

                selAnio.insertAdjacentHTML(
                    "beforeend",
                    `<option>${anio}</option>`
                );

            }
        );


    // =====================================================
    // COINCIDENCIAS
    // =====================================================

    function coincideAutor(
        preprint,
        busqueda
    ) {

        if (!busqueda) {
            return true;
        }

        const needle =
            normalizarTexto(busqueda);

        return (
            preprint.autores || []
        ).some(
            autor =>
                normalizarTexto(autor)
                    .includes(needle)
        );

    }


    function coincideTitulo(
        preprint,
        busqueda
    ) {

        if (!busqueda) {
            return true;
        }

        return normalizarTexto(
            preprint.titulo
        ).includes(
            normalizarTexto(busqueda)
        );

    }


    function coincidePalabra(
        preprint,
        busqueda
    ) {

        if (!busqueda) {
            return true;
        }

        const needle =
            normalizarTexto(busqueda);


        const textoCompleto = normalizarTexto(
            [
                preprint.id_preprint,
                preprint.titulo,
                preprint.resumen,
                preprint.coleccion,
                preprint.serie,
                ...(preprint.autores || [])
            ].join(" ")
        );


        return textoCompleto.includes(
            needle
        );

    }


    // =====================================================
    // ORDEN
    // =====================================================

    function compararTituloAsc(a, b) {

        return String(
            a.titulo || ""
        ).localeCompare(
            String(b.titulo || ""),
            "es",
            {
                sensitivity: "base"
            }
        );

    }


    function compararTituloDesc(a, b) {

        return -compararTituloAsc(a, b);

    }


    function fechaActualizacion(preprint) {

        const version =
            versionActual(preprint);

        if (!version) {
            return "";
        }

        return version.fecha || "";

    }


    function compararFechaDesc(a, b) {

        const fechaA =
            fechaActualizacion(a);

        const fechaB =
            fechaActualizacion(b);


        if (
            fechaA === "" &&
            fechaB === ""
        ) {

            return compararTituloAsc(a, b);

        }


        if (fechaA === "") {
            return 1;
        }


        if (fechaB === "") {
            return -1;
        }


        const comparacion =
            fechaB.localeCompare(fechaA);


        if (comparacion !== 0) {
            return comparacion;
        }


        return compararTituloAsc(a, b);

    }


    function compararFechaAsc(a, b) {

        const fechaA =
            fechaActualizacion(a);

        const fechaB =
            fechaActualizacion(b);


        if (
            fechaA === "" &&
            fechaB === ""
        ) {

            return compararTituloAsc(a, b);

        }


        if (fechaA === "") {
            return 1;
        }


        if (fechaB === "") {
            return -1;
        }


        const comparacion =
            fechaA.localeCompare(fechaB);


        if (comparacion !== 0) {
            return comparacion;
        }


        return compararTituloAsc(a, b);

    }


    function getComparator(modo) {

        switch (modo) {

            case "titulo-asc":
                return compararTituloAsc;

            case "titulo-desc":
                return compararTituloDesc;

            case "fecha-asc":
                return compararFechaAsc;

            case "fecha-desc":
                return compararFechaDesc;

            default:
                return compararFechaDesc;

        }

    }


    // =====================================================
    // RENDER
    // =====================================================

    function prepararResumenes() {

    const wrappers =
        contenedor.querySelectorAll(
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


        if (
            resumen.scrollHeight <=
            resumen.clientHeight + 2
        ) {

            boton.hidden = true;

        }


        boton.addEventListener(
            "click",
            () => {

                const estaCerrado =
                    resumen.classList.contains(
                        "preprint-summary-collapsed"
                    );


                resumen.classList.toggle(
                    "preprint-summary-collapsed"
                );


                boton.textContent =
                    estaCerrado
                        ? "Ver menos"
                        : "Ver más";

            }
        );

    });

}

    function render(lista) {

        if (!Array.isArray(lista)) {

            contenedor.textContent =
                "Error: datos inválidos.";

            contador.textContent = "";

            return;

        }


        contador.textContent =
            `${lista.length} ${
                lista.length === 1
                    ? "resultado"
                    : "resultados"
            }`;


        if (!lista.length) {

            contenedor.innerHTML = `
                <div class="preprints-no-results">

                    <strong>
                        No se encontraron preprints.
                    </strong>

                    <span>
                        Intenta modificar o limpiar
                        alguno de los filtros.
                    </span>

                </div>
            `;

            return;

        }


        contenedor.innerHTML =
            lista.map(
                preprint => {

                    const versiones =
                        versionesOrdenadas(
                            preprint
                        );


                    const actual =
                        versiones.length
                            ? versiones[0]
                            : null;


                    const numeroVersion =
                        actual
                            ? actual.version
                            : "—";


                    const fecha =
                        actual
                            ? actual.fecha
                            : "Sin versión disponible";


                    const textoVersiones =
                        versiones.length === 1
                            ? "1 versión"
                            : `${versiones.length} versiones`;


                    // Portada real o placeholder.
                    let portadaHTML;


                    if (preprint.portada) {

                        portadaHTML = `
                            <div class="preprint-cover">

                                <img
                                    src="${BASE}portadas_preprints/${preprint.portada}"
                                    alt="Portada de ${preprint.titulo}"
                                    loading="lazy">

                            </div>
                        `;

                    } else {

                        portadaHTML = `
                            <div
                                class="preprint-cover
                                       preprint-cover-placeholder">

                                <span>
                                    ${preprint.id_preprint}
                                </span>

                                <small>
                                    Preprint
                                </small>

                            </div>
                        `;

                    }


                    // Botón del PDF actual.
                    let botonPDF = "";


                    if (
                        actual &&
                        actual.archivo
                    ) {

                        botonPDF = `
                            <a
                                href="${BASE}archivos_preprints/${actual.archivo}"
                                class="md-button
                                       preprint-secondary-button">
                                Ver PDF
                            </a>
                        `;

                    }


                    return `
                        <article class="preprint-card">

                            <div class="preprint-card-layout">

                                ${portadaHTML}


                                <div class="preprint-card-main">


                                    <div class="preprint-card-top">

                                        <span class="preprint-id">
                                            ${preprint.id_preprint}
                                        </span>

                                        <span class="preprint-date">
                                            Actualizado ${fecha}
                                        </span>

                                    </div>


                                    <div class="preprint-card-content">

                                        <h3 class="preprint-title">

                                            <a
                                                href="${BASE}preprints/${preprint.id_preprint}/">

                                                ${preprint.titulo}

                                            </a>

                                        </h3>


                                        <p class="preprint-authors">

                                            ${
                                                (
                                                    preprint.autores ||
                                                    []
                                                ).join(" · ")
                                            }

                                        </p>


                                        <div class="preprint-summary-wrapper">

                                            <p class="preprint-summary preprint-summary-collapsed">

                                                ${preprint.resumen || ""}

                                            </p>

                                            <button
                                                type="button"
                                                class="preprint-summary-toggle">

                                                Ver más

                                            </button>

                                        </div>


                                        <div class="busqueda-preprint-meta">

                                            ${
                                                preprint.coleccion
                                                    ? `<span>
                                                        <strong>Colección:</strong>
                                                        ${preprint.coleccion}
                                                       </span>`
                                                    : ""
                                            }

                                            ${
                                                preprint.serie
                                                    ? `<span>
                                                        <strong>Serie:</strong>
                                                        ${preprint.serie}
                                                       </span>`
                                                    : ""
                                            }


                                        </div>

                                    </div>


                                    <div class="preprint-card-footer">

                                        <div class="preprint-version-info">

                                            <span class="preprint-version-badge">
                                                v${numeroVersion}
                                            </span>

                                            <span class="preprint-version-count">
                                                ${textoVersiones}
                                            </span>

                                        </div>


                                        <div class="preprint-actions">

                                            <a
                                                href="${BASE}preprints/${preprint.id_preprint}/"
                                                class="md-button
                                                       md-button--primary">

                                                Ver ficha

                                            </a>

                                            ${botonPDF}

                                        </div>

                                    </div>


                                </div>

                            </div>

                        </article>
                    `;

                }
            ).join("");
            requestAnimationFrame(actualizarBotonesResumenes);

    }


    // =====================================================
    // FILTROS
    // =====================================================

    function filtrar() {

        const coleccion =
            selColeccion.value;

        const serie =
            selSerie.value;

        const anio =
            selAnio.value;

        const autor =
            inpAutor.value.trim();

        const titulo =
            inpTitulo.value.trim();

        const palabra =
            inpPalabra.value.trim();


        const comparador =
            getComparator(
                selOrder.value ||
                "fecha-desc"
            );


        const resultado =
            preprints

                .filter(
                    preprint =>

                        (
                            !coleccion ||
                            preprint.coleccion ===
                                coleccion
                        )

                        &&

                        (
                            !serie ||
                            String(
                                preprint.serie || ""
                            ) === String(serie)
                        )

                        &&

                        (
                            !anio ||
                            anioActualizacion(
                                preprint
                            ) === anio
                        )

                        &&

                        coincideAutor(
                            preprint,
                            autor
                        )

                        &&

                        coincideTitulo(
                            preprint,
                            titulo
                        )

                        &&

                        coincidePalabra(
                            preprint,
                            palabra
                        )

                )

                .sort(comparador);


        render(resultado);

    }


    // =====================================================
    // EVENTOS
    // =====================================================

    selColeccion.addEventListener(
        "change",
        filtrar
    );

    selSerie.addEventListener(
        "change",
        filtrar
    );

    selAnio.addEventListener(
        "change",
        filtrar
    );

    inpAutor.addEventListener(
        "input",
        filtrar
    );

    inpTitulo.addEventListener(
        "input",
        filtrar
    );

    inpPalabra.addEventListener(
        "input",
        filtrar
    );

    selOrder.addEventListener(
        "change",
        filtrar
    );


    // =====================================================
    // LIMPIAR
    // =====================================================

    function limpiar() {

        selColeccion.value = "";
        selSerie.value = "";
        selAnio.value = "";

        inpAutor.value = "";
        inpTitulo.value = "";
        inpPalabra.value = "";

        selOrder.value =
            "fecha-desc";

        filtrar();

        inpPalabra.focus();

    }


    btnClear.addEventListener(
        "click",
        limpiar
    );


    // Primera carga.
    filtrar();

})();

</script>