# 9° Seminario de Ciberseguridad PDI-USM 2026

Malla de aprendizaje sobre **protección de la infraestructura crítica y ciberresiliencia**, basada en el 9° Seminario Internacional de Ciberseguridad organizado por la Policía de Investigaciones de Chile (PDI) y la Universidad Técnica Federico Santa María (USM).

Las lecciones presentan analogías, explicaciones, tres aprendizajes, una lista de chequeo preventiva y una autoevaluación con respuesta desplegable. El recorrido reúne **una guía de fundamentos y 19 lecciones: 9 del día 1, 7 del día 2 y 3 de investigación global**, para estudiar la protección de servicios como electricidad, agua, salud, banca e Internet.

Abre una lección desde la tabla para leerla en la aplicación móvil o en la web de GitHub. Todo el material de lectura está en GitHub Flavored Markdown (GFM), sin CSS, JavaScript, frameworks ni despliegue.

## Malla Curricular

Empieza por fundamentos y sigue el orden de la tabla. Al final de cada lección encontrarás enlaces a la anterior, a la siguiente y a esta malla curricular; al inicio y al final del recorrido se indica el límite correspondiente.

| Módulo | Lección | Speaker | Nivel |
| --- | --- | --- | --- |
| Fundamentos | [Glosario y conceptos clave](malla-curricular/01-fundamentos/01-glosario-y-conceptos-clave.md) | Documento base del seminario | Principiante |
| Día 1 del seminario | [Adversarios digitales IA y el nuevo escenario de amenazas a la infraestructura crítica](malla-curricular/02-dia1-seminario/01-wong-ia-cibercrimen.md) | Subprefecto Marcelo Wong Cea | Principiante |
| Día 1 del seminario | [Infraestructura de Internet: Seguridad, Continuidad y Resiliencia](malla-curricular/02-dia1-seminario/02-lama-infraestructura-dns.md) | Guillermo Lama | Principiante |
| Día 1 del seminario | [El lado práctico del crimen con IA](malla-curricular/02-dia1-seminario/03-fernandez-crimen-ia.md) | Manu Fernández | Intermedio |
| Día 1 del seminario | [Ciberseguridad y Resiliencia: Un Desafío Nacional](malla-curricular/02-dia1-seminario/04-bordachar-anci-regulacion.md) | Michelle Bordachar | Principiante |
| Día 1 del seminario | [Un Incidente, Múltiples Impactos: La Criticidad de la Ciberseguridad](malla-curricular/02-dia1-seminario/05-evirtus-efecto-domino.md) | Representante Técnico Sectorial | Intermedio |
| Día 1 del seminario | [Anatomía de un dispositivo médico conectado: explorando sus superficies de ataque](malla-curricular/02-dia1-seminario/06-fernandez-dispositivos-medicos.md) | Víctor Fernández | Avanzado |
| Día 1 del seminario | [Protegiendo lo Esencial: Ciberseguridad y Resiliencia en Sectores Críticos](malla-curricular/02-dia1-seminario/07-panel-sectores-criticos.md) | Panel Multisectorial (Soledad Bastías, Patricio Leyton, Juan Huechucura, Cristián Bravo) | Intermedio |
| Día 1 del seminario | [Agentes IA e infraestructura crítica: entre la falla operativa y el arma de ciberguerra](malla-curricular/02-dia1-seminario/08-bonnaire-agentes-ia.md) | Dr. Xavier Bonnaire | Avanzado |
| Día 1 del seminario | [Seguridad en la Red: Hacia una infraestructura crítica resiliente](malla-curricular/02-dia1-seminario/09-evirtus-zero-trust.md) | Especialista en Redes | Intermedio |
| Día 2 del seminario | [Blue team aumentado por inteligencia artificial: modelos de ciberdefensa y resiliencia para infraestructuras críticas](malla-curricular/03-dia2-seminario/01-caceres-blue-team-ia.md) | Diego Cáceres | Intermedio |
| Día 2 del seminario | [Cyber Threat Intelligence (CTI)](malla-curricular/03-dia2-seminario/02-fuentes-threat-intelligence.md) | Omar Fuentes | Intermedio |
| Día 2 del seminario | [El Rol de la Tecnología en la Continuidad y Resiliencia Operacional](malla-curricular/03-dia2-seminario/03-cordero-resiliencia-hardware.md) | César Cordero | Intermedio |
| Día 2 del seminario | [Ciberseguridad en Salud: Protegiendo la Infraestructura que Protege Vidas](malla-curricular/03-dia2-seminario/04-alli-salud-ciberseguridad.md) | Nina Alli | Principiante |
| Día 2 del seminario | [Seguridad Digital: Prevención, Detección y Respuesta ante Ciberamenazas](malla-curricular/03-dia2-seminario/05-albuquerque-deteccion-respuesta.md) | Tales Albuquerque | Intermedio |
| Día 2 del seminario | [Amenazas híbridas en la era digital](malla-curricular/03-dia2-seminario/06-norman-amenazas-hibridas.md) | James Norman | Principiante |
| Día 2 del seminario | [Transformación Digital y Ciberresiliencia: El Rol de la Academia](malla-curricular/03-dia2-seminario/07-abbas-academia-talento.md) | Nadezda Abbas | Principiante |
| Investigación global | [Marco NIST CSF 2.0 y Guías de Ciberresiliencia CISA/NCSC](malla-curricular/04-investigacion-global/01-nist-cisa-ncsc.md) | Marco CISA / NIST & NCSC | Intermedio |
| Investigación global | [Reglamento de Infraestructura de Información Crítica (CII 2021) y Soberanía de Datos](malla-curricular/04-investigacion-global/02-china-cii-cac.md) | Administración del Ciberespacio de China (CAC) | Avanzado |
| Investigación global | [Ley Federal N° 187-FZ de Seguridad de Infraestructura Crítica y GosSOPKA](malla-curricular/04-investigacion-global/03-rusia-187fz-fstec.md) | Servicio Federal de Control Técnico y Exportaciones (FSTEC / FSB) | Avanzado |

