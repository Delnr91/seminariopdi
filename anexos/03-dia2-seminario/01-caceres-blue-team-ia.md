# Anexo práctico: Blue Team Aumentado por Inteligencia Artificial - Diego Cáceres

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 00:10:40](https://www.youtube.com/watch?v=jLbdG67TqW8&t=640s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Evaluar si la asistencia de IA mejora la detección sin perder trazabilidad ni aumentar acciones erróneas.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Detection engineering** | Relacionar hipótesis adversaria, evento disponible, regla y criterio de triage; registrar vacíos de telemetría. | Ficha de detección con fuente de datos y alcance. |
| **Comparación controlada** | Usar el mismo conjunto etiquetado para un proceso manual y otro asistido; mantener separada una colección de evaluación. | Resultados comparables con errores explicados. |
| **Purple Team acotado** | Ensayar un comportamiento autorizado y comprobar su recorrido hasta la alerta y la decisión del analista. | Evidencia de cobertura end-to-end en el laboratorio. |

## Herramientas open source

* [Sigma](https://github.com/SigmaHQ/sigma) — Formato y repositorio de detecciones; requiere adaptar campos y backend a la telemetría real.
* [CALDERA](https://github.com/apache/caldera) — Emulación adversaria en laboratorios autorizados; los plugins y perfiles deben revisarse antes de ejecutarlos.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Crear 20 registros ficticios de creación de procesos Windows y etiquetar cinco escenarios del laboratorio; incluir PowerShell administrativo, otros procesos y registros con campos ausentes.
2. Seleccionar una detección Sigma y documentar qué campos necesita. Si faltan datos, marcar la detección como no evaluable.
3. Comparar clasificación manual y asistida por un modelo local o un proveedor autorizado; conservar salida y evidencia citada para cada alerta.
4. Revisar falsos positivos y negativos. Como extensión, preparar una emulación CALDERA aislada; no ejecutarla en infraestructura real.

### Código y configuración de referencia

Regla Sigma experimental que exige indicios de descarga y de ejecución, además del proceso PowerShell. Debe convertirse con el backend y mapeo de campos apropiados.

```yaml
title: PowerShell con indicadores combinados de descarga y ejecucion
id: 5fb69381-2c60-4c41-91fb-fb121f51509f
status: experimental
description: Senal para revision; puede coincidir con administracion legitima.
tags:
    - attack.execution
    - attack.t1059.001
logsource:
    category: process_creation
    product: windows
detection:
    imagen:
        Image|endswith:
            - '\powershell.exe'
            - '\pwsh.exe'
    descarga:
        CommandLine|contains:
            - 'DownloadString'
            - 'Net.WebClient'
    ejecucion:
        CommandLine|contains:
            - 'Invoke-Expression'
            - 'IEX'
    condition: imagen and descarga and ejecucion
falsepositives:
    - Automatizacion administrativa autorizada.
level: medium
```

**Alcance:** Una coincidencia no confirma intrusión. Probar casos positivos y negativos, incluidos scripts legítimos y telemetría incompleta; no aislar equipos automáticamente por esta regla aislada.

**Comprobación:** YAML leído y estructura revisada. No se desplegó la configuración ni se convirtió con un backend operativo.

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Precisión: verdaderos positivos / alertas generadas.
* Recall: verdaderos positivos / anomalías etiquetadas.
* Tiempo de triage y proporción de conclusiones con evidencia verificable.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html).
* [Sigma: Getting Started](https://sigmahq.io/docs/guide/getting-started.html).
* [MITRE D3FEND](https://d3fend.mitre.org/).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/01-caceres-blue-team-ia.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
