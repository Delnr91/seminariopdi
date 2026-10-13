# Agentes de IA y Riesgo en Infraestructura Crítica - Xavier Bonnaire

## Síntesis Ejecutiva

Un agente de IA incorpora un modelo, fuentes de datos, memoria y herramientas que convierten inferencias en acciones. Al integrarlo con una función crítica, la superficie de riesgo incluye las interfaces de ejecución y las credenciales, además de la precisión del modelo. La evaluación debe distinguir errores no intencionales, entradas adversarias y autorizaciones excesivas. El control de permisos y la validación externa de acciones resultan decisivos: una respuesta plausible no demuestra que la operación propuesta respete los límites físicos, económicos o de seguridad del sistema. [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

La inyección indirecta de instrucciones muestra cómo una aplicación puede confundir contenido recuperado con órdenes operativas. Reducir este riesgo requiere separar instrucciones y datos, restringir las herramientas disponibles y verificar cada acción según una política independiente del modelo. Como diseño prudente, las acciones de alto impacto deben contar con aprobación humana, límites de ejecución y vías de recuperación ensayadas. La evaluación necesita casos adversarios reproducibles y registros de decisiones, sin suponer que un filtro de texto o un benchmark aislado certifica la seguridad de toda la arquitectura. [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173).

## Conceptos Core

* **Agente con herramientas:** Aplicación que utiliza un modelo para planificar tareas e invocar operaciones sobre sistemas externos.
* **Indirect Prompt Injection:** Introducción de instrucciones adversarias en contenido que una aplicación recupera o procesa.
* **Exceso de agencia:** Concesión de acciones o permisos superiores a los necesarios para una tarea.
* **Human-in-the-loop:** Intervención humana definida para revisar decisiones o autorizar acciones según su impacto.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — organizar identificación, medición y gestión de riesgos de IA.
* [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — revisar amenazas de aplicaciones con LLM, incluidas inyección y permisos excesivos.

### Papers y Literatura de Frontera

* [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — estudiar el conflicto entre datos externos e instrucciones en aplicaciones con LLM.
* [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — clasificar ataques y límites de mitigación a lo largo del ciclo de vida.

### Repositorios y Herramientas Open Source

* [garak](https://github.com/NVIDIA/garak) — evaluar comportamiento adversario de modelos.
* [Promptfoo](https://github.com/promptfoo/promptfoo) — mantener pruebas reproducibles de aplicaciones con LLM; las llamadas a proveedores pueden tener coste.

### Ruta de Aprendizaje Autónoma

* [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — comprender modelos, búsqueda y aprendizaje; contenido gratuito, requiere base de Python.
* [Mitigate threats using Microsoft Security Copilot](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-copilot-for-security/) — estudiar asistencia generativa en operaciones de seguridad; lectura gratuita, prácticas con licencias o consumo adicional según el entorno.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/08-bonnaire-agentes-ia.mp3)

---

[⬅ Lección Anterior](07-panel-sectores-criticos.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](09-evirtus-zero-trust.md)
