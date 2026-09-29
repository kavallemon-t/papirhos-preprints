
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


        <article class="preprint-card">

            <div class="preprint-card-layout">

                
            <div class="preprint-cover preprint-cover-placeholder">

                <span>
                    pap-pre-001
                </span>

                <small>
                    Preprint
                </small>

            </div>
        


                <div class="preprint-card-main">


                    <div class="preprint-card-top">

                        <span class="preprint-id">
                            pap-pre-001
                        </span>

                        <span class="preprint-date">
                            Actualizado 2026-09-17
                        </span>

                    </div>


                    <div class="preprint-card-content">

                        <h3 class="preprint-title">

                            <a href="pap-pre-001/">
                                Preprint de prueba
                            </a>

                        </h3>


                        <p class="preprint-authors">
                            Jean-Paul Brasselet · Felipe Cano
                        </p>


                        <p class="preprint-summary">
                            Documento utilizado para probar el sistema de prepublicaciones.
                        </p>

                    </div>


                    <div class="preprint-card-footer">

                        <div class="preprint-version-info">

                            <span class="preprint-version-badge">
                                v2
                            </span>

                            <span class="preprint-version-count">
                                2 versiones
                            </span>

                        </div>


                        <div class="preprint-actions">

                            <a
                                href="pap-pre-001/"
                                class="md-button md-button--primary">
                                Ver ficha
                            </a>

                            <a href="../archivos_preprints/pap-pre-001-v2.pdf" class="md-button preprint-secondary-button">Ver PDF</a>

                        </div>

                    </div>


                </div>

            </div>

        </article>

        <article class="preprint-card">

            <div class="preprint-card-layout">

                
            <div class="preprint-cover preprint-cover-placeholder">

                <span>
                    pap-pre-002
                </span>

                <small>
                    Preprint
                </small>

            </div>
        


                <div class="preprint-card-main">


                    <div class="preprint-card-top">

                        <span class="preprint-id">
                            pap-pre-002
                        </span>

                        <span class="preprint-date">
                            Actualizado 2026-09-17
                        </span>

                    </div>


                    <div class="preprint-card-content">

                        <h3 class="preprint-title">

                            <a href="pap-pre-002/">
                                Segundo preprint de prueba
                            </a>

                        </h3>


                        <p class="preprint-authors">
                            Jean-Paul Brasselet
                        </p>


                        <p class="preprint-summary">
                            Segundo documento utilizado para probar el sistema de prepublicaciones.
                        </p>

                    </div>


                    <div class="preprint-card-footer">

                        <div class="preprint-version-info">

                            <span class="preprint-version-badge">
                                v1
                            </span>

                            <span class="preprint-version-count">
                                1 versión
                            </span>

                        </div>


                        <div class="preprint-actions">

                            <a
                                href="pap-pre-002/"
                                class="md-button md-button--primary">
                                Ver ficha
                            </a>

                            <a href="../archivos_preprints/pap-pre-002-v1.pdf" class="md-button preprint-secondary-button">Ver PDF</a>

                        </div>

                    </div>


                </div>

            </div>

        </article>

    </section>

</div>

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


    function normalizar(texto) {

        return texto
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
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
