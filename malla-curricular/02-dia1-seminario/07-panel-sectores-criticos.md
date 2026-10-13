# Protegiendo lo Esencial: Ciberseguridad y Resiliencia en Sectores Críticos - Panel Multisectorial (Codelco, CEN, Aguas Andinas, CSIRT)

## Síntesis Ejecutiva

La defensa técnica de los pilares productivos del país (minería de gran escala, despacho eléctrico interconectado, distribución de agua potable y coordinación gubernamental) expone la tensión estructural existente entre las tecnologías de la información (TI) y las tecnologías operativas (TO). En los entornos industriales, el paradigma tradicional de confidencialidad cede el paso a la supremacía absoluta de la disponibilidad y la seguridad física (Safety). Los controladores lógicos programables (PLC) y las unidades terminales remotas (RTU) ejecutan procesos continuos de alta presión que no toleran reinicios aleatorios ni ventanas intempestivas para la aplicación de parches.

Los líderes de la industria subrayan que los grupos de ciberdelincuencia y los agentes patrocinados por estados hostiles actúan con un pragmatismo oportunista: buscan la vía de menor resistencia técnica para interrumpir el servicio. Frente a este escenario, la cooperación multisectorial y el intercambio en tiempo real de Indicadores de Compromiso (IoCs) a través del CSIRT Nacional constituyen la barrera defensiva más eficaz. La verdadera resiliencia no reside únicamente en la capacidad de resistir intrusiones, sino en garantizar planes de maniobra analógica y procedimientos de contingencia degradada que permitan operar manualmente ante la caída total de los sistemas informáticos.

---

## Conceptos Core

* **IT/OT Convergence & Purdue Model:** Integración de redes corporativas con sistemas de control industrial, requiriendo segmentación jerárquica estricta (Nivel 0 a Nivel 5) para aislar actuadores físicos.
* **Operational Technology (OT) Safety Supremacy:** Filosofía de diseño industrial donde la protección de la vida humana y la integridad física de las instalaciones priman sobre la confidencialidad de la información.
* **Degraded Mode Operations (Analog Fallback):** Capacidad operacional entrenada de una central eléctrica o planta hidráulica para operar con mandos manuales mecánicos durante un apagón cibernético prolongado.
* **Cross-Sector Threat Sharing:** Protocolos automatizados de inteligencia compartida donde una amenaza detectada en una minera blinda preventivamente al sector energético y sanitario.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [ISA/IEC 62443 Series: Security for Industrial Automation and Control Systems](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa62443): Estándar de oro global que define la arquitectura por zonas y conductos (Zones and Conduits) para redes de control industrial.
* [NERC CIP (Critical Infrastructure Protection Standards)](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx): Marco regulatorio obligatorio en Norteamérica para la ciberseguridad del sistema eléctrico de potencia interconectado.
* [NIST SP 800-82 Rev. 3: Guide to Operational Technology (OT) Security](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final): Directrices técnicas del NIST sobre mitigación de amenazas en sistemas SCADA, DCS y PLCs.
* [Marco Sectorial de Ciberseguridad del Coordinador Eléctrico Nacional](https://www.coordinador.cl): Normativa técnica y estándares de reporte de incidentes para el Sistema Eléctrico Nacional chileno.

### Papers y Literatura de Frontera
* **IEEE Transactions on Smart Grid (2022):** *Cyber-Physical Resilience in Power Grids: Detection, Mitigation, and Restoration* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9779342)) — Modelado de dinámicas de red eléctrica frente a ataques coordinados de deslastre de carga por compromiso de RTUs.
* **Reliability Engineering & System Safety (2021):** *Modeling Cross-Sector Cascading Failures in Coupled Critical Infrastructures* ([DOI: 10.1016/j.ress.2021.107693](https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety)) — Análisis estocástico sobre cómo un fallo en telecomunicaciones o agua interrumpe operaciones de minería y generación termoeléctrica.

### Repositorios y Herramientas (Open Source)
* [Malcolm (CISA & Idaho National Laboratory)](https://github.com/cisagov/Malcolm): Suite de análisis de tráfico de red de código abierto orientada a protocolos industriales (Modbus, DNP3, EtherNet/IP) basada en Zeek y Suricata.
* [GRASSMARLIN (National Security Agency)](https://github.com/iadgov/grassmarlin): Herramienta de la NSA para mapeo pasivo de topologías de red en sistemas de control industrial y detección de violaciones al modelo Purdue.
* [OpenPLC Project](https://github.com/thiagoralves/OpenPLC_v3): Plataforma de controlador lógico programable open source compatible con estándar IEC 61131-3, ideal para investigación y simulación defensiva.
* [ScadaBR](https://github.com/ScadaBR/ScadaBR): Software de código abierto para supervisión y adquisición de datos (SCADA) utilizado para pruebas de laboratorio y monitoreo de procesos.

### Ruta de Aprendizaje Autónoma
* [CISA ICS-CERT Virtual Learning Courses (101 & 201)](https://www.cisa.gov/ics-training-available-through-cisa): Cursos oficiales gratuitos con acreditación sobre arquitecturas de ciberdefensa en infraestructuras de control industrial.
* [SANS Industrial Cybersecurity Community Curriculum](https://www.sans.org/cyber-security-courses/ics-scada-cyber-security-essentials/): Whitepapers, hojas de trucos y talleres abiertos sobre defensa de plantas eléctricas y acueductos.
* [TryHackMe: Industrial Control Systems Room](https://tryhackme.com/module/defensive-security): Laboratorio interactivo para explorar el modelo Purdue, descifrar tramas Modbus y mitigar inyecciones maliciosas de comandos PLC.
* [Cisco NetAcad: OT Network Architecture & Industrial Switching](https://www.netacad.com): Especialización técnica en despliegue de switches industriales resistentes y microsegmentación de subestaciones.

---

## Enlace al Audio

[▶️ Escuchar Podcast Resumen](../../assets/audio/dia1_07_panel_multisectorial.mp3)

---

[⬅️ Lección Anterior](06-fernandez-dispositivos-medicos.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](08-bonnaire-agentes-ia.md)
