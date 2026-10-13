# Prevención, Detección y Respuesta ante Ciberamenazas - Tales Albuquerque

## Síntesis Ejecutiva

La prevención reduce oportunidades de compromiso, mientras la detección y la respuesta permiten gestionar ataques que superan los controles iniciales. La efectividad depende de combinar visibilidad de identidad, endpoints y red con reglas vinculadas a escenarios de riesgo. Los avisos deben permitir reconstruir secuencias de actividad y evaluar el impacto sobre activos prioritarios. Un antivirus sin alertas o un tablero con baja severidad no acreditan ausencia de intrusión; la conclusión necesita considerar cobertura de sensores, calidad de los registros y comportamiento esperado del entorno. [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

El desafío operativo es convertir señales incompletas en decisiones proporcionales y recuperables. La contención debe coordinarse con propietarios de servicios, preservar evidencia y tratar credenciales o persistencia asociadas al incidente. Los procedimientos automatizados requieren criterios de activación, permisos acotados y revisión de sus efectos. Como práctica de evaluación, conviene probar detecciones, restauraciones y escalamiento con escenarios reproducibles, midiendo tiempo de análisis y recuperación efectiva. El aprendizaje posterior debe modificar controles y procedimientos, en lugar de cerrar el caso cuando desaparecen las alertas visibles. [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026).

## Conceptos Core

* **Endpoint Detection and Response (EDR):** Capacidad de observar eventos de endpoints, investigar actividad y ejecutar medidas de respuesta.
* **Threat hunting:** Búsqueda guiada por hipótesis de actividad adversaria que las detecciones existentes podrían no identificar.
* **Security Orchestration, Automation and Response (SOAR):** Coordinación de acciones y procedimientos automatizados de gestión de incidentes.
* **Contención proporcional:** Limitación del impacto de un incidente considerando evidencia, criticidad y consecuencias de la intervención.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — conectar respuesta con gestión de riesgos y recuperación.
* [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/) — definir comportamientos y brechas de cobertura.

### Papers y Literatura de Frontera

* [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) — contrastar escenarios de defensa con tendencias y amenazas documentadas.

### Repositorios y Herramientas Open Source

* [Velociraptor](https://github.com/Velocidex/velociraptor) — consultar artefactos y obtener visibilidad de endpoints.
* [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) — validar detecciones mediante pruebas pequeñas, revisadas previamente y ejecutadas en laboratorio.

### Ruta de Aprendizaje Autónoma

* [Create detections and perform investigations using Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-create-detections-perform-investigations-azure-sentinel/) — construir detecciones e investigar casos.
* [Perform threat hunting in Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) — desarrollar búsquedas basadas en hipótesis; lectura gratuita, prácticas con servicios Azure sujetas a costes.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/05-albuquerque-deteccion-respuesta.mp3)

---

[⬅ Lección Anterior](04-alli-salud-ciberseguridad.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](06-norman-amenazas-hibridas.md)
