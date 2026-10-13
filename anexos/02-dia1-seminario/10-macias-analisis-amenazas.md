# Anexo práctico: Análisis de amenazas y filtraciones - Fernanda Macías

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 04:22:00](https://www.youtube.com/watch?v=PEqWRTb1idE&t=15720s) · [Índice y límites de los tiempos](../../VIDEOS.md)

Intervención adicional identificada mediante el rótulo «Fernanda Macías — ANCI y CSIRT Nacional». Este anexo es una propuesta práctica de Lattices, no una transcripción.

## Objetivo

Transformar una alerta de filtración en un análisis contextualizado y un intercambio responsable entre equipos de respuesta.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Triage de filtración** | Registrar qué se observó, dónde, cuándo y con qué confianza; distinguir exposición confirmada de una afirmación externa. | Ficha de incidente con evidencia y datos faltantes. |
| **Priorización por impacto** | Relacionar activos, identidades, permisos y servicio afectado; tratar una cuenta válida comprometida como hipótesis a comprobar. | Prioridad justificada y acciones de verificación. |
| **Coordinación CSIRT** | Mantener una cronología única, responsables y reglas de distribución; compartir solo los datos necesarios. | Caso colaborativo con decisiones y destinatarios. |

## Herramientas open source

* [DFIR-IRIS](https://github.com/dfir-iris/iris-web) — Casos, cronología y colaboración en investigación; ajustar acceso al mínimo necesario.
* [MISP](https://github.com/MISP/MISP) — Contexto e intercambio de indicadores; una etiqueta TLP debe acompañarse de controles efectivos de distribución.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Crear un aviso ficticio de filtración con un dominio reservado y una cuenta inventada. No obtener credenciales de filtraciones reales.
2. Registrar el caso y separar la afirmación inicial de una observación técnica independiente, como un log sintético de acceso.
3. Mapear el abuso potencial de cuenta con ATT&CK y redactar un paquete de intercambio con propósito, fuente, vigencia y destinatarios.
4. Ensayar escalamiento y cierre, conservando hipótesis refutadas y el motivo de cada decisión.

### Ejemplo de trabajo

```json
{"caso":"CSIRT-LAB-01","servicio":"portal_ficticio","observacion":"aviso_no_corroborado","confianza":"baja","siguiente_paso":"revisar_log_sintetico","datos_personales":false}
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Avisos corroborados o refutados con evidencia independiente.
* Tiempo de clasificación y asignación de responsable en el ejercicio.
* Paquetes de intercambio sin datos ajenos al propósito.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
* [ATT&CK: Valid Accounts](https://attack.mitre.org/techniques/T1078/).
* [FIRST TLP](https://www.first.org/tlp/).

Para continuar: [CS50’s Introduction to Cybersecurity](https://cs50.harvard.edu/cybersecurity/) (contenido gratuito) y [Perform threat hunting in Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) (lectura gratuita; las prácticas con Azure pueden generar costes).

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
