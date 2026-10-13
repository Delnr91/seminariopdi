# Ciberresiliencia en Sectores Críticos - Panel Multisectorial

## Síntesis Ejecutiva

Energía, agua, minería y comunicaciones forman redes de dependencias donde el impacto de un incidente no coincide necesariamente con el perímetro de la organización comprometida. La protección requiere comprender procesos físicos, sistemas de control y servicios de soporte compartidos. En tecnología operacional, los cambios de seguridad deben equilibrarse con disponibilidad, rendimiento y seguridad del proceso. La priorización debe partir de las funciones esenciales y de sus modos de falla, identificando qué controles y recursos permiten sostenerlas cuando una dependencia digital deja de responder. [NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).

La respuesta multisectorial necesita vocabulario común, responsables identificados y mecanismos de intercambio de información con criterios de sensibilidad. Compartir indicadores ayuda, pero no reemplaza la interpretación del contexto ni una capacidad local de recuperación. Los ejercicios conjuntos permiten evaluar escenarios de degradación, escalamiento y restauración con dependencias cruzadas. Como criterio de evaluación, conviene medir continuidad de la función y tiempos de coordinación, no solo disponibilidad de activos individuales. La planificación debe distinguir alternativas realmente independientes de respaldos que utilizan las mismas identidades, redes o proveedores. [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026).

## Conceptos Core

* **Operational Technology (OT):** Sistemas que supervisan o controlan procesos y eventos físicos.
* **Interdependencia sectorial:** Relación por la cual la continuidad de un servicio depende de funciones de otro sector.
* **Continuidad operacional:** Capacidad de sostener funciones prioritarias durante una interrupción o recuperación.
* **Intercambio de inteligencia:** Transferencia de información contextualizada sobre amenazas bajo reglas de calidad y confidencialidad.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — adaptar controles a restricciones de sistemas operacionales.
* [ISA/IEC 62443 — Industrial Automation and Control Systems Security](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) — estudiar zonas, conductos y gestión de seguridad industrial; los textos completos de la serie pueden requerir compra.

### Papers y Literatura de Frontera

* [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) — examinar amenazas y dependencias del ecosistema digital europeo, distinguiendo ese contexto del local.

### Repositorios y Herramientas Open Source

* [Malcolm](https://github.com/cisagov/Malcolm) — analizar capturas y protocolos de red en un laboratorio.
* [MISP](https://github.com/MISP/MISP) — estructurar el intercambio de indicadores y contexto entre equipos.

### Ruta de Aprendizaje Autónoma

* [CISA — ICS Cybersecurity (101)](https://www.cisa.gov/resources-tools/programs/ics-training-available-through-cisa) — comenzar por ICS Cybersecurity (101), formación gratuita con registro sobre sistemas de control.

## 📺 Video de la intervención

[▶️ Ir al bloque: 07:17:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=26260s) · [Cierre aproximado: 08:02:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=28960s)

**Duración estimada del bloque:** ≈ 45 min 00 s. **Formato:** Panel compartido. Puntos de navegación aproximados por inspección visual; pueden incluir introducción o preguntas. [Consultar metodología y recorrido de ambas jornadas](../../VIDEOS.md).

El video corresponde al panel completo. Este anexo no atribuye todas las recomendaciones a cada participante individual.

## 🛠️ Anexo de métodos y herramientas

[Práctica guiada, estrategias y herramientas open source](../../anexos/02-dia1-seminario/07-panel-sectores-criticos.md). Incluye entregables y métricas para contrastar resultados.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/07-panel-sectores-criticos.mp3)

---

[⬅ Lección Anterior](06-fernandez-dispositivos-medicos.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](08-bonnaire-agentes-ia.md)
