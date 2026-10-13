# Cyber Threat Intelligence y Decisiones de Defensa - Omar Fuentes

## Síntesis Ejecutiva

Cyber Threat Intelligence transforma observaciones de actividad adversaria en conocimiento útil para decidir qué proteger, detectar e investigar. Su calidad depende de preguntas explícitas, fuentes trazables y una evaluación de confianza que distinga hechos de hipótesis. Una lista de direcciones IP no constituye por sí sola inteligencia accionable: necesita contexto temporal, relación con campañas y relevancia para los activos de la organización. El producto debe conectar objetivos estratégicos con tareas técnicas, como ajustar una detección o revisar una exposición prioritaria. [NIST SP 800-150 — Guide to Cyber Threat Information Sharing](https://csrc.nist.gov/pubs/sp/800/150/final).

Los desafíos incluyen duplicación de fuentes, indicadores obsoletos, sesgos de cobertura y atribuciones débiles. El ciclo analítico requiere registrar procedencia, corroborar hallazgos y obtener retroalimentación de quienes consumen la información. El intercambio mediante formatos estructurados facilita la automatización, pero no elimina la necesidad de controlar calidad y restricciones de difusión. Conviene medir si la inteligencia modifica decisiones y mejora cobertura, evitando evaluar un programa por el volumen de indicadores importados. Las hipótesis sobre actores deben expresar incertidumbre y poder revisarse con nueva evidencia. [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology).

## Conceptos Core

* **Priority Intelligence Requirements (PIR):** Preguntas priorizadas que orientan la recopilación y el análisis hacia necesidades de decisión.
* **Indicator of Compromise (IoC):** Observable que, interpretado en contexto, puede indicar actividad o compromiso adversario.
* **STIX/TAXII:** Modelo de información y protocolo de intercambio utilizados para compartir inteligencia de amenazas.
* **Confianza analítica:** Evaluación explícita de la solidez de una conclusión a partir de fuentes, corroboración y supuestos.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-150 — Guide to Cyber Threat Information Sharing](https://csrc.nist.gov/pubs/sp/800/150/final) — definir objetivos y reglas del intercambio.
* [OASIS Cyber Threat Intelligence — STIX/TAXII](https://oasis-open.github.io/cti-documentation/) — estudiar modelos y protocolos de intercambio estructurado.

### Papers y Literatura de Frontera

* [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology) — seguir una metodología transparente para construir panoramas de amenazas.

### Repositorios y Herramientas Open Source

* [OpenCTI](https://github.com/OpenCTI-Platform/opencti) — modelar entidades, relaciones y procedencia.
* [MISP](https://github.com/MISP/MISP) — curar e intercambiar indicadores con contexto.

### Ruta de Aprendizaje Autónoma

* [Perform threat hunting in Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) — contrastar hipótesis de inteligencia con eventos y entidades; contenido gratuito, prácticas Azure sujetas a consumo.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/02-fuentes-threat-intelligence.mp3)

---

[⬅ Lección Anterior](01-caceres-blue-team-ia.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](03-cordero-resiliencia-hardware.md)