## Cómo escuchar las audio-clases

**Estado actual: los 19 MP3 están pendientes.** Las lecciones conservan el bloque de audio de la plantilla solicitada; sus enlaces de descarga aún no funcionan porque no existen los archivos. Los guiones están disponibles en el campo `guion_audio` de [datos_seminario.json](datos_seminario.json), y el [inventario de audios](assets/audio/README.md) indica los nombres esperados.

GitHub filtra el HTML al renderizar Markdown: no se debe depender de un reproductor `<audio>` incrustado en la lección. La [documentación del renderizador de GitHub](https://github.com/github/markup) describe este filtrado. La comprobación de una muestra mediante la API de Markdown de GitHub figura en el [informe de verificación](VERIFICACION.md).

Cuando se incorporen los MP3:

1. Abre la lección y pulsa **Descargar MP3**, o busca el archivo correspondiente en [assets/audio](assets/audio/).
2. En la vista del archivo de GitHub, usa **Download / Descargar archivo** o **Raw / Ver sin procesar**, según la interfaz disponible.
3. Abre el MP3 en el navegador o en el reproductor de tu dispositivo. La reproducción depende del navegador y de la app; no se garantiza un reproductor dentro del Markdown de GitHub.

El encabezado «1 Minuto» pertenece a la plantilla. Los guiones tienen entre 113 y 124 palabras, por lo que su extensión no garantiza una duración exacta de 60 segundos. La duración efectiva deberá verificarse cuando existan las grabaciones. La guía de fundamentos no dispone de un guion de audio propio.

## Recursos y procedencia

- [Datos de AGY](datos_seminario.json): fuente de las 19 lecciones y sus guiones, con las carpetas sincronizadas con la malla curricular.
- [Resumen de speakers](resumen_speakers_seminario_ciberseguridad.md): documento base del seminario.
- [Documentos PDF](assets/docs-pdf/README.md): directorio reservado, sin archivos PDF suministrados.
- [Verificación y pendientes](VERIFICACION.md): enlaces revisados, correcciones y límites de la comprobación.

Los recursos internacionales son material complementario. Se conserva el contenido pedagógico de AGY; su incorporación no equivale a una validación independiente de todas las afirmaciones técnicas o normativas.
