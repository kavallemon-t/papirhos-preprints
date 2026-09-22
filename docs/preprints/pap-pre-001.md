# Preprint de prueba

**Autores:** Jean-Paul Brasselet, Felipe Cano

**Identificador:** `pap-pre-001`

---

## Resumen

Documento utilizado para probar el sistema de prepublicaciones.

## Versión actual

**v2**

**Fecha:** 2026-09-17

**Cambios:** Correcciones menores

[Ver PDF](../archivos_preprints/pap-pre-001-v2.pdf)

## Cómo citar

<div class="citation-box">

<blockquote id="cita-actual-pap-pre-001">
Jean-Paul Brasselet, Felipe Cano. (2026). Preprint de prueba. Papirhos Preprints, pap-pre-001, v2. https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-001/
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="cita-actual-pap-pre-001">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="bibtex-actual-pap-pre-001"
    rows="7"
    cols="80"
    class="verbatim">@misc{pap-pre-001v2,
  author = {Jean-Paul Brasselet and Felipe Cano},
  title = {Preprint de prueba},
  year = {2026},
  note = {Papirhos Preprints: pap-pre-001, v2},
  url = {https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-001/}
}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="bibtex-actual-pap-pre-001">
    Copiar BibTeX
</button>

</details>

## Historial de versiones

### v2

- **Fecha:** 2026-09-17
- **Cambios:** Correcciones menores
- [Ver PDF](../archivos_preprints/pap-pre-001-v2.pdf)

**Cómo citar esta versión**

<div class="citation-box">

<blockquote id="cita-pap-pre-001-v2">
Jean-Paul Brasselet, Felipe Cano. (2026). Preprint de prueba. Papirhos Preprints, pap-pre-001, v2. https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-001/
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="cita-pap-pre-001-v2">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="bibtex-pap-pre-001-v2"
    rows="7"
    cols="80"
    class="verbatim">@misc{pap-pre-001v2,
  author = {Jean-Paul Brasselet and Felipe Cano},
  title = {Preprint de prueba},
  year = {2026},
  note = {Papirhos Preprints: pap-pre-001, v2},
  url = {https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-001/}
}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="bibtex-pap-pre-001-v2">
    Copiar BibTeX
</button>

</details>

### v1

- **Fecha:** 2026-09-01
- **Cambios:** Primera versión
- [Ver PDF](../archivos_preprints/pap-pre-001-v1.pdf)

**Cómo citar esta versión**

<div class="citation-box">

<blockquote id="cita-pap-pre-001-v1">
Jean-Paul Brasselet, Felipe Cano. (2026). Preprint de prueba. Papirhos Preprints, pap-pre-001, v1. https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-001/
</blockquote>

<button
    type="button"
    class="citation-copy-button"
    data-target="cita-pap-pre-001-v1">
    Copiar cita
</button>

</div>

<details>

<summary>BibTeX</summary>

<textarea
    id="bibtex-pap-pre-001-v1"
    rows="7"
    cols="80"
    class="verbatim">@misc{pap-pre-001v1,
  author = {Jean-Paul Brasselet and Felipe Cano},
  title = {Preprint de prueba},
  year = {2026},
  note = {Papirhos Preprints: pap-pre-001, v1},
  url = {https://kavallemon-t.github.io/papirhos-preprints/preprints/pap-pre-001/}
}</textarea>

<br>

<button
    type="button"
    class="bibtex-copy-button"
    data-target="bibtex-pap-pre-001-v1">
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
