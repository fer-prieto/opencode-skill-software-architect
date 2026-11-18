# dev-arquitecto-software

Skill para desarrollo guiado por arquitectura, usable con cualquier agente que cargue skills por carpeta. El usuario define la arquitectura; el agente investiga referentes, hace preguntas, formaliza el diseño y solo escribe el código que el usuario aprueba. Si el usuario aún no tiene arquitectura, la skill le entrega los conceptos previos y material de estudio (documentación oficial, videos de canales de renombre, keywords) para que decida con fundamento; si lo que quiere es delegar todo el desarrollo, existe la skill hermana `dev-implementador-autonomo`.

## Qué garantiza

- **Cero inferencias silenciosas**: lo que no está en la arquitectura, en el repositorio o en una respuesta del usuario es una pregunta.
- **Investigación verificable**: repositorios, foros, documentación y postmortems, con enlaces y sin métricas inventadas.
- **Comprensión antes de proponer**: el agente repite tu punto de vista y pregunta lo que falta.
- **Traspaso de estudio**: si aún no hay arquitectura, conceptos previos y material interactivo (docs oficiales, videos de canales de renombre, keywords) para que el usuario decida; nunca clases largas por chat.
- **Aprobación antes de codificar**: diagrama, árbol de archivos y manifiesto explícitos.
- **Alcance bloqueado**: después de aprobar, solo se tocan los archivos del manifiesto.
- **Verificación honesta**: comandos ejecutados, resultados y limitaciones; nada de "debería funcionar".

## Instalación

La skill es una carpeta con `SKILL.md` en la raíz y funciona con cualquier agente que cargue skills por carpeta. Clona el repositorio donde el agente busque skills y recarga la lista de skills del agente. Por ejemplo:

- OpenCode: `~/.config/opencode/skills/` (global) o `.opencode/skills/` (por proyecto).
- Otros agentes: la carpeta que indique su documentación.

```bash
git clone https://github.com/fer-prieto/opencode-skill-software-architect.git \
  ~/.config/opencode/skills/dev-arquitecto-software
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
