# Anexo práctico: Ciberseguridad y Continuidad Asistencial en Salud - Nina Alli

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 02:51:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=10300s) · [Índice y límites de los tiempos](../../VIDEOS.md)

El bloque audiovisual es una conversación compartida con Nina Alli y otras personas. Su duración no equivale al tiempo de voz individual de Nina Alli.

## Objetivo

Evaluar continuidad asistencial y recuperación de información sin utilizar pacientes ni sistemas clínicos reales.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Impacto asistencial** | Relacionar una interrupción digital con admisión, diagnóstico, medicación y seguimiento; diferenciar urgencias. | Mapa de funciones clínicas y dependencias. |
| **Operación degradada** | Preparar procedimientos alternativos, roles y criterios de reconciliación al recuperar el sistema. | Plan de continuidad con decisiones trazables. |
| **Restauración verificable** | Comprobar integridad y consistencia funcional de datos ficticios tras restaurar, además de arrancar el servicio. | Acta de recuperación y reconciliación. |

## Herramientas open source

* [OpenEMR](https://github.com/openemr/openemr) — Sistema de historia clínica y gestión asistencial; usar una instancia aislada con datos totalmente ficticios.
* [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) — Modelo de flujos entre admisión, historia clínica, laboratorio y dispositivos.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Dibujar un flujo ficticio de admisión, orden de laboratorio y resultado; identificar el paso cuya interrupción afecta primero al servicio.
2. Crear cinco pacientes sintéticos en un entorno de práctica o una tabla local equivalente y preparar una copia de respaldo.
3. Representar una indisponibilidad en mesa: registrar órdenes pendientes y responsables mediante un procedimiento alternativo.
4. Restaurar la instancia de laboratorio cuando exista y reconciliar los registros; si se usa una tabla, informar que se evaluó el procedimiento y no la restauración del software.

### Código y configuración de referencia

Proponer pasos de continuidad para una mesa de trabajo. El código no desconecta redes, activa réplicas ni valida disponibilidad clínica.

```python
def proponer_plan(alerta_confirmada):
    if type(alerta_confirmada) is not bool:
        raise ValueError("La confirmación del ejercicio debe ser un booleano")
    pasos = ["confirmar alcance con responsables clínicos y técnicos",
             "evaluar impacto antes de proponer aislamiento",
             "comprobar respaldo y alternativa de atención",
             "ensayar reconciliación y recuperación"] if alerta_confirmada else []
    return {"modo": "simulacion", "pasos_propuestos": pasos,
            "cambios_ejecutados": False, "continuidad_comprobada": False}

if __name__ == "__main__":
    print(proponer_plan(True))
```

**Alcance:** La salida es un plan pendiente de ensayo. Su validación exige responsables asistenciales, pruebas de restauración y reconciliación; imprimir mensajes no implementa continuidad.

**Comprobación:** ejemplo ejecutado con datos ficticios; se probaron entradas válidas, límites y errores. La prueba cubre el comportamiento local de la función, no un sistema de producción.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Funciones críticas con alternativa probada.
* Registros sintéticos reconciliados sin omisiones ni duplicados.
* Tiempo de recuperación y trabajo pendiente dentro del escenario.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST SP 1800-8](https://csrc.nist.gov/pubs/sp/1800/8/final).
* [ENISA Health Threat Landscape](https://www.enisa.europa.eu/publications/health-threat-landscape).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/04-alli-salud-ciberseguridad.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
