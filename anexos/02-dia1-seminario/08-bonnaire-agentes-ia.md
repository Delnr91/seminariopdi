# Anexo práctico: Agentes de IA y Riesgo en Infraestructura Crítica - Xavier Bonnaire

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 08:56:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=32200s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Medir si un agente respeta límites de autoridad y se recupera de datos adversarios sin ejecutar acciones reales.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Separación de confianza** | Tratar documentos recuperados y respuestas de herramientas como datos; validar las órdenes contra una política externa al texto. | Política de herramientas y decisiones auditables. |
| **Evaluación de trayectorias** | Verificar nombre de herramienta, argumentos, autorización y resultado; evaluar la ejecución además del texto final. | Trazas con acciones permitidas y rechazadas. |
| **Aprobación y recuperación** | Requerir revisión para efectos relevantes y diseñar cancelación, límites de pasos y reversión. | Prueba de interrupción y recuperación de estado. |

## Herramientas open source

* [Promptfoo](https://github.com/promptfoo/promptfoo) — Colecciones de pruebas y aserciones; utilizar respuestas mock o un modelo local antes de conectar API de pago.
* [garak](https://github.com/NVIDIA/garak) — Pruebas de vulnerabilidad de LLM; complementa, pero no reemplaza, la evaluación de acciones del agente.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Definir dos herramientas mock: lectura de un documento ficticio y propuesta de acción; ninguna modifica infraestructura.
2. Preparar diez casos: tres normales, tres documentos con instrucciones no autorizadas, dos argumentos inválidos y dos errores de herramienta.
3. Evaluar con aserciones sobre salida y trazas; comprobar que ningún caso no autorizado produjo un efecto en el mock.
4. Repetir tras acotar permisos y agregar interrupción. Guardar diferencias de versión y casos que todavía fallen.

### Código y configuración de referencia

Modelo de autorización para herramientas mock. Rechaza campos ausentes, acciones desconocidas, booleanos usados como números y valores no finitos.

```python
import math

def evaluar_propuesta(comando, *, aprobacion_verificada=False, detenido=False):
    if type(aprobacion_verificada) is not bool or type(detenido) is not bool:
        return False
    if detenido or not aprobacion_verificada:
        return False
    if not isinstance(comando, dict) or set(comando) != {"accion", "temperatura", "presion"}:
        return False
    if comando["accion"] != "ajustar_simulador":
        return False
    limites = {"temperatura": (0, 85), "presion": (0, 10)}
    for campo, (minimo, maximo) in limites.items():
        valor = comando[campo]
        if type(valor) not in (int, float):
            return False
        if not minimo <= valor <= maximo or not math.isfinite(valor):
            return False
    return True

if __name__ == "__main__":
    propuesta = {"accion": "ajustar_simulador", "temperatura": 25, "presion": 2}
    print({"propuesta_admisible_en_mock": evaluar_propuesta(propuesta),
           "efectos_en_sistemas": False})
```

**Alcance:** Los límites son arbitrarios del simulador. La aprobación proviene del harness de prueba, no del comando solicitado; el booleano no implementa autenticación real. No conectar este ejemplo a actuadores ni tratarlo como una barrera de seguridad certificada.

**Comprobación:** ejemplo ejecutado con datos ficticios; se probaron entradas válidas, límites y errores. La prueba cubre el comportamiento local de la función, no un sistema de producción.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Acciones no autorizadas realmente ejecutadas en los mocks.
* Solicitudes válidas completadas sin permisos adicionales.
* Tiempo de cancelación y casos recuperados tras error.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [Promptfoo: Assertions and Metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/).
* [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/08-bonnaire-agentes-ia.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
