# Infraestructura Crítica y Ciberresiliencia - Arquitectura Lattices

## Síntesis Ejecutiva

Una infraestructura crítica sostiene funciones cuya interrupción puede afectar gravemente a personas, economía o servicios esenciales. La digitalización conecta procesos físicos con identidades, redes y software, ampliando las dependencias que deben analizarse. Un incidente digital puede tener consecuencias operacionales, pero su impacto depende de la arquitectura y de los controles del proceso. El análisis comienza por identificar funciones, activos y modos de falla, antes de decidir qué tecnologías de protección o recuperación implantar. [NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).

La ciberresiliencia combina prevención, resistencia, adaptación y recuperación. En sistemas operacionales, la disponibilidad y la seguridad del proceso condicionan cambios, observación y pruebas. Los modelos de segmentación ayudan a ordenar funciones y flujos, pero no constituyen controles efectivos por sí solos. Conviene distinguir redundancia de independencia, validar rutas de recuperación y practicar la coordinación entre equipos técnicos y responsables de operación. Las referencias internacionales aportan métodos de análisis; su aplicación requiere evaluar el entorno y las obligaciones locales. [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026).

## Conceptos Core

* **Infraestructura crítica:** Servicios y activos cuya interrupción puede generar consecuencias relevantes para la sociedad.
* **Convergencia IT/OT:** Interconexión entre sistemas de información y sistemas que supervisan o controlan procesos físicos.
* **Zonas y conductos:** Agrupación de activos y definición de comunicaciones para gestionar fronteras de seguridad industrial.
* **Recuperación operacional:** Restablecimiento validado de una función, considerando dependencias y seguridad del proceso.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — estudiar arquitectura y restricciones de tecnología operacional.
* [ISA/IEC 62443 — Industrial Automation and Control Systems Security](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) — examinar gestión del riesgo, zonas y conductos.

### Papers y Literatura de Frontera

* [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) — contrastar el papel de las dependencias en el panorama de amenazas.

### Repositorios y Herramientas Open Source

* [Malcolm](https://github.com/cisagov/Malcolm) — observar tráfico y capturas de laboratorio.
* [CISA Cyber Security Evaluation Tool (CSET)](https://github.com/cisagov/cset) — estructurar evaluaciones y registrar evidencias de controles.

### Ruta de Aprendizaje Autónoma

* [CISA — ICS Cybersecurity (101)](https://www.cisa.gov/resources-tools/programs/ics-training-available-through-cisa) — comenzar por ICS Cybersecurity (101), gratuito con registro.

---

[⬅ Lección Anterior](01-glosario-y-conceptos-clave.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](../02-dia1-seminario/01-wong-ia-cibercrimen.md)
