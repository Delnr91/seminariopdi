# Anexo práctico: Desarrollo de Talento para la Ciberresiliencia - Nadezda Abbas

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 06:14:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=22480s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Construir una ruta de formación basada en tareas y evidencias observables, con evaluación repetible de capacidades.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Perfil de capacidades** | Relacionar tareas, conocimientos y habilidades con el rol que necesita un equipo, usando NICE y ECSF. | Matriz de capacidades con criterio de dominio. |
| **Aprendizaje por escenarios** | Asignar problemas que requieran detectar, explicar y recuperar, no solo encontrar una bandera. | Laboratorio con entregables y rúbrica. |
| **Evaluación y retroalimentación** | Comparar desempeño inicial y posterior con casos equivalentes; observar transferencia a un caso nuevo. | Portafolio con evidencia y revisión entre pares. |

## Herramientas open source

* [CTFd](https://github.com/CTFd/CTFd) — Organización de retos y puntuación; verificar licencia y disponibilidad de plugins antes de depender de ellos.
* [Sigma](https://github.com/SigmaHQ/sigma) — Material para retos de detección con registros sintéticos y mapeo de campos.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Elegir un rol defensivo y tres tareas observables: clasificar alerta, documentar evidencia y justificar recuperación.
2. Preparar tres retos con datos ficticios y una rúbrica publicada previamente. La bandera puede indicar avance, pero no demuestra toda la capacidad.
3. Cargar los retos en CTFd si existe una instancia de laboratorio; como alternativa ligera, utilizar archivos y revisión manual.
4. Evaluar un caso nuevo sin revelar la solución anterior y revisar el informe con otra persona. Identificar errores, no solo la puntuación total.

### Ejemplo de trabajo

```csv
criterio,peso_porcentaje,evidencia
hipotesis_y_contexto,25,explicacion_verificable
analisis_tecnico,35,registro_y_resultado
respuesta_y_recuperacion,25,plan_justificado
comunicacion,15,informe_claro
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Tareas completadas con evidencia suficiente según la rúbrica.
* Mejora respecto a la evaluación inicial y desempeño en el caso nuevo.
* Diferencias de puntuación entre revisores explicadas y resueltas.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NICE Framework Resource Center](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center).
* [CTFd: Challenge Overview](https://docs.ctfd.io/docs/challenges/overview/).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/07-abbas-academia-talento.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
