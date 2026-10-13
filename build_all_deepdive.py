import os
import json

# Directorio raíz del proyecto
BASE_DIR = "/home/dani/proyectos/seminario-pdi"

def format_markdown(lesson):
    title = lesson["title"]
    sintesis = lesson["sintesis"].strip()
    audio = lesson["audio"]
    
    conceptos_str = "\n".join([f"* {c}" for c in lesson["conceptos"]])
    frameworks_str = "\n".join([f"* {f}" for f in lesson["frameworks"]])
    papers_str = "\n".join([f"* {p}" for p in lesson["papers"]])
    tools_str = "\n".join([f"* {t}" for t in lesson["tools"]])
    learning_str = "\n".join([f"* {l}" for l in lesson["learning"]])
    
    # Barra de navegación
    prev_link = f"[⬅️ Lección Anterior]({lesson['prev']})" if lesson.get("prev") else "[⬅️ Inicio de Malla](../../README.md)"
    next_link = f"[Siguiente Lección ➡️]({lesson['next']})" if lesson.get("next") else "[Fin de Malla 🏁](../../README.md)"
    nav_bar = f"---\n\n{prev_link} | [🏠 Volver a la Malla Curricular](../../README.md) | {next_link}\n"
    
    md_content = f"""# {title}

## Síntesis Ejecutiva

{sintesis}

---

## Conceptos Core

{conceptos_str}

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
{frameworks_str}

### Papers y Literatura de Frontera
{papers_str}

### Repositorios y Herramientas (Open Source)
{tools_str}

### Ruta de Aprendizaje Autónoma
{learning_str}

---

## Enlace al Audio

[▶️ Escuchar Podcast Resumen]({audio})

{nav_bar}"""
    return md_content

# Cargar las lecciones definidas
from build_deepdive_part1 import lessons_data

