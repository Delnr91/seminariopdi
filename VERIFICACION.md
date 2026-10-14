# Verificación del Contenido Educativo

Revisión realizada el **13 de octubre de 2026**.

## Estructura y Navegación

El recorrido conserva **21 páginas: dos documentos de fundamentos y 19 lecciones temáticas**. Se integraron **21 anexos prácticos**, su índice y un índice audiovisual. Las 16 lecciones de las jornadas enlazan su intervención y su anexo; los tres módulos internacionales enlazan su ejercicio complementario. El README permite abrir los videos y mantiene la atribución a Lattices.

La revisión de rutas abarcó los 50 documentos Markdown del repositorio y 339 referencias locales. Se comprobaron tablas, anclas, enlaces locales, catálogo y navegación; los únicos destinos locales pendientes son los 19 nombres de MP3 declarados como pendientes. Se ejecutaron los 12 ejemplos Python de biblioteca estándar con datos ficticios y se probaron sus funciones con 17 pruebas automatizadas, que incluyen casos normales, límites y errores. Se revisó la sintaxis de tres bloques Bash y se leyeron tres configuraciones YAML; una regla de Suricata se contrastó con documentación oficial. Además se validaron los ejemplos de datos conservados en las guías complementarias.

La API de Markdown de GitHub renderizó correctamente el README, el índice de anexos y tres guías representativas de Python, YAML e investigación internacional. La navegación audiovisual conserva el renderizado comprobado en la revisión anterior. Se comprobó la aparición de las tablas y los enlaces audiovisuales; esto no equivale a una prueba de cada app móvil ni a ejecutar los laboratorios.

El catálogo de datos mantiene las 19 lecciones y agrega 17 bloques de video y 21 anexos. Se comprobó que los intervalos no se superponen, están dentro de la duración de cada grabación y coinciden entre catálogo, lecciones y enlaces. Las dos ampliaciones de E-Virtus apuntan al mismo bloque de Mauricio Barrera.

## Navegación Audiovisual

El [índice de videos](VIDEOS.md) documenta el método de inspección visual, los límites de precisión y puntos de contraste de las identidades. Se revisaron las grabaciones públicas de ambas jornadas y los rótulos de las intervenciones. No se realizó una transcripción completa ni una medición del tiempo individual de voz.

Los inicios, cierres y duraciones son **aproximados**. Los paneles se registran como bloques compartidos; las entradas de Fernanda Macías y Sergey Nikitin amplían la cobertura inicial. Los enlaces permiten saltar a una posición y no recortan, detienen ni eliminan anuncios del reproductor.

La consulta de la API de GitHub confirmó `visibility: public`, `private: false` y rama predeterminada `main`.

## Enlaces Externos

La revisión previa de las lecciones registró **87 URL únicas**, de las que **84 respondieron HTTP 200**; se conserva ese resultado como antecedente, sin presentarlo como una nueva comprobación de todos esos destinos.

En la ampliación audiovisual anterior se incorporaron **16 destinos adicionales** al normalizar enlaces y agrupar los distintos minutos de cada video: **13 respondieron HTTP 200**, los **dos videos** se contrastaron mediante sus metadatos e imágenes públicas y **una guía de Zeek devolvió HTTP 429** al comprobador. La guía de Zeek pudo consultarse mediante el lector web, pero la petición directa quedó limitada. Se contrastaron las funciones de herramientas y ejemplos de comandos con documentación primaria.

La integración técnica incorporó **10 referencias nuevas**, todas con respuesta **HTTP 200**. Se contrastaron documentos oficiales de DNSSEC, STIX, Sigma, Suricata, TPM, CTFd y verificación de firmas. No se revalidaron todos los destinos de revisiones anteriores.

Las siguientes referencias existen en sus fuentes oficiales, pero su disponibilidad no pudo verificarse completamente desde el entorno de comprobación:

| Fuente | Resultado |
| --- | --- |
| [https://eur-lex.europa.eu/eli/dir/2022/2555/oj](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | HTTP 202: respuesta sin contenido verificable |
| [https://publication.pravo.gov.ru/document/view/0001201707260023](https://publication.pravo.gov.ru/document/view/0001201707260023) | Tiempo de espera agotado, también en los reintentos |
| [https://trustedcomputinggroup.org/resource/tpm-library-specification/](https://trustedcomputinggroup.org/resource/tpm-library-specification/) | HTTP 403: comprobación automatizada bloqueada |
| [Zeek Quick Start Guide](https://docs.zeek.org/en/current/quickstart.html) | HTTP 429 en la petición directa; contenido consultado mediante el lector web |

Un HTTP 200 acredita una respuesta, no certifica la exactitud de toda la publicación ni disponibilidad permanente. Las páginas legales enlazadas deben contrastarse con modificaciones y disposiciones aplicables antes de deducir obligaciones concretas.

## Alcance de los Ejemplos Técnicos

Los ejemplos distinguen evidencia y simulación: un patrón léxico no autoriza un agente, un contador sintético no verifica vida o identidad y una coincidencia de proceso o mensaje no demuestra una intrusión ni coordinación. El control de herramientas mock rechaza acciones desconocidas, parámetros ausentes, negativos, valores no finitos y booleanos usados como números.

La verificación del SBOM de proveedor se separa del inventario generado localmente. Los ejercicios internacionales no implementan conectores oficiales ni una fórmula certificada de madurez. Las fichas de incidentes declaran explícitamente que no se enviaron y no afirman bloqueos que no ejecutaron. Las configuraciones de laboratorio conservan el acceso local y exigen preparar versiones y datos de confianza.

## Recursos Pendientes

**Faltan los 19 MP3**. Cada lección identifica la grabación pendiente y su nombre esperado; el [inventario de audio](assets/audio/README.md) es coherente con esas rutas. Los enlaces de podcast son placeholders hasta incorporar los archivos. Los documentos de fundamentos no tienen enlace de audio propio.

El directorio de [documentos PDF](assets/docs-pdf/README.md) permanece reservado. No se crearon archivos vacíos ni enlaces a PDF locales inexistentes.

## Alcance

La revisión comprueba estructura, navegación, catálogo, sintaxis de ejemplos y referencias. Las síntesis y los anexos son análisis educativo complementario, no transcripciones de las charlas. Se ejecutaron los ejemplos locales de Python y sus pruebas. Los 21 laboratorios completos no se ejecutaron ni se desplegaron sus herramientas externas; una lectura válida de YAML o Bash no verifica su comportamiento en un clúster, sensor o servicio real. Cada guía distingue entradas que debe preparar el estudiante, evidencias esperadas y métricas que todavía debe medir.

Las herramientas y perfiles enlazados no se presentan como certificados de conformidad; las prácticas que requieren infraestructura, servicios de pago o licencias indican ese posible coste. El [índice de anexos](anexos/README.md) propone comenzar con alternativas ligeras antes de preparar stacks completos.
