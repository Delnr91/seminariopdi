# Verificación del Contenido Educativo

Revisión realizada el **13 de octubre de 2026**.

## Estructura y Navegación

El recorrido conserva **21 páginas: dos documentos de fundamentos y 19 lecciones temáticas**. Se agregaron **18 anexos prácticos**, su índice y un índice audiovisual. Las 16 lecciones de las jornadas enlazan su intervención y su anexo. El README permite abrir los videos y mantiene la atribución a Lattices.

La revisión de rutas abarcó los 47 documentos Markdown del repositorio y 321 referencias locales. Se comprobaron tablas, anclas, enlaces locales, catálogo y navegación; los únicos destinos locales pendientes son los 19 nombres de MP3 declarados como pendientes. Se validó la sintaxis de 13 ejemplos JSON, CSV y YAML. Los cinco ejemplos restantes son comandos de consulta o procesamiento de archivos.

La API de Markdown de GitHub renderizó correctamente el README, el índice de videos, el índice de anexos, una lección y un anexo representativos. Se comprobó la aparición de las tablas y los enlaces audiovisuales; esto no equivale a una prueba de cada app móvil ni a ejecutar los laboratorios.

El catálogo de datos mantiene las 19 lecciones y agrega 17 bloques de video y 18 anexos. Se comprobó que los intervalos no se superponen, están dentro de la duración de cada grabación y coinciden entre catálogo, lecciones y enlaces. Las dos ampliaciones de E-Virtus apuntan al mismo bloque de Mauricio Barrera.

## Navegación Audiovisual

El [índice de videos](VIDEOS.md) documenta el método de inspección visual, los límites de precisión y puntos de contraste de las identidades. Se revisaron las grabaciones públicas de ambas jornadas y los rótulos de las intervenciones. No se realizó una transcripción completa ni una medición del tiempo individual de voz.

Los inicios, cierres y duraciones son **aproximados**. Los paneles se registran como bloques compartidos; las entradas de Fernanda Macías y Sergey Nikitin amplían la cobertura inicial. Los enlaces permiten saltar a una posición y no recortan, detienen ni eliminan anuncios del reproductor.

La consulta de la API de GitHub confirmó `visibility: public`, `private: false` y rama predeterminada `main`.

## Enlaces Externos

La revisión previa de las lecciones registró **87 URL únicas**, de las que **84 respondieron HTTP 200**; se conserva ese resultado como antecedente, sin presentarlo como una nueva comprobación de todos esos destinos.

En esta ampliación se incorporaron **16 destinos adicionales** al normalizar enlaces y agrupar los distintos minutos de cada video: **13 respondieron HTTP 200**, los **dos videos** se contrastaron mediante sus metadatos e imágenes públicas y **una guía de Zeek devolvió HTTP 429** al comprobador. La guía de Zeek pudo consultarse mediante el lector web, pero la petición directa quedó limitada. Se contrastaron las funciones de herramientas y ejemplos de comandos con documentación primaria.

Las siguientes referencias existen en sus fuentes oficiales, pero su disponibilidad no pudo verificarse completamente desde el entorno de comprobación:

| Fuente | Resultado |
| --- | --- |
| [https://eur-lex.europa.eu/eli/dir/2022/2555/oj](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | HTTP 202: respuesta sin contenido verificable |
| [https://publication.pravo.gov.ru/document/view/0001201707260023](https://publication.pravo.gov.ru/document/view/0001201707260023) | Tiempo de espera agotado, también en los reintentos |
| [https://trustedcomputinggroup.org/resource/tpm-library-specification/](https://trustedcomputinggroup.org/resource/tpm-library-specification/) | HTTP 403: comprobación automatizada bloqueada |
| [Zeek Quick Start Guide](https://docs.zeek.org/en/current/quickstart.html) | HTTP 429 en la petición directa; contenido consultado mediante el lector web |

Un HTTP 200 acredita una respuesta, no certifica la exactitud de toda la publicación ni disponibilidad permanente. Las páginas legales enlazadas deben contrastarse con modificaciones y disposiciones aplicables antes de deducir obligaciones concretas.

## Recursos Pendientes

**Faltan los 19 MP3**. Cada lección identifica la grabación pendiente y su nombre esperado; el [inventario de audio](assets/audio/README.md) es coherente con esas rutas. Los enlaces de podcast son placeholders hasta incorporar los archivos. Los documentos de fundamentos no tienen enlace de audio propio.

El directorio de [documentos PDF](assets/docs-pdf/README.md) permanece reservado. No se crearon archivos vacíos ni enlaces a PDF locales inexistentes.

## Alcance

La revisión comprueba estructura, navegación, catálogo, sintaxis de ejemplos y referencias. Las síntesis y los anexos son análisis educativo complementario, no transcripciones de las charlas. Los 18 laboratorios propuestos no se ejecutaron ni se desplegaron sus herramientas. Cada guía distingue entradas que debe preparar el estudiante, evidencias esperadas y métricas que todavía debe medir.

Las herramientas y perfiles enlazados no se presentan como certificados de conformidad; las prácticas que requieren infraestructura, servicios de pago o licencias indican ese posible coste. El [índice de anexos](anexos/README.md) propone comenzar con alternativas ligeras antes de preparar stacks completos.
