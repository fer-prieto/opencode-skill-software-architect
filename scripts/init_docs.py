#!/usr/bin/env python3
"""Crea la carpeta de documentos de dev-arquitecto-software.

Uso:
    python scripts/init_docs.py --root . --slug acortador --title "Acortador de URLs"

No sobrescribe nada. Si la carpeta ya existe, falla para que el agente pregunte.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

TEMPLATES = (
    "00-entendimiento.md",
    "01-investigacion.md",
    "02-arquitectura-propuesta.md",
    "03-plan-implementacion.md",
)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crea docs/dev-arquitecto-software/<slug>/ con las plantillas 00-03."
    )
    parser.add_argument("--root", default=".", help="Raíz del proyecto (default: .)")
    parser.add_argument("--slug", required=True, help="Slug en kebab-case, por ejemplo: acortador")
    parser.add_argument("--title", required=True, help="Título legible del trabajo")
    parser.add_argument(
        "--docs-root",
        default="docs/dev-arquitecto-software",
        help="Carpeta base de documentos (default: docs/dev-arquitecto-software)",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Fecha ISO (default: hoy)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slug = args.slug.strip()
    title = args.title.strip()
    date = args.date.strip()

    if not SLUG_RE.fullmatch(slug) or len(slug) > 60:
        print(
            "Error: --slug debe ser kebab-case (minúsculas, números y guiones), máximo 60 caracteres.",
            file=sys.stderr,
        )
        return 2

    if not title:
        print("Error: --title no puede estar vacío.", file=sys.stderr)
        return 2

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        print(f"Error: la raíz no existe o no es un directorio: {root}", file=sys.stderr)
        return 2

    templates_dir = Path(__file__).resolve().parent.parent / "assets"
    missing = [name for name in TEMPLATES if not (templates_dir / name).is_file()]
    if missing:
        print(f"Error: faltan plantillas en {templates_dir}: {', '.join(missing)}", file=sys.stderr)
        return 2

    docs_dir = root / args.docs_root / slug
    if docs_dir.exists():
        print(
            f"Error: la carpeta ya existe: {docs_dir}\n"
            "No se sobrescribe. Pregunta al usuario si continúa el trabajo existente "
            "o usa otro slug.",
            file=sys.stderr,
        )
        return 1

    docs_dir.mkdir(parents=True)
    created = []
    for name in TEMPLATES:
        content = (templates_dir / name).read_text(encoding="utf-8")
        content = (
            content.replace("{{TITLE}}", title)
            .replace("{{SLUG}}", slug)
            .replace("{{DATE}}", date)
        )
        target = docs_dir / name
        target.write_text(content, encoding="utf-8")
        created.append(target)

    print(f"Documentos creados en: {docs_dir}")
    for path in created:
        print(f"  - {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
