---
title: "Teoría de singularidades en topología, geometría y foliaciones II"
authors: [[['Jean-Paul'], ['Brasselet']], [['Felipe'], ['Cano']], [['Dominique'], ['Cerveau']], [['Dung', 'Tráng'], ['Lê']], [['Frank'], ['Loray']], [['Mutsuo'], ['Oka']], [['José'], ['Seade']], [['Mark'], ['Spivakovsky']]]
tags: [Papirhos, Notas]
---
<section class="libro-hero">
<div class="libro-hero-portada">
<img src="../../assets/covers/pap-not-2.jpg" alt="Portada de Teoría de singularidades en topología, geometría y foliaciones II">
</div>
<div class="libro-hero-contenido">
<p class="libro-eyebrow">Ficha bibliográfica</p>
<h1 class="libro-titulo">Teoría de singularidades en topología, geometría y foliaciones II</h1>
<div class="chips"><span class="chip">Notas</span> <span class="chip">Papirhos</span> <span class="chip">Físico</span></div>
</div>
</section>

<section class="libro-seccion libro-resumen">
<h2>Resumen</h2>
Resumen proximamente
</section>

<section class="libro-seccion libro-ediciones">
<h2>Ediciones disponibles</h2>

<div class="edition-selector" id="edition-selector-pap-not-2">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-not-2-0">Edición sin especificar</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-not-2-0" class="edition-panel"><h3 class="edition-panel-title">Edición sin especificar</h3><section class="libro-subseccion libro-metadatos"><h3>Metadatos</h3>
<table>
    <tbody>
        <tr><th>Autores</th><td>Jean-Paul Brasselet, Felipe Cano, Dominique Cerveau, Dung Tráng Lê, Frank Loray, Mutsuo Oka, José Seade, Mark Spivakovsky</td></tr><tr><th>Colección</th><td>Papirhos</td></tr><tr><th>Serie</th><td>Notas</td></tr><tr><th>Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th>ISBN (Colección)</th><td>000</td></tr>
    </tbody>
</table>
</section><section class="libro-subseccion libro-cita"><h3>Cómo citar</h3><div class="citation-box"><blockquote id="cita-ed-016">Jean-Paul Brasselet, Felipe Cano, Dominique Cerveau, Dung Tráng Lê, Frank Loray, Mutsuo Oka, José Seade, Mark Spivakovsky. <em>Teoría de singularidades en topología, geometría y foliaciones II</em>. Instituto de Matemáticas, UNAM.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-016">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-016" rows="9" cols="80" class="verbatim">@BOOK{ed-016,
title = {Teoría de singularidades en topología, geometría y foliaciones II},
author = {Brasselet, Jean-Paul and Cano, Felipe and Cerveau, Dominique and Lê, Dung and Loray, Frank and Oka, Mutsuo and Seade, José and Spivakovsky, Mark},
publisher = {Instituto de Matemáticas, UNAM},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-016">Copiar BibTeX</button></details></section></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-not-2");

    if (!selector) return;

    const botones = selector.querySelectorAll(".edition-button");
    const paneles = selector.querySelectorAll(".edition-panel");

    botones.forEach((boton) => {
        boton.addEventListener("click", () => {
            botones.forEach((b) => b.classList.remove("active"));
            paneles.forEach((panel) => panel.hidden = true);

            boton.classList.add("active");

            const panelActivo = selector.querySelector(
                "#" + boton.dataset.target
            );

            if (panelActivo) {
                panelActivo.hidden = false;
            }
        });
    });

    const botonesBibtex = selector.querySelectorAll(".bibtex-copy-button");

    botonesBibtex.forEach((boton) => {
        boton.addEventListener("click", () => {
            const textarea = selector.querySelector(
                "#" + boton.dataset.target
            );

            if (!textarea) return;

            navigator.clipboard.writeText(textarea.value).then(() => {
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
    const botonesCita = selector.querySelectorAll(".citation-copy-button");

    botonesCita.forEach((boton) => {
       boton.addEventListener("click", () => {
           const cita = selector.querySelector(
               "#" + boton.dataset.target
           );

           if (!cita) return;

           navigator.clipboard.writeText(cita.innerText).then(() => {
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

</section>

<section class="libro-seccion libro-seccion-descargas">
<h2>Descargas</h2>
<div class="libro-descargas">
<a class="md-button data-book-id=pap-not-2 download-link" data-book-id="pap-not-2" href = "pap-not-2_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-not-2 download-link" data-book-id="pap-not-2" href ="pap-not-2_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-not-2_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-not-2_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>
</div>
</section>

<div class="libro-navegacion">
<a href="../../catalogo/" class="md-button md-button--primary">Volver al catálogo</a>
<a href="../../explorar/" class="md-button">Explorar libros</a>
</div>
