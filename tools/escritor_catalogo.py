def estado_legible(estado):
    estados = {
        "Publicado": "Disponible en línea",
        "publicado": "Disponible en línea",
        "Físico": "Disponible en formato físico",
        "Fisico": "Disponible en formato físico",
        "fisico": "Disponible en formato físico",
        "Por recibir": "Pendiente de recibir",
        "por_recibir": "Pendiente de recibir",
    }

    return estados.get(estado, estado)


def slug_simple(texto):
    texto = (texto or "sin-coleccion").strip().lower()

    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n",
    }

    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)

    limpio = []

    for caracter in texto:
        if caracter.isalnum():
            limpio.append(caracter)
        elif caracter in [" ", "-", "_"]:
            limpio.append("-")

    slug = "".join(limpio)

    while "--" in slug:
        slug = slug.replace("--", "-")

    return slug.strip("-") or "sin-coleccion"


def lista_catalogo(lista_datos):
    colecciones = {}

    for r in lista_datos:
        coleccion = (r.get("coleccion") or "Sin colección").strip()
        colecciones.setdefault(coleccion, []).append(r)

    total_libros = len(lista_datos)
    total_colecciones = len(colecciones)

    lineas = [
        '<section class="catalogo-hero">',
        '<p class="catalogo-eyebrow">Colecciones</p>',
        "<h1>Explora por colección</h1>",
        "<p>",
        "Consulta los títulos disponibles de Papirhos Digital organizados por colección. "
        "Cada sección reúne libros con sus fichas bibliográficas, metadatos de edición, "
        "reimpresiones registradas y archivos disponibles.",
        "</p>",
        '<div class="catalogo-hero-colecciones">',
    ]

    for coleccion in sorted(colecciones):
        libros = colecciones[coleccion]
        id_coleccion = slug_simple(coleccion)

        lineas.extend([
            f'<a class="catalogo-hero-chip" href="#{id_coleccion}">',
            f"<strong>{coleccion}</strong>",
            f"<span>{len(libros)} {'título' if len(libros) == 1 else 'títulos'}</span>",
            "</a>",
        ])

    lineas.extend([
        "</div>",
        "</section>",
        "",
    ])

    for coleccion in sorted(colecciones):
        libros = sorted(
            colecciones[coleccion],
            key=lambda libro: (libro.get("titulo") or "").lower()
        )

        id_coleccion = slug_simple(coleccion)

        lineas.extend([
            f'<section class="catalogo-seccion" id="{id_coleccion}">',
            f"<h2>{coleccion}</h2>",
            '<div class="catalogo-libros-grid">',
        ])

        for r in libros:
            ident = (r.get("id") or "").strip()
            titulo = (r.get("titulo") or "").strip()
            autores = (r.get("autores") or "").strip()
            autores_limpios = ", ".join(
                parte.replace(">", " ").strip()
                for parte in autores.split(",")
                if parte.strip()
            )
            serie = (r.get("serie") or "").strip()
            estado = estado_legible((r.get("estado") or "Por recibir").strip())

            lineas.extend([
                f'<a class="catalogo-libro" href="../libros/{ident}/">',
                '<div class="catalogo-libro-portada">',
                f'''<img
                    src="../assets/covers/{ident}.png"
                    alt="Portada de {titulo}"
                    loading="lazy"
                    onerror="this.onerror=null; this.src='../assets/covers/{ident}.jpg';"
                >''',
                "</div>",
                f"<h3>{titulo}</h3>",
                f'<div class="catalogo-autores">{autores_limpios}</div>' if autores_limpios else "",
                f'<div class="catalogo-serie">{serie}</div>' if serie else "",
                f'<div class="catalogo-estado">{estado}</div>',
                "</a>",
            ])

        lineas.extend([
            "</div>",
            "</section>",
            "",
        ])

    return lineas