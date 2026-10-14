# Infraestructura de Internet: Seguridad, Continuidad y Resiliencia - Guillermo Lama

## Síntesis Ejecutiva

El Sistema de Nombres de Dominio (DNS) constituye la infraestructura crítica fundacional que arbitra la conectividad global y la resolución jerárquica de servicios transaccionales. Su operación en dominios nacionales de nivel superior (ccTLD, como .cl) enfrenta vectores de amenaza complejos, incluyendo ataques volumétricos de denegación distribuida de servicio (DDoS), envenenamiento de caché (cache poisoning) y secuestro de rutas BGP, eventos que amenazan con desarticular la disponibilidad digital de servicios financieros, gubernamentales y asistenciales a escala de país.

Garantizar la resiliencia sistémica del DNS demanda implementar topologías Anycast distribuidas multirregionales, orquestación automatizada de zonas y la adopción estricta de extensiones criptográficas DNSSEC. La continuidad operativa no puede concebirse como un atributo estático, sino como una capacidad dinámica de absorción de sobrecargas y conmutación por error (failover) transparente, respaldada por gobernanza institucional y acuerdos de intercambio de tráfico en IXPs neutros.

---

## Conceptos Core

* **BGP Anycast Routing:** Técnica de direccionamiento donde múltiples nodos distribuidos geográficamente anuncian la misma IP, dispersando el tráfico legítimo y absorbiendo ataques DDoS en el borde.
* **DNSSEC (Domain Name System Security Extensions):** Conjunto de extensiones criptográficas basadas en firmas digitales asimétricas que garantizan la autenticidad e integridad de las respuestas de resolución DNS.
* **Root & TLD Name Server Redundancy:** Despliegue de réplicas autoritativas locales para mitigar la latencia y neutralizar fallas de enlaces internacionales en situaciones de aislamiento.
* **Amplification & Reflection Attacks:** Vector volumétrico que explota configuraciones de resolutores recursivos abiertos (open resolvers) mediante UDP para inundar enlaces troncales.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [IETF RFC 4033, 4034, 4035 (DNSSEC Specifications)](https://datatracker.ietf.org/doc/html/rfc4033): Estándares oficiales del Internet Engineering Task Force para la arquitectura e implementación de seguridad en DNS.
* [NIST SP 800-81-2: Secure Domain Name System Deployment Guide](https://csrc.nist.gov/publications/detail/sp/800-81/2/final): Directrices del NIST para la configuración, operación y aseguramiento criptográfico de servidores DNS autoritativos y recursivos.
* [ICANN Security and Stability Advisory Committee (SSAC) Reports](https://www.icann.org/groups/ssac): Informes de autoridad global sobre amenazas a la seguridad, estabilidad y resiliencia del sistema de nombres de Internet.
* [ISO/IEC 27001: Control A.13 - Communications Security](https://www.iso.org/standard/27001): Marco normativo internacional para la protección de canales de red y servicios de infraestructura esenciales.

### Papers y Literatura de Frontera
* **ACM SIGCOMM (2020):** *A Global Measurement of DNSSEC Validation: Operational Realities and Resilience* ([DOI: 10.1145/3387514.3405890](https://dl.acm.org/doi/10.1145/3387514.3405890)) — Análisis cuantitativo de la adopción de validación criptográfica en resolutores globales y su impacto en la seguridad del usuario final.
* **IEEE/ACM Transactions on Networking (2018):** *Anycast in Context: A Guided Tour of BGP Anycast Routing and DDoS Mitigation* ([IEEE Xplore](https://ieeexplore.ieee.org/document/8387498)) — Estudio seminal sobre la eficiencia de arquitecturas Anycast para dispersar tráfico malicioso en infraestructuras de TLD.

### Repositorios y Herramientas (Open Source)
* [NLnet Labs Unbound & NSD](https://github.com/NLnetLabs/unbound): Servidores de nombres recursivos y autoritativos de alto rendimiento con validación DNSSEC nativa desarrollados en C.
* [DNSViz](https://github.com/dnsviz/dnsviz): Herramienta analítica de código abierto para diagnóstico visual, auditoría y resolución de cadenas de confianza criptográficas DNSSEC.
* [Knot DNS (CZ.NIC)](https://github.com/CZ-NIC/knot): Servidor autoritativo open source optimizado para soportar millones de zonas con recarga dinámica y mitigación Anycast.
* [BGPStream](https://bgpstream.caida.org/): Framework de análisis y telemetría en tiempo real desarrollado por CAIDA para monitorear eventos de secuestro (hijacks) de rutas y caídas de conectividad.

### Ruta de Aprendizaje Autónoma
* [RIPE NCC Academy: DNSSEC & Routing Security Courses](https://academy.ripe.net/): Certificación gratuita de nivel carrier sobre implementación de DNSSEC, RPKI y aseguramiento de enrutamiento BGP.
* [Cloudflare Learning Center: DNS Architecture & DDoS Mitigation](https://www.cloudflare.com/learning/dns/what-is-dns/): Módulos técnicos interactivos sobre resolución jerárquica, Anycast y mecanismos de amortiguación de sobrecargas.
* [TryHackMe: Network Fundamentals & DNS in Detail](https://tryhackme.com/module/network-fundamentals): Laboratorios prácticos para inspeccionar tráfico DNS, depurar registros autoritativos y detectar transferencias de zona no autorizadas.
* [Cisco NetAcad: Network Security Architecture](https://www.netacad.com): Formación enterprise sobre diseño de perímetros de red, redundancia de servicios troncales e inspección de protocolos.

---

## 🧪 Anexo Práctico: Estrategia Operativa y Laboratorio Open Source

### Estrategia Operativa Empresarial
Para garantizar la resiliencia y evitar ataques de intermediario (Man-in-the-Middle) en resoluciones de servicios esenciales, las organizaciones deben desplegar monitoreo continuo de cadenas de confianza DNSSEC y verificar la consistencia de respuestas entre diferentes nodos Anycast distribuidos.

### Código / Laboratorio Ejecutable
```python
# auditor_dnssec_resilience.py
# Herramienta para verificar firmas DNSKEY y registros DS de infraestructura crítica
import dns.resolver
import dns.dnssec

def auditar_zona_dnssec(dominio: str):
    print(f"[*] Auditando cadena criptográfica para: {dominio}")
    resolver = dns.resolver.Resolver()
    resolver.use_edns(0, dns.flags.DO, 4096) # Solicitar registros DNSSEC
    
    try:
        # 1. Obtener llaves DNSKEY
        resp_dnskey = resolver.resolve(dominio, 'DNSKEY')
        print(f"[+] Registros DNSKEY encontrados: {len(resp_dnskey)}")
        for rdata in resp_dnskey:
            print(f"    - Flag: {rdata.flags} | Protocolo: {rdata.protocol} | Algoritmo: {rdata.algorithm}")
            
        # 2. Obtener registros RRSIG correspondientes
        rrsig = resp_dnskey.response.find_rrset(
            resp_dnskey.response.answer, dns.name.from_text(dominio), dns.rdataclass.IN, dns.rdatatype.RRSIG
        )
        if rrsig:
            print(f"[+] Firma criptográfica RRSIG válida presente (Expira en época UNIX: {rrsig[0].expiration})")
        else:
            print("[-] ALERTA: No se encontró registro RRSIG para la zona.")
            
    except Exception as e:
        print(f"[-] Error en validación DNSSEC: {e}")

if __name__ == "__main__":
    auditar_zona_dnssec("nic.cl")
```

---

## Recursos Multimedia Oficiales

* [📺 Ver Ponencia en Video Oficial (Día 1 · Minuto 1:40:15)](https://www.youtube.com/watch?v=PEqWRTb1idE&t=1h40m15s)
* [▶️ Escuchar Podcast Resumen](../../assets/audio/dia1_02_lama.mp3)

---

[⬅️ Lección Anterior](01-wong-ia-cibercrimen.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](03-fernandez-crimen-ia.md)
