# Resiliencia de Hardware y Firmware - César Cordero

## Síntesis Ejecutiva

La confianza en una plataforma depende de código y configuración que operan antes o por debajo del sistema operativo. UEFI, firmware de periféricos y mecanismos de actualización pueden mantener una exposición que no desaparece al reinstalar aplicaciones. La resiliencia exige proteger componentes críticos, detectar cambios no autorizados y disponer de recuperación confiable. Secure Boot y el arranque medido aportan garantías diferentes: el primero valida componentes del arranque según una política, mientras el segundo registra mediciones que pueden utilizarse para evaluar el estado de la plataforma. [NIST SP 800-193 — Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final).

El reto empresarial es gestionar equipos heterogéneos, soporte de fabricantes, claves y recuperación sin perder continuidad. Las políticas deben relacionar inventario de hardware, versiones de firmware y procedencia de actualizaciones con decisiones de mantenimiento. Una atestación necesita una referencia confiable y un proceso de interpretación; no demuestra que todo el equipo sea invulnerable. Conviene validar actualizaciones y recuperación en equipos de prueba representativos, conservando evidencias del estado inicial y final. La cadena de suministro requiere visibilidad adicional sobre componentes físicos y proveedores, además del inventario de software. [CISA — A Hardware Bill of Materials Framework for Supply Chain Risk Management](https://www.cisa.gov/sites/default/files/2023-09/A%20Hardware%20Bill%20of%20Materials%20Framework%20for%20Supply%20Chain%20Risk%20Management%20%28508%29.pdf).

## Conceptos Core

* **Root of Trust:** Componente o función confiable que sirve como base de una cadena de verificación de la plataforma.
* **Secure Boot:** Verificación de componentes del arranque frente a una política de firmas y confianza.
* **Measured Boot:** Registro de mediciones del arranque que permite comparar o atestar el estado observado.
* **Resiliencia de firmware:** Capacidad de proteger, detectar alteraciones y recuperar firmware y datos críticos de la plataforma.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [NIST SP 800-193 — Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final) — estudiar protección, detección y recuperación de plataforma.
* [TPM 2.0 Library Specification](https://trustedcomputinggroup.org/resource/tpm-library-specification/) — comprender funciones y límites del Trusted Platform Module.

### Papers y Literatura de Frontera

* [CISA — A Hardware Bill of Materials Framework for Supply Chain Risk Management](https://www.cisa.gov/sites/default/files/2023-09/A%20Hardware%20Bill%20of%20Materials%20Framework%20for%20Supply%20Chain%20Risk%20Management%20%28508%29.pdf) — analizar inventarios de hardware para gestionar riesgos de suministro.

### Repositorios y Herramientas Open Source

* [CHIPSEC](https://github.com/chipsec/chipsec) — evaluar controles de plataforma en equipos de prueba, revisando primero los requisitos de cada módulo.
* [UEFITool](https://github.com/LongSoft/UEFITool) — inspeccionar imágenes UEFI obtenidas con autorización.

### Ruta de Aprendizaje Autónoma

* [Introduction to RISC-V (LFD110)](https://training.linuxfoundation.org/training/introduction-to-riscv-lfd110/) — cursar la introducción gratuita de Linux Foundation para comprender arquitectura y herramientas; complementarla con los ejercicios de CHIPSEC.

## 📺 Video de la intervención

[▶️ Ir al bloque: 02:17:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=8260s) · [Cierre aproximado: 02:48:20](https://www.youtube.com/watch?v=jLbdG67TqW8&t=10100s)

**Duración estimada del bloque:** ≈ 30 min 40 s. **Formato:** Exposición. Puntos de navegación aproximados por inspección visual; pueden incluir introducción o preguntas. [Consultar metodología y recorrido de ambas jornadas](../../VIDEOS.md).

La exposición observada aborda una estrategia de ciberresiliencia más amplia. El análisis de firmware es una profundización educativa de Lattices.

## 🛠️ Anexo de métodos y herramientas

[Práctica guiada, estrategias y herramientas open source](../../anexos/03-dia2-seminario/03-cordero-resiliencia-hardware.md). Incluye entregables y métricas para contrastar resultados.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/03-cordero-resiliencia-hardware.mp3)

---

[⬅ Lección Anterior](02-fuentes-threat-intelligence.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](04-alli-salud-ciberseguridad.md)
