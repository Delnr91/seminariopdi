# Anexo práctico: Gestión del Riesgo y Ciberresiliencia: NIST, CISA y NCSC

**Curaduría:** [Lattices](https://lattices.cl). Material de investigación y práctica, sin atribución a un speaker ni a una ponencia audiovisual.

## Objetivo

Comparar resultados de seguridad y evidencia por función sin convertir una rúbrica local en una certificación.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Perfil actual y objetivo** | Elegir resultados relevantes para un servicio ficticio y explicar por qué se incluyen. | Lista de resultados, contexto y responsables. |
| **Evidencia trazable** | Relacionar cada afirmación con una observación o prueba; distinguir ausencia de evidencia de resultado no evaluado. | Matriz de evidencias y brechas. |
| **Ejercicio de recuperación** | Ensayar un incidente y observar continuidad, restauración y comunicación. | Acta con decisiones y mejoras. |

## Herramientas open source

* [CSET](https://github.com/cisagov/cset) — herramienta de análisis para un laboratorio preparado; su uso no acredita cumplimiento normativo.
* [OpenSCAP](https://github.com/OpenSCAP/openscap) — herramienta de análisis para un laboratorio preparado; su uso no acredita cumplimiento normativo.

## Laboratorio guiado

Usar únicamente archivos sintéticos y entornos de práctica; el ejemplo de Python usa la biblioteca estándar y no instala dependencias ni accede al sistema.

1. Elegir un servicio ficticio y seis resultados de estudio, uno por función CSF; conservar el identificador y texto de la fuente oficial.
2. Seleccionar evidencia y marcar por separado qué resultado aún no se evaluó.
3. Aplicar el resumen local y revisar manualmente calidad y vigencia de las evidencias.
4. Comparar con CSET o un perfil OpenSCAP de laboratorio cuando haya un entorno preparado; registrar alcance y diferencias.

### Código y configuración de referencia

Resumir conteos de resultados con o sin evidencia para cada función del ejercicio, manteniendo visibles los resultados no evaluados.

```python
FUNCIONES = ("GV", "ID", "PR", "DE", "RS", "RC")

def resumir_cobertura(resultados):
    campos = {"con_evidencia", "sin_evidencia", "no_evaluado"}
    if not isinstance(resultados, dict) or set(resultados) != set(FUNCIONES):
        raise ValueError("Se requieren las seis funciones del ejercicio")
    resumen = {}
    for funcion in FUNCIONES:
        r = resultados[funcion]
        if not isinstance(r, dict) or set(r) != campos:
            raise ValueError("Faltan conteos o hay campos desconocidos")
        if any(type(v) is not int or v < 0 for v in r.values()):
            raise ValueError("Los conteos deben ser enteros no negativos")
        total = sum(r.values())
        resumen[funcion] = {**r, "total": total,
                            "fraccion_con_evidencia": r["con_evidencia"] / total if total else None}
    return resumen

if __name__ == "__main__":
    muestra = {f: {"con_evidencia": 1, "sin_evidencia": 1, "no_evaluado": 1}
               for f in FUNCIONES}
    print(resumir_cobertura(muestra))
```

**Alcance:** Los conteos pertenecen a una rúbrica local y no son una fórmula oficial de madurez NIST, un Tier ni una certificación. Las evidencias deben revisarse por calidad y relevancia, no solo por cantidad.

**Comprobación:** ejemplo ejecutado con datos ficticios; se probaron entradas válidas, límites y errores. La prueba cubre el comportamiento local de la función, no un sistema de producción.

## Evaluación del resultado

**Entregable:** informe con entradas, versiones, procedimiento, resultados y limitaciones.

* Resultados con evidencia revisada y vigente.
* Brechas con responsable y fecha de revisión.
* Resultados de recuperación observados durante el ejercicio.

**Criterio de cierre:** otra persona puede repetir el análisis y distinguir lo observado de lo que permanece pendiente de revisión.

## Fuentes y profundización global

* [NIST Cybersecurity Framework (CSF) 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final).
* [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/cyber-assessment-framework).

La [lección de referencia](../../malla-curricular/04-investigacion-global/01-nist-cisa-ncsc.md) reúne literatura y rutas de aprendizaje.

---

[🏠 Malla Curricular](../../README.md) | [🛠️ Todos los anexos](../README.md)
