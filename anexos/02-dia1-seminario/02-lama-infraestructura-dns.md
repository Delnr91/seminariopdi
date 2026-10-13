# Anexo práctico: Seguridad y Resiliencia de la Infraestructura DNS - Guillermo Lama

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 02:49:00](https://www.youtube.com/watch?v=PEqWRTb1idE&t=10140s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Comprobar la cadena DNSSEC y diseñar continuidad de resolución sin confundir redundancia con independencia.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Validación de delegación** | Revisar NS, glue, DS, DNSKEY y RRSIG; distinguir errores de firma de indisponibilidad. | Cadena de confianza y hallazgos reproducibles. |
| **Análisis de dependencias** | Separar proveedores, ubicaciones y rutas de red; dos servidores en el mismo dominio de fallo no dan continuidad independiente. | Mapa de puntos únicos de fallo. |
| **Ensayo de recuperación** | Simular la caída de un servidor en una zona de laboratorio y verificar resolución con y sin caché. | Comparación de respuestas y tiempo de recuperación. |

## Herramientas open source

* [DNSViz](https://github.com/dnsviz/dnsviz) — Obtención y análisis de respuestas DNS/DNSSEC; permite procesar JSON de una captura previa.
* [Unbound](https://github.com/NLnetLabs/unbound) — Resolver validador para un laboratorio local; su configuración y anclas de confianza deben registrarse.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Preparar una zona propia de prueba y capturar respuestas con DNSViz; si solo se dispone de una captura JSON, empezar por el análisis offline.
2. Examinar delegación y firmas, anotando hora de la captura: una firma puede haber expirado al revisar datos antiguos.
3. Crear una variante de la zona con una delegación o firma incorrecta y explicar el error esperado. No modificar una zona productiva.
4. Documentar un plan de recuperación con responsables y comprobar la respuesta del resolver tras la corrección en el laboratorio.

### Ejemplo de trabajo

Con DNSViz ya disponible y una captura propia guardada como `zona.json`:

```bash
dnsviz grok -r zona.json -o zona-evaluada.json
dnsviz print -r zona.json
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Errores de delegación y autenticación explicados con evidencia.
* Tiempo de recuperación de la resolución en la simulación.
* Dependencias compartidas detectadas entre servidores supuestamente redundantes.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [DNSSEC Protocol Modifications (RFC 4035)](https://www.rfc-editor.org/rfc/rfc4035).
* [DNSViz: ejemplos y diagnóstico](https://github.com/dnsviz/dnsviz#usage).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/02-lama-infraestructura-dns.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
