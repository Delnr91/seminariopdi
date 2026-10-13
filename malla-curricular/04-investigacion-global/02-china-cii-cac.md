# Reglamento de Infraestructura de Información Crítica (CII 2021) y Soberanía de Datos - Administración del Ciberespacio de China (CAC)

## Síntesis Ejecutiva

El modelo de seguridad digital de la República Popular China se rige bajo una doctrina de 'Soberanía Digital Absoluta' y control estatal centralizado de los flujos de información. Este esquema tiene como eje vinculante el Reglamento de Protección de Seguridad de Infraestructuras de Información Crítica (Reglamento CII, Decreto N° 745 del Consejo de Estado de 2021), complementado por la Ley de Ciberseguridad (2017), la Ley de Seguridad de Datos (2021) y la Ley de Protección de Información Personal (PIPL). Para Beijing, las redes que operan la energía, las telecomunicaciones, el transporte, las finanzas y los servicios gubernamentales son extensiones territoriales de la seguridad nacional.

El marco chino destaca por imponer estrictos requisitos de localización de datos dentro de sus fronteras y severas restricciones a la transferencia transfronteriza de información corporativa y científica. A través del Esquema de Protección de Seguridad Multi-Nivel (MLPS 2.0 / 等保2.0), supervisado por el Ministerio de Seguridad Pública (MPS), los operadores de infraestructura crítica de nivel 3 o superior están legalmente obligados a adquirir productos y servicios de red previamente auditados por revisiones de seguridad nacional de la CAC. Esta política busca descartar puertas traseras externas y acelerar la sustitución tecnológica por componentes de desarrollo nacional independiente.

---

## Conceptos Core

* **Cyber Sovereignty (网络主权):** Doctrina jurídica y política que sostiene el derecho inalienable de cada Estado a regular, supervisar y controlar su ciberespacio nacional sin injerencia extranjera.
* **Critical Information Infrastructure Regulations (CII - 关键信息基础设施):** Normativa estricta que define sectores protegidos y responsabilidades legales directas para los directivos encargados de su operación.
* **Multi-Level Protection Scheme 2.0 (MLPS 2.0 / 等级保护):** Sistema de categorización obligatoria (Niveles 1 al 5) que fija los controles técnicos, de red y de criptografía nacional exigidos a cada sistema informático.
* **Data Localization & National Security Reviews:** Obligación de almacenar datos importantes y personales dentro de China y someter software y hardware extranjero a auditorías antes de su implementación.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [Reglamento de Protección de Seguridad de Infraestructuras de Información Crítica (Decreto N° 745 del Consejo de Estado)](http://www.cac.gov.cn): Texto legal oficial que regula las obligaciones de auditoría anual y reporte de incidentes para operadores críticos.
* [Estándar Nacional GB/T 22239-2019: Requisitos de Seguridad de la Información para MLPS 2.0](http://www.tc260.org.cn): Estándar técnico obligatorio que desglosa los controles de seguridad física, de red, de host y de datos según el nivel clasificado.
* [Ley de Seguridad de Datos de la República Popular China (2021)](http://www.npc.gov.cn/): Legislación que categoriza los datos en 'Datos Centrales del Estado' y 'Datos Importantes', penalizando su filtración al exterior.
* [Ley de Ciberseguridad de la República Popular China (2017)](http://www.cac.gov.cn): Pilar normativo fundacional que inauguró el marco de soberanía y auditorías obligatorias a operadores de red.

### Papers y Literatura de Frontera
* **Harvard Belfer Center (2021):** *China's Cyber Power and the Governance of Critical Information Infrastructure* ([Belfer Center](https://www.belfercenter.org/publication/chinas-cyber-power)) — Análisis detallado sobre la arquitectura de supervisión de la CAC y el impacto del desacoplamiento tecnológico en la cadena de suministro.
* **Georgetown CSET (2022):** *China's Cyber Law Landscape: Standards, Supply Chains, and National Security* ([Center for Security and Emerging Technology](https://cset.georgetown.edu/)) — Desglose de los estándares técnicos del comité TC260 y su aplicación en auditorías a proveedores tecnológicos extranjeros.

### Repositorios y Herramientas (Open Source)
* [Wazuh MLPS Configuration Profiles](https://github.com/wazuh/wazuh): Conjunto de reglas y perfiles comunitarios para auditar sistemas operativos Linux frente a los requerimientos del estándar MLPS 2.0.
* [CNVD (China National Vulnerability Database Telemetry Monitor)](https://www.cnvd.org.cn/): Base de datos nacional de vulnerabilidades de China, referencia para la catalogación de fallas en software operativo en el mercado asiático.
* [OpenSCAP Chinese National Profile Rulesets](https://github.com/OpenSCAP/scap-security-guide): Plantillas de endurecimiento de sistemas para evaluar configuraciones de cumplimiento normativo en entornos corporativos globales.
* [Suricata IDS/IPS Engine](https://github.com/OISF/suricata): Motor de inspección profunda de paquetes adoptado ampliamente para la implementación de sensores de borde y monitoreo de tráfico perimetral.

### Ruta de Aprendizaje Autónoma
* [Stanford University DigiChina Project: Comprehensive Regulatory Translations & Analysis](https://digichina.stanford.edu/): Proyecto de la Universidad de Stanford con traducciones oficiales y análisis profundos de toda la legislación digital y de ciberseguridad china.
* [ISO/IEC 27001 Cross-Walk to Chinese Cybersecurity Standards Guide](https://www.iso.org): Recursos comparativos sobre cómo las multinacionales homologan sus controles occidentales con las exigencias del MLPS 2.0.
* [TryHackMe: Global Compliance, Governance & Data Sovereignty](https://tryhackme.com/module/security-operations): Módulos sobre adaptación de políticas de seguridad a marcos normativos multinacionales y control de transferencias de datos.
* [Coursera / Tsinghua University: Chinese Law and Society in the Digital Age](https://www.coursera.org): Análisis sobre el marco institucional, soberanía jurídica y gobernanza de la tecnología en el gigante asiático.

---

## Enlace al Audio

[▶️ Escuchar Podcast Resumen](../../assets/audio/intl_02_china.mp3)

---

[⬅️ Lección Anterior](01-nist-cisa-ncsc.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](03-rusia-187fz-fstec.md)
