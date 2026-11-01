#!/usr/bin/env python3
"""Genera assets/gallery.json a partir de carpetas de imágenes. Ejecutar antes de commit."""
from pathlib import Path
import json
from urllib.parse import quote
root = Path(__file__).resolve().parent
base = root / 'assets' / 'images'
allowed={'.jpg','.jpeg','.png','.webp','.gif','.avif'}
manifest={}
for cat_dir in sorted(base.iterdir()):
    if not cat_dir.is_dir(): continue
    for code_dir in sorted(cat_dir.iterdir()):
        if not code_dir.is_dir(): continue
        photos=[quote(p.relative_to(root).as_posix(), safe='/') for p in sorted(code_dir.iterdir()) if p.is_file() and p.suffix.lower() in allowed]
        if photos: manifest.setdefault(cat_dir.name,{})[code_dir.name.upper()]=photos
(root/'assets'/'gallery.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Galería actualizada:',sum(map(len,(c for c in manifest.values())),0),'códigos con fotos')
