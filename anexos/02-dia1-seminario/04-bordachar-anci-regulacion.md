# Anexo práctico: Regulación ANCI y Gobernanza de Ciberseguridad - Michelle Bordachar

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 03:48:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=13720s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Traducir decisiones de gobernanza en responsables, evidencias y un proceso de respuesta que pueda revisarse.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Perfil actual y objetivo** | Describir servicios esenciales para el negocio, resultados de seguridad existentes y brechas prioritarias. | Perfil con evidencia y prioridades justificadas. |
| **Matriz de responsabilidad** | Asignar quién decide, ejecuta, revisa y comunica durante un incidente; comprobar suplencias. | RACI y directorio de contactos del ejercicio. |
| **Ejercicio de mesa** | Simular una filtración y ensayar evaluación, escalamiento, comunicación y recuperación con una cronología única. | Registro de decisiones y acciones de mejora. |

## Herramientas open source

* [DFIR-IRIS](https://github.com/dfir-iris/iris-web) — Gestión colaborativa de casos; fijar una versión estable y revisar permisos antes de un laboratorio.
* [CSET](https://github.com/cisagov/cset) — Autoevaluación estructurada de controles; sus resultados son insumos de análisis, no certificaciones.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Inventariar cinco servicios ficticios y justificar el impacto de perder cada uno. Asociar un responsable y una dependencia externa.
2. Crear un caso de filtración de datos sintéticos en IRIS o una tabla local equivalente; separar hechos, hipótesis y decisiones.
3. Introducir tres eventos: aviso inicial, confirmación de alcance y recuperación. Registrar qué información falta en cada etapa.
4. Comparar la cronología con el procedimiento aprobado y documentar las obligaciones aplicables mediante revisión jurídica del contexto, sin deducir plazos de este ejercicio.

### Ejemplo de trabajo

```csv
servicio,responsable,evidencia,brecha,accion
portal_ficticio,operaciones,prueba_restauracion,sin_suplente,asignar_reemplazo
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Decisiones con responsable, fecha y evidencia.
* Servicios con restauración probada y suplencias definidas.
* Tiempo de clasificación y escalamiento en el ejercicio.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final).
* [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/04-bordachar-anci-regulacion.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
