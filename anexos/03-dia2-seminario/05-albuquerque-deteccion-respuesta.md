# Anexo práctico: Prevención, Detección y Respuesta ante Ciberamenazas - Tales Albuquerque

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 03:24:00](https://www.youtube.com/watch?v=jLbdG67TqW8&t=12240s) · [Índice y límites de los tiempos](../../VIDEOS.md)

## Objetivo

Conectar una hipótesis de intrusión con evidencia mínima, una decisión de contención y una recuperación comprobable.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Threat hunting por hipótesis** | Formular qué comportamiento se busca y qué eventos podrían demostrarlo o refutarlo. | Consulta o búsqueda con criterio de descarte. |
| **Recopilación mínima** | Seleccionar artefactos pertinentes a la hipótesis; registrar permisos, período e integridad. | Paquete de evidencia acotado y documentado. |
| **Contención proporcional** | Comparar revocación de sesión, aislamiento y suspensión de cuenta según impacto; definir reversión antes de actuar. | Plan de respuesta con autoridad y condiciones de cierre. |

## Herramientas open source

* [Velociraptor](https://github.com/Velocidex/velociraptor) — Recolección y consulta de artefactos; revisar cada definición y alcance antes de autorizarla.
* [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) — Pruebas asociadas a ATT&CK; algunas alteran sistemas o descargan componentes. Su ejecución queda para un laboratorio aislado y revisado.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Crear una cronología sintética: autenticación, acceso a archivo ficticio y solicitud de privilegio; incluir una explicación benigna alternativa.
2. Seleccionar un artefacto de Velociraptor y leer su definición; identificar qué datos recoge y qué evidencia no proporciona.
3. Si hay una VM de práctica autorizada, recoger únicamente los artefactos elegidos y comparar la cronología; en caso contrario, trabajar con un paquete sintético.
4. Diseñar contención y recuperación en una mesa de trabajo. Definir quién autoriza, cómo se conserva evidencia y qué prueba permite cerrar el caso.

### Ejemplo de trabajo

```csv
hora_utc,evento,evidencia,hipotesis
2026-10-13T10:00:00Z,acceso_ficticio,registro_auth,cuenta_posiblemente_abusada
2026-10-13T10:02:00Z,archivo_consultado,registro_app,requiere_correlacion
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Hipótesis confirmadas o refutadas mediante dos evidencias independientes cuando sea posible.
* Tiempo desde clasificación hasta decisión de contención en el ejercicio.
* Acciones con autorización, reversión y comprobación de recuperación.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [Velociraptor Artifacts](https://docs.velociraptor.app/docs/artifacts/).
* [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

La [lección de referencia](../../malla-curricular/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