# Añadimos las lecciones restantes (Día 2 e Internacionales)
lessons_dia2_and_intl = [
    # --- DIA 2 ---
    {
        "path": "malla-curricular/03-dia2-seminario/01-caceres-blue-team-ia.md",
        "title": "Blue Team Aumentado por Inteligencia Artificial: Modelos de Ciberdefensa y Resiliencia para Infraestructuras Críticas - Diego Cáceres",
        "audio": "../../assets/audio/dia2_01_caceres.mp3",
        "prev": "../02-dia1-seminario/09-evirtus-zero-trust.md",
        "next": "02-fuentes-threat-intelligence.md",
        "sintesis": (
            "Los Centros de Operaciones de Ciberseguridad (SOC) modernos enfrentan una crisis estructural de fatiga de alertas generada por la ingestion continua de millones de eventos por segundo en redes de infraestructura crítica. La dispersión de telemetría y el alto volumen de falsos positivos desbordan la capacidad cognitiva de los analistas del Blue Team, provocando demoras críticas en el tiempo medio de detección (MTTD) e identificación de anomalías sutiles asociadas a campañas de intrusión avanzadas.\n\n"
            "La integración de modelos de aprendizaje automático y agentes autónomos defensivos transforma radicalmente esta dinámica operacional, evolucionando el SOC reactivo hacia arquitecturas A-SOC (AI-Augmented SOC). Mediante la correlación probabilística en tiempo real y la orquestación automatizada de respuestas (SOAR), los equipos defensores pueden contener endpoints comprometidos, revocar credenciales filtradas y aislar subredes industriales en milisegundos, blindando la continuidad del servicio ante adversarios que operan a velocidad de máquina."
        ),
        "conceptos": [
            "**AI-Augmented Security Operations Center (A-SOC):** Centro de defensa digital potenciado por modelos analíticos para la priorización inteligente de alertas y reducción de ruido operacional.",
            "**Security Orchestration, Automation, and Response (SOAR):** Plataforma que ejecuta libros de jugadas (playbooks) preprogramados para contener ataques automáticamente sin esperar intervención manual.",
            "**Mean Time to Detect (MTTD) & Contain (MTTC):** Métricas clave de rendimiento operativo en ciberdefensa que miden la rapidez para identificar y neutralizar una intrusión.",
            "**Unsupervised Anomaly Detection:** Algoritmos de clustering que modelan la línea base del comportamiento normal de la red para detectar desviaciones anómalas sin depender de firmas conocidas."
        ],
        "frameworks": [
            "[MITRE D3FEND: A Knowledge Graph of Cybersecurity Countermeasures](https://d3fend.mitre.org/): Matriz complementaria a ATT&CK desarrollada por NSA y MITRE que cataloga técnicas defensivas de ingeniería y respuesta.",
            "[NIST SP 800-137: Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/publications/detail/sp/800-137/final): Marco técnico del NIST para el monitoreo continuo de la postura de seguridad operacional.",
            "[CISA Automated Indicator Sharing (AIS)](https://www.cisa.gov/resources-tools/programs/automated-indicator-sharing): Ecosistema para el intercambio bidireccional en tiempo real de indicadores de compromiso entre gobierno e industrias.",
            "[ISO/IEC 27035 Series: Information Security Incident Management](https://www.iso.org/standard/60803.html): Estándar internacional para planificar, detectar, responder y aprender de incidentes de seguridad."
        ],
        "papers": [
            "**IEEE Transactions on Information Forensics and Security (2022):** *Machine Learning for Security Operations Centers: Alert Triage, Prioritization, and Explainability* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9681421)) — Modelado empírico de redes neuronales aplicadas a la reducción del 90% de falsos positivos en SOCs corporativos.",
            "**Computers & Security (2021):** *Automating Incident Response in Critical Infrastructures: A Comparative Evaluation of SOAR Architectures* ([DOI: 10.1016/j.cose.2021.102340](https://www.sciencedirect.com/journal/computers-and-security)) — Análisis sobre latencia y resiliencia en la ejecución de playbooks automáticos en plantas de energía."
        ],
        "tools": [
            "[Shuffle (Open Source SOAR)](https://github.com/Shuffle/Shuffle): Plataforma de orquestación y automatización de seguridad de código abierto orientada a flujos de trabajo en equipos Blue Team.",
            "[Wazuh (Open Source XDR & SIEM)](https://github.com/wazuh/wazuh): Solución open source enterprise para monitoreo de seguridad, detección de amenazas, integridad de archivos y respuesta en endpoints.",
            "[Sigma Rules Repository](https://github.com/SigmaHQ/sigma): Formato de firma genérico y abierto para describir eventos de registro relevantes de forma independiente del SIEM utilizado.",
            "[Velociraptor (DFIR Endpoint Visibility)](https://github.com/Velocidex/velociraptor): Herramienta avanzada para recolección forense digital y cacería de amenazas distribuida en miles de equipos en vivo."
        ],
        "learning": [
            "[TryHackMe: SOC Level 1 & Level 2 Career Paths](https://tryhackme.com/path/outline/soclevel1): Ruta de formación interactiva que entrena en análisis de logs, uso de SIEM (Splunk/ELK) y respuesta a incidentes en tiempo real.",
            "[Microsoft Learn: Creación de Reglas Analíticas y Automatización con Microsoft Sentinel](https://learn.microsoft.com/es-es/training/modules/configure-microsoft-sentinel-rules/): Laboratorios oficiales sobre automatización de incidentes y uso de Kusto Query Language (KQL).",
            "[HackTheBox: Blue Team Sherlocks & Defensive Modules](https://www.hackthebox.com): Desafíos forenses reales para investigar capturas de memoria RAM, tráfico malicioso y persistencia de atacantes.",
            "[Cisco NetAcad: CyberOps Associate Certification](https://www.netacad.com): Curso profesional sobre operaciones defensivas, análisis de alertas y monitoreo de infraestructura crítica."
        ]
    },
    {
        "path": "malla-curricular/03-dia2-seminario/02-fuentes-threat-intelligence.md",
        "title": "Cyber Threat Intelligence (CTI) - Omar Fuentes",
        "audio": "../../assets/audio/dia2_02_fuentes.mp3",
        "prev": "01-caceres-blue-team-ia.md",
        "next": "03-cordero-resiliencia-hardware.md",
        "sintesis": (
            "La Inteligencia de Ciberamenazas (CTI) constituye el eje estratégico que transforma la ciberdefensa de una postura reactiva y genérica a una disciplina de anticipación analítica informada. En un contexto donde los actores de amenazas avanzadas persistentes (APTs) diseñan ataques específicos adaptados a cada industria, proteger todos los activos por igual resulta inviable. La CTI recolecta, refina y correlaciona datos de fuentes abiertas (OSINT), foros clandestinos (Dark Web) y telemetría global para desarticular las ventajas asimétricas del atacante.\n\n"
            "La efectividad de la CTI radica en su capacidad de articular tres niveles de decisión: estratégico (para directores y toma de decisiones presupuestarias), operacional (para planificadores de seguridad y arquitectos) y táctico (indicadores de compromiso y firmas para firewalls y EDRs). Al mapear los procedimientos del adversario mediante el modelo Diamond y marcos de referencia globales, las organizaciones pueden anticipar qué puertas intentará forzar el enemigo, fortaleciendo proactivamente sus controles defensivos antes del impacto."
        ),
        "conceptos": [
            "**Diamond Model of Intrusion Analysis:** Metodología que vincula cuatro elementos centrales de cada actividad maliciosa: Adversario, Capacidad, Infraestructura y Víctima.",
            "**Pyramid of Pain (David Bianco):** Concepto que jerarquiza el grado de dificultad que se le impone al atacante al bloquear sus recursos (desde valores Hash fáciles de cambiar hasta TTPs complejas).",
            "**Actionable Threat Intelligence:** Datos refinados y contextualizados que ofrecen la información precisa necesaria para que un defensor tome una decisión operativa inmediata.",
            "**TTPs (Tactics, Techniques, and Procedures):** Patrones de comportamiento, herramientas y métodos característicos que identifican y distinguen a un grupo de cibercrimen o actor patrocinado por un Estado."
        ],
        "frameworks": [
            "[OASIS STIX 2.1 & TAXII Standards](https://oasis-open.github.io/cti-documentation/): Estándares internacionales abiertos para la representación estructurada y transporte automatizado de inteligencia de ciberamenazas.",
            "[MITRE ATT&CK Matrix for Enterprise](https://attack.mitre.org/): Taxonomía universal que clasifica y documenta las fases operativas de adversarios digitales en entornos empresariales.",
            "[NIST SP 800-150: Guide to Cyber Threat Information Sharing](https://csrc.nist.gov/publications/detail/sp/800-150/final): Directrices técnicas para formalizar acuerdos y plataformas de intercambio de inteligencia entre pares del sector.",
            "[Traffic Light Protocol (TLP 2.0 - FIRST)](https://www.first.org/tlp/): Estándar internacional que norma la clasificación y compartición segura de información sensible (TLP:RED, AMBER, GREEN, CLEAR)."
        ],
        "papers": [
            "**IEEE Security & Privacy (2021):** *Measuring and Improving the Actionability of Cyber Threat Intelligence Feeds* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9444459)) — Estudio cuantitativo sobre la redundancia, frescura y efectividad real de los feeds comerciales y abiertos de IoCs.",
            "**Journal of Cybersecurity (Oxford, 2020):** *Adversary Modeling, Attribution, and the Cyber Threat Intelligence Process* ([Oxford Academic](https://academic.oup.com/cybersecurity/article/6/1/tyaa016/5923053)) — Análisis riguroso sobre las dificultades técnicas y sesgos metodológicos en la atribución formal de ciberataques."
        ],
        "tools": [
            "[OpenCTI (Open Cyber Threat Intelligence)](https://github.com/OpenCTI-Platform/opencti): Plataforma enterprise de código abierto para gestionar relaciones de conocimiento de amenazas y actores APT compatible con STIX2.",
            "[MISP (Malware Information Sharing Platform)](https://github.com/MISP/MISP): Software de código abierto líder a nivel gubernamental y corporativo para compartir telemetría de ciberseguridad.",
            "[YARA (The Pattern Matching Swiss Army Knife)](https://github.com/VirusTotal/yara): Herramienta estándar de la industria desarrollada por VirusTotal para clasificar e identificar familias de malware según patrones.",
            "[AlienVault OTX Python SDK](https://github.com/AlienVault-OTX/OTX-Python-SDK): Biblioteca para conectar de forma automatizada aplicaciones de seguridad con la base comunitaria global de Open Threat Exchange."
        ],
        "learning": [
            "[Mandiant / Google Cloud: Threat Intelligence Fundamentals](https://cloud.google.com/security/products/threat-intelligence): Cursos y whitepapers de nivel enterprise sobre modelado del adversario e investigación de actores hostiles globales.",
            "[TryHackMe: Cyber Threat Intelligence Path](https://tryhackme.com/path/outline/cyber-threat-intelligence): Laboratorios interactivos para analizar reportes CTI, construir reglas YARA y mapear campañas contra MITRE ATT&CK.",
            "[SANS CTI Summit Open Archive](https://www.sans.org/cyber-security-summits/cyber-threat-intelligence-summit/): Grabaciones magistrales y diapositivas de las investigaciones más avanzadas presentadas en la cumbre mundial de CTI.",
            "[Cisco NetAcad: Threat Hunting & Intelligence Operations](https://www.netacad.com): Formación estructurada sobre correlación de alertas y utilización de marcos de inteligencia para defensas preventivas."
        ]
    },
    {
        "path": "malla-curricular/03-dia2-seminario/03-cordero-resiliencia-hardware.md",
        "title": "El Rol de la Tecnología en la Continuidad y Resiliencia Operacional - César Cordero",
        "audio": "../../assets/audio/dia2_03_cordero.mp3",
        "prev": "02-fuentes-threat-intelligence.md",
        "next": "04-alli-salud-ciberseguridad.md",
        "sintesis": (
            "La seguridad por debajo del sistema operativo representa la frontera más crítica e invisible de la ciberresiliencia corporativa. Durante décadas, los modelos de defensa se concentraron en proteger capas superiores (aplicaciones, redes y sistemas operativos), ignorando la superficie física de arranque: la memoria BIOS, el firmware del controlador de gestión de placa base (BMC) y los microcódigos de los procesadores. Si un actor sofisticado compromete estas capas profundas mediante un bootkit o implante físico, obtiene persistencia absoluta, invisibilidad frente a soluciones EDR y control total e irreversible del activo.\n\n"
            "César Cordero destaca que la continuidad operacional exige blindar la cadena de suministro desde la manufactura del silicio. La incorporación de raíces de confianza basadas en hardware (Hardware Root of Trust), módulos criptográficos discretos (TPM 2.0) y estándares de resiliencia de firmware de plataforma (NIST SP 800-193) permite a las máquinas verificar criptográficamente cada línea de código antes de su ejecución. Ante un desastre o sabotaje físico, contar con arquitecturas de auto-recuperación y replicación en la nube garantiza el restablecimiento de puestos de trabajo operativos en cuestión de minutos."
        ),
        "conceptos": [
            "**Hardware Root of Trust (HRoT):** Módulo o componente de silicio inmutable que almacena claves criptográficas maestras y ejecuta la validación inicial del arranque del sistema.",
            "**Platform Firmware Resiliency (PFR):** Capacidad del hardware para proteger la integridad del firmware (Protection), detectar alteraciones maliciosas (Detection) y auto-restaurar una copia limpia (Recovery).",
            "**Trusted Platform Module (TPM 2.0):** Microchip criptográfico dedicado a almacenar claves de cifrado de disco (BitLocker), certificados de plataforma y medidas de estado del sistema (PCRs).",
            "**Baseboard Management Controller (BMC) Security:** Aseguramiento del procesador de servicio independiente que permite la administración remota fuera de banda de servidores empresariales."
        ],
        "frameworks": [
            "[NIST SP 800-193: Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/publications/detail/sp/800-193/final): Estándar técnico del NIST que define los mecanismos de protección, detección y recuperación para firmwares de servidores y terminales.",
            "[NIST SP 800-147: BIOS Protection Guidelines](https://csrc.nist.gov/publications/detail/sp/800-147/final): Principios para asegurar que las actualizaciones de BIOS sean criptográficamente autenticadas y no manipulables.",
            "[Trusted Computing Group (TCG) TPM 2.0 Library Specification](https://trustedcomputinggroup.org/resource/tpm-library-specification/): Especificación técnica internacional que norma la arquitectura y funciones criptográficas de los chips TPM.",
            "[ISO/IEC 11889 Series: Information Technology - Trusted Platform Module](https://www.iso.org/standard/66510.html): Estándar formal ISO que adopta la especificación del módulo de plataforma confiable."
        ],
        "papers": [
            "**IEEE Micro (2020):** *Hardware Roots of Trust: From Boot to Execution Security* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9079541)) — Análisis sobre arquitecturas de confianza desde la inicialización del procesador hasta entornos de ejecución confiables (TEE).",
            "**ACM Transactions on Computer Systems (2022):** *Firmware Vulnerability Landscapes: Measuring Supply-Chain Risks in Enterprise Compute Nodes* ([ACM Digital Library](https://dl.acm.org/journal/tocs)) — Estudio empírico sobre vulnerabilidades sin parchar en BMCs y controladores de interfaz de red."
        ],
        "tools": [
            "[CHIPSEC Platform Security Assessment Framework](https://github.com/chipsec/chipsec): Framework de código abierto desarrollado por Intel para analizar la seguridad de plataformas de hardware, chipsets y firmwares UEFI/BIOS.",
            "[Coreboot](https://github.com/coreboot/coreboot): Proyecto de firmware de código abierto de arranque rápido y auditable que reemplaza las BIOS privativas en servidores y laptops seguros.",
            "[UEFITool](https://github.com/LongSoft/UEFITool): Utilidad open source para inspeccionar, extraer y analizar componentes y módulos dentro de imágenes de firmware UEFI.",
            "[Flashrom](https://github.com/flashrom/flashrom): Utilidad multiplataforma para identificar, leer, escribir y verificar chips de memoria flash en placas base y tarjetas de red."
        ],
        "learning": [
            "[Intel Developer Zone: Platform Security Architecture Training](https://software.intel.com/content/www/us/en/develop/topics/security.html): Cursos y manuales de arquitectura sobre arranque seguro, Intel Boot Guard y memoria SGX.",
            "[Microsoft Learn: Arquitectura de Dispositivos Secured-Core PCs](https://learn.microsoft.com/es-es/windows-hardware/design/device-experiences/secured-core-pcs): Documentación técnica sobre integración de hardware de alta seguridad, protección de hypervisor y mitigación de DMA.",
            "[HackTheBox: Hardware & Reverse Engineering Modules](https://www.hackthebox.com): Prácticas de laboratorio sobre análisis de binarios de bajo nivel, volcado de memoria SPI y depuración con JTAG.",
            "[Coursera / University of Colorado Boulder: Embedded Systems Security](https://www.coursera.org): Especialización en aseguramiento de microcontroladores y cadenas de arranque criptográficas."
        ]
    },
    {
        "path": "malla-curricular/03-dia2-seminario/04-alli-salud-ciberseguridad.md",
        "title": "Ciberseguridad en Salud: Protegiendo la Infraestructura que Protege Vidas - Nina Alli",
        "audio": "../../assets/audio/dia2_04_alli.mp3",
        "prev": "03-cordero-resiliencia-hardware.md",
        "next": "05-albuquerque-deteccion-respuesta.md",
        "sintesis": (
            "La intersección entre la ciberseguridad y el ecosistema sanitario representa la manifestación más directa del impacto cibernético sobre la preservación de la vida humana. Cuando una organización de salud es paralizada por un ciberataque de ransomware, las métricas financieras y contables quedan en segundo plano: las ambulancias de emergencia deben desviarse a recintos a kilómetros de distancia, las terapias oncológicas se suspenden de emergencia y los cirujanos pierden acceso inmediato al historial farmacológico y alérgico de pacientes críticos en pabellón.\n\n"
            "Nina Alli, líder de Biohacking Village, apela a una profunda transformación ética y operativa en la gestión de la tecnología clínica. Superar las vulnerabilidades hospitalarias requiere desterrar la cultura punitiva y los tecnicismos intimidantes que alejan al personal de enfermería y facultativos médicos de la higiene digital. Se promueve una alianza simbiótica entre fabricantes de equipamiento clínico, administradores de salud y comunidades de hackers éticos para descubrir, reportar y parchar vulnerabilidades de forma coordinada, asegurando que la tecnología médica sea una aliada inexpugnable para salvar vidas."
        ),
        "conceptos": [
            "**Clinical Cyber-Physical Harm:** Consecuencias médicas directas (aumento de mortalidad o morbilidad) resultantes de la disrupción o manipulación de sistemas de información hospitalaria.",
            "**EHR (Electronic Health Record) Resilience:** Diseño de sistemas de registros clínicos con capacidad de alta disponibilidad, inmutabilidad de copias de seguridad y contingencia en papel.",
            "**Empathetic Digital Hygiene:** Enfoque pedagógico que adapta las mejores prácticas de seguridad a los flujos reales de atención clínica sin sobrecargar al personal asistencial.",
            "**Medical Device Vulnerability Coordination (CVD):** Protocolos formalizados para que investigadores reporten fallas en dispositivos de soporte de vida a los fabricantes de manera segura y regulada."
        ],
        "frameworks": [
            "[Health Sector Coordinating Council (HSCC) Joint Security Plan (JSP)](https://healthsectorcouncil.org/): Marco de referencia de la industria sanitaria para la seguridad de dispositivos médicos en todo su ciclo de vida.",
            "[HIPAA Security Rule (U.S. Department of Health and Human Services)](https://www.hhs.gov/hipaa/for-professionals/security/index.html): Estándar legal y técnico que norma la protección, confidencialidad e integridad de datos médicos protegidos (ePHI).",
            "[ENISA Procurement Guidelines for Cybersecurity in Hospitals](https://www.enisa.europa.eu/publications/procurement-guidelines-for-cybersecurity-in-hospitals): Guía práctica de la agencia europea para evaluar la seguridad de sistemas médicos antes de su compra.",
            "[FDA Medical Device Cybersecurity Action Plan](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity): Plan de acción estratégico de la FDA para mejorar la vigilancia posterior al mercado y la seguridad del paciente."
        ],
        "papers": [
            "**The Lancet Digital Health (2023):** *The Impact of Ransomware Attacks on Health Care Systems: A Population-Based Clinical Study* ([The Lancet](https://www.thelancet.com/journals/landig/home)) — Investigación empírica que cuantifica el incremento en la tasa de complicaciones médicas durante apagones cibernéticos hospitalarios.",
            "**NEJM Catalyst (2021):** *Preparing Health Systems for Disruptive Cyber Incidents: Operational and Clinical Playbooks* ([NEJM](https://catalyst.nejm.org/)) — Directrices de liderazgo hospitalario para mantener la continuidad del cuidado médico durante caídas totales de sistemas informáticos."
        ],
        "tools": [
            "[CISA Healthcare Cybersecurity Assessment Toolkit](https://www.cisa.gov/topics/critical-infrastructure-sectors/healthcare-and-public-health): Conjunto de herramientas de evaluación de vulnerabilidades y madurez gratuitas diseñadas por CISA para hospitales y clínicas.",
            "[OpenEMR Platform](https://github.com/openemr/openemr): Sistema de registros médicos electrónicos de código abierto certificado por ONC, utilizado en entornos de prueba para simulación de incidentes y auditoría.",
            "[BloodHound Community Edition](https://github.com/SpecterOps/BloodHound): Herramienta utilizada por equipos de auditoría para mapear y eliminar rutas de escalamiento de privilegios en redes hospitalarias.",
            "[Wireshark (con Dissectores Médicos HL7/DICOM)](https://github.com/wireshark/wireshark): Herramienta fundamental para verificar el cifrado y detectar accesos no autorizados en flujos de telemedicina e imágenes médicas."
        ],
        "learning": [
            "[CISA Healthcare and Public Health (HPH) Sector Cybersecurity Training](https://www.cisa.gov/cyber-training): Cursos oficiales en línea para administradores de salud sobre gestión de riesgos y respuesta a incidentes clínicos.",
            "[HealthIT.gov Security Risk Assessment (SRA) Tool Guidance](https://www.healthit.gov/topic/privacy-security-and-hipaa/security-risk-assessment-tool): Recursos paso a paso para realizar autoevaluaciones de ciberseguridad en recintos de atención primaria.",
            "[Biohacking Village DEF CON Open Archives](https://www.villageb.io/): Charlas y talleres sobre diseño seguro de respiradores, marcapasos y estaciones de enfermería digital.",
            "[TryHackMe: Incident Response in Regulated Environments](https://tryhackme.com/module/incident-response): Laboratorios sobre protocolos de contención y preservación de evidencia forense en infraestructuras reguladas."
        ]
    },
    {
        "path": "malla-curricular/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md",
        "title": "Seguridad Digital: Prevención, Detección y Respuesta ante Ciberamenazas - Tales Albuquerque",
        "audio": "../../assets/audio/dia2_05_albuquerque.mp3",
        "prev": "04-alli-salud-ciberseguridad.md",
        "next": "06-norman-amenazas-hibridas.md",
        "sintesis": (
            "El mito del ciberataque instantáneo ha sido superado por la realidad forense de las intrusiones corporativas contemporáneas. En las campañas dirigidas contra infraestructuras críticas y grandes organizaciones, los adversarios suelen permanecer infiltrados durante semanas o meses dentro de la red corporativa (Dwell Time). Durante este intervalo de silencio táctico, los atacantes se dedican al reconocimiento pasivo, mapeo de relaciones de confianza, escalamiento de privilegios y neutralización metódica de los repositorios de respaldo antes de desplegar el payload de cifrado masivo.\n\n"
            "Tales Albuquerque resalta que los atacantes modernos eluden los antivirus tradicionales explotando técnicas Living off the Land (LotL), utilizando las propias herramientas nativas y legítimas del sistema operativo (PowerShell, WMI, bitsadmin) para ocultar sus operaciones. Para revertir esta asimetría, las organizaciones deben desplegar servicios de Detección y Respuesta Gestionadas (MDR) y ejecutar cacería activa de amenazas (Threat Hunting) las 24 horas del día. La resiliencia moderna se mide en la capacidad de detectar desvíos de comportamiento en minutos y neutralizar al adversario antes de que ejecute su objetivo de impacto."
        ),
        "conceptos": [
            "**Dwell Time (Tiempo de Permanencia):** Tiempo transcurrido desde que un atacante logra acceso inicial a una red hasta que su presencia es detectada y contenida.",
            "**Living off the Land (LotL / LOLBAS):** Técnica adversarial que utiliza binarios, scripts y utilidades legítimas del sistema operativo para evadir la detección de antivirus y EDRs.",
            "**Managed Detection and Response (MDR):** Servicio de seguridad 24/7 que combina analítica avanzada y cazadores humanos expertos para investigar alertas y contener incidentes en vivo.",
            "**Proactive Threat Hunting:** Búsqueda reiterativa e informada de atacantes que ya han eludido los controles preventivos automatizados, formulando hipótesis basadas en inteligencia."
        ],
        "frameworks": [
            "[LOLBAS (Living Off The Land Binaries and Scripts) Project](https://lolbas-project.github.io/): Repositorio y marco de referencia global que cataloga los ejecutables legítimos de Windows comúnmente utilizados para evasión y ejecución maliciosa.",
            "[CISA Alert AA23-144A: Hunting Russian/State-Sponsored LotL Techniques](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a): Asesoría técnica internacional sobre cómo identificar el abuso de utilidades nativas en redes de infraestructura crítica.",
            "[MITRE ATT&CK: Defense Evasion Tactic (TA0005)](https://attack.mitre.org/tactics/TA0005/): Taxonomía que agrupa las técnicas utilizadas por atacantes para evitar ser detectados por soluciones de seguridad.",
            "[NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final): Manual de referencia de respuesta a incidentes del gobierno de Estados Unidos."
        ],
        "papers": [
            "**USENIX Security (2022):** *Measuring Dwell Time and Lateral Movement Dynamics in Modern Enterprise Ransomware Intrusions* ([USENIX](https://www.usenix.org/conference/usenixsecurity22)) — Estudio cuantitativo basado en cientos de incidentes reales que correlaciona el tiempo de permanencia con el impacto financiero.",
            "**IEEE Transactions on Dependable and Secure Computing (2021):** *Graph-Based Detection of Living-off-the-Land Exploitation in Enterprise Systems* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9417124)) — Propuesta de modelado de grafos de procesos para identificar secuencias anómalas de ejecución de PowerShell y utilidades de comando."
        ],
        "tools": [
            "[Microsoft Sysmon (System Monitor)](https://learn.microsoft.com/es-es/sysinternals/downloads/sysmon): Servicio del sistema de Windows que registra eventos detallados de procesos, conexiones de red y modificaciones de archivos, esencial con configuraciones comunitarias como SwiftOnSecurity.",
            "[Atomic Red Team (Red Canary)](https://github.com/redcanaryco/atomic-red-team): Biblioteca de pruebas simples y automatizadas para simular tácticas de MITRE ATT&CK y verificar si los controles de detección funcionan.",
            "[Hayabusa (Fast Windows Event Log Forensics)](https://github.com/Yamato-Security/hayabusa): Analizador forense ultrarrápido en Rust que escanea terabytes de registros de eventos de Windows contra reglas Sigma.",
            "[Velociraptor (Endpoint DFIR Platform)](https://github.com/Velocidex/velociraptor): Framework de telemetría distribuida para recopilar evidencia de procesos LotL en endpoints de forma masiva."
        ],
        "learning": [
            "[Microsoft Learn: Implementación de Capacidades EDR con Microsoft Defender for Endpoint](https://learn.microsoft.com/es-es/training/paths/mde-deploy/): Ruta oficial sobre detección de comportamiento anómalo, aislamiento de terminales y remediación automatizada.",
            "[TryHackMe: Threat Hunting with Splunk & Sysmon](https://tryhackme.com/module/threat-hunting): Módulos prácticos para escribir consultas avanzadas de detección e interceptar movimientos laterales silenciosos.",
            "[HackTheBox: Enterprise Incident Response (Sherlocks Track)](https://www.hackthebox.com): Escenarios forenses reales de investigación de ransomware para reconstruir la línea de tiempo del atacante.",
            "[SANS Cyber Defense Open Resources](https://www.sans.org): Colección de pósteres de comandos, hojas de referencia forense y guías de caza de anomalías en memoria."
        ]
    },
    {
        "path": "malla-curricular/03-dia2-seminario/06-norman-amenazas-hibridas.md",
        "title": "Amenazas Híbridas en la Era Digital - James Norman",
        "audio": "../../assets/audio/dia2_06_norman.mp3",
        "prev": "05-albuquerque-deteccion-respuesta.md",
        "next": "07-abbas-academia-talento.md",
        "sintesis": (
            "En el tablero geopolítico del siglo XXI, el ciberespacio se ha consolidado como el teatro de operaciones predilecto para la ejecución de agresiones en la denominada 'Zona Gris'. Las amenazas híbridas orquestan de manera sincrónica vectores de sabotaje informático contra infraestructuras críticas (puertos marítimos, redes eléctricas y telecomunicaciones) con sofisticadas campañas de desinformación masiva en redes sociales y plataformas de mensajería. El objetivo no es solo desconectar un servicio técnico, sino quebrar la cohesión social, inducir pánico colectivo y erosionar la confianza de la ciudadanía en las instituciones democráticas.\n\n"
            "James Norman, diplomático y experto del FCDO británico, demuestra cómo estas operaciones están diseñadas deliberadamente para mantenerse por debajo del umbral formal de un acto de guerra armada, dificultando la atribución jurídica y la activación de tratados de defensa mutua. La respuesta ante este vector asimétrico trasciende las soluciones exclusivamente técnicas: requiere una doctrina de resiliencia nacional total, sustentada en la cooperación diplomática multilateral, la comunicación gubernamental transparente en tiempo de crisis y el fortalecimiento del pensamiento crítico como primera línea de defensa cívica."
        ),
        "conceptos": [
            "**Hybrid Threats & Gray Zone Warfare:** Estrategia hostil que combina coerción cibernética, desinformación, presión económica y operaciones encubiertas por debajo del umbral de guerra abierta.",
            "**Information Operations (IO) & Disinformation Swarms:** Campañas automatizadas mediante granjas de bots y cuentas sintéticas diseñadas para amplificar el caos social durante una emergencia física o digital.",
            "**Strategic Attribution in Cyberspace:** Proceso político y técnico mediante el cual una coalición internacional imputa formal y públicamente la autoría de un ciberataque a un Estado hostil.",
            "**Societal Cyber Resilience:** Capacidad de una población civil informada para resistir la manipulación informativa, verificar noticias y mantener la calma ante contingencias críticas."
        ],
        "frameworks": [
            "[European Centre of Excellence for Countering Hybrid Threats (Hybrid CoE) Framework](https://www.hybridcoe.fi/): Marco analítico de referencia conjunto de la UE y la OTAN para clasificar y responder a agresiones híbridas.",
            "[NATO Cyber Defence Pledge](https://www.nato.int/cps/en/natohq/topics_78170.htm): Compromiso de los países aliados de fortalecer la resiliencia ciberespacial como parte indivisible de la defensa colectiva (Artículo 5).",
            "[CISA Mis-, Dis-, and Malinformation (MDM) Planning Guidance](https://www.cisa.gov/topics/election-security/mis-dis-and-malinformation): Guía estratégica para infraestructuras críticas sobre mitigación de campañas de manipulación psicológica en contingencias electorales y de servicios básicos.",
            "[Tallinn Manual 2.0 on the International Law Applicable to Cyber Operations](https://ccdcoe.org/research/tallinn-manual/): Tratado doctrinal de referencia publicado por el Centro de Excelencia de la OTAN en Tallin sobre el derecho internacional aplicable a la ciberguerra."
        ],
        "papers": [
            "**International Affairs (Chatham House, 2022):** *Hybrid Warfare in the Digital Age: Geopolitics, Critical Infrastructure, and the Erosion of Democratic Trust* ([Chatham House](https://www.chathamhouse.org/publications/ia)) — Estudio sobre cómo los ciberataques coordinados con desinformación desestabilizan sistemas electorales y cadenas de abastecimiento.",
            "**Global Cyber Security Capacity Centre (Oxford, 2021):** *Cyber Resilience and Democratic Stability: The Role of Societal Education and Verification* ([Oxford University](https://gcscc.ox.ac.uk/)) — Evaluación del impacto de la alfabetización mediática en la reducción del pánico inducido durante incidentes cibernéticos."
        ],
        "tools": [
            "[Gephi (Open Source Network Exploration & Manipulation)](https://github.com/gephi/gephi): Software líder de código abierto para visualización y análisis de grafos complejos, utilizado para mapear redes de bots y flujos de desinformación.",
            "[Botometer (Observatory on Social Media)](https://botometer.osome.iu.edu/): Herramienta analítica para evaluar la probabilidad de que una cuenta de red social sea un agente automatizado en campañas coordinadas.",
            "[Maltego Community Edition](https://www.maltego.com/): Plataforma de inteligencia gráfica para investigación de fuentes abiertas (OSINT), relaciones de infraestructura y atribución de dominios.",
            "[Spiderfoot (Automated OSINT Collection)](https://github.com/smicallef/spiderfoot): Herramienta de automatización de inteligencia de fuentes abiertas para recopilar datos de huella digital y amenazas de forma pasiva."
        ],
        "learning": [
            "[NATO CCDCOE: Cyber Defence Open Lectures & Exercises](https://ccdcoe.org/): Materiales y grabaciones del ejercicio internacional Locked Shields sobre defensa de infraestructuras nacionales ante guerra híbrida.",
            "[United States Institute of Peace (USIP): Countering Disinformation in Crises](https://www.usip.org): Curso en línea sobre estrategias cívicas y gubernamentales para desarticular operaciones psicológicas en emergencias.",
            "[Cisco NetAcad: Cybersecurity and Geopolitical Risk](https://www.netacad.com): Módulo sobre el papel de las telecomunicaciones y la seguridad de los cables submarinos en la soberanía de las naciones.",
            "[Coursera / Sciences Po: Geopolitics of Cyberspace](https://www.coursera.org): Especialización en diplomacia cibernética, atribución internacional y normas de comportamiento responsable de los Estados en el ciberespacio."
        ]
    },
    {
        "path": "malla-curricular/03-dia2-seminario/07-abbas-academia-talento.md",
        "title": "Transformación Digital y Ciberresiliencia: El Rol de la Academia - Nadezda Abbas",
        "audio": "../../assets/audio/dia2_07_abbas.mp3",
        "prev": "06-norman-amenazas-hibridas.md",
        "next": "../04-investigacion-global/01-nist-cisa-ncsc.md",
        "sintesis": (
            "El fortalecimiento de la ciberresiliencia nacional enfrenta una limitante estructural que no se resuelve con adquisiciones presupuestarias de software: la dramática brecha global y regional de profesionales calificados en ciberdefensa. Las organizaciones de infraestructura crítica compiten por un número reducido de especialistas capacitados, mientras que las amenazas digitales evolucionan con una celeridad que supera con creces los ciclos tradicionales de actualización curricular universitaria. Sin capital humano preparado, la tecnología más avanzada se convierte en un activo inerte e indefenso.\n\n"
            "Nadezda Abbas plantea una modernización pedagógica radical basada en el aprendizaje activo y la simulación técnica. Se requiere migrar de la teoría abstracta hacia laboratorios interactivos, competencias de Capture The Flag (CTF) y alianzas estrechas de triple hélice entre academia, Estado y empresas estratégicas. Asimismo, la expositora recalca el imperativo estratégico de promover la inclusión activa de mujeres y jóvenes de regiones en carreras STEM: la diversidad de perspectivas cognitivas y disciplinas es indispensable para diseñar defensas robustas capaces de anticipar la creatividad táctica del adversario."
        ),
        "conceptos": [
            "**Cybersecurity Skills Gap:** Déficit estructural cuantificado de millones de vacantes laborales no cubiertas en seguridad de la información a nivel mundial.",
            "**Hands-On Cyber Range Training:** Entornos de simulación controlados donde los estudiantes se enfrentan a escenarios de ataque y defensa reales contra redes industriales simuladas.",
            "**Capture The Flag (CTF) Competitions:** Metodología gamificada de alta exigencia donde los participantes resuelven acertijos de ingeniería inversa, forense y explotación web para capturar marcadores de código.",
            "**STEM Gender Inclusion & Diversity:** Iniciativas orientadas a desmantelar barreras de entrada para mujeres en áreas tecnológicas, enriqueciendo los equipos de seguridad con enfoques multidisciplinarios."
        ],
        "frameworks": [
            "[NIST NICE Workforce Framework for Cybersecurity (NIST SP 800-181 Rev. 1)](https://csrc.nist.gov/publications/detail/sp/800-181/rev-1/final): Marco nacional de EE.UU. que estandariza las categorías, roles laborales, competencias y conocimientos de los profesionales de ciberseguridad.",
            "[ENISA European Cybersecurity Skills Framework (ECSF)](https://www.enisa.europa.eu/topics/education/european-cybersecurity-skills-framework): Clasificación europea de 12 roles clave en ciberseguridad para armonizar la formación superior y el mercado laboral.",
            "[ACM / IEEE Cybersecurity Curricular Guidance (CSEC2017)](https://www.acm.org/education/curricula-recommendations): Guía internacional de diseño de mallas curriculares de pregrado en ciberseguridad estructurada en ocho áreas de conocimiento.",
            "[Women in Cybersecurity (WiCyS) Global Guidelines](https://www.wicys.org/): Estándares comunitarios para fomentar la mentoría, retención y liderazgo femenino en la industria tecnológica."
        ],
        "papers": [
            "**IEEE Frontiers in Education Conference (2022):** *Bridging the Cybersecurity Workforce Gap: Evaluating Hands-on CTF Competitions as Pedagogical Accelerators* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9962534)) — Estudio empírico sobre cómo las competencias prácticas aceleran el desarrollo de pensamiento analítico defensivo.",
            "**Computers & Education (2021):** *Diversity in Cyber Defense: Analyzing Retention Factors and Career Pathways for Underrepresented Groups in STEM* ([DOI: 10.1016/j.compedu.2021.104245](https://www.sciencedirect.com/journal/computers-and-education)) — Análisis sobre el impacto de la mentoría activa y comunidades de apoyo en la incorporación de talento diverso."
        ],
        "tools": [
            "[CTFd (Capture The Flag Platform)](https://github.com/CTFd/CTFd): Plataforma de código abierto líder en el mundo para organizar, alojar y gestionar torneos de ciberseguridad y desafíos técnicos.",
            "[picoCTF Framework (Carnegie Mellon University)](https://github.com/picoCTF/picoCTF): Plataforma educativa open source diseñada para enseñar fundamentos de computación y ciberseguridad a estudiantes desde nivel inicial.",
            "[Root-Me Community Platform](https://github.com/Root-Me): Entorno y repositorio abierto de cientos de laboratorios prácticos sobre criptografía, forense, red y explotación de software.",
            "[OWASP Juice Shop](https://github.com/juice-shop/juice-shop): Aplicación web intencionalmente vulnerable desarrollada para entrenamiento ético en auditoría y pentesting según el OWASP Top 10."
        ],
        "learning": [
            "[Cisco Networking Academy: Junior Cybersecurity Analyst Career Path (Gratuito)](https://www.netacad.com/courses/cybersecurity/cybersecurity-analyst): Formación oficial completa con laboratorios Packet Tracer y preparación para certificaciones de la industria.",
            "[Microsoft Learn: Fundamentos de Seguridad, Cumplimiento e Identidad (SC-900)](https://learn.microsoft.com/es-es/training/paths/describe-concepts-of-security-compliance-identity/): Módulos gratuitos para sentar las bases conceptuales de la ciberseguridad empresarial.",
            "[TryHackMe: Pre-Security & Complete Beginner Paths](https://tryhackme.com/path/outline/pre-security): Ruta práctica guiada para personas sin conocimientos previos de informática que deseen dominar redes, sistemas operativos y seguridad.",
            "[Code.org & CSforALL Initiatives](https://code.org): Cursos introductorios abiertos para despertar el interés por la ciencia computacional y la ciberseguridad en jóvenes y niñas."
        ]
    },

    # --- INVESTIGACION GLOBAL ---
    {
        "path": "malla-curricular/04-investigacion-global/01-nist-cisa-ncsc.md",
        "title": "Marco NIST CSF 2.0 y Guías de Ciberresiliencia CISA/NCSC - Marco CISA / NIST & NCSC",
        "audio": "../../assets/audio/intl_01_eeuu_uk.mp3",
        "prev": "../03-dia2-seminario/07-abbas-academia-talento.md",
        "next": "02-china-cii-cac.md",
        "sintesis": (
            "El modelo de ciberresiliencia desarrollado por la comunidad anglosajona, liderado por el Instituto Nacional de Estándares y Tecnología (NIST) de EE.UU. junto a CISA y el Centro Nacional de Ciberseguridad (NCSC) del Reino Unido, constituye el referente normativo y metodológico más extendido en el mundo corporativo internacional. La publicación del marco NIST Cybersecurity Framework 2.0 (CSF 2.0) introduce una evolución estratégica fundamental al incorporar la función de 'Gobernar' (Govern) de forma transversal a las tradicionales 'Identificar', 'Proteger', 'Detectar', 'Responder' y 'Recuperar', posicionando la gestión del riesgo cibernético como una responsabilidad indivisible de la junta directiva y la alta dirección empresarial.\n\n"
            "El paradigma anglosajón se distingue por articular mandatos legales de reporte acelerado con una cultura de colaboración pública y privada altamente coordinada. Instrumentos como los Objetivos de Rendimiento en Ciberseguridad Intersectoriales (CPGs) de CISA y los mandatos de la ley CIRCIA (reporte de incidentes en 72 horas) establecen una línea base de seguridad obligatoria para sectores críticos. A su vez, el Cyber Assessment Framework (CAF) del Reino Unido proporciona una métrica de madurez pragmática para auditar sistemas industriales, complementada con programas de Ciberdefensa Activa (ACD) para neutralizar amenazas a escala nacional."
        ),
        "conceptos": [
            "**NIST CSF 2.0 Core Functions:** Estructura que organiza el ciclo de gestión del riesgo cibernético en seis pilares: Govern (Gobernar), Identify (Identificar), Protect (Proteger), Detect (Detectar), Respond (Responder) y Recover (Recuperar).",
            "**CISA Cross-Sector Cybersecurity Performance Goals (CPGs):** Conjunto priorizado de prácticas defensivas de alto impacto diseñadas para reducir drásticamente el riesgo de intrusiones en infraestructuras críticas.",
            "**NCSC Cyber Assessment Framework (CAF 3.2):** Marco sistemático del gobierno británico para evaluar cómo las organizaciones esenciales gestionan la seguridad de la información y la resiliencia operativa.",
            "**CIRCIA 72h / 24h Mandatory Reporting:** Régimen legal estadounidense que exige a operadores críticos reportar ciberataques significativos ante CISA en menos de 72 horas y pagos de ransomware en 24 horas."
        ],
        "frameworks": [
            "[NIST Cybersecurity Framework 2.0 (CSF 2.0)](https://www.nist.gov/cyberframework): Versión actualizada del marco de ciberseguridad más adoptado del mundo, aplicable a todo tipo de organizaciones y cadenas de suministro.",
            "[CISA Cross-Sector Cybersecurity Performance Goals (CPGs)](https://www.cisa.gov/cpgs): Guía técnica de controles esenciales de ciberseguridad para operadores de agua, energía, transporte y salud.",
            "[NCSC Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf): Guía metodológica del Reino Unido para la auditoría técnica y regulatoria bajo las normas NIS.",
            "[NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final): Documento que define la arquitectura y componentes del modelo de Confianza Cero en infraestructuras federales y corporativas."
        ],
        "papers": [
            "**NIST Special Publication 800-53 Rev. 5:** *Security and Privacy Controls for Information Systems and Organizations* ([NIST CSRC](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)) — El catálogo de controles técnicos más exhaustivo del mundo para proteger sistemas contra amenazas avanzadas.",
            "**UK Cabinet Office (2022):** *National Cyber Strategy 2022: Pioneering a Cyber Resilient Future* ([Gov.uk](https://www.gov.uk/government/publications/national-cyber-strategy-2022)) — Estrategia de estado británica sobre ciberdefensa activa, soberanía tecnológica y resiliencia de servicios públicos esenciales."
        ],
        "tools": [
            "[CISA CSET (Cyber Security Evaluation Tool)](https://github.com/cisagov/cset): Herramienta oficial de CISA para autoevaluar la postura de ciberseguridad de redes industriales y corporativas frente a múltiples normas (NIST, IEC 62443).",
            "[NIST CSF 2.0 Reference Tool](https://csrc.nist.gov/Projects/cybersecurity-framework/filters): Explorador interactivo oficial de categorías, subcategorías y ejemplos de implementación del nuevo marco NIST.",
            "[Lynis (Security Auditing Tool for Unix/Linux)](https://github.com/CISOfy/lynis): Herramienta de auditoría de seguridad open source para comprobar configuraciones del sistema frente a directrices de endurecimiento (hardening).",
            "[OpenSCAP Platform](https://github.com/OpenSCAP/openscap): Ecosistema de código abierto para automatizar la evaluación de cumplimiento normativo y parches en sistemas operativos empresariales."
        ],
        "learning": [
            "[NIST CSF 2.0 Online Learning Modules](https://www.nist.gov/cyberframework/online-learning): Recursos oficiales y guías de inicio rápido para implementar la nueva función Govern y mapear controles corporativos.",
            "[CISA Federal Virtual Training Environment (FedVTE)](https://www.cisa.gov/cyber-training): Plataforma de capacitación gubernamental con cientos de horas de formación en ciberdefensa y análisis de vulnerabilidades.",
            "[NCSC UK: Certified Cyber Professional (CCP) Knowledge Areas](https://www.ncsc.gov.uk): Guías formativas sobre arquitectura de resiliencia y gestión de incidentes industriales.",
            "[Coursera / Infosec: NIST Cybersecurity Framework Implementation](https://www.coursera.org): Especialización profesional en planificación e implementación práctica del marco NIST en organizaciones."
        ]
    },
    {
        "path": "malla-curricular/04-investigacion-global/02-china-cii-cac.md",
        "title": "Reglamento de Infraestructura de Información Crítica (CII 2021) y Soberanía de Datos - Administración del Ciberespacio de China (CAC)",
        "audio": "../../assets/audio/intl_02_china.mp3",
        "prev": "01-nist-cisa-ncsc.md",
        "next": "03-rusia-187fz-fstec.md",
        "sintesis": (
            "El modelo de seguridad digital de la República Popular China se rige bajo una doctrina de 'Soberanía Digital Absoluta' y control estatal centralizado de los flujos de información. Este esquema tiene como eje vinculante el Reglamento de Protección de Seguridad de Infraestructuras de Información Crítica (Reglamento CII, Decreto N° 745 del Consejo de Estado de 2021), complementado por la Ley de Ciberseguridad (2017), la Ley de Seguridad de Datos (2021) y la Ley de Protección de Información Personal (PIPL). Para Beijing, las redes que operan la energía, las telecomunicaciones, el transporte, las finanzas y los servicios gubernamentales son extensiones territoriales de la seguridad nacional.\n\n"
            "El marco chino destaca por imponer estrictos requisitos de localización de datos dentro de sus fronteras y severas restricciones a la transferencia transfronteriza de información corporativa y científica. A través del Esquema de Protección de Seguridad Multi-Nivel (MLPS 2.0 / 等保2.0), supervisado por el Ministerio de Seguridad Pública (MPS), los operadores de infraestructura crítica de nivel 3 o superior están legalmente obligados a adquirir productos y servicios de red previamente auditados por revisiones de seguridad nacional de la CAC. Esta política busca descartar puertas traseras externas y acelerar la sustitución tecnológica por componentes de desarrollo nacional independiente."
        ),
        "conceptos": [
            "**Cyber Sovereignty (网络主权):** Doctrina jurídica y política que sostiene el derecho inalienable de cada Estado a regular, supervisar y controlar su ciberespacio nacional sin injerencia extranjera.",
            "**Critical Information Infrastructure Regulations (CII - 关键信息基础设施):** Normativa estricta que define sectores protegidos y responsabilidades legales directas para los directivos encargados de su operación.",
            "**Multi-Level Protection Scheme 2.0 (MLPS 2.0 / 等级保护):** Sistema de categorización obligatoria (Niveles 1 al 5) que fija los controles técnicos, de red y de criptografía nacional exigidos a cada sistema informático.",
            "**Data Localization & National Security Reviews:** Obligación de almacenar datos importantes y personales dentro de China y someter software y hardware extranjero a auditorías antes de su implementación."
        ],
        "frameworks": [
            "[Reglamento de Protección de Seguridad de Infraestructuras de Información Crítica (Decreto N° 745 del Consejo de Estado)](http://www.cac.gov.cn): Texto legal oficial que regula las obligaciones de auditoría anual y reporte de incidentes para operadores críticos.",
            "[Estándar Nacional GB/T 22239-2019: Requisitos de Seguridad de la Información para MLPS 2.0](http://www.tc260.org.cn): Estándar técnico obligatorio que desglosa los controles de seguridad física, de red, de host y de datos según el nivel clasificado.",
            "[Ley de Seguridad de Datos de la República Popular China (2021)](http://www.npc.gov.cn/): Legislación que categoriza los datos en 'Datos Centrales del Estado' y 'Datos Importantes', penalizando su filtración al exterior.",
            "[Ley de Ciberseguridad de la República Popular China (2017)](http://www.cac.gov.cn): Pilar normativo fundacional que inauguró el marco de soberanía y auditorías obligatorias a operadores de red."
        ],
        "papers": [
            "**Harvard Belfer Center (2021):** *China's Cyber Power and the Governance of Critical Information Infrastructure* ([Belfer Center](https://www.belfercenter.org/publication/chinas-cyber-power)) — Análisis detallado sobre la arquitectura de supervisión de la CAC y el impacto del desacoplamiento tecnológico en la cadena de suministro.",
            "**Georgetown CSET (2022):** *China's Cyber Law Landscape: Standards, Supply Chains, and National Security* ([Center for Security and Emerging Technology](https://cset.georgetown.edu/)) — Desglose de los estándares técnicos del comité TC260 y su aplicación en auditorías a proveedores tecnológicos extranjeros."
        ],
        "tools": [
            "[Wazuh MLPS Configuration Profiles](https://github.com/wazuh/wazuh): Conjunto de reglas y perfiles comunitarios para auditar sistemas operativos Linux frente a los requerimientos del estándar MLPS 2.0.",
            "[CNVD (China National Vulnerability Database Telemetry Monitor)](https://www.cnvd.org.cn/): Base de datos nacional de vulnerabilidades de China, referencia para la catalogación de fallas en software operativo en el mercado asiático.",
            "[OpenSCAP Chinese National Profile Rulesets](https://github.com/OpenSCAP/scap-security-guide): Plantillas de endurecimiento de sistemas para evaluar configuraciones de cumplimiento normativo en entornos corporativos globales.",
            "[Suricata IDS/IPS Engine](https://github.com/OISF/suricata): Motor de inspección profunda de paquetes adoptado ampliamente para la implementación de sensores de borde y monitoreo de tráfico perimetral."
        ],
        "learning": [
            "[Stanford University DigiChina Project: Comprehensive Regulatory Translations & Analysis](https://digichina.stanford.edu/): Proyecto de la Universidad de Stanford con traducciones oficiales y análisis profundos de toda la legislación digital y de ciberseguridad china.",
            "[ISO/IEC 27001 Cross-Walk to Chinese Cybersecurity Standards Guide](https://www.iso.org): Recursos comparativos sobre cómo las multinacionales homologan sus controles occidentales con las exigencias del MLPS 2.0.",
            "[TryHackMe: Global Compliance, Governance & Data Sovereignty](https://tryhackme.com/module/security-operations): Módulos sobre adaptación de políticas de seguridad a marcos normativos multinacionales y control de transferencias de datos.",
            "[Coursera / Tsinghua University: Chinese Law and Society in the Digital Age](https://www.coursera.org): Análisis sobre el marco institucional, soberanía jurídica y gobernanza de la tecnología en el gigante asiático."
        ]
    },
    {
        "path": "malla-curricular/04-investigacion-global/03-rusia-187fz-fstec.md",
        "title": "Ley Federal N° 187-FZ de Seguridad de Infraestructura Crítica y GosSOPKA - Servicio Federal de Control Técnico y Exportaciones (FSTEC / FSB)",
        "audio": "../../assets/audio/intl_03_rusia.mp3",
        "prev": "02-china-cii-cac.md",
        "next": None,
        "sintesis": (
            "La doctrina de ciberseguridad de la Federación Rusa concibe la protección de la infraestructura crítica como un pilar indivisible de la defensa nacional y la soberanía estatal. Este marco se fundamenta en la Ley Federal N° 187-FZ ('Sobre la Seguridad de la Infraestructura de Información Crítica'), promulgada para blindar las redes esenciales de energía, transporte, banca, defensa, industria nuclear y química. Bajo la supervisión técnica del Servicio Federal de Control Técnico y de Exportaciones (FSTEC) y el Centro Nacional de Coordinación de Incidentes Informáticos (NKTsKI, adscrito al FSB), el modelo impone una estructura de comando altamente centralizada.\n\n"
            "El componente operacional distintivo del esquema ruso es el sistema estatal GosSOPKA (ГосСОПКА). Todos los operadores de importancia vital están obligados a integrar sus centros de monitoreo con esta plataforma centralizada para alimentar la detección y mitigación de ciberataques a escala nacional en tiempo real. Este modelo se articula con la estrategia del 'Runet Soberano' (Ley N° 90-FZ) y decretos presidenciales de sustitución obligatoria de importaciones, que exigen a las organizaciones estratégicas migrar de plataformas occidentales hacia hardware, sistemas operativos rusos certificados (Astra Linux) y algoritmos criptográficos propios homologados bajo estándares GOST."
        ),
        "conceptos": [
            "**Federal Law No. 187-FZ (Федеральный закон № 187-ФЗ):** Marco legal que clasifica los objetos de infraestructura crítica en tres categorías de significancia según su impacto potencial en la defensa y economía.",
            "**GosSOPKA System (ГосСОПКА):** Sistema Estatal para la Detección, Prevención y Eliminación de Consecuencias de Ataques Informáticos contra los recursos informáticos de la Federación Rusa.",
            "**Import Substitution (Импортозамещение):** Mandato estatal que prohíbe el uso de software, firmware y hardware extranjeros en infraestructuras críticas, forzando la adopción de tecnología rusa certificada.",
            "**GOST Cryptography Standards (Криптография ГОСТ):** Conjunto de algoritmos criptográficos oficiales y asimétricos aprobados por el FSB para la firma digital y cifrado en redes de infraestructura estratégica."
        ],
        "frameworks": [
            "[Ley Federal N° 187-FZ 'Sobre la Seguridad de la Infraestructura de Información Crítica'](http://pravo.gov.ru): Texto legal oficial que norma los deberes de categorización técnica, seguridad informática y reporte obligatorio de incidentes.",
            "[Orden FSTEC N° 239: Requisitos de Seguridad de la Información para Sistemas de Control en CII](https://fstec.ru): Norma técnica que especifica los controles de hardware, software y segmentación para PLCs y servidores de infraestructura crítica.",
            "[GOST R 57580.1-2017: Seguridad de Operaciones Financieras y Transacciones Críticas](https://www.gost.ru/): Estándar nacional de seguridad de la información para el sector bancario y financiero ruso.",
            "[Ley Federal N° 90-FZ 'Sobre el Internet Soberano' (Runet)](http://pravo.gov.ru): Marco legislativo que establece la infraestructura técnica necesaria para aislar el tráfico de internet ruso de los servidores raíz internacionales en caso de desconexión externa."
        ],
        "papers": [
            "**Center for Strategic and International Studies (CSIS, 2022):** *Russian Cyber Warfare Doctrine, Critical Infrastructure Defense, and Sovereign Networks* ([CSIS](https://www.csis.org/analysis/russian-cyber-warfare)) — Estudio sobre la arquitectura de GosSOPKA y su relación con las capacidades ofensivas y defensivas del Estado ruso.",
            "**Chatham House (2021):** *The Sovereign Internet Law and the Architecture of GosSOPKA: Security through Isolation* ([Chatham House](https://www.chathamhouse.org/)) — Investigación sobre los desafíos técnicos y de gobernanza de la sustitución tecnológica y el enrutamiento autónomo nacional."
        ],
        "tools": [
            "[Suricata IDS/IPS Engine](https://github.com/OISF/suricata): Motor de detección de intrusiones de código abierto ampliamente utilizado como componente de sensores de red distribuidos en centros de GosSOPKA.",
            "[Greenbone Vulnerability Management (OpenVAS)](https://github.com/greenbone/gvmd): Suite de análisis de vulnerabilidades open source adoptada para auditorías internas de cumplimiento de la orden FSTEC 239.",
            "[MISP GosSOPKA Connectors](https://github.com/MISP): Módulos comunitarios para formatear y reenviar indicadores de compromiso conforme a los esquemas de telemetría requeridos por el NKTsKI.",
            "[Wazuh FSTEC Compliance Mapping](https://github.com/wazuh/wazuh): Reglas de telemetría de endpoints mapeadas a los requisitos de integridad de archivos y auditoría de accesos de la normativa 187-FZ."
        ],
        "learning": [
            "[European University Institute: Cyber Resilience, Sovereignty and Post-Soviet Geopolitics](https://www.eui.eu): Módulos académicos abiertos sobre gobernanza de internet soberano, diplomacia de ciberdefensa y marcos de seguridad euroasiáticos.",
            "[TryHackMe: Threat Hunting State-Sponsored Actors (Sandworm, APT28/29)](https://tryhackme.com/module/threat-hunting): Laboratorios interactivos para analizar las tácticas, herramientas (BlackEnergy, Industroyer) y telemetría de actores avanzados de la región.",
            "[SANS Reading Room: National CERT and Incident Response Architectures](https://www.sans.org/white-papers/): Documentación técnica sobre la coordinación centralizada de CSIRTs nacionales e intercambio de alertas críticas.",
            "[Coursera / Stanford: International Security in a Changing World](https://www.coursera.org): Análisis sobre doctrinas militares de disuasión cibernética, ciberguerra y soberanía de infraestructura crítica."
        ]
    }
]

