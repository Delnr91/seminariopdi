# Inteligencia Artificial aplicada al Cibercrimen - Marcelo Wong Cea

## Síntesis Ejecutiva

La IA generativa reduce el coste de producir mensajes de suplantación, adaptar señuelos y procesar información obtenida durante el reconocimiento. Para una organización crítica, el impacto relevante es la combinación de escala y personalización: un acceso inicial aparentemente menor puede comprometer identidades con permisos sobre servicios esenciales. La defensa debe relacionar autenticación, telemetría y exposición de activos con escenarios adversarios concretos; evaluar únicamente la calidad visual de un mensaje deja fuera el contexto técnico del ataque. [MITRE ATLAS](https://atlas.mitre.org/).

El desafío operativo consiste en investigar campañas asistidas por IA sin convertir inferencias en evidencia. La conservación de registros, la trazabilidad de los artefactos y la revisión humana de hipótesis ayudan a separar hechos observables de atribuciones inciertas. Como criterio de diseño, conviene medir cobertura de detección, calidad de los avisos y capacidad de revocar accesos, mientras se ensayan controles frente a abuso de modelos en un laboratorio. La automatización defensiva requiere permisos acotados y validación de resultados antes de actuar sobre sistemas críticos. [2023 Redacted Europol Report on the Impact of ChatGPT and Large Language Models on Law Enforcement](https://www.europol.europa.eu/publications-events/publications/2023-redacted-europol-report-impact-of-chatgpt-and-large-language-models-law-enforcement).

## Conceptos Core

* **Spear phishing asistido por IA:** Producción de señuelos adaptados a una persona o función utilizando información contextual.
* **Adversarial Machine Learning:** Estudio de ataques y defensas que afectan datos, modelos o aplicaciones basadas en aprendizaje automático.
* **Tactics, Techniques and Procedures (TTP):** Descripción del comportamiento adversario que permite relacionar señales con una estrategia de ataque.
* **Cadena de custodia digital:** Registro verificable de obtención, conservación y tratamiento de evidencia para mantener su integridad.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [MITRE ATLAS](https://atlas.mitre.org/) — relacionar amenazas contra IA con escenarios de evaluación.
* [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/) — modelar el acceso inicial y el abuso de identidades.

### Papers y Literatura de Frontera

* [2023 Redacted Europol Report on the Impact of ChatGPT and Large Language Models on Law Enforcement](https://www.europol.europa.eu/publications-events/publications/2023-redacted-europol-report-impact-of-chatgpt-and-large-language-models-law-enforcement) — analizar usos delictivos de LLM y desafíos de investigación.
* [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) — estudiar la recuperación de datos de entrenamiento mediante consultas a un modelo.

### Repositorios y Herramientas Open Source

* [garak](https://github.com/NVIDIA/garak) — evaluar vulnerabilidades de LLM con datos de laboratorio.
* [Adversarial Robustness Toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) — comparar robustez de modelos frente a evasión, envenenamiento y extracción.

### Ruta de Aprendizaje Autónoma

* [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — estudiar los fundamentos de los modelos y sus límites; requiere experiencia previa en Python.
* [Perform threat hunting in Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) — practicar investigaciones basadas en telemetría; lectura gratuita, con posibles costes si se despliegan servicios Azure.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/01-wong-ia-cibercrimen.mp3)

---

[⬅ Lección Anterior](../01-fundamentos/01-conceptos-infraestructura-critica.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](02-lama-infraestructura-dns.md)
