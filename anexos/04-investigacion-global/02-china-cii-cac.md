# Anexo práctico: Protección de Infraestructura de Información Crítica en China

**Curaduría:** [Lattices](https://lattices.cl). Material de investigación y práctica, sin atribución a un speaker ni a una ponencia audiovisual.

## Objetivo

Analizar evidencia de configuración y retención con un alcance técnico y jurídico explícito.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Matriz de aplicabilidad** | Separar requisitos de la fuente oficial, hipótesis sobre alcance y controles técnicos del laboratorio. | Registro con referencia, fecha y revisión pendiente. |
| **Evaluación de configuración** | Comparar un perfil documentado con una imagen de práctica, conservando versión y resultados. | Informe de diferencias; no certificado legal. |
| **Retención con contexto** | Estudiar fechas, periodicidad y huecos, además del número de archivos retenidos. | Cronología de registros y limitaciones. |

## Herramientas open source

* [OpenSCAP](https://github.com/OpenSCAP/openscap) — herramienta de análisis para un laboratorio preparado; su uso no acredita cumplimiento normativo.
* [ComplianceAsCode Content](https://github.com/ComplianceAsCode/content) — herramienta de análisis para un laboratorio preparado; su uso no acredita cumplimiento normativo.

## Laboratorio guiado

Usar únicamente archivos sintéticos y entornos de práctica; el ejemplo de Python usa la biblioteca estándar y no instala dependencias ni accede al sistema.

1. Preparar una tabla de requisitos a investigar y asociar cada uno con su fuente y ámbito; no extrapolar un plazo a cualquier organización.
2. Crear fechas y registros totalmente ficticios, incluyendo un hueco y una fecha posterior a la referencia.
3. Ejecutar el ejemplo local y explicar por qué la antigüedad no acredita cobertura continua.
4. Seleccionar un perfil OpenSCAP compatible para una VM de práctica; no denominarlo perfil MLPS certificado salvo evidencia específica.

### Código y configuración de referencia

Comparar la antigüedad de un registro ficticio con la fecha de referencia del ejercicio. El código no inspecciona el equipo ni interpreta obligaciones de MLPS.

```python
from datetime import datetime

def revisar_antiguedad(fecha_registro, fecha_referencia):
    if any(not isinstance(s, str) or not s.strip() for s in (fecha_registro, fecha_referencia)):
        raise ValueError("Se requieren fechas ISO con zona horaria")
    fechas = [datetime.fromisoformat(s.replace("Z", "+00:00"))
              for s in (fecha_registro, fecha_referencia)]
    if any(d.utcoffset() is None for d in fechas):
        raise ValueError("Se requiere zona horaria explícita")
    registro, referencia = fechas
    if registro > referencia:
        raise ValueError("El registro no puede ser posterior a la referencia")
    return {"dias_observados": (referencia - registro).days,
            "continuidad_demostrada": False, "cumplimiento_legal": "no_evaluado"}

if __name__ == "__main__":
    print(revisar_antiguedad("2026-09-13T00:00:00Z", "2026-10-13T00:00:00Z"))
```

**Alcance:** Un archivo antiguo o rotate N no prueba retención continua ni un número de días normativo. Revisar periodicidad, rotación por tamaño, huecos, permisos y alcance jurídico con fuentes oficiales y especialistas.

**Comprobación:** ejemplo ejecutado con datos ficticios; se probaron entradas válidas, límites y errores. La prueba cubre el comportamiento local de la función, no un sistema de producción.

## Evaluación del resultado

**Entregable:** informe con entradas, versiones, procedimiento, resultados y limitaciones.

* Afirmaciones jurídicas con fuente y revisión de aplicabilidad.
* Huecos y configuraciones no evaluadas visibles.
* Diferencias de configuración reproducibles en el laboratorio.

**Criterio de cierre:** otra persona puede repetir el análisis y distinguir lo observado de lo que permanece pendiente de revisión.

## Fuentes y profundización global

* [Regulation to strengthen protection over critical information infrastructure](https://english.www.gov.cn/policies/latestreleases/202108/17/content_WS611b8062c6d0df57f98de907.html).
* [NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

La [lección de referencia](../../malla-curricular/04-investigacion-global/02-china-cii-cac.md) reúne literatura y rutas de aprendizaje.

---

[🏠 Malla Curricular](../../README.md) | [🛠️ Todos los anexos](../README.md)
