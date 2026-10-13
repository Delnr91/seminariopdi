# Arquitecturas Zero Trust para Redes Críticas - E-Virtus (ampliación temática)

## Síntesis Ejecutiva

Zero Trust reemplaza la confianza implícita basada en ubicación de red por decisiones de acceso centradas en identidades, recursos y contexto. El objetivo es limitar accesos y movimientos laterales incluso cuando una cuenta o segmento ya fue comprometido. La arquitectura distingue la decisión de política de su aplicación y necesita información confiable sobre usuarios, dispositivos y cargas de trabajo. Implantar este enfoque exige inventariar flujos y dependencias; añadir autenticación fuerte a una red plana no resuelve por sí solo la autorización excesiva. [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final).

El principal desafío es sostener controles granulares sin introducir fallos de disponibilidad ni dependencias concentradas en el plano de identidad. Las políticas deben tener propietarios, mecanismos de observación y procedimientos de cambio y recuperación. En entornos operacionales, las capacidades de autenticación de equipos heredados pueden requerir controles compensatorios en puntos de acceso y zonas de red. Conviene desplegar de forma incremental y contrastar las políticas con flujos reales. La microsegmentación debe demostrar reducción de rutas de ataque sin interrumpir comunicaciones necesarias para la función crítica. [Planning for a Zero Trust Architecture: A Planning Guide for Federal Administrators](https://csrc.nist.gov/pubs/cswp/20/planning-for-a-zero-trust-architecture/final).

## Conceptos Core

* **Policy Decision Point (PDP):** Componente que evalúa las condiciones y reglas para permitir o denegar un acceso.
* **Policy Enforcement Point (PEP):** Componente que aplica la decisión de acceso en una interfaz o flujo.
* **Identidad de carga de trabajo:** Identidad verificable asignada a un servicio o proceso para autorizar sus comunicaciones.
* **Microsegmentación:** Separación granular de flujos entre recursos para limitar accesos y propagación de compromisos.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — estudiar componentes y modelos de despliegue de Zero Trust.

### Papers y Literatura de Frontera

* [Planning for a Zero Trust Architecture: A Planning Guide for Federal Administrators](https://csrc.nist.gov/pubs/cswp/20/planning-for-a-zero-trust-architecture/final) — planificar la migración desde dependencias y políticas existentes.

### Repositorios y Herramientas Open Source

* [SPIRE](https://github.com/spiffe/spire) — emitir identidades de cargas de trabajo basadas en SPIFFE.
* [Cilium](https://github.com/cilium/cilium) — aplicar políticas y observar tráfico en plataformas compatibles con su modelo de red.

### Ruta de Aprendizaje Autónoma

* [Establish the guiding principles and core components of Zero Trust](https://learn.microsoft.com/en-us/training/paths/zero-trust-principles/) — seguir la ruta gratuita de principios, componentes y protección de recursos.

## 📺 Video de la intervención

[▶️ Ir al bloque: 09:26:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=34000s) · [Cierre aproximado: 09:46:20](https://www.youtube.com/watch?v=PEqWRTb1idE&t=35180s)

**Duración estimada del bloque:** ≈ 19 min 40 s. **Formato:** Exposición. Puntos de navegación aproximados por inspección visual; pueden incluir introducción o preguntas. [Consultar metodología y recorrido de ambas jornadas](../../VIDEOS.md).

Ampliación temática de Lattices. Se enlaza el mismo bloque de Mauricio Barrera que la lección de efecto dominó; no se ha identificado una segunda charla dedicada a Zero Trust.

## 🛠️ Anexo de métodos y herramientas

[Práctica guiada, estrategias y herramientas open source](../../anexos/02-dia1-seminario/09-evirtus-zero-trust.md). Incluye entregables y métricas para contrastar resultados.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/09-evirtus-zero-trust.mp3)

---

[⬅ Lección Anterior](08-bonnaire-agentes-ia.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](../03-dia2-seminario/01-caceres-blue-team-ia.md)
