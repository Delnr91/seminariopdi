# 🛡️ Knowledge Base: Ciberseguridad e Infraestructura Crítica (Lattices Architecture)

Base de conocimiento abierta de alto nivel técnico sobre **protección de infraestructura crítica, inteligencia artificial adversarial y ciberresiliencia**. Este repositorio recopila y expande las ponencias técnicas del 9° Seminario Internacional de Ciberseguridad (PDI-USM) junto a un análisis exhaustivo de los tres principales modelos regulatorios globales (EE.UU./UK, China y Rusia).

El material está estructurado bajo los estándares de ingeniería de contenidos de **Lattices** para profesionales de ciberdefensa, arquitectos de infraestructura e investigadores.

---

## 🧭 Malla Curricular, Minutaje de Transmisiones y Laboratorios Open Source

Cada lección incluye:
1. **Síntesis Ejecutiva:** Diagnóstico de impacto y vectores de ataque en 2 párrafos técnicos.
2. **Conceptos Core:** 4 términos clave de frontera.
3. **🧠 Ecosistema de Recursos Globales:** Estándares (NIST, ISO, MITRE), Papers indexados (IEEE, ACM, arXiv), Repositorios Open Source y Rutas de certificación (Microsoft, AWS, Cisco, TryHackMe, HackTheBox).
4. **🧪 Anexo Práctico y Laboratorio Open Source:** Estrategia operativa paso a paso y código ejecutable (Python, Reglas Sigma, Reglas Suricata/YARA, Políticas Cilium/eBPF, Bash).
5. **📺 Enlace a Ponencia en Video Oficial:** Enlace directo con minutaje de inicio (`&t=...`).
6. **🎧 Audio-Clase (Podcast Técnico):** Resumen de alta densidad de 60 segundos.

---

### 01. Fundamentos
| Módulo | Documento | Enfoque Técnico |
| :--- | :--- | :--- |
| Fundamentos | [Conceptos Fundamentales de Infraestructura Crítica y Ciberresiliencia](malla-curricular/01-fundamentos/01-conceptos-infraestructura-critica.md) | Modelo Purdue, Convergencia IT/OT y Resiliencia |

