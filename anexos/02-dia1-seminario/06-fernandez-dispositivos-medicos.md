# Anexo práctico: Superficies de Ataque en Dispositivos Médicos Conectados - Víctor Fernández

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 06:57:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=25040s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Relacionar interfaces de un dispositivo médico con riesgos técnicos y consecuencias asistenciales, usando únicamente artefactos de laboratorio.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Modelo de amenazas** | Dibujar dispositivo, estación clínica, actualización y operador; marcar límites de confianza y flujos imprescindibles. | Diagrama de flujo y amenazas priorizadas. |
| **Análisis estático de firmware** | Inspeccionar una copia autorizada sin ejecutar el binario; registrar formato, componentes y hallazgos reproducibles. | Informe con offsets, hashes y nivel de certeza. |
| **Reducción de superficie** | Definir comunicaciones necesarias y mantenimiento; evaluar controles compensatorios cuando una actualización no sea viable. | Matriz de flujos permitidos y excepciones con responsable. |

## Herramientas open source

* [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) — Modelado visual de amenazas con límites de confianza.
* [Ghidra](https://github.com/NationalSecurityAgency/ghidra) — Ingeniería inversa de binarios autorizados; los hallazgos requieren contexto y corroboración.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Crear un dispositivo ficticio conectado a una estación clínica, un servidor de actualización y un sistema de monitoreo.
2. Modelar al menos cuatro interfaces y tres amenazas. Diferenciar confidencialidad, integridad de una orden y continuidad del servicio.
3. Abrir un firmware de práctica en Ghidra como archivo para análisis estático; conservar el original y anotar el hash de la copia.
4. Proponer segmentación y mantenimiento mediante la matriz de flujos; explicar cómo comprobar continuidad sin conectar equipos clínicos reales.

### Ejemplo de trabajo

```csv
origen,destino,flujo,necesario,justificacion
dispositivo_ficticio,estacion_clinica,telemetria,si,seguimiento_simulado
dispositivo_ficticio,internet_general,navegacion,no,sin_requisito_operacional
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Interfaces y flujos con propietario y justificación.
* Amenazas con consecuencia clínica descrita y evidencia técnica separada.
* Controles que mantienen los flujos indispensables en la simulación.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST SP 1800-8](https://csrc.nist.gov/pubs/sp/1800/8/final).
* [Ghidra](https://github.com/NationalSecurityAgency/ghidra).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/06-fernandez-dispositivos-medicos.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
