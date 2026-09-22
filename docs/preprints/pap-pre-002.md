# Segundo preprint de prueba

**Autores:** Jean-Paul Brasselet

**Identificador:** `pap-pre-002`

---

## Resumen

Segundo documento utilizado para probar el sistema de prepublicaciones.

## Versión actual

**v1**

**Fecha:** 2026-09-17

**Cambios:** Correcciones menores

[Ver PDF](../archivos_preprints/pap-pre-002-v1.pdf)

## Cómo citar

<div class="citation-box">

<blockquote id="cita-actual-pap-pre-002">
Jean-Paul Brasselet. (2026). Segundo preprint de prueba. Papirhos Preprints, pap-pre-002, v1. https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-002/
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="cita-actual-pap-pre-002">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="bibtex-actual-pap-pre-002"
    rows="7"
    cols="80"
    class="verbatim">@misc{pap-pre-002v1,
  author = {Jean-Paul Brasselet},
  title = {Segundo preprint de prueba},
  year = {2026},
  note = {Papirhos Preprints: pap-pre-002, v1},
  url = {https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-002/}
}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="bibtex-actual-pap-pre-002">
    Copiar BibTeX
</button>

</details>

## Historial de versiones

### v1

- **Fecha:** 2026-09-17
- **Cambios:** Correcciones menores
- [Ver PDF](../archivos_preprints/pap-pre-002-v1.pdf)

**Cómo citar esta versión**

<div class="citation-box">

<blockquote id="cita-pap-pre-002-v1">
Jean-Paul Brasselet. (2026). Segundo preprint de prueba. Papirhos Preprints, pap-pre-002, v1. https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-002/
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="cita-pap-pre-002-v1">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="bibtex-pap-pre-002-v1"
    rows="7"
    cols="80"
    class="verbatim">@misc{pap-pre-002v1,
  author = {Jean-Paul Brasselet},
  title = {Segundo preprint de prueba},
  year = {2026},
  note = {Papirhos Preprints: pap-pre-002, v1},
  url = {https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-002/}
}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="bibtex-pap-pre-002-v1">
    Copiar BibTeX
</button>

</details>


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
