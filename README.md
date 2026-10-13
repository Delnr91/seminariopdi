# 🏛️ Seminario PDI — Ecosistema Educativo en Ciberseguridad e IA

**Curaduría y arquitectura de contenidos: [Lattices](https://lattices.cl).**

Base de conocimiento abierta sobre protección de infraestructura crítica, inteligencia artificial y ciberresiliencia, vinculada a las temáticas del 9° Seminario Internacional de Ciberseguridad PDI-USM 2026. Las síntesis son material educativo complementario, con referencias a fuentes originales; no son transcripciones de las charlas ni publicaciones institucionales oficiales.

[Malla Curricular](#malla-curricular) · [Videos por speaker](VIDEOS.md) · [Anexos prácticos](anexos/README.md) · [Audio Hub](#audio-hub) · [Investigación Global](#investigación-global) · [Verificación](VERIFICACION.md)

## Filosofía del Proyecto

Lattices reúne conceptos, estándares, literatura técnica, herramientas open source y rutas de aprendizaje para estudiar a distintos niveles de experiencia. El contenido se lee directamente en la web o la app de GitHub mediante GitHub Flavored Markdown (GFM), sin CSS, JavaScript, frameworks ni despliegue adicional.

Las 19 lecciones temáticas incluyen dos párrafos de síntesis, cuatro conceptos fundamentales, cuatro categorías de recursos y un enlace de audio identificado como pendiente. El recorrido incorpora también dos documentos de fundamentos. Cada página permite avanzar, retroceder y volver a esta malla.

## Malla Curricular

### Fundamentos

| Documento | Enfoque |
| --- | --- |
| [Glosario y conceptos clave](malla-curricular/01-fundamentos/01-glosario-y-conceptos-clave.md) | Phishing, ransomware, Zero Trust, IoMT y CTF |
| [Infraestructura crítica y ciberresiliencia](malla-curricular/01-fundamentos/01-conceptos-infraestructura-critica.md) | Dependencias, IT/OT, zonas y recuperación operacional |

### Día 1: Amenazas, Regulación y Protección Sectorial

| Lección | Speaker | Conceptos principales | Video y práctica |
| --- | --- | --- | --- |
| [Inteligencia Artificial aplicada al Cibercrimen](malla-curricular/02-dia1-seminario/01-wong-ia-cibercrimen.md) | Marcelo Wong Cea | Spear phishing asistido por IA, Adversarial Machine Learning | [▶️ 01:02:00 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=3720s) · [Anexo](anexos/02-dia1-seminario/01-wong-ia-cibercrimen.md) |
| [Seguridad y Resiliencia de la Infraestructura DNS](malla-curricular/02-dia1-seminario/02-lama-infraestructura-dns.md) | Guillermo Lama | DNSSEC, Cadena de confianza | [▶️ 02:49:00 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=10140s) · [Anexo](anexos/02-dia1-seminario/02-lama-infraestructura-dns.md) |
| [Fraude y Suplantación de Identidad con IA](malla-curricular/02-dia1-seminario/03-fernandez-crimen-ia.md) | Manu Fernández | Deepfake, Autenticación resistente al phishing | [▶️ 03:20:20 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=12020s) · [Anexo](anexos/02-dia1-seminario/03-fernandez-crimen-ia.md) |
| [Regulación ANCI y Gobernanza de Ciberseguridad](malla-curricular/02-dia1-seminario/04-bordachar-anci-regulacion.md) | Michelle Bordachar | Gobernanza del riesgo, Servicios esenciales y OIV | [▶️ 03:48:40 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=13720s) · [Anexo](anexos/02-dia1-seminario/04-bordachar-anci-regulacion.md) |
| [Efecto Dominó de los Incidentes y Riesgo de Proveedores](malla-curricular/02-dia1-seminario/05-evirtus-efecto-domino.md) | E-Virtus (ampliación temática) | Cybersecurity Supply Chain Risk Management (C-SCRM), Software Bill of Materials (SBOM) | [▶️ 09:26:40 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=34000s) · [Anexo](anexos/02-dia1-seminario/05-evirtus-efecto-domino.md) |
| [Superficies de Ataque en Dispositivos Médicos Conectados](malla-curricular/02-dia1-seminario/06-fernandez-dispositivos-medicos.md) | Víctor Fernández | Internet of Medical Things (IoMT), Modelado de amenazas | [▶️ 06:57:20 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=25040s) · [Anexo](anexos/02-dia1-seminario/06-fernandez-dispositivos-medicos.md) |
| [Ciberresiliencia en Sectores Críticos](malla-curricular/02-dia1-seminario/07-panel-sectores-criticos.md) | Panel Multisectorial | Operational Technology (OT), Interdependencia sectorial | [▶️ 07:17:40 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=26260s) · [Anexo](anexos/02-dia1-seminario/07-panel-sectores-criticos.md) |
| [Agentes de IA y Riesgo en Infraestructura Crítica](malla-curricular/02-dia1-seminario/08-bonnaire-agentes-ia.md) | Xavier Bonnaire | Agente con herramientas, Indirect Prompt Injection | [▶️ 08:56:40 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=32200s) · [Anexo](anexos/02-dia1-seminario/08-bonnaire-agentes-ia.md) |
| [Arquitecturas Zero Trust para Redes Críticas](malla-curricular/02-dia1-seminario/09-evirtus-zero-trust.md) | E-Virtus (ampliación temática) | Policy Decision Point (PDP), Policy Enforcement Point (PEP) | [▶️ 09:26:40 aprox.](https://www.youtube.com/watch?v=PEqWRTb1idE&t=34000s) · [Anexo](anexos/02-dia1-seminario/09-evirtus-zero-trust.md) |

### Día 2: Ciberdefensa, Inteligencia y Resiliencia

| Lección | Speaker | Conceptos principales | Video y práctica |
| --- | --- | --- | --- |
| [Blue Team Aumentado por Inteligencia Artificial](malla-curricular/03-dia2-seminario/01-caceres-blue-team-ia.md) | Diego Cáceres | Detection engineering, Enriquecimiento de alertas | [▶️ 00:10:40 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=640s) · [Anexo](anexos/03-dia2-seminario/01-caceres-blue-team-ia.md) |
| [Cyber Threat Intelligence y Decisiones de Defensa](malla-curricular/03-dia2-seminario/02-fuentes-threat-intelligence.md) | Omar Fuentes | Priority Intelligence Requirements (PIR), Indicator of Compromise (IoC) | [▶️ 00:33:20 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=2000s) · [Anexo](anexos/03-dia2-seminario/02-fuentes-threat-intelligence.md) |
| [Resiliencia de Hardware y Firmware](malla-curricular/03-dia2-seminario/03-cordero-resiliencia-hardware.md) | César Cordero | Root of Trust, Secure Boot | [▶️ 02:17:40 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=8260s) · [Anexo](anexos/03-dia2-seminario/03-cordero-resiliencia-hardware.md) |
| [Ciberseguridad y Continuidad Asistencial en Salud](malla-curricular/03-dia2-seminario/04-alli-salud-ciberseguridad.md) | Nina Alli | Continuidad asistencial, Dependencia clínica digital | [▶️ 02:51:40 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=10300s) · [Anexo](anexos/03-dia2-seminario/04-alli-salud-ciberseguridad.md) |
| [Prevención, Detección y Respuesta ante Ciberamenazas](malla-curricular/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) | Tales Albuquerque | Endpoint Detection and Response (EDR), Threat hunting | [▶️ 03:24:00 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=12240s) · [Anexo](anexos/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) |
| [Amenazas Híbridas y Resiliencia Informacional](malla-curricular/03-dia2-seminario/06-norman-amenazas-hibridas.md) | James Norman | Foreign Information Manipulation and Interference (FIMI), Operación de influencia | [▶️ 05:41:40 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=20500s) · [Anexo](anexos/03-dia2-seminario/06-norman-amenazas-hibridas.md) |
| [Desarrollo de Talento para la Ciberresiliencia](malla-curricular/03-dia2-seminario/07-abbas-academia-talento.md) | Nadezda Abbas | Task, Knowledge and Skill (TKS), Aprendizaje basado en evidencias | [▶️ 06:14:40 aprox.](https://www.youtube.com/watch?v=jLbdG67TqW8&t=22480s) · [Anexo](anexos/03-dia2-seminario/07-abbas-academia-talento.md) |

## Videos por intervención y práctica aplicada

El [índice audiovisual de ambas jornadas](VIDEOS.md) reúne **17 bloques temáticos**, con puntos de entrada, cierre y duración aproximada. Permite saltar las largas pausas grabadas; los enlaces no suprimen publicidad de YouTube ni detienen automáticamente el video al cierre. Los paneles incluyen varias personas y su duración no equivale al tiempo de voz de un speaker.

Los [18 anexos prácticos](anexos/README.md) agregan métodos, estrategias, herramientas open source, ejercicios y criterios de evaluación. Las dos guías de E-Virtus son ampliaciones temáticas relacionadas con la misma intervención de **Mauricio Barrera**; no se presentan como dos charlas diferentes.

### Intervenciones adicionales del Día 1

| Speaker identificado en la grabación | Entrada aproximada | Profundización |
| --- | --- | --- |
| Fernanda Macías — ANCI y CSIRT Nacional | [▶️ 04:22:00](https://www.youtube.com/watch?v=PEqWRTb1idE&t=15720s) | [Análisis de amenazas y filtraciones](anexos/02-dia1-seminario/10-macias-analisis-amenazas.md) |
| Sergey Nikitin — Group-IB | [▶️ 09:48:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=35300s) | [Cibercrimen y economía del fraude](anexos/02-dia1-seminario/11-nikitin-cibercrimen-fraude.md) |

Estas entradas amplían la cobertura audiovisual. Las propuestas prácticas son material complementario de Lattices, no una transcripción ni títulos oficiales atribuidos sin corroboración.

## Investigación Global

Los módulos comparan enfoques y fuentes, distinguiendo marcos técnicos de requisitos jurídicos específicos.

| Módulo | Enfoque |
| --- | --- |
| [Gestión del Riesgo y Ciberresiliencia: NIST, CISA y NCSC](malla-curricular/04-investigacion-global/01-nist-cisa-ncsc.md) | Marcos de referencia de Estados Unidos y Reino Unido |
| [Protección de Infraestructura de Información Crítica en China](malla-curricular/04-investigacion-global/02-china-cii-cac.md) | Marco CII y autoridades de ciberseguridad |
| [Seguridad de Infraestructura de Información Crítica en Rusia](malla-curricular/04-investigacion-global/03-rusia-187fz-fstec.md) | Marco de la Ley Federal 187-FZ |

## Audio Hub

**Los 19 MP3 están pendientes.** Las lecciones muestran el nombre esperado de cada grabación. El [inventario de audios](assets/audio/README.md) permite localizar la lección correspondiente; los enlaces de podcast funcionarán cuando se incorporen los archivos.

Cuando haya grabaciones, abre el MP3 desde GitHub y usa la opción de descargar o ver el archivo sin procesar para reproducirlo en tu dispositivo. GitHub filtra etiquetas HTML de audio en el Markdown; la lectura del repositorio no requiere un reproductor incrustado. La duración se medirá al producir cada grabación.

## Metodología Lattices

* **Fuentes precisas:** enlaces al documento, especificación, paper, repositorio o módulo formativo concreto.
* **Análisis verificable:** separación entre evidencia, recomendaciones de arquitectura y obligaciones sujetas a contexto.
* **Práctica controlada:** herramientas para laboratorios autorizados y datos sintéticos; sin promesas de certificación o cumplimiento automático.
* **Aprendizaje autónomo:** materiales gratuitos identificados; cuando las prácticas requieren infraestructura o licencias, se indica el posible coste.

Consulta el [informe de verificación](VERIFICACION.md) para conocer la revisión de estructura, navegación y enlaces. El directorio de [documentos PDF](assets/docs-pdf/README.md) permanece reservado, sin archivos suministrados.

## Acerca de Lattices

[Lattices](https://lattices.cl) es una startup enfocada en infraestructura, inteligencia artificial y automatización. Esta base de conocimiento organiza material educativo para profesionales, equipos técnicos y personas que buscan desarrollar capacidades de ciberseguridad.