### 02. Día 1: Amenazas Emergentes, Regulación y Protección Sectorial
*Transmisión Oficial Día 1:* [`https://www.youtube.com/watch?v=PEqWRTb1idE`](https://www.youtube.com/watch?v=PEqWRTb1idE) *(10h 18m)*

| Lección | Speaker / Institución | Video Timestamp | Laboratorio / Código Incluido |
| :--- | :--- | :--- | :--- |
| [01. Adversarios Digitales IA](malla-curricular/02-dia1-seminario/01-wong-ia-cibercrimen.md) | Subprefecto Marcelo Wong Cea (PDI) | [▶️ Minuto 45:10](https://www.youtube.com/watch?v=PEqWRTb1idE&t=45m10s) | Sanitizador heurístico de prompt injection para agentes |
| [02. Infraestructura DNS y Resiliencia](malla-curricular/02-dia1-seminario/02-lama-infraestructura-dns.md) | Guillermo Lama (NIC Chile) | [▶️ Minuto 1:40:15](https://www.youtube.com/watch?v=PEqWRTb1idE&t=1h40m15s) | Validador de cadenas criptográficas DNSSEC con dnspython |
| [03. El Lado Práctico del Crimen con IA](malla-curricular/02-dia1-seminario/03-fernandez-crimen-ia.md) | Manu Fernández (TRM - IAFIS) | [▶️ Minuto 2:35:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=2h35m20s) | Verificador biométrico dinámico de prueba de vida (Liveness) |
| [04. Ciberseguridad: Desafío Nacional](malla-curricular/02-dia1-seminario/04-bordachar-anci-regulacion.md) | Michelle Bordachar (ANCI) | [▶️ Minuto 3:30:45](https://www.youtube.com/watch?v=PEqWRTb1idE&t=3h30m45s) | Generador de reportes de incidentes OIV en estándar STIX 2.1 |
| [05. Efecto Dominó e Incidentes](malla-curricular/02-dia1-seminario/05-evirtus-efecto-domino.md) | Representante Técnico (E-Virtus) | [▶️ Minuto 5:40:10](https://www.youtube.com/watch?v=PEqWRTb1idE&t=5h40m10s) | Pipeline de auditoría SBOM (Syft/Grype) y firma Cosign |
| [06. Dispositivos Médicos (IoMT)](malla-curricular/02-dia1-seminario/06-fernandez-dispositivos-medicos.md) | Víctor Fernández (Biohacking Village) | [▶️ Minuto 6:30:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=6h30m20s) | Sniffer pasivo con Scapy para detectar anomalías clínicas |
| [07. Sectores Críticos (Minería, Energía, Agua)](malla-curricular/02-dia1-seminario/07-panel-sectores-criticos.md) | Panel (Codelco, CEN, Aguas Andinas, CSIRT) | [▶️ Minuto 7:25:15](https://www.youtube.com/watch?v=PEqWRTb1idE&t=7h25m15s) | Reglas Suricata para detección de comandos no autorizados Modbus |
| [08. Agentes IA e Infraestructura Crítica](malla-curricular/02-dia1-seminario/08-bonnaire-agentes-ia.md) | Dr. Xavier Bonnaire (USM) | [▶️ Minuto 8:30:10](https://www.youtube.com/watch?v=PEqWRTb1idE&t=8h30m10s) | Safety Envelope con Kill-Switch determinista para agentes |
| [09. Seguridad en la Red: Zero Trust](malla-curricular/02-dia1-seminario/09-evirtus-zero-trust.md) | Especialista en Redes (E-Virtus) | [▶️ Minuto 9:20:00](https://www.youtube.com/watch?v=PEqWRTb1idE&t=9h20m00s) | Política de microsegmentación eBPF con Cilium NetworkPolicy |

### 03. Día 2: Ciberdefensa Activa, Inteligencia y Resiliencia Operacional
*Transmisión Oficial Día 2:* [`https://www.youtube.com/watch?v=jLbdG67TqW8`](https://www.youtube.com/watch?v=jLbdG67TqW8) *(7h 31m)*

| Lección | Speaker / Institución | Video Timestamp | Laboratorio / Código Incluido |
| :--- | :--- | :--- | :--- |
| [10. Blue Team Aumentado por IA](malla-curricular/03-dia2-seminario/01-caceres-blue-team-ia.md) | Diego Cáceres (Ganador Call for Papers) | [▶️ Minuto 30:10](https://www.youtube.com/watch?v=jLbdG67TqW8&t=30m10s) | Regla Sigma para detección de descargas Living-off-the-Land |
| [11. Cyber Threat Intelligence (CTI)](malla-curricular/03-dia2-seminario/02-fuentes-threat-intelligence.md) | Omar Fuentes (SEK) | [▶️ Minuto 1:25:30](https://www.youtube.com/watch?v=jLbdG67TqW8&t=1h25m30s) | Compilador automático de IoCs STIX a reglas YARA |
| [12. Resiliencia en Hardware y BIOS](malla-curricular/03-dia2-seminario/03-cordero-resiliencia-hardware.md) | César Cordero (Lenovo) | [▶️ Minuto 2:20:45](https://www.youtube.com/watch?v=jLbdG67TqW8&t=2h20m45s) | Auditoría de PCRs en TPM 2.0 y Secure Boot con bash |
| [13. Ciberseguridad en Salud](malla-curricular/03-dia2-seminario/04-alli-salud-ciberseguridad.md) | Nina Alli (Biohacking Village) | [▶️ Minuto 4:25:10](https://www.youtube.com/watch?v=jLbdG67TqW8&t=4h25m10s) | Protocolo de conmutación a modo degradado clínico aislado |
| [14. Prevención, Detección y Dwell Time](malla-curricular/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) | Tales Albuquerque (Sophos) | [▶️ Minuto 5:15:20](https://www.youtube.com/watch?v=jLbdG67TqW8&t=5h15m20s) | Cazador de procesos LOLBAS y binarios nativos abusados |
| [15. Amenazas Híbridas en la Era Digital](malla-curricular/03-dia2-seminario/06-norman-amenazas-hibridas.md) | James Norman (FCDO Reino Unido) | [▶️ Minuto 6:05:10](https://www.youtube.com/watch?v=jLbdG67TqW8&t=6h05m10s) | Detector de sincronización y campañas de bots coordinadas |
| [16. Transformación Digital y Brecha STEM](malla-curricular/03-dia2-seminario/07-abbas-academia-talento.md) | Nadezda Abbas (UBO) | [▶️ Minuto 6:50:20](https://www.youtube.com/watch?v=jLbdG67TqW8&t=6h50m20s) | Laboratorio Docker-Compose para ciberejercicios CTF |

### 04. Investigación Comparativa Internacional
| Módulo Global | Autoridad / Modelo | Video / Masterclass | Laboratorio / Código Incluido |
| :--- | :--- | :--- | :--- |
| [17. Estados Unidos & Reino Unido](malla-curricular/04-investigacion-global/01-nist-cisa-ncsc.md) | CISA / NIST & NCSC | [▶️ Masterclass NIST](https://www.youtube.com/watch?v=0kH8R5-yUCo) | Evaluador de madurez para las 6 funciones NIST CSF 2.0 |
| [18. República Popular China](malla-curricular/04-investigacion-global/02-china-cii-cac.md) | CAC & MPS (China) | [▶️ Análisis Soberanía](https://www.youtube.com/watch?v=PEqWRTb1idE) | Script de auditoría de hardening Linux para MLPS 2.0 Nivel 3 |
| [19. Federación Rusa](malla-curricular/04-investigacion-global/03-rusia-187fz-fstec.md) | FSTEC & FSB (Rusia) | [▶️ Conferencia Resiliencia](https://www.youtube.com/watch?v=jLbdG67TqW8) | Generador de telemetría de incidentes para red GosSOPKA |

---

## 🎧 Audio-Clases y Podcasts Técnicos

Cada módulo está acompañado de una cápsula de audio técnico de 60 segundos sintetizada a partir de los guiones de alta densidad. El inventario de archivos se gestiona en [assets/audio/README.md](assets/audio/README.md).
