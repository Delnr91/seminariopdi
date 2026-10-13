# Anexo práctico: Efecto Dominó de los Incidentes y Riesgo de Proveedores - E-Virtus · ampliación temática

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 09:26:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=34000s) · [Índice y límites de los tiempos](../../VIDEOS.md)

Ampliación temática de Lattices relacionada con la intervención de Mauricio Barrera sobre IA y ciberresiliencia; no representa una segunda charla de E-Virtus ni su título oficial.

## Objetivo

Analizar cómo un componente o proveedor puede interrumpir varios servicios y priorizar mitigaciones por impacto operacional.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Grafo de dependencias** | Relacionar servicio, identidad, software y proveedor; identificar componentes compartidos. | Grafo con propietario y evidencia por dependencia. |
| **Inventario SBOM** | Generar una lista de componentes y versiones de una muestra local; contrastar cobertura y componentes no reconocidos. | SBOM y lista de limitaciones del inventario. |
| **Escenario de fallo común** | Simular indisponibilidad de un proveedor en una mesa de trabajo y estudiar degradación, sustitución y recuperación. | Secuencia de impacto y alternativas verificables. |

## Herramientas open source

* [Syft](https://github.com/anchore/syft) — Generación de SBOM de directorios e imágenes; no identifica por sí solo todo el riesgo operacional.
* [OpenSSF Scorecard](https://github.com/ossf/scorecard) — Indicadores de prácticas de seguridad de repositorios; no sustituye una revisión del proveedor.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Preparar un directorio `muestra` con una aplicación de ejemplo y sus manifiestos de dependencias; no incluir secretos.
2. Generar un SBOM y relacionar tres componentes con servicios ficticios. Registrar versión de Syft y hash del resultado.
3. Revisar una dependencia con Scorecard y explicar dos checks mediante su documentación; una puntuación agregada no equivale a ausencia de vulnerabilidades.
4. Simular un fallo del componente compartido y definir continuidad, responsable y recuperación para cada servicio afectado.

### Ejemplo de trabajo

Con Syft ya disponible:

```bash
syft ./muestra -o cyclonedx-json > sbom.json
sha256sum sbom.json
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Servicios afectados por una dependencia compartida.
* Componentes sin versión o propietario identificable.
* Tiempo y capacidad de operación degradada durante el escenario.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST SP 800-161 Rev. 1 Update 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).
* [OpenSSF Scorecard: checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/05-evirtus-efecto-domino.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
