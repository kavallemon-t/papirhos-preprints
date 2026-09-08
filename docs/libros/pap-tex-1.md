---
title: "Grupos I"
authors: [[['Diana'], ['Avella']], [['Octavio'], ['Mendoza']], [['Edith', 'Corina'], ['Saenz', 'Valadez']], [['María', 'José'], ['Souto']]]
tags: [Papirhos, Textos]
---
<section class="libro-hero">
<div class="libro-hero-portada">
<img src="../../assets/covers/pap-tex-1.png" alt="Portada de Grupos I">
</div>
<div class="libro-hero-contenido">
<p class="libro-eyebrow">Ficha bibliográfica</p>
<h1 class="libro-titulo">Grupos I</h1>
<div class="chips"><span class="chip">Textos</span> <span class="chip">Papirhos</span> <span class="chip">Publicado</span></div>
</div>
</section>

<section class="libro-seccion libro-resumen">
<h2>Resumen</h2>
Resumen 5
</section>

<section class="libro-seccion libro-ediciones">
<h2>Ediciones disponibles</h2>

<div class="edition-selector" id="edition-selector-pap-tex-1">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-tex-1-0">Edición 3</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-tex-1-0" class="edition-panel"><h3 class="edition-panel-title">Edición 3</h3><section class="libro-subseccion libro-metadatos"><h3>Metadatos</h3>
<table>
    <tbody>
        <tr><th>Autores</th><td>Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto</td></tr><tr><th>Colección</th><td>Papirhos</td></tr><tr><th>Serie</th><td>Textos</td></tr><tr><th>Tomo</th><td>1</td></tr><tr><th>Año</th><td>2014</td></tr><tr><th>Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th>Edición</th><td>3</td></tr><tr><th>ISBN (Colección)</th><td>978-607-02-9375-7</td></tr><tr><th>ISBN (Texto)</th><td>978-607-02-9435-8</td></tr>
    </tbody>
</table>
</section><section class="libro-subseccion libro-cita"><h3>Cómo citar</h3><div class="citation-box"><blockquote id="cita-ed-005">Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto. (2014). <em>Grupos I</em>. Instituto de Matemáticas, UNAM. Edición 3.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-005">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-005" rows="9" cols="80" class="verbatim">@BOOK{ed-005,
title = {Grupos I},
author = {Avella, Diana and Mendoza, Octavio and Saenz, Edith and Souto, María},
year = {2014},
publisher = {Instituto de Matemáticas, UNAM},
edition = {3},
isbn = {978-607-02-9435-8},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-005">Copiar BibTeX</button></details></section></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-tex-1");

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
<a class="md-button data-book-id=pap-tex-1 download-link" data-book-id="pap-tex-1" href = "pap-tex-1_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-tex-1 download-link" data-book-id="pap-tex-1" href ="pap-tex-1_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-tex-1_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-tex-1_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>
</div>
</section>

<div class="libro-navegacion">
<a href="../catalogo/" class="md-button md-button--primary">Volver al catálogo</a>
<a href="../explorar/" class="md-button">Explorar libros</a>
</div>
