# Superficies de Ataque en Dispositivos Médicos Conectados - Víctor Fernández

## Síntesis Ejecutiva

Un dispositivo médico conectado integra firmware, interfaces, servicios de actualización y dependencias de red que amplían su superficie de ataque. La confidencialidad de los datos es solo una dimensión: una pérdida de integridad o disponibilidad puede afectar al proceso asistencial. El modelo de amenazas debe relacionar cada interfaz y límite de confianza con posibles consecuencias operativas. La gestión de seguridad necesita acompañar al producto durante su diseño, integración y mantenimiento, considerando tanto el comportamiento del dispositivo como los sistemas que lo administran. [FDA — Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket).

En una red clínica, las ventanas de intervención, los equipos heredados y la disponibilidad de soporte condicionan el tratamiento de vulnerabilidades. El control de accesos, el inventario y la segmentación reducen exposición, pero su implantación debe validarse con responsables técnicos y asistenciales antes de afectar servicios reales. Conviene comenzar con observación pasiva y pruebas en entornos representativos, documentando dependencias y mecanismos de recuperación. Para equipos con modelos de IA, el análisis debe incluir datos e inferencias, además del software convencional, sin presentar resultados de laboratorio como garantía de seguridad clínica. [Systems-Theoretic and Data-Driven Security Analysis in ML-enabled Medical Devices](https://arxiv.org/abs/2506.15028).

## Conceptos Core

* **Internet of Medical Things (IoMT):** Ecosistema de dispositivos y servicios médicos que intercambian datos a través de redes.
* **Modelado de amenazas:** Análisis de activos, interfaces, adversarios y límites de confianza para identificar escenarios de compromiso.
* **Ciclo de vida seguro:** Gestión de controles, vulnerabilidades y actualizaciones desde el diseño hasta el retiro del dispositivo.
* **Seguridad ciberfísica:** Relación entre un evento digital y sus posibles efectos sobre procesos o personas.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [FDA — Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket) — revisar recomendaciones de diseño y documentación de ciberseguridad de dispositivos.
* [NIST SP 1800-8 — Securing Wireless Infusion Pumps in Healthcare Delivery Organizations](https://csrc.nist.gov/pubs/sp/1800/8/final) — examinar una arquitectura de referencia para proteger un ecosistema de bombas de infusión.

### Papers y Literatura de Frontera

* [Systems-Theoretic and Data-Driven Security Analysis in ML-enabled Medical Devices](https://arxiv.org/abs/2506.15028) — investigar análisis de riesgo de dispositivos con IA/ML; preprint de investigación, no validación clínica.

### Repositorios y Herramientas Open Source

* [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) — representar interfaces y fronteras de confianza.
* [Ghidra](https://github.com/NationalSecurityAgency/ghidra) — analizar firmware autorizado en laboratorio, sin intervenir equipos en uso asistencial.

### Ruta de Aprendizaje Autónoma

* [Establish the guiding principles and core components of Zero Trust](https://learn.microsoft.com/en-us/training/paths/zero-trust-principles/) — estudiar control de identidades y endpoints para adaptar principios de acceso a redes clínicas.

## 📺 Video de la intervención

[▶️ Ir al bloque: 06:57:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=25040s) · [Cierre aproximado: 07:14:00](https://www.youtube.com/watch?v=PEqWRTb1idE&t=26040s)

**Duración estimada del bloque:** ≈ 16 min 40 s. **Formato:** Exposición. Puntos de navegación aproximados por inspección visual; pueden incluir introducción o preguntas. [Consultar metodología y recorrido de ambas jornadas](../../VIDEOS.md).

## 🛠️ Anexo de métodos y herramientas

[Práctica guiada, estrategias y herramientas open source](../../anexos/02-dia1-seminario/06-fernandez-dispositivos-medicos.md). Incluye entregables y métricas para contrastar resultados.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/06-fernandez-dispositivos-medicos.mp3)

---

[⬅ Lección Anterior](05-evirtus-efecto-domino.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](07-panel-sectores-criticos.md)
