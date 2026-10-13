# Seguridad y Resiliencia de la Infraestructura DNS - Guillermo Lama

## Síntesis Ejecutiva

El DNS conecta los nombres de los servicios con los destinos utilizados por aplicaciones y usuarios. Su indisponibilidad puede impedir el acceso a sistemas que continúan funcionando, mientras una resolución manipulada puede desviar conexiones hacia infraestructura hostil. DNSSEC incorpora autenticación del origen y verificación de integridad mediante firmas y una cadena de confianza; no cifra las consultas ni elimina los riesgos de saturación. La arquitectura debe abordar por separado autenticidad, disponibilidad y privacidad. [RFC 4033 — DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033).

La resiliencia exige distribuir autoridad y resolución sin reproducir dependencias comunes de red, energía o administración. Anycast puede mejorar la distribución del tráfico, pero no sustituye la capacidad suficiente ni la operación correcta de las zonas. La rotación de claves, la publicación de registros DS y la monitorización de errores de validación necesitan procedimientos de cambio y recuperación. La evaluación debe considerar expiraciones, fallos de proveedores y tiempos de propagación, además de distinguir una respuesta criptográficamente válida de un destino seguro para el usuario. [CISA — DNS Risk Assessment](https://www.cisa.gov/sites/default/files/c3vp/DNS_Risk_Assessment.pdf).

## Conceptos Core

* **DNSSEC:** Extensiones que permiten verificar el origen y la integridad de los datos DNS mediante firmas digitales.
* **Cadena de confianza:** Relación entre anclas de confianza, registros DS y claves DNSKEY utilizada para validar zonas.
* **Anycast:** Anuncio de una dirección desde múltiples ubicaciones para dirigir tráfico según el enrutamiento de la red.
* **Resiliencia de resolución:** Capacidad de mantener consultas y respuestas correctas ante fallos de nodos, rutas o dependencias.

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks

* [RFC 4033 — DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033) — comprender el modelo de seguridad y sus límites.
* [RFC 4035 — Protocol Modifications for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4035) — estudiar validación, firmas y comportamiento del protocolo.

### Papers y Literatura de Frontera

* [CISA — DNS Risk Assessment](https://www.cisa.gov/sites/default/files/c3vp/DNS_Risk_Assessment.pdf) — examinar riesgos de las funciones de resolución y de la operación DNS.

### Repositorios y Herramientas Open Source

* [Unbound](https://github.com/NLnetLabs/unbound) — construir un laboratorio de resolución con validación DNSSEC.
* [DNSViz](https://github.com/dnsviz/dnsviz) — analizar cadenas de confianza y problemas de configuración DNSSEC.

### Ruta de Aprendizaje Autónoma

* [Host your domain on Azure DNS](https://learn.microsoft.com/en-us/training/modules/host-domain-azure-dns/) — aprender gestión de zonas y registros; material gratuito, despliegues Azure sujetos a costes.

## 🎧 Audio Resumen

**Grabación pendiente.** El siguiente enlace estará disponible al incorporar el MP3.

[▶️ Escuchar Podcast Resumen](../../assets/audio/02-lama-infraestructura-dns.mp3)

---

[⬅ Lección Anterior](01-wong-ia-cibercrimen.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](03-fernandez-crimen-ia.md)
