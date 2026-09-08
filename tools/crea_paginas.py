import os
import csv
from textwrap import dedent

import extractidatos
import escribe_metadatos
import escritor_bibtex

BASE = os.path.dirname(os.path.dirname(__file__))
DOCS = os.path.join(BASE, "docs")

REIMPRESIONES_CSV = os.path.join(BASE, "tools", "catalogo_qr", "reimpresiones.csv")

def cargar_reimpresiones():
       reimpresiones_por_edicion = {}

       if not os.path.exists(REIMPRESIONES_CSV):
              return reimpresiones_por_edicion

       with open(REIMPRESIONES_CSV, newline="", encoding="utf-8") as archivo:
              lector = csv.DictReader(archivo)

              for fila in lector:
                     id_edicion = (fila.get("id_edicion") or "").strip()

                     if not id_edicion:
                            continue

                     reimpresion = {
                            "id_reimpresion": (fila.get("id_reimpresion") or "").strip(),
                            "reimpresion": (fila.get("reimpresion") or "").strip(),
                            "anio": (fila.get("anio") or "").strip(),
                     }

                     reimpresiones_por_edicion.setdefault(
                            id_edicion,
                            []
                     ).append(reimpresion)

       return reimpresiones_por_edicion

def fila_a_obj(filas_libro):
       r = filas_libro[0]  # Usamos la primera fila como referencia para los metadatos del libro
       autores, anio, _id, titulo, coleccion, serie, tomo, editorial, edicion, isbn_col, isbn_libro, estado, resumen, downs = extractidatos.extractidatos(r)

       reimpresiones_por_edicion = cargar_reimpresiones()

       #Autores para citar:
       #Recuerda que se recibe una lista del tipo [[nombre1, nombre2], [apellido1, apellido2]]
       autsnor = [" ".join(autor[0]) + " " + " ".join(autor[1]) for autor in autores]

       #Autores bibtex:
       
       autbib =  [autor[1][0] +", "+ autor[0][0] for autor in autores]


       #Obtención de gráficos
       covername = f"assets/covers/{_id}"
       cover_rel = covername+".png" 
       cover_abs = os.path.join(DOCS, cover_rel)
       cover_file = f'\"../../{cover_rel}\"' if os.path.exists(cover_abs) else '\"../../'+covername+'.jpg\"' 


       if downs and downs.strip():
              bloque_descargas = downs
       else:
              bloque_descargas = "Aún no hay archivos digitales disponibles para este título."
              bloque_aviso = ""

       # Datos breves que identifican la ficha en el encabezado.
       def chip(val):
              return f'<span class="chip">{val}</span>' if val else ""

       chips = " ".join(
              x for x in [
                     chip(serie),
                     chip(coleccion),
                     chip(estado.replace("_", " ")),
              ] if x
       )

       # Selector de ediciones
       
       ediciones= []
       
       for fila in filas_libro:
              id_edicion = (fila.get("id_edicion") or "").strip()

              ediciones.append({
                     "id_edicion": id_edicion,
                     "edicion": (fila.get("edicion") or "").strip(),
                     "anio": (fila.get("anio") or "").strip(),
                     "isbn_libro": (fila.get("isbn_libro") or "").strip(),
                     "editorial": (fila.get("editorial") or "").strip(),
                     "reimpresiones": reimpresiones_por_edicion.get(id_edicion, []),
              })

       # Coloca primero la edición con el número más alto.
       # Si el número de edición es desconocido, queda al final.
       def numero_edicion(valor):
              try:
                     return int(float(valor))
              except (ValueError, TypeError):
                     return -1

       ediciones.sort(
              key=lambda e: numero_edicion(e["edicion"]),
              reverse=True
       )

       botones_ediciones = []
       paneles_ediciones = []

       for i, info_edicion in enumerate(ediciones):
              id_panel = f"edicion-{_id}-{i}"

              num_edicion = info_edicion["edicion"]
              anio_edicion = info_edicion["anio"]
              isbn_edicion = info_edicion["isbn_libro"]
              editorial_edicion = info_edicion["editorial"]
              id_edicion = info_edicion["id_edicion"]

              items_reimpresiones = []

              for rep in info_edicion.get("reimpresiones", []):
                     numero_rep = rep.get("reimpresion", "")
                     anio_rep = rep.get("anio", "")

                     if not numero_rep and not anio_rep:
                            continue

                     if numero_rep and anio_rep:
                            texto_rep = f"{numero_rep} ({anio_rep})"

                     elif numero_rep:
                          texto_rep = numero_rep

                     else:
                            texto_rep = anio_rep


                     items_reimpresiones.append(texto_rep)

              reimpresiones_edicion = ", ".join(items_reimpresiones)

              metadatos_edicion = escribe_metadatos.escribe_metadatos(
                     autores,
                     coleccion,
                     serie,
                     tomo,
                     anio_edicion,
                     editorial_edicion,
                     num_edicion,
                     reimpresiones_edicion,
                     isbn_col,
                     isbn_edicion
              )

              partes_cita = []

              if autores:
                     partes_cita.append(", ".join(autsnor) + ".")

              if anio_edicion:
                     partes_cita.append(f"({anio_edicion}).")

              partes_cita.append(f"<em>{titulo}</em>.")

              if editorial_edicion:
                     partes_cita.append(editorial_edicion + ".")

              if num_edicion:
                     partes_cita.append(f"Edición {num_edicion}.")

              cita_edicion = " ".join(partes_cita)

              bibtex_edicion = escritor_bibtex.escribe_bibtex(
                     id_edicion,
                     _id,
                     titulo,
                     autbib,
                     anio_edicion,
                     editorial_edicion,
                     num_edicion,
                     isbn_edicion
              )

              if info_edicion["edicion"]:
                     etiqueta = f"Edición {info_edicion['edicion']}"
              else:
                     etiqueta = "Edición sin especificar"

              clase_activa = " active" if i == 0 else ""

              botones_ediciones.append(
                     f'<button type="button" '
                     f'class="edition-button{clase_activa}" '
                     f'data-target="{id_panel}">'
                     f'{etiqueta}'
                     f'</button>'
              )

              oculto = "" if i == 0 else " hidden"

              id_bibtex = f"bibtex-{id_edicion or i}"

              id_cita = f"cita-{id_edicion or i}"

              paneles_ediciones.append(
                     f'<div id="{id_panel}" class="edition-panel"{oculto}>'
                     f'<h3 class="edition-panel-title">{etiqueta}</h3>'
                     f'<section class="libro-subseccion libro-metadatos">'
                     f'<h3>Metadatos</h3>'
                     f'{metadatos_edicion}'
                     f'</section>'
                     f'<section class="libro-subseccion libro-cita">'
                     f'<h3>Cómo citar</h3>'
                     f'<div class="citation-box">'
                     f'<blockquote id="{id_cita}">{cita_edicion}</blockquote>'
                     f'<button type="button" class="citation-copy-button" '
                     f'data-target="{id_cita}">'
                     f'Copiar cita'
                     f'</button>'
                     f'</div>'
                     f'<details>'
                     f'<summary>BibTeX</summary>'
                     f'<textarea id="{id_bibtex}" rows="9" cols="80" class="verbatim">'
                     f'{bibtex_edicion}'
                     f'</textarea>'
                     f'<br>'
                     f'<button type="button" class="bibtex-copy-button" '
                     f'data-target="{id_bibtex}">'
                     f'Copiar BibTeX'
                     f'</button>'
                     f'</details>'
                     f'</section>'
                     f'</div>'
        )

       selector_ediciones = f"""
<div class="edition-selector" id="edition-selector-{_id}">
    <div class="edition-buttons">
        {''.join(botones_ediciones)}
    </div>

    <div class="edition-content">
        {''.join(paneles_ediciones)}
    </div>
</div>

<script>
(() => {{
    const selector = document.getElementById("edition-selector-{_id}");

    if (!selector) return;

    const botones = selector.querySelectorAll(".edition-button");
    const paneles = selector.querySelectorAll(".edition-panel");

    botones.forEach((boton) => {{
        boton.addEventListener("click", () => {{
            botones.forEach((b) => b.classList.remove("active"));
            paneles.forEach((panel) => panel.hidden = true);

            boton.classList.add("active");

            const panelActivo = selector.querySelector(
                "#" + boton.dataset.target
            );

            if (panelActivo) {{
                panelActivo.hidden = false;
            }}
        }});
    }});
    
    const botonesBibtex = selector.querySelectorAll(".bibtex-copy-button");

    botonesBibtex.forEach((boton) => {{
        boton.addEventListener("click", () => {{
            const textarea = selector.querySelector(
                "#" + boton.dataset.target
            );

            if (!textarea) return;

            navigator.clipboard.writeText(textarea.value).then(() => {{
              const textoOriginal = boton.textContent;

              boton.textContent = "Copiado";
              boton.classList.add("copied");

              setTimeout(() => {{
                       boton.textContent = textoOriginal;
                       boton.classList.remove("copied");
              }}, 1500);
            }});
        }});
    }});
    const botonesCita = selector.querySelectorAll(".citation-copy-button");

    botonesCita.forEach((boton) => {{
       boton.addEventListener("click", () => {{
           const cita = selector.querySelector(
               "#" + boton.dataset.target
           );

           if (!cita) return;

           navigator.clipboard.writeText(cita.innerText).then(() => {{
              const textoOriginal = boton.textContent;

              boton.textContent = "Copiado";
              boton.classList.add("copied");

              setTimeout(() => {{
                 boton.textContent = textoOriginal;
                 boton.classList.remove("copied");
              }}, 1500);
           }});
       }});
}});
}})();
</script>
"""
  
       #YAML front matter para búsqueda SEO
       front_matter = dedent(f"""\
       ---
       title: "{titulo}"
       authors: {autores if autores else []}
       tags: [{", ".join(t for t in [coleccion, serie] if t)}]
       ---
       """)
       #Contenido de la ficha en MARKDOWN. Nota que quité la sangría porque estoy dentro del entorno con tres comillas, entonces no importa la indentación. Si esto no se hace así, la ficha no se genera correctamente.
       contenido = front_matter + dedent(f"""<section class="libro-hero">
<div class="libro-hero-portada">
<img src={cover_file} alt="Portada de {titulo}">
</div>
<div class="libro-hero-contenido">
<p class="libro-eyebrow">Ficha bibliográfica</p>
<h1 class="libro-titulo">{titulo}</h1>
<div class="chips">{chips}</div>
</div>
</section>

<section class="libro-seccion libro-resumen">
<h2>Resumen</h2>
{(resumen if resumen else "_Resumen próximamente._")}
</section>

<section class="libro-seccion libro-ediciones">
<h2>Ediciones disponibles</h2>
{selector_ediciones}
</section>

<section class="libro-seccion libro-seccion-descargas">
<h2>Descargas</h2>
<div class="libro-descargas">
{bloque_descargas}
</div>
</section>

<div class="libro-navegacion">
<a href="../catalogo/" class="md-button md-button--primary">Volver al catálogo</a>
<a href="../explorar/" class="md-button">Explorar libros</a>
</div>
""")
       #Crear el archivo con los datos
       out_path = os.path.join(os.path.join(BASE,"docs","libros"), f"{_id}.md")
       with open(out_path, "w", encoding="utf-8") as fh:
              fh.write(contenido)

