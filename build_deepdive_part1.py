import os
import json

# Definición completa de las 19 lecciones con el estándar Deep Dive de Lattices
lessons_data = [
    # --- DIA 1 ---
    {
        "path": "malla-curricular/02-dia1-seminario/01-wong-ia-cibercrimen.md",
        "title": "Adversarios Digitales IA y el Nuevo Escenario de Amenazas a la Infraestructura Crítica - Subprefecto Marcelo Wong Cea",
        "audio": "../../assets/audio/dia1_01_wong.mp3",
        "prev": None,
        "next": "02-lama-infraestructura-dns.md",
        "sintesis": (
            "La convergencia entre modelos generativos de lenguaje, síntesis multimodal y automatización de exploits ha reconfigurado asimétricamente el vector de amenazas sobre infraestructuras críticas (OT/IT). Los adversarios computacionales ya no dependen de procesos manuales lineales de reconocimiento; actualmente despliegan pipelines automatizados capaces de ejecutar escaneos probabilísticos masivos sobre superficies expuestas, generar campañas de spear-phishing contextualizadas con telemetría de objetivos en tiempo real y sintetizar identidades biométricas de alta fidelidad para eludir controles de acceso perimetrales.\n\n"
            "Este cambio de paradigma exige una transición desde esquemas de ciberdefensa reactivos hacia arquitecturas de resiliencia continua orientadas a inteligencia y contención proactiva. La mitigación frente a actores hostiles potenciados por IA requiere integrar capas de inspección criptográfica profunda, validación de identidad fuera de banda (Out-of-Band), telemetría unificada en centros de operaciones (SOC/CSIRT) y la formalización de políticas de detección que asuman la brecha como premisa operativa fundamental en redes de energía, agua potable, telecomunicaciones y sistemas financieros."
        ),
        "conceptos": [
            "**AI-Driven Offensive Automation:** Orquestación de flujos de ataque mediante algoritmos de aprendizaje automático para acelerar fases de reconocimiento, mapeo de puertos y explotación sistemática en entornos industriales y corporativos.",
            "**Synthetic Identity Fraud & Multimodal Deepfakes:** Generación de identidades sintéticas y clonación de patrones biométricos (voz y rostro) a partir de Large Language Models (LLMs) y redes generativas antagónicas (GANs) para ejecutar fraudes ejecutivos de alta precisión.",
            "**Critical Infrastructure Interdependency:** Red de acoplamiento operativo entre sistemas de control industrial (ICS/SCADA) y plataformas transaccionales IT, donde la caída de un único nodo perimetral propaga fallas en cascada sobre servicios esenciales.",
            "**Continuous Threat Exposure Management (CTEM):** Enfoque sistemático y continuo para la priorización, validación y remediación de vectores de ataque explotables basado en la telemetría del adversario y el impacto en el negocio."
        ],
        "frameworks": [
            "[NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework): Estándar del National Institute of Standards and Technology para gobernar, mapear, medir y gestionar riesgos de seguridad en sistemas de Inteligencia Artificial.",
            "[MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/): Matriz global de tácticas, técnicas y procedimientos (TTPs) orientada a modelar y neutralizar ciberataques contra sistemas basados en Machine Learning e IA.",
            "[MITRE ATT&CK for Enterprise & ICS](https://attack.mitre.org/): Base de conocimiento taxonómica sobre el comportamiento de actores de amenazas avanzadas (APTs) en redes corporativas e infraestructura operativa.",
            "[CISA Cross-Sector Cybersecurity Performance Goals (CPGs)](https://www.cisa.gov/cpgs): Conjunto de controles prioritarios y medibles emitidos por CISA para mitigar los riesgos de ciberseguridad más comunes en infraestructura crítica."
        ],
        "papers": [
            "**IEEE Access (2023):** *Adversarial Attacks on Machine Learning in Critical Infrastructure: A Systematic Survey* ([DOI: 10.1109/ACCESS.2023.3283296](https://ieeexplore.ieee.org/document/10121435)) — Estudio exhaustivo sobre técnicas de envenenamiento de datos, ataques de evasión y estrategias de robustez en sistemas ciberfísicos.",
            "**ENISA Threat Landscape Report:** *Artificial Intelligence Threat Landscape* ([ENISA Publications](https://www.enisa.europa.eu/publications/artificial-intelligence-threat-landscape)) — Diagnóstico de la Agencia de la Unión Europea para la Ciberseguridad sobre vectores de explotación emergentes en cadenas de suministro estratégicas.",
            "**USENIX Security / arXiv (2021):** *Extracting Training Data from Large Language Models* ([arXiv:2012.07805](https://arxiv.org/abs/2012.07805)) — Investigación clave sobre filtración de secretos, extracción de datos de entrenamiento y vulnerabilidades estructurales en arquitecturas basadas en Transformers."
        ],
        "tools": [
            "[Microsoft Counterfit](https://github.com/Azure/counterfit): Framework de automatización para pruebas de penetración y evaluación de seguridad adversarial en modelos de Machine Learning.",
            "[Adversarial Robustness Toolbox (ART - Linux Foundation)](https://github.com/Trusted-AI/adversarial-robustness-toolbox): Biblioteca en Python para pruebas de evasión, envenenamiento de modelos y análisis de robustez algorítmica frente a adversarios digitales.",
            "[Garak (LLM Vulnerability Scanner)](https://github.com/leondz/garak): Escáner de seguridad dinámico de código abierto especializado en detectar jailbreaks, inyecciones de prompts y vectores de fuga de datos en modelos fundacionales.",
            "[Zeek Network Security Monitor](https://github.com/zeek/zeek): Plataforma de telemetría y análisis de tráfico de red en tiempo real a escala enterprise para la detección de comportamientos anómalos."
        ],
        "learning": [
            "[Microsoft Learn: SC-200 - Mitigación de Amenazas con Microsoft Sentinel y Defender](https://learn.microsoft.com/es-es/training/paths/sc-200-mitigate-threats-using-microsoft-sentinel/): Especialización técnica en operaciones SOC para correlación de eventos y orquestación defensiva basada en analítica avanzada.",
            "[CISA ICS Training Program (Federal Virtual Training Environment)](https://www.cisa.gov/cyber-training): Ruta de entrenamiento técnico del gobierno de EE.UU. sobre seguridad en sistemas de control industrial (ICS/SCADA) y respuesta a incidentes en infraestructura crítica.",
            "[TryHackMe: Defensive Security & Security Operations](https://tryhackme.com/module/defensive-security): Entorno práctico interactivo con laboratorios para detección de amenazas, telemetría de red y ciberdefensa asistida.",
            "[HackTheBox: Enterprise Pro Labs & ICS Challenges](https://www.hackthebox.com): Laboratorios de explotación y aseguramiento de protocolos industriales (Modbus, DNP3, OPC UA) y redes corporativas segmentadas."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/02-lama-infraestructura-dns.md",
        "title": "Infraestructura de Internet: Seguridad, Continuidad y Resiliencia - Guillermo Lama",
        "audio": "../../assets/audio/dia1_02_lama.mp3",
        "prev": "01-wong-ia-cibercrimen.md",
        "next": "03-fernandez-crimen-ia.md",
        "sintesis": (
            "El Sistema de Nombres de Dominio (DNS) constituye la infraestructura crítica fundacional que arbitra la conectividad global y la resolución jerárquica de servicios transaccionales. Su operación en dominios nacionales de nivel superior (ccTLD, como .cl) enfrenta vectores de amenaza complejos, incluyendo ataques volumétricos de denegación distribuida de servicio (DDoS), envenenamiento de caché (cache poisoning) y secuestro de rutas BGP, eventos que amenazan con desarticular la disponibilidad digital de servicios financieros, gubernamentales y asistenciales a escala de país.\n\n"
            "Garantizar la resiliencia sistémica del DNS demanda implementar topologías Anycast distribuidas multirregionales, orquestación automatizada de zonas y la adopción estricta de extensiones criptográficas DNSSEC. La continuidad operativa no puede concebirse como un atributo estático, sino como una capacidad dinámica de absorción de sobrecargas y conmutación por error (failover) transparente, respaldada por gobernanza institucional y acuerdos de intercambio de tráfico en IXPs neutros."
        ),
        "conceptos": [
            "**BGP Anycast Routing:** Técnica de direccionamiento donde múltiples nodos distribuidos geográficamente anuncian la misma IP, dispersando el tráfico legítimo y absorbiendo ataques DDoS en el borde.",
            "**DNSSEC (Domain Name System Security Extensions):** Conjunto de extensiones criptográficas basadas en firmas digitales asimétricas que garantizan la autenticidad e integridad de las respuestas de resolución DNS.",
            "**Root & TLD Name Server Redundancy:** Despliegue de réplicas autoritativas locales para mitigar la latencia y neutralizar fallas de enlaces internacionales en situaciones de aislamiento.",
            "**Amplification & Reflection Attacks:** Vector volumétrico que explota configuraciones de resolutores recursivos abiertos (open resolvers) mediante UDP para inundar enlaces troncales."
        ],
        "frameworks": [
            "[IETF RFC 4033, 4034, 4035 (DNSSEC Specifications)](https://datatracker.ietf.org/doc/html/rfc4033): Estándares oficiales del Internet Engineering Task Force para la arquitectura e implementación de seguridad en DNS.",
            "[NIST SP 800-81-2: Secure Domain Name System Deployment Guide](https://csrc.nist.gov/publications/detail/sp/800-81/2/final): Directrices del NIST para la configuración, operación y aseguramiento criptográfico de servidores DNS autoritativos y recursivos.",
            "[ICANN Security and Stability Advisory Committee (SSAC) Reports](https://www.icann.org/groups/ssac): Informes de autoridad global sobre amenazas a la seguridad, estabilidad y resiliencia del sistema de nombres de Internet.",
            "[ISO/IEC 27001: Control A.13 - Communications Security](https://www.iso.org/standard/27001): Marco normativo internacional para la protección de canales de red y servicios de infraestructura esenciales."
        ],
        "papers": [
            "**ACM SIGCOMM (2020):** *A Global Measurement of DNSSEC Validation: Operational Realities and Resilience* ([DOI: 10.1145/3387514.3405890](https://dl.acm.org/doi/10.1145/3387514.3405890)) — Análisis cuantitativo de la adopción de validación criptográfica en resolutores globales y su impacto en la seguridad del usuario final.",
            "**IEEE/ACM Transactions on Networking (2018):** *Anycast in Context: A Guided Tour of BGP Anycast Routing and DDoS Mitigation* ([IEEE Xplore](https://ieeexplore.ieee.org/document/8387498)) — Estudio seminal sobre la eficiencia de arquitecturas Anycast para dispersar tráfico malicioso en infraestructuras de TLD."
        ],
        "tools": [
            "[NLnet Labs Unbound & NSD](https://github.com/NLnetLabs/unbound): Servidores de nombres recursivos y autoritativos de alto rendimiento con validación DNSSEC nativa desarrollados en C.",
            "[DNSViz](https://github.com/dnsviz/dnsviz): Herramienta analítica de código abierto para diagnóstico visual, auditoría y resolución de cadenas de confianza criptográficas DNSSEC.",
            "[Knot DNS (CZ.NIC)](https://github.com/CZ-NIC/knot): Servidor autoritativo open source optimizado para soportar millones de zonas con recarga dinámica y mitigación Anycast.",
            "[BGPStream](https://bgpstream.caida.org/): Framework de análisis y telemetría en tiempo real desarrollado por CAIDA para monitorear eventos de secuestro (hijacks) de rutas y caídas de conectividad."
        ],
        "learning": [
            "[RIPE NCC Academy: DNSSEC & Routing Security Courses](https://academy.ripe.net/): Certificación gratuita de nivel carrier sobre implementación de DNSSEC, RPKI y aseguramiento de enrutamiento BGP.",
            "[Cloudflare Learning Center: DNS Architecture & DDoS Mitigation](https://www.cloudflare.com/learning/dns/what-is-dns/): Módulos técnicos interactivos sobre resolución jerárquica, Anycast y mecanismos de amortiguación de sobrecargas.",
            "[TryHackMe: Network Fundamentals & DNS in Detail](https://tryhackme.com/module/network-fundamentals): Laboratorios prácticos para inspeccionar tráfico DNS, depurar registros autoritativos y detectar transferencias de zona no autorizadas.",
            "[Cisco NetAcad: Network Security Architecture](https://www.netacad.com): Formación enterprise sobre diseño de perímetros de red, redundancia de servicios troncales e inspección de protocolos."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/03-fernandez-crimen-ia.md",
        "title": "El Lado Práctico del Crimen con IA - Manu Fernández",
        "audio": "../../assets/audio/dia1_03_fernandez_manu.mp3",
        "prev": "02-lama-infraestructura-dns.md",
        "next": "04-bordachar-anci-regulacion.md",
        "sintesis": (
            "La mercantilización de herramientas generativas avanzadas ha democratizado tácticas de ingeniería social de grado militar para organizaciones delictivas de alcance global. A través de la síntesis neuronal de voz (Voice Cloning) y la generación de avatares sintéticos dinámicos en tiempo real, los ciberdelincuentes están ejecutando con éxito ataques de compromiso de correo corporativo (BEC 3.0) y fraudes de autorización financiera, sorteando los filtros de verificación auditiva y visual tradicionales aplicados por el personal operativo.\n\n"
            "Simultáneamente, la fiabilidad de las credenciales biométricas convencionales (reconocimiento facial y huella dactilar) se encuentra en entredicho frente a vectores de ataque de presentación (PAD) construidos con modelos de difusión y máscaras tridimensionales. Neutralizar estas amenazas requiere evolucionar los esquemas de autenticación hacia arquitecturas de confianza cero contextuales, exigiendo desafíos de prueba de vida dinámicos (liveness verification), canales independientes de autorización fuera de banda y una reingeniería profunda de los procesos de autorización corporativa."
        ),
        "conceptos": [
            "**Presentation Attack Detection (PAD):** Conjunto de algoritmos y sensores fisiológicos diseñados para discriminar entre una muestra biométrica humana viva y una suplantación sintética o pregrabada.",
            "**Business Email Compromise 3.0 (AI-BEC):** Evolución del fraude corporativo donde se integran llamadas y videoconferencias sintéticas hiperrealistas para ordenar transferencias monetarias urgentes.",
            "**Voice Biometrics Spoofing:** Técnicas adversariales basadas en síntesis de audio texto-a-voz (TTS) condicionadas a muestras acústicas de pocos segundos para burlar IVRs bancarios.",
            "**Out-of-Band Multi-Factor Authentication (OOB-MFA):** Mecanismo de validación criptográfica que utiliza canales físicos y de red completamente desacoplados para confirmar instrucciones críticas."
        ],
        "frameworks": [
            "[ISO/IEC 30107 (Biometric Presentation Attack Detection Framework)](https://www.iso.org/standard/67381.html): Estándar internacional que regula la evaluación, métricas y pruebas de resistencia frente a ataques de suplantación biométrica.",
            "[NIST SP 800-63-3: Digital Identity Guidelines](https://pages.nist.gov/800-63-3/): Directrices técnicas del NIST sobre niveles de aseguramiento de identidad (IAL), autenticación (AAL) y federación (FAL).",
            "[FIDO Alliance Biometric Certification Requirements](https://fidoalliance.org/certification/biometric-component-certification/): Criterios de certificación independiente para garantizar que los sensores y algoritmos biométricos resistan falsificaciones de alta complejidad.",
            "[MITRE ATT&CK: Technique T1566.002 (Spearphishing Link) & T1656 (Impersonation)](https://attack.mitre.org/techniques/T1656/): Mapeo formal de técnicas de suplantación de identidad e ingeniería social dirigida."
        ],
        "papers": [
            "**IEEE Transactions on Biometrics, Behavior, and Identity Science (2022):** *Deepfake Detection in Biometrics: A Comprehensive Review and Future Directions* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9672074)) — Evaluación de modelos de aprendizaje profundo para identificar anomalías espectrales y micropatrones en rostros sintéticos.",
            "**arXiv / Computer Vision Foundation (2023):** *Real-Time Deepfake Detection via Physiological Dynamics* ([arXiv:2303.04838](https://arxiv.org/abs/2303.04838)) — Propuesta metodológica para validar la pulsación sanguínea dérmica (fotopletismografía remota) en videollamadas."
        ],
        "tools": [
            "[FaceForensics++ Toolkit](https://github.com/ondyari/FaceForensics): Benchmark y biblioteca forense de referencia desarrollada por la Universidad Técnica de Múnich para detección de manipulaciones faciales.",
            "[DeepFaceLab](https://github.com/iperov/DeepFaceLab): Framework de código abierto líder en pipeline de generación neural facial, utilizado por investigadores para diseñar defensas y pruebas de penetración biométrica.",
            "[OpenFace 2.0](https://github.com/TadasBaltrusaitis/OpenFace): Herramienta de análisis facial open source capaz de capturar microexpresiones y puntos de referencia de mirada para detectar patrones sintéticos anómalos.",
            "[Canarytokens (Thinkst Canary)](https://github.com/thinkst/canarytokens): Generador de señuelos digitales y trampas de credenciales para alertar tempranamente accesos no autorizados en canales corporativos."
        ],
        "learning": [
            "[Microsoft Learn: Implementación de Soluciones Biométricas con Azure AI Face](https://learn.microsoft.com/es-es/training/modules/detect-analyze-faces/): Módulo técnico sobre integración de verificación facial, detección de máscaras y prueba de vida.",
            "[AWS Skill Builder: Architecting Identity and Access Management](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-identity-and-access-management-iam-foundations): Formación sobre políticas de mínimo privilegio, autenticación multifactor contextual y control de accesos federados.",
            "[TryHackMe: Phishing & Social Engineering Analysis](https://tryhackme.com/module/phishing): Laboratorios interactivos para analizar cabeceras de correo, desarmar señuelos de ingeniería social y desplegar contramedidas en gateways.",
            "[SANS Cyber Defense Community Curriculum](https://www.sans.org): Recursos abiertos sobre mitigación de fraudes ejecutivos y procedimientos de control interno ante incidentes financieros."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/04-bordachar-anci-regulacion.md",
        "title": "Ciberseguridad y Resiliencia: Un Desafío Nacional - Michelle Bordachar",
        "audio": "../../assets/audio/dia1_04_bordachar.mp3",
        "prev": "03-fernandez-crimen-ia.md",
        "next": "05-evirtus-efecto-domino.md",
        "sintesis": (
            "La promulgación de la Ley Marco de Ciberseguridad (Ley N° 21.663) y la creación de la Agencia Nacional de Ciberseguridad (ANCI) marcan un punto de inflexión institucional en la gobernanza tecnológica de Chile. La normativa establece un régimen vinculante de deberes preventivos, estándares operacionales y fiscalización técnica, transitando de un modelo de recomendaciones voluntarias hacia una doctrina de cumplimiento regulatorio estricto con responsabilidad directa para directores y gerentes de organizaciones públicas y privadas.\n\n"
            "Un eje neurálgico del marco es la calificación formal de Operadores de Importancia Vital (OIV) e Instituciones Proveedoras de Servicios Esenciales. Dichas entidades quedan sujetas a obligaciones de implementación de sistemas de gestión de seguridad de la información, auditorías externas periódicas y protocolos de notificación obligatoria de incidentes graves en plazos perentorios de pocas horas. La gobernanza de la ciberseguridad se consolida así como un componente irrenunciable de la seguridad nacional y la estabilidad económica del país."
        ),
        "conceptos": [
            "**Operadores de Importancia Vital (OIV):** Designación jurídica para entidades cuya interrupción operativa genera un impacto severo sobre la seguridad pública, la salud o el abastecimiento de la población.",
            "**Mandatory Incident Reporting:** Obligación legal de notificar brechas de seguridad e incidentes disruptivos ante la autoridad rectora en plazos mínimos definidos para coordinar la respuesta nacional.",
            "**Cybersecurity Regulatory Governance:** Integración de la gestión del riesgo cibernético dentro del marco fiduciario y de responsabilidad legal del directorio y la alta administración.",
            "**National CSIRT Coordination:** Esquema de articulación operativa multisectorial liderado por la ANCI para emitir alertas tempranas y contener vectores de ataque antes de su propagación."
        ],
        "frameworks": [
            "[Ley N° 21.663 - Ley Marco de Ciberseguridad de Chile](https://www.bcn.cl/leychile/navegar?idNorma=1202517): Texto legal oficial publicado en la Biblioteca del Congreso Nacional que crea la ANCI y fija las obligaciones para OIV.",
            "[Directiva NIS 2 (Directiva UE 2022/2555)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj): Marco regulatorio europeo de alta exigencia para la resiliencia de entidades esenciales e importantes, referencia global para legislaciones modernas.",
            "[ISO/IEC 27103: Cybersecurity and ISO and IEC Standards](https://www.iso.org/standard/64104.html): Guía de buenas prácticas para mapear requerimientos legales y regulatorios nacionales a la familia de normas ISO/IEC 27000.",
            "[CISA CIRCIA (Cyber Incident Reporting for Critical Infrastructure Act)](https://www.cisa.gov/circia): Estatuto de EE.UU. que norma la obligatoriedad de notificación de incidentes graves en 72 horas y pagos de ransomware en 24 horas."
        ],
        "papers": [
            "**Harvard Belfer Center (2022):** *National Cyber Power Index and the Architecture of Regulatory Compliance* ([Belfer Center](https://www.belfercenter.org/publication/national-cyber-power-index-2022)) — Metodología comparada sobre cómo las democracias articulan agencias nacionales de ciberseguridad y mandatos a infraestructuras vitales.",
            "**Oxford Cybersecurity Centre (2021):** *Harmonizing Cyber Incident Reporting: Operational and Legal Challenges* ([Oxford Academic](https://academic.oup.com/cybersecurity/)) — Análisis de la fricción entre confidencialidad corporativa y deberes de reporte público en operadores críticos."
        ],
        "tools": [
            "[OpenCTI (Open Cyber Threat Intelligence)](https://github.com/OpenCTI-Platform/opencti): Plataforma enterprise open source para estructurar, almacenar y correlacionar información de amenazas compatible con estándares STIX2.",
            "[MISP (Malware Information Sharing Platform)](https://github.com/MISP/MISP): Herramienta colaborativa adoptada por gobiernos y CSIRTs globales para el intercambio automatizado de indicadores de compromiso (IoCs).",
            "[Eramba GRC Platform](https://www.eramba.org/): Sistema de gobernanza, riesgo y cumplimiento de código abierto diseñado para auditar controles ISO 27001, NIS 2 y leyes de ciberseguridad.",
            "[TheHive Project](https://github.com/TheHive-Project/TheHive): Plataforma escalable de gestión y respuesta a incidentes de seguridad diseñada para equipos SOC y CSIRT nacionales."
        ],
        "learning": [
            "[ENISA Training Resources for CSIRTs](https://www.enisa.europa.eu/topics/training-and-exercises): Módulos oficiales de formación técnica sobre gestión de crisis, marco legal y procedimientos de coordinación ante incidentes.",
            "[Cisco NetAcad: Cybersecurity Governance, Law and Compliance](https://www.netacad.com): Curso sobre marcos de gobernanza corporativa, auditoría de sistemas y responsabilidad civil/penal en tecnologías de la información.",
            "[Coursera / Erasmus University Rotterdam: European Cyber Security Law and Policy](https://www.coursera.org): Especialización en regulación digital, deberes de notificación de brechas y cumplimiento normativo internacional.",
            "[TryHackMe: Incident Handling Process (IH&R)](https://tryhackme.com/module/incident-response): Laboratorios para ejercitar la cadena de custodia, reporte técnico y documentación forense ante requerimientos legales."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/05-evirtus-efecto-domino.md",
        "title": "Un Incidente, Múltiples Impactos: La Criticidad de la Ciberseguridad - Representante Técnico Sectorial (E-Virtus)",
        "audio": "../../assets/audio/dia1_05_evirtus_incidentes.mp3",
        "prev": "04-bordachar-anci-regulacion.md",
        "next": "06-fernandez-dispositivos-medicos.md",
        "sintesis": (
            "La hiperconectividad de los ecosistemas productivos modernos ha transformado las cadenas de suministro en el principal vector de intrusión estratégica hacia infraestructuras críticas. Los adversarios informáticos reconocen que las corporaciones matrices invierten millones en defensas perimetrales directas, por lo que desvían su foco ofensivo hacia proveedores externos de servicios gestionados (MSPs), contratistas de mantenimiento y desarrolladores de software de terceros que poseen accesos VPN directos y credenciales privilegiadas dentro de la red interna.\n\n"
            "Un incidente aislado en un eslabón logístico o de soporte técnico desata un efecto dominó que trasciende fronteras operativas: la paralización de flujos de distribución de combustible detiene el transporte público, inhabilita generadores auxiliares en hospitales y colapsa cadenas de frío en la industria alimentaria. Diseñar organizaciones resilientes exige adoptar una doctrina de gestión del riesgo en la cadena de suministro (C-SCRM), restringiendo accesos permanentes mediante modelos Just-In-Time (JIT) y auditando exhaustivamente la postura técnica de cada actor interconectado."
        ),
        "conceptos": [
            "**Cybersecurity Supply Chain Risk Management (C-SCRM):** Disciplina formal orientada a identificar, evaluar y mitigar los riesgos derivados del aprovisionamiento de software, hardware y servicios externos.",
            "**Cascading Infrastructure Failure:** Dinámica donde el colapso funcional de un sector crítico (ej. energía o logística) desencadena fallas consecutivas en sectores dependientes (salud, finanzas, agua).",
            "**Just-In-Time (JIT) Privileged Access:** Paradigma de control que otorga privilegios administrativos a proveedores únicamente durante la ventana de mantenimiento requerida, revocándolos de manera automática.",
            "**Third-Party Attack Surface:** Porción de la red corporativa y activos digitales accesibles directa o indirectamente por socios comerciales y subcontratistas."
        ],
        "frameworks": [
            "[NIST SP 800-161 Rev. 1: Cybersecurity Supply Chain Risk Management Practices](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final): Guía integral del NIST para integrar la gestión de riesgos de proveedores en sistemas de información federales y empresariales.",
            "[CISA & NSA: Defending Against Software Supply Chain Attacks](https://www.cisa.gov/resources-tools/resources/defending-against-software-supply-chain-attacks): Recomendaciones técnicas conjuntas para evaluar la integridad de código y repositorios de terceros.",
            "[ISO 28000: Security Management Systems for the Supply Chain](https://www.iso.org/standard/79612.html): Norma internacional para certificar la gestión de la seguridad en cadenas de suministro industriales y logísticas.",
            "[ENISA Good Practices for Supply Chain Cybersecurity](https://www.enisa.europa.eu/publications/good-practices-for-supply-chain-cybersecurity): Mapeo de controles preventivos y cláusulas contractuales exigibles a proveedores tecnológicos."
        ],
        "papers": [
            "**ACM Computing Surveys (2023):** *A Survey on Software Supply Chain Security: Vulnerabilities, Attacks, and Defenses* ([DOI: 10.1145/3604930](https://dl.acm.org/doi/10.1145/3604930)) — Análisis sistemático sobre inyección de código malicioso en repositorios públicos y manipulación de paquetes de compilación.",
            "**IEEE Security & Privacy (2021):** *Analyzing Downstream Cascades in Industrial Supply Networks* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9444458)) — Modelado cuantitativo de propagación de incidentes cibernéticos a través de redes de distribución automatizadas."
        ],
        "tools": [
            "[OpenSSF Scorecard](https://github.com/ossf/scorecard): Herramienta automatizada de la Open Source Security Foundation para evaluar riesgos de seguridad y posturas de mantenimiento en dependencias de código.",
            "[Syft & Grype (Anchore)](https://github.com/anchore/syft): Utilidades de terminal open source para generar listas de materiales de software (SBOM) y escanear vulnerabilidades en contenedores y archivos binarios.",
            "[Sigstore / Cosign](https://github.com/sigstore/cosign): Estándar y herramienta criptográfica para la firma digital de contenedores, binarios y artefactos de software, asegurando la no manipulación de la cadena.",
            "[BloodHound Community Edition](https://github.com/SpecterOps/BloodHound): Herramienta analítica de relaciones de Active Directory para mapear rutas de ataque y permisos ocultos otorgados a cuentas de proveedores externos."
        ],
        "learning": [
            "[Linux Foundation: LFX - Securing the Software Supply Chain](https://training.linuxfoundation.org/): Capacitación gratuita sobre estándares SLSA, generación de SBOM y verificación criptográfica de dependencias.",
            "[Microsoft Learn: Implementación de Control de Acceso Just-In-Time con Microsoft Entra ID](https://learn.microsoft.com/es-es/training/modules/manage-privileged-access/): Módulo técnico sobre asignación temporal de roles privilegiados y reducción de la superficie de ataque.",
            "[TryHackMe: Attacking & Defending Supply Chains](https://tryhackme.com/module/vulnerability-management): Laboratorios interactivos sobre análisis de vulnerabilidades en librerías de terceros y contención de movimientos laterales.",
            "[AWS Skill Builder: Supply Chain Security & Governance](https://explore.skillbuilder.aws): Rutas de arquitectura en la nube para auditar accesos de proveedores y segregar entornos de producción."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/06-fernandez-dispositivos-medicos.md",
        "title": "Anatomía de un Dispositivo Médico Conectado: Explorando sus Superficies de Ataque - Víctor Fernández",
        "audio": "../../assets/audio/dia1_06_fernandez_victor.mp3",
        "prev": "05-evirtus-efecto-domino.md",
        "next": "07-panel-sectores-criticos.md",
        "sintesis": (
            "El despliegue masivo del Internet de las Cosas Médicas (IoMT) en redes hospitalarias contemporáneas ha expandido drásticamente la superficie de ataque ciberfísica en el sector salud. Equipos de soporte vital como bombas de infusión continua, monitores de constantes hemodinámicas y desfibriladores implantables incorporan interfaces inalámbricas (WiFi, BLE) y pilas de red embebidas que fueron concebidas para maximizar la interoperabilidad clínica, postergando con frecuencia los mecanismos básicos de autenticación criptográfica y validación de entrada.\n\n"
            "Un compromiso de seguridad en este vector trasciende la filtración de datos clínicos personales: constituye una amenaza directa e inminente para la vida del paciente. Atacantes con presencia en la red local o que explotan vulnerabilidades en firmwares desactualizados pueden alterar remotamente la velocidad de dosificación de fármacos vasoactivos o inducir lecturas diagnósticas falsas en salas de terapia intensiva. Blindar estos entornos exige una estricta microsegmentación de redes clínicas mediante VLANs médicas dedicadas, auditorías continuas de interfaces de hardware (JTAG/UART) y un compromiso formal de los fabricantes con el principio de seguridad por diseño."
        ),
        "conceptos": [
            "**IoMT (Internet of Medical Things):** Ecosistema de dispositivos médicos conectados en red que recopilan, transmiten y actúan sobre datos clínicos en tiempo real.",
            "**Hardware Attack Surface (JTAG/UART):** Interfaces físicas de depuración en placas de circuitos que, de quedar expuestas o sin bloqueo criptográfico, permiten la extracción directa de firmware y claves privadas.",
            "**Clinical Network Microsegmentation:** Aislamiento lógico estricto del tráfico de dispositivos médicos respecto de las redes administrativas del hospital y el tráfico de internet de visitas.",
            "**Coordinated Vulnerability Disclosure (CVD):** Protocolo ético y seguro entre investigadores de seguridad, fabricantes de instrumental médico y agencias reguladoras sanitarias para parchar fallas sin poner en riesgo a los pacientes."
        ],
        "frameworks": [
            "[FDA: Cybersecurity in Medical Devices - Quality System System Regulations](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity): Guía regulatoria obligatoria de la FDA de EE.UU. que exige documentación de ciberseguridad y SBOM para dispositivos médicos conectados.",
            "[IEC 81001-5-1: Health Software and Health IT Systems Cybersecurity](https://www.iso.org/standard/76503.html): Estándar internacional sobre actividades del ciclo de vida de desarrollo seguro para software e infraestructura médica.",
            "[NIST SP 800-53: Healthcare Overlay for Information Security Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final): Catálogo de controles de seguridad federales adaptados específicamente a la preservación de la vida en entornos clínicos.",
            "[MDCG 2019-16: Guidance on Cybersecurity for Medical Devices (Unión Europea)](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en): Marco europeo de cumplimiento para el marcado CE de equipamiento médico digital."
        ],
        "papers": [
            "**Journal of Medical Systems (2021):** *Vulnerability Assessment and Attack Surface Mapping in Connected Infusion Pumps* ([DOI: 10.1007/s10916-021-01789-5](https://link.springer.com/journal/10916)) — Estudio forense experimental sobre explotación de memoria y control remoto en sistemas de dispensación hospitalaria.",
            "**IEEE Internet of Things Journal (2023):** *Cyber-Physical Security in Connected Healthcare: Threat Modeling, Vulnerabilities, and Countermeasures* ([IEEE Xplore](https://ieeexplore.ieee.org/document/10041235)) — Mapeo integral de vectores de intrusión contra dispositivos IoMT y protocolos propietarios inalámbricos."
        ],
        "tools": [
            "[Scapy (Packet Manipulation Tool)](https://github.com/secdev/scapy): Potente biblioteca en Python para forjar, decodificar y analizar paquetes de red en protocolos médicos propietarios y diagnósticos HL7/DICOM.",
            "[Frida (Dynamic Instrumentation Toolkit)](https://github.com/frida/frida): Herramienta de inyección de código para auditoría en caliente de aplicaciones de control médico y depuración de ejecutables embebidos.",
            "[Ghidra (NSA Reverse Engineering Suite)](https://github.com/NationalSecurityAgency/ghidra): Framework de ingeniería inversa para desensamblar y decompilar imágenes de firmware de dispositivos médicos extraídas por puertos físicos.",
            "[Wireshark (con Dissectores Médicos HL7/DICOM)](https://github.com/wireshark/wireshark): Analizador de protocolos de red para inspeccionar comunicaciones biomédicas no cifradas y detectar anomalías en tiempo real."
        ],
        "learning": [
            "[CISA Healthcare and Public Health (HPH) Sector Training](https://www.cisa.gov/topics/critical-infrastructure-sectors/healthcare-and-public-health): Rutas de concientización y aseguramiento de infraestructura clínica para profesionales de IT y biomédica.",
            "[Biohacking Village DEF CON Open Resources](https://www.villageb.io/): Charlas magistrales, talleres y laboratorios prácticos sobre ingeniería inversa de marcapasos, bombas y resonadores magnéticos.",
            "[HackTheBox: Hardware & IoT Hacking Tracks](https://www.hackthebox.com): Laboratorios técnicos sobre volcado de memoria Flash, emulación de arquitecturas ARM/MIPS y explotación de puertos UART.",
            "[TryHackMe: Wireshark Traffic Analysis](https://tryhackme.com/module/network-security): Módulo práctico para adquirir maestría en inspección de paquetes, filtros de captura y detección de balizas maliciosas."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/07-panel-sectores-criticos.md",
        "title": "Protegiendo lo Esencial: Ciberseguridad y Resiliencia en Sectores Críticos - Panel Multisectorial (Codelco, CEN, Aguas Andinas, CSIRT)",
        "audio": "../../assets/audio/dia1_07_panel_multisectorial.mp3",
        "prev": "06-fernandez-dispositivos-medicos.md",
        "next": "08-bonnaire-agentes-ia.md",
        "sintesis": (
            "La defensa técnica de los pilares productivos del país (minería de gran escala, despacho eléctrico interconectado, distribución de agua potable y coordinación gubernamental) expone la tensión estructural existente entre las tecnologías de la información (TI) y las tecnologías operativas (TO). En los entornos industriales, el paradigma tradicional de confidencialidad cede el paso a la supremacía absoluta de la disponibilidad y la seguridad física (Safety). Los controladores lógicos programables (PLC) y las unidades terminales remotas (RTU) ejecutan procesos continuos de alta presión que no toleran reinicios aleatorios ni ventanas intempestivas para la aplicación de parches.\n\n"
            "Los líderes de la industria subrayan que los grupos de ciberdelincuencia y los agentes patrocinados por estados hostiles actúan con un pragmatismo oportunista: buscan la vía de menor resistencia técnica para interrumpir el servicio. Frente a este escenario, la cooperación multisectorial y el intercambio en tiempo real de Indicadores de Compromiso (IoCs) a través del CSIRT Nacional constituyen la barrera defensiva más eficaz. La verdadera resiliencia no reside únicamente en la capacidad de resistir intrusiones, sino en garantizar planes de maniobra analógica y procedimientos de contingencia degradada que permitan operar manualmente ante la caída total de los sistemas informáticos."
        ),
        "conceptos": [
            "**IT/OT Convergence & Purdue Model:** Integración de redes corporativas con sistemas de control industrial, requiriendo segmentación jerárquica estricta (Nivel 0 a Nivel 5) para aislar actuadores físicos.",
            "**Operational Technology (OT) Safety Supremacy:** Filosofía de diseño industrial donde la protección de la vida humana y la integridad física de las instalaciones priman sobre la confidencialidad de la información.",
            "**Degraded Mode Operations (Analog Fallback):** Capacidad operacional entrenada de una central eléctrica o planta hidráulica para operar con mandos manuales mecánicos durante un apagón cibernético prolongado.",
            "**Cross-Sector Threat Sharing:** Protocolos automatizados de inteligencia compartida donde una amenaza detectada en una minera blinda preventivamente al sector energético y sanitario."
        ],
        "frameworks": [
            "[ISA/IEC 62443 Series: Security for Industrial Automation and Control Systems](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa62443): Estándar de oro global que define la arquitectura por zonas y conductos (Zones and Conduits) para redes de control industrial.",
            "[NERC CIP (Critical Infrastructure Protection Standards)](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx): Marco regulatorio obligatorio en Norteamérica para la ciberseguridad del sistema eléctrico de potencia interconectado.",
            "[NIST SP 800-82 Rev. 3: Guide to Operational Technology (OT) Security](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final): Directrices técnicas del NIST sobre mitigación de amenazas en sistemas SCADA, DCS y PLCs.",
            "[Marco Sectorial de Ciberseguridad del Coordinador Eléctrico Nacional](https://www.coordinador.cl): Normativa técnica y estándares de reporte de incidentes para el Sistema Eléctrico Nacional chileno."
        ],
        "papers": [
            "**IEEE Transactions on Smart Grid (2022):** *Cyber-Physical Resilience in Power Grids: Detection, Mitigation, and Restoration* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9779342)) — Modelado de dinámicas de red eléctrica frente a ataques coordinados de deslastre de carga por compromiso de RTUs.",
            "**Reliability Engineering & System Safety (2021):** *Modeling Cross-Sector Cascading Failures in Coupled Critical Infrastructures* ([DOI: 10.1016/j.ress.2021.107693](https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety)) — Análisis estocástico sobre cómo un fallo en telecomunicaciones o agua interrumpe operaciones de minería y generación termoeléctrica."
        ],
        "tools": [
            "[Malcolm (CISA & Idaho National Laboratory)](https://github.com/cisagov/Malcolm): Suite de análisis de tráfico de red de código abierto orientada a protocolos industriales (Modbus, DNP3, EtherNet/IP) basada en Zeek y Suricata.",
            "[GRASSMARLIN (National Security Agency)](https://github.com/iadgov/grassmarlin): Herramienta de la NSA para mapeo pasivo de topologías de red en sistemas de control industrial y detección de violaciones al modelo Purdue.",
            "[OpenPLC Project](https://github.com/thiagoralves/OpenPLC_v3): Plataforma de controlador lógico programable open source compatible con estándar IEC 61131-3, ideal para investigación y simulación defensiva.",
            "[ScadaBR](https://github.com/ScadaBR/ScadaBR): Software de código abierto para supervisión y adquisición de datos (SCADA) utilizado para pruebas de laboratorio y monitoreo de procesos."
        ],
        "learning": [
            "[CISA ICS-CERT Virtual Learning Courses (101 & 201)](https://www.cisa.gov/ics-training-available-through-cisa): Cursos oficiales gratuitos con acreditación sobre arquitecturas de ciberdefensa en infraestructuras de control industrial.",
            "[SANS Industrial Cybersecurity Community Curriculum](https://www.sans.org/cyber-security-courses/ics-scada-cyber-security-essentials/): Whitepapers, hojas de trucos y talleres abiertos sobre defensa de plantas eléctricas y acueductos.",
            "[TryHackMe: Industrial Control Systems Room](https://tryhackme.com/module/defensive-security): Laboratorio interactivo para explorar el modelo Purdue, descifrar tramas Modbus y mitigar inyecciones maliciosas de comandos PLC.",
            "[Cisco NetAcad: OT Network Architecture & Industrial Switching](https://www.netacad.com): Especialización técnica en despliegue de switches industriales resistentes y microsegmentación de subestaciones."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/08-bonnaire-agentes-ia.md",
        "title": "Agentes IA e Infraestructura Crítica: Entre la Falla Operativa y el Arma de Ciberguerra - Dr. Xavier Bonnaire",
        "audio": "../../assets/audio/dia1_08_bonnaire.mp3",
        "prev": "07-panel-sectores-criticos.md",
        "next": "09-evirtus-zero-trust.md",
        "sintesis": (
            "La delegación de bucles de decisión autónomos a agentes de Inteligencia Artificial en entornos de infraestructura crítica introduce vulnerabilidades epistemológicas y operativas sin precedentes. A medida que las redes de distribución eléctrica, plantas químicas y centros de control de transporte integran modelos basados en aprendizaje por refuerzo y arquitecturas de lenguaje para optimizar flujos en tiempo real, se diluyen las garantías deterministas tradicionales de la ingeniería de control, abriendo la puerta a fallas catastróficas inducidas por sesgos algorítmicos, datos envenenados o desalineación de objetivos.\n\n"
            "El Dr. Xavier Bonnaire enfatiza la delgada y peligrosa frontera entre un error de software no intencionado (alucinación, colapso de gradiente o desvío estocástico) y un ataque deliberado de ciberguerra encubierto. En el plano de la soberanía digital, un agente comprometido puede ser manipulado mediante ataques de inyección indirecta de prompts o descalibración imperceptible de sensores para provocar sabotajes ciberfísicos que simulan anomalías naturales. Resulta imperativo consagrar normativamente el principio de Human-in-the-Loop y exigir mecanismos analógicos de desacoplamiento físico e irreversible (Kill-Switch) como salvaguarda innegociable."
        ),
        "conceptos": [
            "**Human-in-the-Loop (HITL) Architecture:** Diseño de sistemas donde las decisiones operacionales de impacto físico o vital deben ser explícitamente autorizadas por un operador humano calificado antes de su ejecución.",
            "**Indirect Prompt Injection in Autonomous Agents:** Ataque donde un agente inteligente procesa entradas no confiables del entorno físico o de red que contienen instrucciones maliciosas ocultas que subvierten sus directrices de seguridad.",
            "**Stochastic Drift vs. Deliberate Cyber-Sabotage:** Dificultad forense para distinguir si una orden anómala emitida por un modelo fue fruto de una desviación estadística natural o de un exploit patrocinado por un actor adversarial.",
            "**Deterministic Safety Envelope:** Capa dura de reglas invariables implementadas a nivel de hardware o lógica booleana que bloquea cualquier comando del agente de IA que viole los límites térmicos o mecánicos seguros."
        ],
        "frameworks": [
            "[OWASP Top 10 for Large Language Model Applications & Autonomous Agents](https://owasp.org/www-project-top-10-for-large-language-model-applications/): Estándar de la industria que categoriza vulnerabilidades críticas como inyección de prompts, consumo inseguro de salidas y manejo indebido de plugins.",
            "[IEEE 7000-2021: Model Process for Addressing Ethical and Safety Concerns in System Design](https://standards.ieee.org/ieee/7000/7048/): Estándar internacional para la gobernanza de sistemas autónomos e inteligentes.",
            "[NIST AI Trustworthy and Responsible AI Resource Center](https://www.nist.gov/itl/ai-risk-management-framework): Principios rectores sobre precisión, explicabilidad, robustez y gobernanza en sistemas de inteligencia artificial de alto riesgo.",
            "[ISO/IEC 42001: Artificial Intelligence Management System (AIMS)](https://www.iso.org/standard/81230.html): Norma certificable global para la gobernanza corporativa y aseguramiento del ciclo de vida de productos basados en IA."
        ],
        "papers": [
            "**arXiv / Stanford AI Safety (2023):** *Safety and Security Challenges of Autonomous LLM Agents: A Comprehensive Survey* ([arXiv:2308.00029](https://arxiv.org/abs/2308.00029)) — Investigación sobre riesgos de ejecución de código no autorizado, manipulación de herramientas externas y derivas operativas en agentes autónomos.",
            "**Science Robotics (2022):** *Safety Guarantees and Failure Modes of Deep Reinforcement Learning in Physical Control Systems* ([DOI: 10.1126/scirobotics.abm6595](https://www.science.org/journal/scirobotics)) — Evaluación de cómo perturbaciones mínimas en sensores pueden inducir inestabilidad física destructiva en actuadores industriales."
        ],
        "tools": [
            "[Promptfoo (LLM Red Teaming & Security Testing)](https://github.com/promptfoo/promptfoo): Herramienta de línea de comandos para automatizar pruebas de robustez, inyección de prompts y fugas de contexto en pipelines de IA generativa.",
            "[NeMo Guardrails (NVIDIA)](https://github.com/NVIDIA/NeMo-Guardrails): Framework open source para programar barreras de contención lógicas y temáticas alrededor de modelos de lenguaje en aplicaciones críticas.",
            "[LangKit (Whylabs)](https://github.com/whylabs/langkit): Biblioteca de telemetría y métricas para monitorear en tiempo real la toxicidad, detección de prompts maliciosos y calidad de respuestas en agentes autónomos.",
            "[Giskard (Quality & Security Testing for AI)](https://github.com/Giskard-AI/giskard): Plataforma de código abierto para auditoría de modelos tabulares y LLMs frente a vulnerabilidades de rendimiento, alucinaciones y sesgos."
        ],
        "learning": [
            "[DeepLearning.AI: Red Teaming LLM Applications](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/): Curso técnico especializado en técnicas adversariales para evaluar vulnerabilidades y diseñar defensas en agentes inteligentes.",
            "[Microsoft Learn: Principios y Prácticas de IA Responsable](https://learn.microsoft.com/es-es/training/paths/responsible-ai-business-principles/): Módulos sobre equidad, fiabilidad, seguridad, privacidad y rendición de cuentas en modelos automatizados.",
            "[TryHackMe: Prompt Injection & Adversarial AI Exploitation](https://tryhackme.com/module/defensive-security): Laboratorios interactivos para analizar cómo los agentes procesan entradas engañosas y cómo aplicar defensas programáticas.",
            "[Coursera / Johns Hopkins University: Trustworthy AI and Autonomous Systems](https://www.coursera.org): Formación de posgrado abierta sobre verificación formal y contención de fallas en sistemas de control guiados por algoritmos."
        ]
    },
    {
        "path": "malla-curricular/02-dia1-seminario/09-evirtus-zero-trust.md",
        "title": "Seguridad en la Red: Hacia una Infraestructura Crítica Resiliente - Especialista en Redes (E-Virtus)",
        "audio": "../../assets/audio/dia1_09_evirtus_redes.mp3",
        "prev": "08-bonnaire-agentes-ia.md",
        "next": "10-caceres-blue-team-ia.md", # Link a dia 2
        "sintesis": (
            "El modelo de seguridad perimetral tradicional (Castillo y Foso) ha quedado formalmente obsoleto frente al auge del trabajo híbrido, la dispersión de cargas en nubes múltiples y la proliferación de credenciales corporativas robadas. Asumir que cualquier dispositivo o usuario conectado dentro de la red corporativa es inherentemente confiable constituye una vulnerabilidad estructural crítica: una vez que el adversario franquea el firewall de borde, disfruta de libertad irrestricta para ejecutar escaneos laterales no detectados y propagar ransomware hacia servidores transaccionales y salas de control industrial.\n\n"
            "La construcción de una infraestructura verdaderamente resiliente exige la adopción integral del paradigma de Confianza Cero (Zero Trust: 'Nunca confíes, siempre verifica'). Este modelo descompone la red en microsegmentos granulares donde cada petición de conexión, tanto este-oeste como norte-sur, debe autenticarse, autorizarse y cifrarse continuamente en función de la identidad de la carga de trabajo, la postura del dispositivo y el contexto de riesgo. Si un endpoint en el área administrativa resulta infectado, las políticas de microsegmentación actúan como mamparas estancas en un buque, impidiendo que el compromiso alcance los sistemas SCADA de control eléctrico o bombeo de agua."
        ),
        "conceptos": [
            "**Zero Trust Architecture (ZTA):** Paradigma de ciberseguridad que asume la red interna como hostil y exige autenticación y autorización continua para cada acceso a recursos.",
            "**East-West Microsegmentation:** División granular de la red interna para inspeccionar y bloquear el tráfico lateral no autorizado entre servidores de un mismo segmento o centro de datos.",
            "**Least Privilege Principle (POLP):** Asignación estricta del mínimo nivel de acceso y permisos temporales necesarios para que un usuario o máquina ejecute su tarea legítima.",
            "**Software-Defined Perimeter (SDP):** Tecnología que vuelve invisibles los servicios de infraestructura en internet, otorgando conectividad encriptada uno a uno solo tras una validación de identidad rigurosa."
        ],
        "frameworks": [
            "[NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final): Documento fundacional y estándar de referencia que describe los componentes lógicos (Policy Engine, Policy Administrator, PEP) de una arquitectura de confianza cero.",
            "[CISA Zero Trust Maturity Model 2.0](https://www.cisa.gov/zero-trust-maturity-model): Guía técnica para que organizaciones evalúen y evolucionen su madurez en cinco pilares: Identidad, Dispositivos, Redes, Cargas de trabajo y Datos.",
            "[DoD Zero Trust Strategy and Roadmap](https://dodcio.defense.gov/Cybersecurity/Zero-Trust/): Marco estratégico del Departamento de Defensa de EE.UU. para implementar Zero Trust a escala global en entornos de máxima criticidad.",
            "[ISO/IEC 27033 Series: Information Technology - Network Security](https://www.iso.org/standard/63462.html): Conjunto de normas internacionales sobre arquitectura, diseño, implementación y aseguramiento de redes corporativas."
        ],
        "papers": [
            "**IEEE Communications Surveys & Tutorials (2021):** *Zero Trust Architecture: A Comprehensive Survey and Future Directions* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9485088)) — Revisión exhaustiva sobre protocolos, mecanismos de decisión contextual y desafíos de despliegue en redes híbridas.",
            "**ACM Digital Threats: Research and Practice (2022):** *Microsegmentation in Industrial Networks: Evaluating Latency and Resilience under Attack* ([DOI: 10.1145/3510582](https://dl.acm.org/journal/dtrap)) — Análisis experimental del impacto operativo de firewalls basados en host sobre controladores industriales."
        ],
        "tools": [
            "[Cilium (eBPF-based Networking & Security)](https://github.com/cilium/cilium): Plataforma de código abierto para observabilidad, conectividad y aplicación de políticas de seguridad Zero Trust en contenedores y Linux mediante tecnología eBPF.",
            "[Tailscale / WireGuard](https://github.com/tailscale/tailscale): Red en malla segura de código abierto basada en el protocolo WireGuard que implementa acceso de confianza cero sin requerir complejas VPNs centralizadas.",
            "[Open Policy Agent (OPA)](https://github.com/open-policy-agent/opa): Motor de políticas de propósito general de código abierto que permite unificar y desacoplar el control de autorización en APIs, redes y microservicios.",
            "[SPIFFE / SPIRE](https://github.com/spiffe/spire): Estándares y herramientas de la Cloud Native Computing Foundation (CNCF) para emitir identidades criptográficas mutuas y efímeras entre cargas de trabajo heterogéneas."
        ],
        "learning": [
            "[Microsoft Learn: SC-100 - Arquitecto de Ciberseguridad: Diseño de Estrategias Zero Trust](https://learn.microsoft.com/es-es/training/paths/sc-100-design-zero-trust-strategy/): Especialización técnica oficial para planificar e implementar arquitecturas de confianza cero empresariales.",
            "[AWS Skill Builder: Implementing Zero Trust on AWS Cloud](https://explore.skillbuilder.aws): Capacitación técnica sobre autenticación contextual, políticas de red privadas y cifrado en tránsito continuo.",
            "[Cisco NetAcad: Network Security Architecture & Defense](https://www.netacad.com): Formación profesional sobre configuración de cortafuegos de próxima generación (NGFW), VPNs IPSec y políticas de acceso 802.1X.",
            "[TryHackMe: Network Security & Traffic Analysis](https://tryhackme.com/module/network-security): Laboratorios interactivos para diseñar reglas de firewall iptables, inspeccionar tráfico cifrado TLS y segmentar subredes virtuales."
        ]
    }
]

print("Script cargado con lecciones base. Generando módulos...")
