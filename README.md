# Catálogo unificado de criterios geológicos – Cerro Lindo

Repositorio para GitHub Pages. Sitio de consulta sin edición pública.

## Códigos

- `index.html`: catálogo completo, con las modificaciones visuales actuales.
- `catalogo_abreviaturas.csv`: **177 códigos mineralógicos NEXA del Excel** y **30 códigos geológicos adicionales no duplicados** previamente presentes.
- Los 177 registros NEXA conservan su número, código y las tres traducciones exactamente según el archivo Excel.
- `assets/images/abbrevs/CODIGO/`: una carpeta por código del catálogo.
- `assets/images/domains/CODIGO/`, `textures/CODIGO/`, `alterations/CODIGO/`, `minerals/CODIGO/`: galerías por tipo.

## Agregar fotografías

1. Copia las fotos `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif` o `.avif` en `assets/images/<categoria>/<CODIGO>/`.
2. Ejecuta `python update_gallery.py` en la raíz del repositorio. Esto actualiza `assets/gallery.json`.
3. Sube las fotos y `assets/gallery.json` a GitHub (commit a la rama publicada).
4. GitHub Pages mostrará la foto dentro de la fila correspondiente.

**Nota:** GitHub Pages es alojamiento estático: los usuarios consultan, pero no suben ni modifican registros desde la web. Las carpetas vacías contienen `.gitkeep` para poder subirlas a GitHub.

## Publicación

Sube **el contenido de esta carpeta** a la raíz de `geologia_cl` y activa GitHub Pages desde `main / (root)`. Reemplaza `index.html`, `assets`, `update_gallery.py` y el CSV. No anides toda esta carpeta dentro de otra.
