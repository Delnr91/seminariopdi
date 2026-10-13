# Verificación de la malla curricular

Comprobación realizada el **13 de octubre de 2026** sobre la construcción local del repositorio.

## Contenido y estructura

- 19 lecciones procedentes de `datos_seminario.json`: 9 del día 1, 7 del día 2 y 3 de investigación global.
- Las lecciones conservan los campos pedagógicos de AGY y las secciones de la plantilla, incluidos los bloques `<audio>` y `<details>`.
- Las listas contienen tres aprendizajes y tres casillas sin prefijos duplicados.
- `04-comparativa-internacional` se ubica en `malla-curricular/04-investigacion-global`, según la estructura solicitada.
- Los directorios sin material cuentan con un README para conservarlos en Git.
- Los archivos creados en el repositorio son Markdown. Se conservan el JSON y el generador Python preexistentes de AGY.

## Enlaces locales y material pendiente

Se comprobaron todos los destinos relativos en los archivos Markdown, incluidos los atributos `href` y `src` de la plantilla. Los enlaces de navegación y a documentos existentes resuelven correctamente.

**Excepción pendiente: faltan 19 MP3**, referenciados en 38 atributos de las lecciones (un `src` y un `href` por lección). Por tanto, no se puede declarar que todos los enlaces estén operativos. No se crearon archivos vacíos con extensión MP3 para ocultar el problema.

El inventario está en [assets/audio/README.md](assets/audio/README.md). Los guiones están en [datos_seminario.json](datos_seminario.json). Faltan también los documentos PDF y el contenido del módulo de fundamentos; no se enlazan documentos PDF ni lecciones que aún no existen.

## Compatibilidad de audio con GitHub

Se envió una muestra genérica, sin contenido del repositorio, al [endpoint oficial de renderizado Markdown de GitHub](https://docs.github.com/en/rest/markdown/markdown#render-a-markdown-document). El resultado eliminó la etiqueta `<audio>` y su atributo `src`, conservó el enlace `Descargar MP3` y mantuvo `<details>` y `<summary>`.

Esto concuerda con el filtrado de HTML descrito en [GitHub Markup](https://github.com/github/markup). La plantilla se conserva en los archivos fuente, pero no se promete un reproductor incrustado en GitHub. La alternativa es abrir o descargar los MP3 cuando se incorporen. No se ha verificado la reproducción en la app móvil porque no hay audios.

## Correcciones de enlaces

Se preservó el JSON original; las correcciones se aplicaron a las lecciones generadas.

| URL recibida | URL usada | Evidencia |
| --- | --- | --- |
| `https://www.youtube.com/@PDIChileOficial` (HTTP 404) | `https://www.youtube.com/@PDIChile` | [La PDI enlaza su canal oficial](https://www.pdichile.cl/centro-de-prensa/detalle-prensa/2024/06/24/cuenta-p%C3%BAblica-2024) |
| `https://www.iafis.com` (no resuelve DNS) | `https://www.iafisgroup.com/nosotros/` | [Sitio corporativo de IAFIS Group](https://www.iafisgroup.com/nosotros/) |
| `https://www.village.bio` (no resuelve DNS) | `https://www.villageb.io/` | [Sitio oficial de Biohacking Village](https://www.villageb.io/) |

## Comprobación de enlaces externos de las lecciones

Se efectuaron peticiones HTTP GET a las 27 URL únicas, con validación TLS y un límite de 15 segundos por petición. Se comprobaron las tres correcciones y se reintentó Sophos por tiempo de espera agotado.

**Resultado: 19 URL con HTTP 200 y 8 sin verificar.** Un HTTP 200 acredita una respuesta del servidor; no certifica el contenido de la página ni la disponibilidad de un video para todos los usuarios. Un 403, un problema TLS o una limitación de conectividad no prueban que el enlace sea inexistente.

Las lecciones del día 2 enlazan el canal oficial porque AGY no suministró una grabación específica de esa jornada. Las tres lecciones internacionales no tienen video oficial en los datos y lo indican sin inventar una URL.

| Destino usado en las lecciones | Resultado |
| --- | --- |
| [http://pravo.gov.ru](http://pravo.gov.ru) | HTTP 200 |
| [http://safe-surf.ru](http://safe-surf.ru) | HTTP 200 |
| [http://www.cac.gov.cn](http://www.cac.gov.cn) | HTTP 200 |
| [http://www.tc260.org.cn](http://www.tc260.org.cn) | HTTP 200 |
| [https://e-virtus.com](https://e-virtus.com) | HTTP 200 |
| [https://fstec.ru](https://fstec.ru) | Error de verificación TLS; no se desactivó la validación del certificado |
| [https://inf.utfsm.cl](https://inf.utfsm.cl) | Destino inaccesible desde este entorno |
| [https://sek.com](https://sek.com) | HTTP 200 |
| [https://usm.cl](https://usm.cl) | HTTP 200 |
| [https://www.cisa.gov/cpgs](https://www.cisa.gov/cpgs) | HTTP 200 |
| [https://www.coordinador.cl](https://www.coordinador.cl) | HTTP 403: acceso automatizado bloqueado |
| [https://www.csirt.gob.cl](https://www.csirt.gob.cl) | HTTP 200 |
| [https://www.gob.cl](https://www.gob.cl) | HTTP 200 |
| [https://www.gov.uk/fcdo](https://www.gov.uk/fcdo) | HTTP 200 |
| [https://www.iafisgroup.com/nosotros/](https://www.iafisgroup.com/nosotros/) | HTTP 403: acceso automatizado bloqueado |
| [https://www.lenovo.com](https://www.lenovo.com) | HTTP 200 |
| [https://www.mps.gov.cn](https://www.mps.gov.cn) | HTTP 521: servidor no disponible para esta comprobación |
| [https://www.ncsc.gov.uk](https://www.ncsc.gov.uk) | HTTP 200 |
| [https://www.nic.cl](https://www.nic.cl) | HTTP 200 |
| [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework) | HTTP 200 |
| [https://www.pdichile.cl](https://www.pdichile.cl) | HTTP 403: acceso automatizado bloqueado |
| [https://www.pdichile.cl/seminariociberseguridad](https://www.pdichile.cl/seminariociberseguridad) | HTTP 403: acceso automatizado bloqueado |
| [https://www.sophos.com](https://www.sophos.com) | Tiempo de espera agotado (también en el reintento) |
| [https://www.ubo.cl](https://www.ubo.cl) | HTTP 200 |
| [https://www.villageb.io/](https://www.villageb.io/) | HTTP 200 |
| [https://www.youtube.com/@PDIChile](https://www.youtube.com/@PDIChile) | HTTP 200 |
| [https://www.youtube.com/watch?v=PEqWRTb1idE](https://www.youtube.com/watch?v=PEqWRTb1idE) | HTTP 200 |

## Alcance de la verificación

Se comprobó la construcción y navegación del material, no la exactitud independiente de cada afirmación pedagógica ni la vigencia de todos los marcos normativos del contenido recibido. La comprobación HTTP no usa sesiones privadas ni modifica los servicios consultados.
