# Conceptos Fundamentales: Infraestructura Crítica y Ciberresiliencia - Arquitectura Lattices

## Síntesis Ejecutiva

La infraestructura crítica representa el entramado físico y computacional sobre el cual descansa el funcionamiento de la civilización moderna: redes de generación y despacho eléctrico, matrices de tratamiento y distribución de agua potable, servicios de transporte masivo, sistemas financieros y la columna vertebral de telecomunicaciones e Internet. La digitalización masiva y la interconexión de sistemas de control industrial (ICS/SCADA) con plataformas corporativas ha generado una superficie de ataque continua donde una falla inducida en el dominio lógico tiene consecuencias destructivas inmediatas sobre el dominio físico.

La ciberresiliencia trasciende la noción clásica de ciberseguridad defensiva basada en la ilusión de la invulnerabilidad perimetral. En el contexto operacional contemporáneo, la resiliencia se define como la capacidad arquitectónica de una organización para absorber un impacto severo o una brecha confirmada, contener la propagación lateral del compromiso, mantener los servicios esenciales en modo degradado o analógico y restaurar la operación completa con rapidez y rigor forense.

---

## Conceptos Core

* **Infraestructura Crítica (Critical Infrastructure):** Redes, servicios y activos vitales cuya interrupción prolongada provocaría un colapso en la seguridad nacional, la salud pública o la economía de un país.
* **Ciberresiliencia Operacional:** Capacidad proactiva y probada para anticipar, resistir, recuperarse y evolucionar ante condiciones adversas, estrés o ataques cibernéticos deliberados.
* **Modelo Purdue (Purdue Enterprise Reference Architecture - PERA):** Modelo jerárquico clásico de segmentación en redes industriales que separa los niveles de procesos físicos (Nivel 0/1/2) de los niveles de supervisión empresarial y conectividad IT (Nivel 3/4/5).
* **Convergencia IT/OT:** Desafío arquitectónico derivado de unir las tecnologías de la información empresariales (centradas en la confidencialidad de datos) con las tecnologías de operación industrial (centradas en la disponibilidad, tiempo real y seguridad física humana).

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [NIST SP 800-82 Rev. 3: Guide to Operational Technology (OT) Security](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final): Manual de referencia de estándares de seguridad en sistemas de control y supervisión industrial.
* [ISA/IEC 62443: Security for Industrial Automation and Control Systems](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa62443): Estándar internacional por excelencia para la definición de zonas, conductos y niveles de seguridad (SL-1 a SL-4).
* [CISA Critical Infrastructure Sectors Overview](https://www.cisa.gov/topics/critical-infrastructure-sectors): Mapeo oficial de los 16 sectores de infraestructura crítica definidos por el gobierno de Estados Unidos.

### Papers y Literatura de Frontera
* **IEEE Transactions on Industrial Informatics (2021):** *Cyber-Physical Security in Industrial Control Systems: A Survey of Architectures and Mitigation Models* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9354921)).
* **ACM Digital Threats (2020):** *Resilience by Design: Analyzing the Evolution of SCADA Systems under Adversarial Pressure* ([ACM DTRAP](https://dl.acm.org/journal/dtrap)).

### Repositorios y Herramientas (Open Source)
* [Malcolm Network Traffic Analysis](https://github.com/cisagov/Malcolm): Suite de observabilidad y análisis profundo de paquetes para protocolos de control industrial.
* [GRASSMARLIN](https://github.com/iadgov/grassmarlin): Herramienta de mapeo pasivo de redes OT desarrollada por la NSA.
* [OpenPLC Project](https://github.com/thiagoralves/OpenPLC_v3): Simulador y software PLC de código abierto para investigación de control físico.

### Ruta de Aprendizaje Autónoma
* [CISA Virtual Learning: ICS Cybersecurity Fundamentals (101)](https://www.cisa.gov/ics-training-available-through-cisa): Módulos oficiales gratuitos sobre fundamentos de control industrial.
* [SANS Industrial Cybersecurity Whitepaper Library](https://www.sans.org/white-papers/): Repositorio abierto de documentos técnicos y guías de defensa en profundidad.
* [TryHackMe: Intro to ICS & SCADA](https://tryhackme.com/module/defensive-security): Laboratorio interactivo para comprender las bases del modelo Purdue.

---

[🏠 Volver a la Malla Curricular](../../README.md) | [Comenzar Día 1: Charla 01 (Marcelo Wong Cea) ➡️](../02-dia1-seminario/01-wong-ia-cibercrimen.md)