# Unimos todas las 19 lecciones
all_lessons = lessons_data + lessons_dia2_and_intl
print(f"Total lecciones a escribir: {len(all_lessons)}")

# Escribir cada archivo
for lesson in all_lessons:
    full_path = os.path.join(BASE_DIR, lesson["path"])
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    content = format_markdown(lesson)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Escrito: {lesson['path']}")

# Escribir el módulo 01-fundamentos
fundamentos_path = os.path.join(BASE_DIR, "malla-curricular/01-fundamentos/01-conceptos-infraestructura-critica.md")
fundamentos_content = """# Conceptos Fundamentales: Infraestructura Crítica y Ciberresiliencia - Arquitectura Lattices

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
"""

with open(fundamentos_path, "w", encoding="utf-8") as f:
    f.write(fundamentos_content)
print(f"Escrito módulo de fundamentos: {fundamentos_path}")

# Actualizar README de fundamentos
fundamentos_readme = os.path.join(BASE_DIR, "malla-curricular/01-fundamentos/README.md")
with open(fundamentos_readme, "w", encoding="utf-8") as f:
    f.write("""# 01 - Fundamentos de Infraestructura Crítica y Ciberresiliencia

Módulo introductorio para sentar las bases conceptuales, técnicas y regulatorias de la protección de infraestructuras vitales.

* [📘 Lección 01: Conceptos Fundamentales de Infraestructura Crítica y Resiliencia](01-conceptos-infraestructura-critica.md)

[Volver a la Malla Curricular](../../README.md).
""")
print(f"Actualizado: {fundamentos_readme}")

