# Anexo práctico: Cibercrimen y economía del fraude - Sergey Nikitin (Group-IB)

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 09:48:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=35300s) · [Índice y límites de los tiempos](../../VIDEOS.md)

Intervención adicional identificada mediante el rótulo «Sergey Nikitin — Group-IB». El anexo amplía la temática observada de cibercrimen y fraude; no reproduce sus palabras.

## Objetivo

Analizar fraude vinculado a abuso de identidades y sesiones mediante telemetría sintética y decisiones de respuesta trazables.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Correlación de identidad y sesión** | Relacionar cuenta, dispositivo, sesión y cambios de privilegio; no tratar una autenticación exitosa como prueba de legitimidad. | Cronología con señales y explicaciones alternativas. |
| **Detección por comportamiento** | Formular hipótesis de uso de cuenta válida o abuso de sesión; especificar campos, ventana y limitaciones de la regla. | Ficha de detección mapeada a ATT&CK. |
| **Contención y prevención de fraude** | Ensayar revisión fuera de banda, revocación de sesión y recuperación de acceso en un escenario ficticio. | Plan con autoridad, evidencia y control de impacto. |

## Herramientas open source

* [Sigma](https://github.com/SigmaHQ/sigma) — Reglas de detección para adaptar a registros de identidad; necesitan campos compatibles y evaluación de falsos positivos.
* [OpenCTI](https://github.com/OpenCTI-Platform/opencti) — Relaciones y contexto de inteligencia; para equipos pequeños comenzar con tablas antes de desplegar el stack.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Preparar 12 eventos ficticios de identidad y marcar cuatro secuencias anómalas; incluir viaje legítimo y cambio autorizado de dispositivo.
2. Definir una detección que combine contexto de sesión con acción sensible. Documentar qué señales no están disponibles.
3. Clasificar los eventos y explicar errores. Vincular T1078 o T1539 solo cuando la evidencia del escenario sostenga ese comportamiento.
4. Simular el cierre de una sesión y la verificación independiente de una orden financiera; comprobar continuidad para el usuario legítimo del laboratorio.

### Ejemplo de trabajo

```csv
evento,cuenta,sesion,dispositivo,accion,contexto
FR-01,cuenta_ficticia,SES-01,DEV-A,consulta,habitual
FR-02,cuenta_ficticia,SES-01,DEV-B,orden_financiera,no_autorizado_en_escenario
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Secuencias anómalas detectadas y benignas clasificadas correctamente.
* Tiempo hasta una decisión de contención dentro de la simulación.
* Decisiones financieras verificadas por un canal independiente.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [ATT&CK: Valid Accounts](https://attack.mitre.org/techniques/T1078/).
* [ATT&CK: Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539/).
* [Sigma: Getting Started](https://sigmahq.io/docs/guide/getting-started.html).

Para continuar: [CS50’s Introduction to Cybersecurity](https://cs50.harvard.edu/cybersecurity/) (contenido gratuito) y [Perform threat hunting in Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) (lectura gratuita; las prácticas con Azure pueden generar costes).

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
