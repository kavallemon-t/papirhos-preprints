---
title: "Teoría de las gráficas: algunas aportaciones desde México"
authors: [[['Julian'], ['Fresán']], [['Ilán'], ['Goldfeder']], [['Nahid'], ['Javier']], [['Rita'], ['Zuazua']]]
tags: [Papirhos, Notas]
---
<section class="libro-hero">
<div class="libro-hero-portada">
<img src="../../assets/covers/pap-not-3.png" alt="Portada de Teoría de las gráficas: algunas aportaciones desde México">
</div>
<div class="libro-hero-contenido">
<p class="libro-eyebrow">Ficha bibliográfica</p>
<h1 class="libro-titulo">Teoría de las gráficas: algunas aportaciones desde México</h1>
<div class="chips"><span class="chip">Notas</span> <span class="chip">Papirhos</span> <span class="chip">Físico</span></div>
</div>
</section>

<section class="libro-seccion libro-resumen">
<h2>Resumen</h2>
Resumen proximamente
</section>

<section class="libro-seccion libro-ediciones">
<h2>Ediciones disponibles</h2>

<div class="edition-selector" id="edition-selector-pap-not-3">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-not-3-0">Edición sin especificar</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-not-3-0" class="edition-panel"><h3 class="edition-panel-title">Edición sin especificar</h3><section class="libro-subseccion libro-metadatos"><h3>Metadatos</h3>
<table>
    <tbody>
        <tr><th>Autores</th><td>Julian Fresán, Ilán Goldfeder, Nahid Javier, Rita Zuazua</td></tr><tr><th>Colección</th><td>Papirhos</td></tr><tr><th>Serie</th><td>Notas</td></tr><tr><th>Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th>ISBN (Colección)</th><td>000</td></tr>
    </tbody>
</table>
</section><section class="libro-subseccion libro-cita"><h3>Cómo citar</h3><div class="citation-box"><blockquote id="cita-ed-017">Julian Fresán, Ilán Goldfeder, Nahid Javier, Rita Zuazua. <em>Teoría de las gráficas: algunas aportaciones desde México</em>. Instituto de Matemáticas, UNAM.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-017">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-017" rows="9" cols="80" class="verbatim">@BOOK{ed-017,
title = {Teoría de las gráficas: algunas aportaciones desde México},
author = {Fresán, Julian and Goldfeder, Ilán and Javier, Nahid and Zuazua, Rita},
publisher = {Instituto de Matemáticas, UNAM},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-017">Copiar BibTeX</button></details></section></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-not-3");

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
<a class="md-button data-book-id=pap-not-3 download-link" data-book-id="pap-not-3" href = "pap-not-3_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-not-3 download-link" data-book-id="pap-not-3" href ="pap-not-3_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-not-3_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-not-3_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>
</div>
</section>

<div class="libro-navegacion">
<a href="../../catalogo/" class="md-button md-button--primary">Volver al catálogo</a>
<a href="../../explorar/" class="md-button">Explorar libros</a>
</div>
