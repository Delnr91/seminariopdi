# Fraude y Suplantación de Identidad con IA - Manu Fernández

## Síntesis Ejecutiva

La generación de voz, imagen y texto permite fabricar señales de identidad convincentes, pero su apariencia no acredita que una orden proceda de una persona autorizada. El fraude asistido por IA explota la separación entre reconocimiento visual, autenticación y aprobación de operaciones. Una videollamada o un mensaje coherente pueden inducir a eludir controles financieros aunque la sesión no disponga de garantías suficientes. El diseño defensivo debe vincular cada autorización con credenciales verificables, contexto transaccional y validación independiente. [NIST SP 800-63B-4 — Digital Identity Guidelines: Authentication and Authenticator Management](https://csrc.nist.gov/pubs/sp/800/63/b/4/final).

La detección de contenido sintético y la verificación de procedencia aportan señales complementarias, con límites que deben explicitarse. Una firma de procedencia acredita determinadas afirmaciones y su integridad, no la veracidad de todo lo representado; un detector también puede fallar ante material nuevo. Conviene priorizar autenticadores resistentes al phishing, separación de funciones y confirmación por canales previamente establecidos. Las evaluaciones deben comparar falsos positivos y negativos sin utilizar la confianza del modelo como sustituto de evidencia ni de controles de autorización. [Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency](https://www.nist.gov/publications/reducing-risks-posed-synthetic-content-overview-technical-approaches-digital-content).

## Conceptos Core

* **Deepfake:** Contenido sintético o manipulado que reproduce la apariencia o voz de una persona.
* **Autenticación resistente al phishing:** Autenticación diseñada para impedir el uso de una credencial capturada en un servicio impostor.
* **Presentation Attack Detection (PAD):** Controles que buscan identificar intentos de engañar a sensores o procesos biométricos.
* **Procedencia de contenido:** Información verificable sobre el origen y las transformaciones declaradas de un artefacto digital.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-63B-4 — Digital Identity Guidelines: Authentication and Authenticator Management](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) — analizar garantías de autenticadores y resistencia a la suplantación.

### Papers y Literatura de Frontera

* [Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency](https://www.nist.gov/publications/reducing-risks-posed-synthetic-content-overview-technical-approaches-digital-content) — comparar procedencia, marcas de agua y detección de contenido sintético.
* [FaceForensics++: Learning to Detect Manipulated Facial Images](https://arxiv.org/abs/1901.08971) — analizar un benchmark de manipulación facial sin extrapolar sus resultados a todas las tecnologías actuales.

### Repositorios y Herramientas Open Source

* [C2PA Rust SDK](https://github.com/contentauth/c2pa-rs) — validar manifiestos de procedencia sin confundirlos con pruebas de veracidad.
* [FaceForensics++](https://github.com/ondyari/FaceForensics) — estudiar evaluación de detección de manipulación facial y sus condiciones de uso de datos.

### Ruta de Aprendizaje Autónoma

* [CS50's Introduction to Cybersecurity](https://cs50.harvard.edu/cybersecurity/) — estudiar protección de cuentas, datos y sistemas mediante material gratuito.
* [Establish the guiding principles and core components of Zero Trust](https://learn.microsoft.com/en-us/training/paths/zero-trust-principles/) — relacionar verificación explícita y mínimo privilegio con los procesos de autorización.

## 📺 Video de la intervención

[▶️ Ir al bloque: 03:20:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=12020s) · [Cierre aproximado: 03:46:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=13580s)

**Duración estimada del bloque:** ≈ 26 min 00 s. **Formato:** Exposición. Puntos de navegación aproximados por inspección visual; pueden incluir introducción o preguntas. [Consultar metodología y recorrido de ambas jornadas](../../VIDEOS.md).

## 🛠️ Anexo de métodos y herramientas

[Práctica guiada, estrategias y herramientas open source](../../anexos/02-dia1-seminario/03-fernandez-crimen-ia.md). Incluye entregables y métricas para contrastar resultados.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/03-fernandez-crimen-ia.mp3)

---

[⬅ Lección Anterior](02-lama-infraestructura-dns.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](04-bordachar-anci-regulacion.md)
