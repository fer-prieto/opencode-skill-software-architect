# Implementación disciplinada

## 1. El plan está bloqueado

Una vez aprobado el plan, el alcance está cerrado. No agregues archivos, dependencias, refactors, renombres, borrados, endpoints, campos ni tests "de paso".

Si algo falta, es una solicitud de cambio: explica el impacto, actualiza el plan y espera aprobación. No hay excepciones por tamaño.

## 2. Antes de escribir código

Por cada archivo del manifiesto:

- léelo completo si existe;
- lee los archivos cercanos que establecen el estilo;
- identifica el framework, la versión y los comandos desde los archivos del repositorio, no desde tu memoria;
- verifica si hay un formatter, linter o generador;
- confirma que la ruta exacta está en el manifiesto;
- confirma que no vas a tocar un archivo generado o de solo lectura.

Si el archivo no existe y el plan dice "crear", crea la carpeta solo si es necesaria para esa ruta. No crees carpetas vacías.

## 3. Protocolo de lotes

Antes de cada lote:

```text
Lote X/Y — <nombre>
Archivos: <lista exacta>
Cambios: <qué se hará>
Verificación: <comando>
```

Después:

```text
Lote X/Y — completado
Archivos: <lista exacta>
Comandos: <comandos y resultado>
Desviaciones: ninguna
```

Si hay una desviación, no la escondas. Detente, explica y pide aprobación.

## 4. Reglas de código

- Sigue el estilo existente. Cita el archivo que tomaste como referencia.
- Haz cambios pequeños y enfocados.
- No reformatees archivos completos ni código no relacionado.
- No dejes código muerto, comentado ni TODOs que oculten trabajo incompleto.
- No silencies errores. Si el plan define un manejo, impleméntalo; si no, pregunta.
- Valida en los límites del sistema, no en cada función interna, salvo que el plan lo pida.
- No hardcodees secretos, credenciales, tokens ni rutas absolutas del entorno.
- No inventes dependencias. Usa las que ya están o las que el plan aprobó.
- No cambies interfaces públicas sin aprobación.
- No agregues logs, métricas o traces que el plan no contemple. Si crees que faltan, pregunta.
- No uses `git` para hacer commit, push, reescribir historia, borrar cambios ni hacer reset sin instrucción explícita.
- No ejecutes comandos destructivos (`rm -rf`, `git reset --hard`, `git clean -fd`, drop de tablas) sin aprobación explícita.
- No instales herramientas globales ni cambies el entorno del proyecto.

## 5. Pruebas

- Escribe los tests que el plan define, en las rutas del manifiesto.
- Un test debe fallar si la funcionalidad falta y pasar cuando está bien.
- No debilites una aserción para que pase.
- No borres tests existentes para "limpiar".
- No uses `sleep` arbitrarios para sincronizar; usa el mecanismo del stack.
- No hagas tests dependientes de red, reloj o orden si el stack permite evitarlo.
- Ejecuta primero la línea base y registra el resultado.
- Si un test falla por una causa ajena a tu cambio, detente y pregunta.

## 6. Paradas obligatorias

Detente y pregunta si:

- necesitas un archivo que no está en el manifiesto;
- necesitas una dependencia nueva;
- el contrato real no coincide con el plan;
- el repositorio tiene dos convenciones incompatibles;
- un test de línea base falla;
- el comando de verificación no existe o no se puede ejecutar;
- el cambio requiere migración de datos;
- el cambio afecta datos existentes o producción;
- aparece un riesgo de seguridad, privacidad o pérdida de datos;
- el usuario pide algo fuera del alcance aprobado.

## 7. Verificación

Al finalizar:

1. Ejecuta los comandos del plan: tests, build, linter, typecheck.
2. Compara el estado real con el manifiesto.
3. Revisa que no haya archivos temporales, logs o artefactos sin querer.
4. Revisa el diff completo si el control de versiones está disponible.
5. Actualiza `04-registro-implementacion.md`.

No afirmes que algo pasa si no ejecutaste el comando. Si no se pudo ejecutar, escribe "no ejecutado" y explica por qué.

## 8. Informe final

```text
## Implementación terminada
- Plan: docs/dev-arquitecto-software/<slug>/03-plan-implementacion.md
- Aprobación: "<frase>" (<fecha>)
- Archivos creados: ...
- Archivos modificados: ...
- Archivos fuera del manifiesto: ninguno sin aprobar
- Comandos ejecutados: ...
- Resultado: ...
- Criterios de aceptación: ...
- Limitaciones: ...
- Pendiente de tu revisión: ...
```

Incluye la trazabilidad:

| Requisito | Implementación | Test | Estado |
|---|---|---|---|
| ... | ... | ... | ... |

Si algo quedó pendiente, dilo. No lo presentes como terminado.

## 9. Errores típicos que debes evitar

| Error | Por qué es grave | Qué hacer |
|---|---|---|
| Crear un archivo "auxiliar" no planificado | Rompe el contrato de alcance | Detenerse y pedir aprobación |
| Agregar una dependencia para simplificar | Cambia el despliegue y la seguridad | Preguntar primero |
| Refactorizar código cercano | Aumenta el riesgo y el diff | No hacerlo |
| Cambiar un nombre para que "quede mejor" | Rompe interfaces y tests | Proponerlo en el plan |
| Ocultar un test que falla | Falsa sensación de terminado | Reportarlo |
| Decir "debería funcionar" | No es verificación | Ejecutar y mostrar |
| Implementar el cambio de alcance "ya que estoy" | Viola la aprobación | Solicitud de cambio |
