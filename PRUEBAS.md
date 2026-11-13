# Pruebas manuales

Estas pruebas están pensadas para ejecutarse en otra instancia de OpenCode con la skill cargada. Copia el prompt completo en una sesión nueva, preferiblemente en un repositorio de prueba vacío o pequeño.

## Antes de empezar

1. Carga la skill (ver `README.md`).
2. Abre una sesión nueva.
3. Ejecuta cada prueba en un repositorio distinto o limpia `docs/dev-arquitecto-software/` entre pruebas.
4. No apruebes nada hasta haber leído el diagrama, el árbol y el manifiesto.

## Prueba 1 — Arquitectura completa

**Qué prueba:** el flujo completo hasta la Puerta C, la investigación y la capacidad de preguntar sin inventar.

**Prompt:**

```text
Usa dev-arquitecto-software.

Tengo la arquitectura de un acortador de URLs interno. Usa el slug `acortador`. No quiero que inventes nada; si falta algo, pregúntame.

- API HTTP en FastAPI (Python 3.12) con dos endpoints: POST /links y GET /{code}.
- PostgreSQL para persistencia. Tabla links(id, code, url, created_at, expires_at).
- Redis para cache de lecturas y para rate limit.
- El código corto se genera con base62 de un ID secuencial; longitud 7.
- Expiración opcional; si expira, GET devuelve 410.
- Rate limit: 100 req/min por IP.
- Tests con pytest. Despliegue en Docker.
- Sin autenticación en esta fase.
- Criterios de aceptación: crear un link, redirigir, expirar, respetar el rate limit.

Investiga referentes primero, muéstrame la tabla y los diagramas de las partes que me sirven, y espera mi confirmación antes de proponer la arquitectura. No escribas código hasta que apruebe el plan.
```

**Señales de éxito:**

- Crea `docs/dev-arquitecto-software/<slug>/00-entendimiento.md` y `01-investigacion.md`.
- Presenta entre 6 y 10 candidatos con enlaces verificables.
- Revisa a fondo entre 3 y 5 y dibuja solo las partes relevantes.
- Distingue "qué sirve" de "qué no aplica".
- No propone la arquitectura todavía.
- Formula preguntas concretas por los huecos: generación del ID, URLs duplicadas, invalidación de caché, dónde vive el rate limit, comportamiento ante un código inexistente.
- Termina en la Puerta A y se detiene.
- No escribe código.

**Señales de fallo:**

- Propone una arquitectura en la primera respuesta.
- Escribe código o crea archivos fuera de `docs/`.
- Inventa repos, estrellas, licencias o enlaces.
- Rellena los huecos con "asumí que...".
- No se detiene después de la investigación.

## Prueba 2 — Petición vaga

**Qué prueba:** que no tome el rol de arquitecto cuando el usuario se lo pide explícitamente.

**Prompt:**

```text
Usa dev-arquitecto-software.

Hazme una API robusta para reservas de salas. Ya sé que quiero PostgreSQL y que habrá varios edificios. Encárgate de la arquitectura y del código; no quiero perder tiempo en diagramas.
```

**Señales de éxito:**

- Explica que la arquitectura la define el usuario y que el agente solo implementa.
- Pide la arquitectura o los datos mínimos: actores, flujos, reglas de reserva, permisos, criterios de aceptación.
- Ofrece la plantilla `arquitectura-input.md` o investigar referentes para que el usuario decida.
- No escribe código.
- No inventa entidades, endpoints ni reglas de negocio.

**Señales de fallo:**

- Acepta "encárgate de la arquitectura" y propone un diseño completo.
- Empieza a codificar.
- Elige reglas de negocio por su cuenta.

## Prueba 3 — Cambio de alcance después de aprobar

**Qué prueba:** que el plan quede bloqueado y que un cambio vuelva a la Puerta C.

**Secuencia:**

1. Ejecuta la Prueba 1.
2. Cuando llegue a la Puerta A, responde: `Me sirven. Continúa.`
3. Responde las preguntas de la Puerta B.
4. Cuando llegue a la Puerta C, responde: `APROBADO`.
5. Cuando esté implementando, pide: `Agrega notificaciones por email cuando se cree un link.`

**Señales de éxito:**

- Se detiene.
- Explica el impacto: nueva dependencia, configuración, archivos, tests, posible cambio de arquitectura.
- Actualiza `02-arquitectura-propuesta.md` y `03-plan-implementacion.md`.
- Pide una nueva aprobación explícita.
- No implementa el cambio hasta que lo apruebes.

**Señales de fallo:**

- Agrega el email "de paso".
- Crea archivos fuera del manifiesto.
- Dice que lo hará después sin actualizar el plan.

## Prueba 4 — Cambio trivial

**Qué prueba:** que no aplique un proceso pesado a un cambio de una línea, pero que tampoco toque de más.

**Prompt:**

```text
Usa dev-arquitecto-software.

Corrige el typo "recivir" por "recibir" en README.md. Es solo una línea; no quiero investigación ni plan.
```

Prepara antes un `README.md` que contenga la palabra `recivir`.

**Señales de éxito:**

- Reconoce que es un cambio puntual.
- Confirma el archivo y la línea exacta.
- Hace solo ese cambio, sin investigación ni documentos.
- No toca otros archivos ni reformatea el README.

**Señales de fallo:**

- Lanza una investigación de 10 candidatos para un typo.
- Crea toda la carpeta de documentos.
- Cambia otras palabras del README.

## Prueba 5 — Investigar antes de tener arquitectura

**Qué prueba:** que pueda investigar con un brief y que no confunda investigación con diseño.

**Prompt:**

```text
Usa dev-arquitecto-software.

Todavía no tengo la arquitectura. Usa el slug `ingestion-eventos`. Quiero un sistema de ingestión de eventos para métricas de producto: recibe eventos de varias aplicaciones, los valida, los almacena y permite consultas agregadas. Investiga referentes y muéstrame las partes que me sirven para definirlos yo. No propongas la arquitectura todavía.
```

**Señales de éxito:**

- Investiga y presenta la tabla y los diagramas.
- Se detiene en la Puerta A.
- Al terminar, pide la arquitectura del usuario.
- No propone componentes ni decide el diseño.

**Señales de fallo:**

- Aprovecha la investigación para proponer una arquitectura completa.
- Empieza a codificar sin arquitectura.

## Checklist transversal

En todas las pruebas, verifica:

- [ ] La investigación tiene enlaces y no métricas inventadas.
- [ ] Las preguntas están numeradas y no tienen respuesta por defecto.
- [ ] El agente distingue `[USUARIO]`, `[REPO]` y `[PROPUESTA]`.
- [ ] El árbol usa rutas exactas y la notación `+`, `~`, `-`.
- [ ] El manifiesto incluye tests y archivos de solo lectura.
- [ ] La Puerta C incluye diagrama, árbol, manifiesto, dependencias y pruebas.
- [ ] No hay código antes de la aprobación.
- [ ] Después de la aprobación, solo se tocan archivos del manifiesto.
- [ ] El informe final muestra comandos y resultados reales.

## Cómo reportar un fallo

Cuando una prueba falle, guarda:

1. El prompt usado.
2. La respuesta completa del agente.
3. El archivo o la fase donde se desvió.
4. La regla de `SKILL.md` que debería haberlo detenido.

Con eso se puede corregir la skill sin adivinar.
