# Anexo práctico: Cyber Threat Intelligence y Decisiones de Defensa - Omar Fuentes

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 00:33:20](https://www.youtube.com/watch?v=jLbdG67TqW8&t=2000s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Convertir una pregunta de inteligencia en una decisión defensiva, conservando procedencia, vigencia y restricciones de intercambio.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **PIR orientado a decisión** | Definir qué servicio se protege, qué amenaza importa y qué decisión cambiaría con la respuesta. | Pregunta prioritaria y consumidor identificado. |
| **Evaluación de fuentes** | Distinguir credibilidad de la fuente, corroboración del dato y confianza de la conclusión. | Registro de procedencia con hipótesis alternativas. |
| **Ciclo de vida de indicadores** | Agregar contexto y caducidad; retirar indicadores que ya no sostienen una acción útil. | Indicadores versionados y decisión documentada. |

## Herramientas open source

* [MISP](https://github.com/MISP/MISP) — Eventos, atributos y taxonomías para compartir inteligencia con distribución controlada.
* [OpenCTI](https://github.com/OpenCTI-Platform/opencti) — Relaciones de inteligencia y contexto; el stack completo requiere más recursos que un ejercicio con JSON.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Formular un PIR ficticio: qué señales justificarían revisar accesos de terceros a un servicio de agua simulado.
2. Crear tres observaciones sintéticas con fechas, fuente y limitaciones. Utilizar dominios reservados, sin indicadores reales de personas.
3. Representar indicadores y relaciones con STIX 2.1; documentar el significado de cada campo y validar mediante la biblioteca oficial de OASIS.
4. Importar en una instancia de laboratorio si está disponible y redactar una recomendación breve con fecha de revisión y evidencia que podría refutarla.

### Código y configuración de referencia

Comparar el SHA-256 de bytes de laboratorio con un indicador. Se calcula el hash del contenido, en lugar de buscar el texto del hash dentro del archivo.

```python
import hashlib
import re

def comparar_sha256(contenido, esperado):
    if not isinstance(contenido, bytes):
        raise ValueError("Se requieren bytes de laboratorio")
    if not isinstance(esperado, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", esperado):
        raise ValueError("Indicador SHA-256 inválido")
    calculado = hashlib.sha256(contenido).hexdigest()
    return {"sha256": calculado, "coincidencia": calculado == esperado.lower(),
            "veredicto_malware": "no_evaluado"}

if __name__ == "__main__":
    muestra = b"ejemplo educativo"
    indicador = hashlib.sha256(muestra).hexdigest()
    print(comparar_sha256(muestra, indicador))
```

**Alcance:** La coincidencia identifica el contenido comparado, no demuestra malicia. Para reglas YARA de hashes usar el módulo hash y validar con el motor; añadir fuente, vigencia y contexto a los indicadores.

**Comprobación:** ejemplo ejecutado con datos ficticios; se probaron entradas válidas, límites y errores. La prueba cubre el comportamiento local de la función, no un sistema de producción.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Indicadores con procedencia, vigencia y consumidor identificados.
* Recomendaciones que modifican una decisión defensiva concreta.
* Indicadores caducados retirados y conclusiones corroboradas.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [OASIS CTI Documentation](https://oasis-open.github.io/cti-documentation/).
* [OASIS Python STIX 2](https://github.com/oasis-open/cti-python-stix2).
* [FIRST TLP](https://www.first.org/tlp/).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/02-fuentes-threat-intelligence.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
