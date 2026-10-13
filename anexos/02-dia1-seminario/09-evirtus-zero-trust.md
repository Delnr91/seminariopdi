# Anexo práctico: Arquitecturas Zero Trust para Redes Críticas - E-Virtus · ampliación temática

**Curaduría:** [Lattices](https://lattices.cl). Métodos propuestos para profundizar la temática; no son transcripciones ni recomendaciones atribuidas literalmente al speaker.

[▶️ Video relacionado: 09:26:40](https://www.youtube.com/watch?v=PEqWRTb1idE&t=34000s) · [Índice y límites de los tiempos](../../VIDEOS.md)

Ampliación temática de Lattices. Se enlaza el mismo bloque de Mauricio Barrera que la lección de efecto dominó; no se ha identificado una segunda charla dedicada a Zero Trust.

## Objetivo

Diseñar acceso basado en identidad y contexto para limitar propagación de fallos entre cargas de trabajo.

## Métodos y estrategias

| Método | Aplicación | Evidencia esperada |
| --- | --- | --- |
| **Inventario de identidades** | Relacionar persona o workload, servicio, acción y duración; distinguir identidad de pertenencia a una subred. | Matriz de acceso mínimo con propietario. |
| **Decisión y aplicación de política** | Separar autorización y punto de aplicación; registrar razones de rechazo y consecuencias de una dependencia caída. | Casos permitidos y denegados con evidencia. |
| **Microsegmentación comprobable** | Definir flujos indispensables y probar que las excepciones no abren movimientos laterales innecesarios. | Matriz de conectividad antes y después. |

## Herramientas open source

* [SPIRE](https://github.com/spiffe/spire) — Implementación de SPIFFE para identidades de workloads; requiere un diseño de confianza y attestation.
* [Cilium](https://github.com/cilium/cilium) — Políticas y observabilidad de red en entornos compatibles; no constituye por sí solo una arquitectura Zero Trust.

El ejercicio puede comenzar con tablas y archivos pequeños. Registrar la versión de cada herramienta y consultar su licencia y requisitos antes de preparar un entorno; software libre no implica infraestructura ni servicios externos gratuitos.

## Laboratorio guiado

**Entorno:** datos sintéticos o artefactos de ejemplo autorizados, en un espacio de práctica separado. Los archivos nombrados en los ejemplos son entradas o salidas que prepara el estudiante; no se suministran como descargas de este repositorio.

1. Definir tres workloads ficticios: portal, servicio de consulta y administración. Registrar las acciones que cada uno necesita.
2. Diseñar identidades SPIFFE y una política de acceso por servicio. Empezar con una tabla, sin desplegar Kubernetes.
3. En un laboratorio separado y preparado para ello, verificar flujo permitido, denegado, identidad ausente e identidad expirada.
4. Simular indisponibilidad del mecanismo de identidad y comprobar el procedimiento de continuidad sin convertirlo en acceso abierto.

### Ejemplo de trabajo

```csv
identidad,servicio,accion,decision
spiffe://laboratorio.example/portal,consulta,leer,permitir
spiffe://laboratorio.example/portal,administracion,modificar,denegar
```

## Evaluación del resultado

**Entregable:** un informe breve con datos de entrada, versiones, procedimiento, resultados, limitaciones y una mejora justificada.

* Permisos sin necesidad operacional eliminados.
* Casos de denegación y expiración correctamente aplicados.
* Flujos indispensables que siguen disponibles en el laboratorio.

**Criterio de cierre del ejercicio:** otra persona puede repetir el análisis y explicar los mismos hallazgos con la evidencia disponible. Los umbrales se acuerdan antes de evaluar; completar el ejercicio no acredita cumplimiento normativo ni aptitud para una operación crítica.

## Fuentes y profundización global

* [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final).
* [SPIFFE Overview](https://spiffe.io/docs/latest/spiffe-about/overview/).

La [lección de referencia](../../malla-curricular/02-dia1-seminario/09-evirtus-zero-trust.md) reúne papers, estándares y cursos adicionales para esta temática.

---

[🏠 Malla Curricular](../../README.md) | [📺 Videos por intervención](../../VIDEOS.md) | [🛠️ Todos los anexos](../README.md)
