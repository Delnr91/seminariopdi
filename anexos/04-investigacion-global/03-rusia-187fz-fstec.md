# Anexo práctico: Seguridad de Infraestructura de Información Crítica en Rusia

**Curaduría:** [Lattices](https://lattices.cl). Material de investigación y práctica, sin atribución a un speaker ni a una ponencia audiovisual.

## Objetivo

Estudiar clasificación y preparación de evidencia sin inventar protocolos ni conectores oficiales.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Trazabilidad normativa** | Mantener fuente, versión, ámbito y preguntas pendientes separadas de la práctica técnica. | Matriz de referencia con incertidumbre explícita. |
| **Minimización de alertas** | Preparar una ficha sintética con origen, fecha y acción realmente confirmada. | Datos mínimos y estado de envío veraz. |
| **Validación de intercambio** | Antes de cualquier integración, contrastar esquema, autorización y destino con documentación oficial. | Lista de verificaciones y pruebas por realizar. |

## Herramientas open source

* [Suricata](https://github.com/OISF/suricata) — herramienta de análisis para un laboratorio preparado; su uso no acredita cumplimiento normativo.
* [MISP](https://github.com/MISP/MISP) — herramienta de análisis para un laboratorio preparado; su uso no acredita cumplimiento normativo.

## Laboratorio guiado

Usar únicamente archivos sintéticos y entornos de práctica; el ejemplo de Python usa la biblioteca estándar y no instala dependencias ni accede al sistema.

1. Crear un evento ficticio con una dirección reservada para documentación y sin nombres de equipos reales.
2. Generar la ficha local y comprobar que no contiene estados de bloqueo o envío que no sucedieron.
3. Relacionar campos con un evento de laboratorio en MISP o una alerta de PCAP; anotar campos faltantes y restricciones de distribución.
4. Documentar qué especificaciones y autorizaciones faltan para una eventual integración; terminar el ejercicio sin transmitir a terceros.

### Código y configuración de referencia

Generar una ficha local de laboratorio con una dirección documental y estado de envío explícito. No recoge hostname ni contacta servicios externos.

```python
from datetime import datetime, timezone
from ipaddress import ip_address, ip_network
import json
import uuid

def preparar_alerta_local(ip_origen, categoria):
    direccion = ip_address(ip_origen)
    if direccion not in ip_network("198.51.100.0/24"):
        raise ValueError("Usar una dirección documental del laboratorio")
    if not isinstance(categoria, str) or not categoria.strip() or len(categoria) > 120:
        raise ValueError("Categoría inválida")
    return {"esquema": "alerta_local_laboratorio_v1", "id": str(uuid.uuid4()),
            "fecha_utc": datetime.now(timezone.utc).isoformat(),
            "ip_origen": str(direccion), "categoria": categoria.strip(),
            "accion_confirmada": "ninguna", "estado_envio": "no_enviado"}

if __name__ == "__main__":
    print(json.dumps(preparar_alerta_local("198.51.100.23", "evento_ficticio"), indent=2))
```

**Alcance:** El esquema es inventado únicamente para este ejercicio local; no es un protocolo GosSOPKA, una integración NKTsKI ni una prueba de cumplimiento de la Ley 187-FZ. Usar especificaciones oficiales para cualquier implementación real.

**Comprobación:** ejemplo ejecutado con datos ficticios; se probaron entradas válidas, límites y errores. La prueba cubre el comportamiento local de la función, no un sistema de producción.

## Evaluación del resultado

**Entregable:** informe con entradas, versiones, procedimiento, resultados y limitaciones.

* Campos con origen y significado documentados.
* Acciones y envíos declarados solo cuando existen evidencias.
* Esquemas ficticios identificados claramente y sin atribución oficial.

**Criterio de cierre:** otra persona puede repetir el análisis y distinguir lo observado de lo que permanece pendiente de revisión.

## Fuentes y profundización global

* [Федеральный закон от 26.07.2017 № 187-ФЗ](https://publication.pravo.gov.ru/document/view/0001201707260023).
* [NIST SP 800-150 — Guide to Cyber Threat Information Sharing](https://csrc.nist.gov/pubs/sp/800/150/final).

La [lección de referencia](../../malla-curricular/04-investigacion-global/03-rusia-187fz-fstec.md) reúne literatura y rutas de aprendizaje.

---

[🏠 Malla Curricular](../../README.md) | [🛠️ Todos los anexos](../README.md)
