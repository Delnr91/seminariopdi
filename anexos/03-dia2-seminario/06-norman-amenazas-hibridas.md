# Anexo práctico: Amenazas Híbridas y Resiliencia Informacional - James Norman

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 05:41:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=20500s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Analizar una campaña informacional ficticia junto a un incidente técnico sin confundir coordinación, identidad y atribución.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Separación de hipótesis** | Distinguir qué pasó en sistemas, qué narrativa circuló y quién podría beneficiarse; registrar incertidumbre. | Cronología con hechos y supuestos separados. |
| **Mapeo de comportamientos** | Usar DISARM para describir acciones observadas, evitando atribuir actores a partir de similitud aislada. | Técnicas vinculadas a evidencia concreta. |
| **Análisis de relaciones** | Representar vínculos entre publicaciones ficticias, canales y tiempos; comprobar explicaciones alternativas. | Grafo reproducible con límites de inferencia. |

## Herramientas open source

* [DISARMframeworks](https://github.com/DISARMFoundation/DISARMframeworks) — Taxonomías y datos de comportamiento informacional para estructurar análisis.
* [Gephi](https://github.com/gephi/gephi) — Exploración de grafos; una comunidad visual o una medida de centralidad no demuestra coordinación maliciosa.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Crear diez publicaciones ficticias en tres canales y una cronología de caída de un servicio simulado; no recopilar datos personales.
2. Clasificar comportamientos con DISARM y marcar qué datos faltan para sostener cada hipótesis.
3. Importar en Gephi una tabla de nodos y otra de aristas. Comparar agrupación temporal y difusión; conservar parámetros del análisis.
4. Redactar un aviso que describa hechos confirmados y continuidad del servicio, evitando atribución no corroborada y amplificación innecesaria de la narrativa.

### Ejemplo de trabajo

Tabla de aristas para importar junto a un inventario de nodos sintéticos:

```csv
Source,Target,Type,Weight
canal_A,canal_B,Directed,1
canal_B,canal_C,Directed,1
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Conclusiones que distinguen observación de atribución.
* Relaciones con evidencia y explicación alternativa documentadas.
* Tiempo para emitir información verificada y corregir un aviso erróneo en el ejercicio.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [DISARM frameworks](https://github.com/DISARMFoundation/DISARMframeworks).
* [Gephi](https://github.com/gephi/gephi).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/06-norman-amenazas-hibridas.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
