# Anexo práctico: Fraude y Suplantación de Identidad con IA - Manu Fernández

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 03:20:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=12020s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Diseñar una verificación de identidad que resista suplantación audiovisual y no dependa de detectar visualmente un deepfake.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Verificación fuera de banda** | Confirmar una instrucción financiera por un canal obtenido de un directorio previo, no del mensaje sospechoso. | Registro de confirmación y decisión. |
| **Procedencia verificable** | Revisar manifiestos C2PA cuando existan y separar firma válida, identidad confiable y veracidad del contenido. | Informe de procedencia con límites explícitos. |
| **Evaluación de detectores** | Comparar material de referencia y transformaciones controladas; separar datos de entrenamiento y evaluación. | Matriz de errores por compresión, origen y manipulación. |

## Herramientas open source

* [C2PA Tool](https://github.com/contentauth/c2patool) — Inspección de manifiestos de contenido; la ausencia de credenciales no prueba falsificación.
* [FaceForensics](https://github.com/ondyari/FaceForensics) — Recursos de investigación sobre manipulación facial; verificar condiciones de acceso y uso del dataset.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Preparar tres imágenes propias: una con manifiesto válido, otra sin manifiesto y una copia transformada. Registrar el proceso de generación.
2. Inspeccionar cada archivo y comparar integridad y confianza. No convertir un resultado del detector en una identificación de persona.
3. Representar una solicitud ficticia de pago; un participante confirma por un canal independiente y otro documenta la decisión.
4. Evaluar el procedimiento cuando el interlocutor está ausente, la solicitud es urgente o no hay manifiesto disponible.

### Ejemplo de trabajo

Con C2PA Tool ya disponible y un archivo de laboratorio:

```bash
c2patool imagen.jpg
```

Un manifiesto válido acredita relaciones de procedencia comprobables; no demuestra que la escena o la solicitud sean verdaderas.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Solicitudes confirmadas por canal independiente antes de autorizar.
* Falsos positivos y negativos por tipo de transformación.
* Casos sin procedencia resueltos mediante un procedimiento alternativo.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [C2PA Tool: lectura de manifiestos](https://github.com/contentauth/c2patool/blob/main/docs/usage.md).
* [NIST Digital Identity Guidelines: Authentication](https://csrc.nist.gov/pubs/sp/800/63/b/4/final).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/03-fernandez-crimen-ia.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
