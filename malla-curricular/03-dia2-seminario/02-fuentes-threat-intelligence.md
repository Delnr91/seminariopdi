# Cyber Threat Intelligence (CTI) - Omar Fuentes

## Síntesis Ejecutiva

La Inteligencia de Ciberamenazas (CTI) constituye el eje estratégico que transforma la ciberdefensa de una postura reactiva y genérica a una disciplina de anticipación analítica informada. En un contexto donde los actores de amenazas avanzadas persistentes (APTs) diseñan ataques específicos adaptados a cada industria, proteger todos los activos por igual resulta inviable. La CTI recolecta, refina y correlaciona datos de fuentes abiertas (OSINT), foros clandestinos (Dark Web) y telemetría global para desarticular las ventajas asimétricas del atacante.

La efectividad de la CTI radica en su capacidad de articular tres niveles de decisión: estratégico (para directores y toma de decisiones presupuestarias), operacional (para planificadores de seguridad y arquitectos) y táctico (indicadores de compromiso y firmas para firewalls y EDRs). Al mapear los procedimientos del adversario mediante el modelo Diamond y marcos de referencia globales, las organizaciones pueden anticipar qué puertas intentará forzar el enemigo, fortaleciendo proactivamente sus controles defensivos antes del impacto.

---

## Conceptos Core

* **Diamond Model of Intrusion Analysis:** Metodología que vincula cuatro elementos centrales de cada actividad maliciosa: Adversario, Capacidad, Infraestructura y Víctima.
* **Pyramid of Pain (David Bianco):** Concepto que jerarquiza el grado de dificultad que se le impone al atacante al bloquear sus recursos (desde valores Hash fáciles de cambiar hasta TTPs complejas).
* **Actionable Threat Intelligence:** Datos refinados y contextualizados que ofrecen la información precisa necesaria para que un defensor tome una decisión operativa inmediata.
* **TTPs (Tactics, Techniques, and Procedures):** Patrones de comportamiento, herramientas y métodos característicos que identifican y distinguen a un grupo de cibercrimen o actor patrocinado por un Estado.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [OASIS STIX 2.1 & TAXII Standards](https://oasis-open.github.io/cti-documentation/): Estándares internacionales abiertos para la representación estructurada y transporte automatizado de inteligencia de ciberamenazas.
* [MITRE ATT&CK Matrix for Enterprise](https://attack.mitre.org/): Taxonomía universal que clasifica y documenta las fases operativas de adversarios digitales en entornos empresariales.
* [NIST SP 800-150: Guide to Cyber Threat Information Sharing](https://csrc.nist.gov/publications/detail/sp/800-150/final): Directrices técnicas para formalizar acuerdos y plataformas de intercambio de inteligencia entre pares del sector.
* [Traffic Light Protocol (TLP 2.0 - FIRST)](https://www.first.org/tlp/): Estándar internacional que norma la clasificación y compartición segura de información sensible (TLP:RED, AMBER, GREEN, CLEAR).

### Papers y Literatura de Frontera
* **IEEE Security & Privacy (2021):** *Measuring and Improving the Actionability of Cyber Threat Intelligence Feeds* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9444459)) — Estudio cuantitativo sobre la redundancia, frescura y efectividad real de los feeds comerciales y abiertos de IoCs.
* **Journal of Cybersecurity (Oxford, 2020):** *Adversary Modeling, Attribution, and the Cyber Threat Intelligence Process* ([Oxford Academic](https://academic.oup.com/cybersecurity/article/6/1/tyaa016/5923053)) — Análisis riguroso sobre las dificultades técnicas y sesgos metodológicos en la atribución formal de ciberataques.

### Repositorios y Herramientas (Open Source)
* [OpenCTI (Open Cyber Threat Intelligence)](https://github.com/OpenCTI-Platform/opencti): Plataforma enterprise de código abierto para gestionar relaciones de conocimiento de amenazas y actores APT compatible con STIX2.
* [MISP (Malware Information Sharing Platform)](https://github.com/MISP/MISP): Software de código abierto líder a nivel gubernamental y corporativo para compartir telemetría de ciberseguridad.
* [YARA (The Pattern Matching Swiss Army Knife)](https://github.com/VirusTotal/yara): Herramienta estándar de la industria desarrollada por VirusTotal para clasificar e identificar familias de malware según patrones.
* [AlienVault OTX Python SDK](https://github.com/AlienVault-OTX/OTX-Python-SDK): Biblioteca para conectar de forma automatizada aplicaciones de seguridad con la base comunitaria global de Open Threat Exchange.

### Ruta de Aprendizaje Autónoma
* [Mandiant / Google Cloud: Threat Intelligence Fundamentals](https://cloud.google.com/security/products/threat-intelligence): Cursos y whitepapers de nivel enterprise sobre modelado del adversario e investigación de actores hostiles globales.
* [TryHackMe: Cyber Threat Intelligence Path](https://tryhackme.com/path/outline/cyber-threat-intelligence): Laboratorios interactivos para analizar reportes CTI, construir reglas YARA y mapear campañas contra MITRE ATT&CK.
* [SANS CTI Summit Open Archive](https://www.sans.org/cyber-security-summits/cyber-threat-intelligence-summit/): Grabaciones magistrales y diapositivas de las investigaciones más avanzadas presentadas en la cumbre mundial de CTI.
* [Cisco NetAcad: Threat Hunting & Intelligence Operations](https://www.netacad.com): Formación estructurada sobre correlación de alertas y utilización de marcos de inteligencia para defensas preventivas.

---

## Enlace al Audio

[▶️ Escuchar Podcast Resumen](../../assets/audio/dia2_02_fuentes.mp3)

---

[⬅️ Lección Anterior](01-caceres-blue-team-ia.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](03-cordero-resiliencia-hardware.md)
