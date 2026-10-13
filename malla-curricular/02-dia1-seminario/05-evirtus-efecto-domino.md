# Efecto Dominó de los Incidentes y Riesgo de Proveedores - Representante técnico de E-Virtus

## Síntesis Ejecutiva

Las organizaciones críticas dependen de proveedores de identidad, comunicaciones, software y mantenimiento que conectan dominios de confianza distintos. Un incidente en una dependencia puede propagarse mediante permisos compartidos, actualizaciones o interrupciones de servicios, incluso sin comprometer todos los sistemas afectados. Analizar el efecto dominó exige modelar qué funciones consumen cada servicio y qué consecuencias produce su ausencia. La evaluación de terceros debe incluir su exposición técnica y el impacto operacional de la dependencia, no limitarse a su documentación comercial. [NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

La reducción del riesgo combina inventarios de componentes, verificación de artefactos, acceso restringido y alternativas de continuidad. Las listas SBOM ayudan a identificar software, pero no acreditan por sí solas que un proveedor sea confiable ni describen toda la cadena operacional. Como criterio de arquitectura, conviene ensayar la pérdida de una dependencia, validar restauraciones y revisar los permisos concedidos a terceros. El seguimiento debe medir rutas de propagación y tiempos de recuperación de servicios, evitando confundir la redundancia de servidores con independencia de proveedores o de planos de administración. [ENISA — Threat Landscape for Supply Chain Attacks](https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks).

## Conceptos Core

* **Cybersecurity Supply Chain Risk Management (C-SCRM):** Gestión del riesgo cibernético asociado a productos, servicios y proveedores durante su ciclo de vida.
* **Software Bill of Materials (SBOM):** Inventario estructurado de componentes de software y sus relaciones.
* **Radio de impacto:** Conjunto de sistemas o servicios que puede afectar una falla o compromiso inicial.
* **Dependencia común:** Recurso compartido cuya interrupción puede anular varias medidas aparentes de redundancia.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) — organizar la evaluación de riesgos y controles de terceros.
* [NIST Cybersecurity Framework (CSF) 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — vincular riesgo de proveedores y continuidad con responsabilidades de gobernanza.

### Papers y Literatura de Frontera

* [ENISA — Threat Landscape for Supply Chain Attacks](https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks) — estudiar una taxonomía y casos de compromiso de cadenas de suministro.

### Repositorios y Herramientas Open Source

* [Syft](https://github.com/anchore/syft) — generar inventarios SBOM de imágenes y sistemas de archivos.
* [OpenSSF Scorecard](https://github.com/ossf/scorecard) — evaluar señales de prácticas de seguridad de dependencias open source; el puntaje no garantiza seguridad.

### Ruta de Aprendizaje Autónoma

* [CISA — ICS Cybersecurity (101)](https://www.cisa.gov/resources-tools/programs/ics-training-available-through-cisa) — cursar ICS Cybersecurity (101), gratuito con registro, y trasladar el análisis de dependencias a servicios operacionales.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/05-evirtus-efecto-domino.mp3)

---

[⬅ Lección Anterior](04-bordachar-anci-regulacion.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](06-fernandez-dispositivos-medicos.md)
