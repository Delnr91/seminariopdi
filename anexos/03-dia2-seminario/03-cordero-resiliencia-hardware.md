# Anexo práctico: Resiliencia de Hardware y Firmware - César Cordero

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 02:17:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=8260s) · [Índice y límites de los tiempos](../../VIDEOS.md)

La exposición observada aborda una estrategia de ciberresiliencia más amplia. El análisis de firmware es una profundización educativa de Lattices.

## Objetivo

Comprender protección, detección y recuperación del firmware como parte de la continuidad de un servicio.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Inventario de plataforma** | Relacionar equipo, versión de firmware, raíz de confianza, proveedor y mecanismo de actualización. | Inventario con origen de cada dato. |
| **Inspección estática** | Comparar una imagen de firmware autorizada con su referencia y registrar diferencias; un hash distinto no demuestra compromiso. | Informe de estructuras y cambios explicados. |
| **Recuperación preparada** | Definir imagen válida, autorización y procedimiento de restauración; comprobarlos únicamente en hardware de práctica. | Plan de recuperación y evidencia del ejercicio. |

## Herramientas open source

* [UEFITool](https://github.com/LongSoft/UEFITool) — Visor y editor de imágenes UEFI; para este ejercicio usar solo inspección de una copia.
* [CHIPSEC](https://github.com/chipsec/chipsec) — Evaluación de seguridad de plataforma; algunos módulos requieren privilegios o pueden afectar el equipo. Aquí se estudian sus checks sin ejecutarlos.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Obtener una imagen de firmware para análisis educativo, con autorización y referencia del proveedor; anotar modelo, formato y versión.
2. Calcular el hash y abrir una copia en UEFITool sin editar ni flashear. Registrar estructura y advertencias del parser.
3. Comparar con otra versión y explicar al menos dos cambios. No considerar la diferencia de hash como prueba suficiente de alteración maliciosa.
4. Diseñar el plan de recuperación con compatibilidad, respaldo y criterios de reversión; si no hay equipo dedicado, terminar con un ejercicio de mesa.

### Ejemplo de trabajo

Con el archivo de práctica disponible:

```bash
sha256sum firmware.bin
```

Conservar también el origen y la versión: el hash acredita identidad del archivo, no autenticidad del proveedor.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Equipos con versión y procedimiento de actualización identificados.
* Cambios de firmware explicados mediante evidencia.
* Tiempo de recuperación medido solo si existe un ensayo real en equipo de práctica.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST SP 800-193](https://csrc.nist.gov/pubs/sp/800/193/final).
* [UEFITool](https://github.com/LongSoft/UEFITool).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/03-cordero-resiliencia-hardware.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
