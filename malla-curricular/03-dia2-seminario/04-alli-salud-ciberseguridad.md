# Ciberseguridad y Continuidad Asistencial en Salud - Nina Alli

## Síntesis Ejecutiva

La digitalización clínica conecta registros, identidad, comunicaciones y equipos médicos con procesos que dependen de la disponibilidad de información. Un incidente puede interrumpir la atención sin modificar directamente un dispositivo: la pérdida de acceso a sistemas de apoyo ya afecta coordinación y continuidad. La gestión del riesgo debe relacionar datos y servicios con funciones asistenciales, priorizando recuperación e integridad según su impacto. El inventario técnico necesita incorporar procesos, responsables y dependencias para distinguir una interrupción tolerable de una degradación que requiere respuesta inmediata. [NIST SP 1800-8 — Securing Wireless Infusion Pumps in Healthcare Delivery Organizations](https://csrc.nist.gov/pubs/sp/1800/8/final).

El diseño de controles debe considerar ritmos operativos, acceso de terceros y equipos que no admiten las mismas intervenciones que un endpoint convencional. La segmentación, el control de identidad y la capacidad de restauración necesitan validación técnica y asistencial antes de aplicarse a servicios reales. Conviene ensayar procedimientos de trabajo degradado, coordinación de incidentes y recuperación de información en entornos representativos. La evaluación debe observar continuidad de procesos y calidad de la información recuperada, evitando presentar la mera existencia de una copia de seguridad como prueba de que el servicio puede restablecerse. [ENISA — Health Threat Landscape](https://www.enisa.europa.eu/publications/health-threat-landscape).

## Conceptos Core

* **Continuidad asistencial:** Capacidad de mantener funciones de atención durante interrupciones o degradación de sistemas de soporte.
* **Dependencia clínica digital:** Relación entre una actividad asistencial y los datos, dispositivos o servicios necesarios para ejecutarla.
* **Segmentación de red clínica:** Separación de flujos y accesos según funciones y riesgos de equipos y servicios de salud.
* **Recuperación validada:** Restauración ensayada que verifica disponibilidad, integridad y utilidad operacional del servicio.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 1800-8 — Securing Wireless Infusion Pumps in Healthcare Delivery Organizations](https://csrc.nist.gov/pubs/sp/1800/8/final) — estudiar separación de funciones y controles en un ecosistema médico conectado.
* [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — organizar coordinación y recuperación ante incidentes.

### Papers y Literatura de Frontera

* [ENISA — Health Threat Landscape](https://www.enisa.europa.eu/publications/health-threat-landscape) — analizar amenazas, impactos y tendencias observadas en el sector sanitario europeo.

### Repositorios y Herramientas Open Source

* [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) — modelar dependencias de un proceso clínico.
* [OpenEMR](https://github.com/openemr/openemr) — construir un entorno con datos sintéticos para estudiar configuración y dependencias de un sistema clínico.

### Ruta de Aprendizaje Autónoma

* [Establish the guiding principles and core components of Zero Trust](https://learn.microsoft.com/en-us/training/paths/zero-trust-principles/) — estudiar control de acceso y protección de recursos.
* [CS50's Introduction to Cybersecurity](https://cs50.harvard.edu/cybersecurity/) — reforzar principios de protección de cuentas, datos y sistemas con materiales gratuitos.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/04-alli-salud-ciberseguridad.mp3)

---

[⬅ Lección Anterior](03-cordero-resiliencia-hardware.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](05-albuquerque-deteccion-respuesta.md)
