# Blue Team Aumentado por Inteligencia Artificial - Diego Cáceres

## Síntesis Ejecutiva

El Blue Team integra telemetría, ingeniería de detección e investigación para reconocer y contener actividad adversaria. La IA puede apoyar la clasificación de eventos, el enriquecimiento de casos y la construcción de hipótesis, pero necesita datos representativos y contexto del entorno. Su valor operativo se mide en cobertura de comportamiento y reducción del tiempo de análisis, no en la cantidad de respuestas generadas. Una arquitectura consistente separa alertas, evidencias e inferencias, permitiendo reconstruir qué señales justificaron cada decisión de respuesta. [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/).

La calidad de la asistencia depende de la cobertura de sensores, el etiquetado y el cambio de distribución de los datos. Un modelo puede omitir ataques nuevos o ampliar errores presentes en registros y conocimiento recuperado. Conviene evaluar precisión y sensibilidad por escenario, comparar con una referencia sin IA y reservar la ejecución de acciones a controles externos de autorización. La emulación adversaria en laboratorio permite validar detecciones y procedimientos, mientras la revisión humana y las rutas de reversión limitan el impacto de recomendaciones incorrectas o automatizaciones precipitadas. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2025/final).

## Conceptos Core

* **Detection engineering:** Diseño, validación y mantenimiento de reglas o modelos vinculados a comportamientos adversarios.
* **Enriquecimiento de alertas:** Incorporación de contexto de activos, identidades e inteligencia para orientar una investigación.
* **Concept drift:** Cambio en la relación entre datos y objetivos que puede degradar el rendimiento de un modelo.
* **Validación adversaria:** Evaluación controlada de si sensores, detecciones y procedimientos reconocen escenarios de ataque definidos.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/) — definir objetivos de cobertura por comportamiento.
* [MITRE D3FEND](https://d3fend.mitre.org/) — relacionar técnicas defensivas y artefactos observables.

### Papers y Literatura de Frontera

* [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — estudiar ataques y supuestos de seguridad de componentes de aprendizaje automático.

### Repositorios y Herramientas Open Source

* [Apache CALDERA](https://github.com/apache/caldera) — emular comportamientos exclusivamente en un laboratorio autorizado.
* [Sigma](https://github.com/SigmaHQ/sigma) — estudiar reglas portables y adaptar sus supuestos a las fuentes de eventos disponibles.

### Ruta de Aprendizaje Autónoma

* [Mitigate threats using Microsoft Security Copilot](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-copilot-for-security/) — estudiar asistencia generativa a analistas.
* [Create detections and perform investigations using Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-create-detections-perform-investigations-azure-sentinel/) — desarrollar detecciones e investigaciones; los contenidos son gratuitos, los servicios usados en prácticas pueden generar costes.

## 📺 Video de la intervención

[▶️ Ir al bloque: 00:10:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=640s) · [Cierre aproximado: 00:29:00](https://www.youtube.com/watch?v=jLbdG67TqW8&t=1740s)

**Duración estimada del bloque:** ≈ 18 min 20 s. **Formato:** Exposición. Puntos de navegación aproximados por inspección visual; pueden incluir introducción o preguntas. [Consultar metodología y recorrido de ambas jornadas](../../VIDEOS.md).

## 🛠️ Anexo de métodos y herramientas

[Práctica guiada, estrategias y herramientas open source](../../anexos/03-dia2-seminario/01-caceres-blue-team-ia.md). Incluye entregables y métricas para contrastar resultados.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/01-caceres-blue-team-ia.mp3)

---

[⬅ Lección Anterior](../02-dia1-seminario/09-evirtus-zero-trust.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](02-fuentes-threat-intelligence.md)
