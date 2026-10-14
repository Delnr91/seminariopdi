# Anexo práctico: Ciberresiliencia en Sectores Críticos - Panel Multisectorial

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 07:17:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=26260s) · [Índice y límites de los tiempos](../../VIDEOS.md)

El video corresponde al panel completo. Este anexo no atribuye todas las recomendaciones a cada participante individual.

## Objetivo

Ensayar coordinación IT/OT y continuidad entre sectores a partir de información mínima y evidencia compartible.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Mapeo de interdependencias** | Relacionar energía, comunicaciones y operación; incluir quién controla cada dependencia y cómo avisar. | Mapa de fallos comunes y contactos del ejercicio. |
| **Monitoreo pasivo** | Analizar PCAP y registros previamente obtenidos; evitar que la práctica introduzca tráfico en redes operacionales. | Inventario de comunicaciones y anomalías explicadas. |
| **Intercambio contextualizado** | Compartir indicador, fuente, vigencia y restricción de distribución, no una lista de IP sin contexto. | Paquete de inteligencia con alcance y acciones sugeridas. |

## Herramientas open source

* [Malcolm](https://github.com/cisagov/Malcolm) — Suite de análisis de PCAP, Zeek y alertas; su despliegue completo requiere recursos importantes.
* [MISP](https://github.com/MISP/MISP) — Intercambio de información de amenazas; revisar taxonomías y reglas de distribución.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Plantear una caída ficticia de comunicaciones que afecte energía y abastecimiento de agua; asignar roles sectoriales.
2. Analizar un PCAP de ejemplo mediante Zeek o Malcolm y registrar relaciones entre hosts. No instalar sensores en OT para este ejercicio.
3. Crear un evento sintético en MISP con fuente, fecha y etiqueta TLP; comprobar permisos y distribución efectivos antes de compartir.
4. Ensayar avisos y operación degradada, identificando qué sector necesita cada dato y qué información puede omitirse.

### Código y configuración de referencia

Regla de observación de Modbus con el parser del protocolo, para adaptar y probar con PCAP propios. Se usa alert, sin bloquear comunicaciones.

```text
alert tcp any any -> $HOME_NET 502 (msg:"LAB Modbus funcion 6 observada"; flow:to_server,established; modbus: function 6; sid:1000001; rev:1;)
```

**Alcance:** La función 6 puede ser legítima. Autorización, ventana de mantenimiento e impacto necesitan contexto externo. Requiere Suricata con parser Modbus habilitado; validar la regla y sus alertas en un laboratorio antes de cualquier uso operacional.

**Comprobación:** keyword contrastado con documentación oficial. No se ejecutó el motor de detección sobre PCAP.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Dependencias críticas con contacto y alternativa de continuidad.
* Alertas compartidas con contexto, vigencia y restricciones.
* Tiempo de coordinación en el escenario frente al objetivo acordado.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [Suricata 8.0.1: Modbus Keyword](https://docs.suricata.io/en/suricata-8.0.1/rules/modbus-keyword.html).
* [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
* [FIRST Traffic Light Protocol](https://www.first.org/tlp/).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/07-panel-sectores-criticos.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