# Generar README.md principal para gemini/lattices-deepdive
readme_content = """# 🛡️ Knowledge Base: Ciberseguridad e Infraestructura Crítica (Lattices Architecture)

Base de conocimiento abierta de alto nivel técnico sobre **protección de infraestructura crítica, inteligencia artificial adversarial y ciberresiliencia**. Este repositorio recopila y expande las ponencias técnicas del 9° Seminario Internacional de Ciberseguridad (PDI-USM) junto a un análisis exhaustivo de los tres principales modelos regulatorios globales (EE.UU./UK, China y Rusia).

El material está estructurado bajo los estándares de ingeniería de contenidos de **Lattices** para profesionales de ciberdefensa, arquitectos de infraestructura e investigadores.

---

## 🧭 Malla Curricular y Ecosistema de Recursos

Cada lección incluye **Síntesis Ejecutiva**, **Conceptos Core**, **🧠 Ecosistema de Recursos Globales (Estándares, Papers, Repositorios Open Source y Cursos Enterprise)** y enlace a podcast de resumen.

### 01. Fundamentos
| Módulo | Documento | Enfoque Técnico |
| :--- | :--- | :--- |
| Fundamentos | [Conceptos Fundamentales de Infraestructura Crítica y Ciberresiliencia](malla-curricular/01-fundamentos/01-conceptos-infraestructura-critica.md) | Modelo Purdue, Convergencia IT/OT y Resiliencia |

### 02. Día 1: Amenazas Emergentes, Regulación y Protección Sectorial
| Lección | Speaker / Institución | Temática Principal |
| :--- | :--- | :--- |
| [01. Adversarios Digitales IA y Amenazas a IC](malla-curricular/02-dia1-seminario/01-wong-ia-cibercrimen.md) | Subprefecto Marcelo Wong Cea (PDI Cibercrimen) | Automatización ofensiva, síntesis adversarial y CTEM |
| [02. Infraestructura de Internet: DNS y Resiliencia](malla-curricular/02-dia1-seminario/02-lama-infraestructura-dns.md) | Guillermo Lama (NIC Chile) | Topologías BGP Anycast, mitigación DDoS y DNSSEC |
| [03. El Lado Práctico del Crimen con IA](malla-curricular/02-dia1-seminario/03-fernandez-crimen-ia.md) | Manu Fernández (TRM - IAFIS) | Multimodal Deepfakes, fraude BEC 3.0 y evasión biométrica |
| [04. Ciberseguridad y Resiliencia: Desafío Nacional](malla-curricular/02-dia1-seminario/04-bordachar-anci-regulacion.md) | Michelle Bordachar (ANCI) | Ley Marco N° 21.663, Operadores OIV y gobernanza |
| [05. Un Incidente, Múltiples Impactos: Efecto Dominó](malla-curricular/02-dia1-seminario/05-evirtus-efecto-domino.md) | Representante Técnico Sectorial (E-Virtus) | C-SCRM, fallas en cascada y accesos Just-In-Time |
| [06. Dispositivos Médicos Conectados (IoMT)](malla-curricular/02-dia1-seminario/06-fernandez-dispositivos-medicos.md) | Víctor Fernández (Biohacking Village) | Superficies JTAG/UART, microsegmentación y CVD |
| [07. Protegiendo lo Esencial: Sectores Críticos](malla-curricular/02-dia1-seminario/07-panel-sectores-criticos.md) | Panel (Codelco, CEN, Aguas Andinas, CSIRT) | Brecha IT/OT, ISA/IEC 62443 y operación manual |
| [08. Agentes IA e Infraestructura Crítica](malla-curricular/02-dia1-seminario/08-bonnaire-agentes-ia.md) | Dr. Xavier Bonnaire (USM) | Human-in-the-Loop, prompt injection y safety envelopes |
| [09. Seguridad en la Red: Zero Trust Resiliente](malla-curricular/02-dia1-seminario/09-evirtus-zero-trust.md) | Especialista en Redes (E-Virtus) | NIST SP 800-207, microsegmentación y eBPF |

### 03. Día 2: Ciberdefensa Activa, Inteligencia y Resiliencia Operacional
| Lección | Speaker / Institución | Temática Principal |
| :--- | :--- | :--- |
| [10. Blue Team Aumentado por IA](malla-curricular/03-dia2-seminario/01-caceres-blue-team-ia.md) | Diego Cáceres (Especialista en Ciberdefensa) | A-SOC, orquestación SOAR y reducción de fatiga de alertas |
| [11. Cyber Threat Intelligence (CTI)](malla-curricular/03-dia2-seminario/02-fuentes-threat-intelligence.md) | Omar Fuentes (SEK) | Diamond Model, Pyramid of Pain y STIX/TAXII |
| [12. Resiliencia y Continuidad en Hardware](malla-curricular/03-dia2-seminario/03-cordero-resiliencia-hardware.md) | César Cordero (Lenovo) | Hardware Root of Trust, NIST SP 800-193 y TPM 2.0 |
| [13. Ciberseguridad en Salud y Biohacking Ético](malla-curricular/03-dia2-seminario/04-alli-salud-ciberseguridad.md) | Nina Alli (Biohacking Village) | Seguridad del paciente, resiliencia EHR y mitigación ransomware |
| [14. Prevención, Detección y Respuesta Activa](malla-curricular/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) | Tales Albuquerque (Sophos) | Dwell Time, técnicas Living off the Land (LotL) y MDR |
| [15. Amenazas Híbridas en la Era Digital](malla-curricular/03-dia2-seminario/06-norman-amenazas-hibridas.md) | James Norman (FCDO Reino Unido) | Guerra de zona gris, operaciones de desinformación y atribución |
| [16. Transformación Digital y Brecha de Talento](malla-curricular/03-dia2-seminario/07-abbas-academia-talento.md) | Nadezda Abbas (UBO) | NIST NICE Framework, ciberejercicios CTF e inclusión STEM |

### 04. Investigación Comparativa Internacional
| Módulo Global | Autoridad / Modelo | Marco Regulatorio y Tecnológico |
| :--- | :--- | :--- |
| [17. Estados Unidos & Reino Unido](malla-curricular/04-investigacion-global/01-nist-cisa-ncsc.md) | CISA / NIST & NCSC | Marco NIST CSF 2.0 (Función Govern), CIRCIA y NCSC CAF |
| [18. República Popular China](malla-curricular/04-investigacion-global/02-china-cii-cac.md) | CAC & MPS (China) | Reglamento CII 2021, Soberanía de Datos y MLPS 2.0 |
| [19. Federación Rusa](malla-curricular/04-investigacion-global/03-rusia-187fz-fstec.md) | FSTEC & FSB (Rusia) | Ley Federal 187-FZ, Red GosSOPKA y Runet Soberano |

---

## 🎧 Audio-Clases y Podcasts Técnicos

Cada módulo está acompañado de una cápsula de audio técnico de 60 segundos sintetizada a partir de los guiones de alta densidad. El inventario de archivos se gestiona en [assets/audio/README.md](assets/audio/README.md).

---

## 🚀 Metodología de Contenido Lattices

1. **Rigor Académico y Operacional:** Sin generalizaciones superficiales; referencias a RFCs, estándares ISO, marcos NIST/MITRE y papers indexados.
2. **Orientación Práctica (Open Source):** Cada temática se vincula a herramientas reales de GitHub y utilidades de línea de comandos para auditoría y experimentación.
3. **Rutas de Aprendizaje Certificables:** Mapeo directo a laboratorios y especializaciones de Microsoft Learn, AWS Skill Builder, Cisco NetAcad, TryHackMe y HackTheBox.
"""

main_readme = os.path.join(BASE_DIR, "README.md")
with open(main_readme, "w", encoding="utf-8") as f:
    f.write(readme_content)
print(f"Actualizado README principal: {main_readme}")
