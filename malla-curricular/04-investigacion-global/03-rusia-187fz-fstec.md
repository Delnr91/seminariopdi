# Ley Federal N° 187-FZ de Seguridad de Infraestructura Crítica y GosSOPKA - Servicio Federal de Control Técnico y Exportaciones (FSTEC / FSB)

## Síntesis Ejecutiva

La doctrina de ciberseguridad de la Federación Rusa concibe la protección de la infraestructura crítica como un pilar indivisible de la defensa nacional y la soberanía estatal. Este marco se fundamenta en la Ley Federal N° 187-FZ ('Sobre la Seguridad de la Infraestructura de Información Crítica'), promulgada para blindar las redes esenciales de energía, transporte, banca, defensa, industria nuclear y química. Bajo la supervisión técnica del Servicio Federal de Control Técnico y de Exportaciones (FSTEC) y el Centro Nacional de Coordinación de Incidentes Informáticos (NKTsKI, adscrito al FSB), el modelo impone una estructura de comando altamente centralizada.

El componente operacional distintivo del esquema ruso es el sistema estatal GosSOPKA (ГосСОПКА). Todos los operadores de importancia vital están obligados a integrar sus centros de monitoreo con esta plataforma centralizada para alimentar la detección y mitigación de ciberataques a escala nacional en tiempo real. Este modelo se articula con la estrategia del 'Runet Soberano' (Ley N° 90-FZ) y decretos presidenciales de sustitución obligatoria de importaciones, que exigen a las organizaciones estratégicas migrar de plataformas occidentales hacia hardware, sistemas operativos rusos certificados (Astra Linux) y algoritmos criptográficos propios homologados bajo estándares GOST.

---

## Conceptos Core

* **Federal Law No. 187-FZ (Федеральный закон № 187-ФЗ):** Marco legal que clasifica los objetos de infraestructura crítica en tres categorías de significancia según su impacto potencial en la defensa y economía.
* **GosSOPKA System (ГосСОПКА):** Sistema Estatal para la Detección, Prevención y Eliminación de Consecuencias de Ataques Informáticos contra los recursos informáticos de la Federación Rusa.
* **Import Substitution (Импортозамещение):** Mandato estatal que prohíbe el uso de software, firmware y hardware extranjeros en infraestructuras críticas, forzando la adopción de tecnología rusa certificada.
* **GOST Cryptography Standards (Криптография ГОСТ):** Conjunto de algoritmos criptográficos oficiales y asimétricos aprobados por el FSB para la firma digital y cifrado en redes de infraestructura estratégica.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [Ley Federal N° 187-FZ 'Sobre la Seguridad de la Infraestructura de Información Crítica'](http://pravo.gov.ru): Texto legal oficial que norma los deberes de categorización técnica, seguridad informática y reporte obligatorio de incidentes.
* [Orden FSTEC N° 239: Requisitos de Seguridad de la Información para Sistemas de Control en CII](https://fstec.ru): Norma técnica que especifica los controles de hardware, software y segmentación para PLCs y servidores de infraestructura crítica.
* [GOST R 57580.1-2017: Seguridad de Operaciones Financieras y Transacciones Críticas](https://www.gost.ru/): Estándar nacional de seguridad de la información para el sector bancario y financiero ruso.
* [Ley Federal N° 90-FZ 'Sobre el Internet Soberano' (Runet)](http://pravo.gov.ru): Marco legislativo que establece la infraestructura técnica necesaria para aislar el tráfico de internet ruso de los servidores raíz internacionales en caso de desconexión externa.

### Papers y Literatura de Frontera
* **Center for Strategic and International Studies (CSIS, 2022):** *Russian Cyber Warfare Doctrine, Critical Infrastructure Defense, and Sovereign Networks* ([CSIS](https://www.csis.org/analysis/russian-cyber-warfare)) — Estudio sobre la arquitectura de GosSOPKA y su relación con las capacidades ofensivas y defensivas del Estado ruso.
* **Chatham House (2021):** *The Sovereign Internet Law and the Architecture of GosSOPKA: Security through Isolation* ([Chatham House](https://www.chathamhouse.org/)) — Investigación sobre los desafíos técnicos y de gobernanza de la sustitución tecnológica y el enrutamiento autónomo nacional.

### Repositorios y Herramientas (Open Source)
* [Suricata IDS/IPS Engine](https://github.com/OISF/suricata): Motor de detección de intrusiones de código abierto ampliamente utilizado como componente de sensores de red distribuidos en centros de GosSOPKA.
* [Greenbone Vulnerability Management (OpenVAS)](https://github.com/greenbone/gvmd): Suite de análisis de vulnerabilidades open source adoptada para auditorías internas de cumplimiento de la orden FSTEC 239.
* [MISP GosSOPKA Connectors](https://github.com/MISP): Módulos comunitarios para formatear y reenviar indicadores de compromiso conforme a los esquemas de telemetría requeridos por el NKTsKI.
* [Wazuh FSTEC Compliance Mapping](https://github.com/wazuh/wazuh): Reglas de telemetría de endpoints mapeadas a los requisitos de integridad de archivos y auditoría de accesos de la normativa 187-FZ.

### Ruta de Aprendizaje Autónoma
* [European University Institute: Cyber Resilience, Sovereignty and Post-Soviet Geopolitics](https://www.eui.eu): Módulos académicos abiertos sobre gobernanza de internet soberano, diplomacia de ciberdefensa y marcos de seguridad euroasiáticos.
* [TryHackMe: Threat Hunting State-Sponsored Actors (Sandworm, APT28/29)](https://tryhackme.com/module/threat-hunting): Laboratorios interactivos para analizar las tácticas, herramientas (BlackEnergy, Industroyer) y telemetría de actores avanzados de la región.
* [SANS Reading Room: National CERT and Incident Response Architectures](https://www.sans.org/white-papers/): Documentación técnica sobre la coordinación centralizada de CSIRTs nacionales e intercambio de alertas críticas.
* [Coursera / Stanford: International Security in a Changing World](https://www.coursera.org): Análisis sobre doctrinas militares de disuasión cibernética, ciberguerra y soberanía de infraestructura crítica.

---

## Enlace al Audio

[▶️ Escuchar Podcast Resumen](../../assets/audio/intl_03_rusia.mp3)

---

[⬅️ Lección Anterior](02-china-cii-cac.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Fin de Malla 🏁](../../README.md)
