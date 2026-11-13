# dev-arquitecto-software

Skill para desarrollo guiado por arquitectura. El usuario define la arquitectura; el agente investiga referentes, hace preguntas, formaliza el diseño y solo escribe el código que el usuario aprueba.

## Qué garantiza

- **Cero inferencias silenciosas**: lo que no está en la arquitectura, en el repositorio o en una respuesta del usuario es una pregunta.
- **Investigación verificable**: repositorios, foros, documentación y postmortems, con enlaces y sin métricas inventadas.
- **Comprensión antes de proponer**: el agente repite tu punto de vista y pregunta lo que falta.
- **Aprobación antes de codificar**: diagrama, árbol de archivos y manifiesto explícitos.
- **Alcance bloqueado**: después de aprobar, solo se tocan los archivos del manifiesto.
- **Verificación honesta**: comandos ejecutados, resultados y limitaciones; nada de "debería funcionar".

## Instalación en OpenCode

La forma recomendada es clonar el repositorio en la carpeta global de skills de OpenCode:

```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/TUUSUARIO/opencode-skill-software-architect.git \
  ~/.config/opencode/skills/dev-arquitecto-software
```

Queda en:

```text
~/.config/opencode/skills/dev-arquitecto-software/
```

OpenCode descubre automáticamente `~/.config/opencode/skills`, así que no hace falta tocar `opencode.json`. Si la skill no aparece en la lista, ejecuta `/reload` en la sesión.

### Alternativas

1. Instalarla solo para un proyecto, dentro de `.opencode/skills/`:

   ```bash
   mkdir -p .opencode/skills
   git clone https://github.com/TUUSUARIO/opencode-skill-software-architect.git \
     .opencode/skills/dev-arquitecto-software
   ```

2. Añadir una ruta adicional al array `skills` de `opencode.json`:

   ```json
   {
     "skills": ["~/mis-skills"]
   }
   ```

## Uso

Puedes invocarla explícitamente:

```text
Usa dev-arquitecto-software. Tengo esta arquitectura: ...
```

O simplemente describe el trabajo y adjunta tu arquitectura. La skill se activa cuando detecta que el usuario define el diseño y espera implementación.

## Documentos que crea

En el proyecto donde se use:

```text
docs/dev-arquitecto-software/<slug>/
├── 00-entendimiento.md
├── 01-investigacion.md
├── 02-arquitectura-propuesta.md
├── 03-plan-implementacion.md
└── 04-registro-implementacion.md
```

Puedes inicializarlos manualmente con la copia instalada globalmente:

```bash
python ~/.config/opencode/skills/dev-arquitecto-software/scripts/init_docs.py \
  --root . \
  --slug mi-feature \
  --title "Mi feature"
```

Si clonaste el repo en otra ruta, apunta al `scripts/init_docs.py` de esa copia.

El script no sobrescribe carpetas existentes.

## Estructura

```text
dev-arquitecto-software/
├── SKILL.md
├── README.md
├── PRUEBAS.md
├── assets/
│   ├── 00-entendimiento.md
│   ├── 01-investigacion.md
│   ├── 02-arquitectura-propuesta.md
│   ├── 03-plan-implementacion.md
│   ├── 04-registro-implementacion.md
│   └── arquitectura-input.md
├── references/
│   ├── investigacion.md
│   ├── propuesta.md
│   └── implementacion.md
└── scripts/
    └── init_docs.py
```

## Pruebas

Lee `PRUEBAS.md`. Incluye prompts listos para copiar en otra instancia de OpenCode y una lista de señales de éxito y de fallo.

## Licencia

GNU General Public License v3.0. Ver [LICENSE](LICENSE).
