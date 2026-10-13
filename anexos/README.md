# 🛠️ Anexos prácticos de métodos y herramientas

**Curaduría: [Lattices](https://lattices.cl).** Dieciocho guías para profundizar las temáticas de las dos jornadas, con tres métodos por guía, herramientas open source, un laboratorio, evidencias y métricas.

## Cómo recorrer las guías

1. Abrir el bloque correspondiente en el [índice de videos](../VIDEOS.md).
2. Leer la lección de referencia cuando exista y elegir un objetivo práctico.
3. Empezar con tablas y datos sintéticos; preparar herramientas solo si el ejercicio lo requiere.
4. Conservar versiones, entradas, resultados y limitaciones para permitir una revisión independiente.

Los tiempos del video son aproximados; las propuestas prácticas son ampliaciones de Lattices y no se atribuyen literalmente a los speakers. Las dos guías de E-Virtus se relacionan con una única intervención de Mauricio Barrera. Los paneles se tratan como bloques compartidos.

## Recursos y coste de ejecución

La lectura y las tablas requieren pocos recursos. PCAP pequeños, SBOM de muestras y análisis estático pueden trabajarse por separado. OpenCTI, Malcolm, OpenEMR, SPIRE/Cilium o CALDERA completos necesitan un laboratorio dimensionado; en equipos modestos conviene utilizar primero las alternativas con archivos o ejercicios de mesa indicadas en cada guía. Los modelos y servicios de nube pueden consumir recursos o generar costes; no son requisitos para consultar este repositorio.

Los comandos y configuraciones son ejemplos de estudio. Se contrastaron con documentación primaria, pero no se ejecutaron los 18 laboratorios ni se desplegaron sus herramientas durante la curaduría. Sus resultados deben medirse en el entorno que prepare el estudiante.

## Día 1

| Speaker o referencia | Guía | Resultado que se busca |
| --- | --- | --- |
| Marcelo Wong Cea | [Inteligencia Artificial aplicada al Cibercrimen](02-dia1-seminario/01-wong-ia-cibercrimen.md) | Evaluar el abuso de IA y convertir señales observables en hipótesis de investigación reproducibles. |
| Guillermo Lama | [Seguridad y Resiliencia de la Infraestructura DNS](02-dia1-seminario/02-lama-infraestructura-dns.md) | Comprobar la cadena DNSSEC y diseñar continuidad de resolución sin confundir redundancia con independencia. |
| Manu Fernández | [Fraude y Suplantación de Identidad con IA](02-dia1-seminario/03-fernandez-crimen-ia.md) | Diseñar una verificación de identidad que resista suplantación audiovisual y no dependa de detectar visualmente un deepfake. |
| Michelle Bordachar | [Regulación ANCI y Gobernanza de Ciberseguridad](02-dia1-seminario/04-bordachar-anci-regulacion.md) | Traducir decisiones de gobernanza en responsables, evidencias y un proceso de respuesta que pueda revisarse. |
| Mauricio Barrera (E-Virtus) · ampliación temática | [Efecto Dominó de los Incidentes y Riesgo de Proveedores](02-dia1-seminario/05-evirtus-efecto-domino.md) | Analizar cómo un componente o proveedor puede interrumpir varios servicios y priorizar mitigaciones por impacto operacional. |
| Víctor Fernández | [Superficies de Ataque en Dispositivos Médicos Conectados](02-dia1-seminario/06-fernandez-dispositivos-medicos.md) | Relacionar interfaces de un dispositivo médico con riesgos técnicos y consecuencias asistenciales, usando únicamente artefactos de laboratorio. |
| Panel Multisectorial | [Ciberresiliencia en Sectores Críticos](02-dia1-seminario/07-panel-sectores-criticos.md) | Ensayar coordinación IT/OT y continuidad entre sectores a partir de información mínima y evidencia compartible. |
| Xavier Bonnaire | [Agentes de IA y Riesgo en Infraestructura Crítica](02-dia1-seminario/08-bonnaire-agentes-ia.md) | Medir si un agente respeta límites de autoridad y se recupera de datos adversarios sin ejecutar acciones reales. |
| Mauricio Barrera (E-Virtus) · ampliación temática | [Arquitecturas Zero Trust para Redes Críticas](02-dia1-seminario/09-evirtus-zero-trust.md) | Diseñar acceso basado en identidad y contexto para limitar propagación de fallos entre cargas de trabajo. |
| Fernanda Macías | [Análisis de amenazas y filtraciones](02-dia1-seminario/10-macias-analisis-amenazas.md) | Transformar una alerta de filtración en un análisis contextualizado y un intercambio responsable entre equipos de respuesta. |
| Sergey Nikitin (Group-IB) | [Cibercrimen y economía del fraude](02-dia1-seminario/11-nikitin-cibercrimen-fraude.md) | Analizar fraude vinculado a abuso de identidades y sesiones mediante telemetría sintética y decisiones de respuesta trazables. |

## Día 2

| Speaker o referencia | Guía | Resultado que se busca |
| --- | --- | --- |
| Diego Cáceres | [Blue Team Aumentado por Inteligencia Artificial](03-dia2-seminario/01-caceres-blue-team-ia.md) | Evaluar si la asistencia de IA mejora la detección sin perder trazabilidad ni aumentar acciones erróneas. |
| Omar Fuentes | [Cyber Threat Intelligence y Decisiones de Defensa](03-dia2-seminario/02-fuentes-threat-intelligence.md) | Convertir una pregunta de inteligencia en una decisión defensiva, conservando procedencia, vigencia y restricciones de intercambio. |
| César Cordero | [Resiliencia de Hardware y Firmware](03-dia2-seminario/03-cordero-resiliencia-hardware.md) | Comprender protección, detección y recuperación del firmware como parte de la continuidad de un servicio. |
| Nina Alli y participantes | [Ciberseguridad y Continuidad Asistencial en Salud](03-dia2-seminario/04-alli-salud-ciberseguridad.md) | Evaluar continuidad asistencial y recuperación de información sin utilizar pacientes ni sistemas clínicos reales. |
| Tales Albuquerque | [Prevención, Detección y Respuesta ante Ciberamenazas](03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) | Conectar una hipótesis de intrusión con evidencia mínima, una decisión de contención y una recuperación comprobable. |
| James Norman | [Amenazas Híbridas y Resiliencia Informacional](03-dia2-seminario/06-norman-amenazas-hibridas.md) | Analizar una campaña informacional ficticia junto a un incidente técnico sin confundir coordinación, identidad y atribución. |
| Nadezda Abbas | [Desarrollo de Talento para la Ciberresiliencia](03-dia2-seminario/07-abbas-academia-talento.md) | Construir una ruta de formación basada en tareas y evidencias observables, con evaluación repetible de capacidades. |

---

[🏠 Malla Curricular](../README.md) | [📺 Videos por intervención](../VIDEOS.md)
