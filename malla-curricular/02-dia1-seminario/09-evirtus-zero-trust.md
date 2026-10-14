# Seguridad en la Red: Hacia una Infraestructura Crítica Resiliente - Especialista en Redes (E-Virtus)

## Síntesis Ejecutiva

El modelo de seguridad perimetral tradicional (Castillo y Foso) ha quedado formalmente obsoleto frente al auge del trabajo híbrido, la dispersión de cargas en nubes múltiples y la proliferación de credenciales corporativas robadas. Asumir que cualquier dispositivo o usuario conectado dentro de la red corporativa es inherentemente confiable constituye una vulnerabilidad estructural crítica: una vez que el adversario franquea el firewall de borde, disfruta de libertad irrestricta para ejecutar escaneos laterales no detectados y propagar ransomware hacia servidores transaccionales y salas de control industrial.

La construcción de una infraestructura verdaderamente resiliente exige la adopción integral del paradigma de Confianza Cero (Zero Trust: 'Nunca confíes, siempre verifica'). Este modelo descompone la red en microsegmentos granulares donde cada petición de conexión, tanto este-oeste como norte-sur, debe autenticarse, autorizarse y cifrarse continuamente en función de la identidad de la carga de trabajo, la postura del dispositivo y el contexto de riesgo. Si un endpoint en el área administrativa resulta infectado, las políticas de microsegmentación actúan como mamparas estancas en un buque, impidiendo que el compromiso alcance los sistemas SCADA de control eléctrico o bombeo de agua.

---

## Conceptos Core

* **Zero Trust Architecture (ZTA):** Paradigma de ciberseguridad que asume la red interna como hostil y exige autenticación y autorización continua para cada acceso a recursos.
* **East-West Microsegmentation:** División granular de la red interna para inspeccionar y bloquear el tráfico lateral no autorizado entre servidores de un mismo segmento o centro de datos.
* **Least Privilege Principle (POLP):** Asignación estricta del mínimo nivel de acceso y permisos temporales necesarios para que un usuario o máquina ejecute su tarea legítima.
* **Software-Defined Perimeter (SDP):** Tecnología que vuelve invisibles los servicios de infraestructura en internet, otorgando conectividad encriptada uno a uno solo tras una validación de identidad rigurosa.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final): Documento fundacional y estándar de referencia que describe los componentes lógicos (Policy Engine, Policy Administrator, PEP) de una arquitectura de confianza cero.
* [CISA Zero Trust Maturity Model 2.0](https://www.cisa.gov/zero-trust-maturity-model): Guía técnica para que organizaciones evalúen y evolucionen su madurez en cinco pilares: Identidad, Dispositivos, Redes, Cargas de trabajo y Datos.
* [DoD Zero Trust Strategy and Roadmap](https://dodcio.defense.gov/Cybersecurity/Zero-Trust/): Marco estratégico del Departamento de Defensa de EE.UU. para implementar Zero Trust a escala global en entornos de máxima criticidad.
* [ISO/IEC 27033 Series: Information Technology - Network Security](https://www.iso.org/standard/63462.html): Conjunto de normas internacionales sobre arquitectura, diseño, implementación y aseguramiento de redes corporativas.

### Papers y Literatura de Frontera
* **IEEE Communications Surveys & Tutorials (2021):** *Zero Trust Architecture: A Comprehensive Survey and Future Directions* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9485088)) — Revisión exhaustiva sobre protocolos, mecanismos de decisión contextual y desafíos de despliegue en redes híbridas.
* **ACM Digital Threats: Research and Practice (2022):** *Microsegmentation in Industrial Networks: Evaluating Latency and Resilience under Attack* ([DOI: 10.1145/3510582](https://dl.acm.org/journal/dtrap)) — Análisis experimental del impacto operativo de firewalls basados en host sobre controladores industriales.

### Repositorios y Herramientas (Open Source)
* [Cilium (eBPF-based Networking & Security)](https://github.com/cilium/cilium): Plataforma de código abierto para observabilidad, conectividad y aplicación de políticas de seguridad Zero Trust en contenedores y Linux mediante tecnología eBPF.
* [Tailscale / WireGuard](https://github.com/tailscale/tailscale): Red en malla segura de código abierto basada en el protocolo WireGuard que implementa acceso de confianza cero sin requerir complejas VPNs centralizadas.
* [Open Policy Agent (OPA)](https://github.com/open-policy-agent/opa): Motor de políticas de propósito general de código abierto que permite unificar y desacoplar el control de autorización en APIs, redes y microservicios.
* [SPIFFE / SPIRE](https://github.com/spiffe/spire): Estándares y herramientas de la Cloud Native Computing Foundation (CNCF) para emitir identidades criptográficas mutuas y efímeras entre cargas de trabajo heterogéneas.

### Ruta de Aprendizaje Autónoma
* [Microsoft Learn: SC-100 - Arquitecto de Ciberseguridad: Diseño de Estrategias Zero Trust](https://learn.microsoft.com/es-es/training/paths/sc-100-design-zero-trust-strategy/): Especialización técnica oficial para planificar e implementar arquitecturas de confianza cero empresariales.
* [AWS Skill Builder: Implementing Zero Trust on AWS Cloud](https://explore.skillbuilder.aws): Capacitación técnica sobre autenticación contextual, políticas de red privadas y cifrado en tránsito continuo.
* [Cisco NetAcad: Network Security Architecture & Defense](https://www.netacad.com): Formación profesional sobre configuración de cortafuegos de próxima generación (NGFW), VPNs IPSec y políticas de acceso 802.1X.
* [TryHackMe: Network Security & Traffic Analysis](https://tryhackme.com/module/network-security): Laboratorios interactivos para diseñar reglas de firewall iptables, inspeccionar tráfico cifrado TLS y segmentar subredes virtuales.

---

## 🧪 Anexo Práctico: Estrategia Operativa y Laboratorio Open Source

### Estrategia Operativa Empresarial
Para implementar microsegmentación Zero Trust a nivel de kernel sin degradar la latencia de servicios críticos, se deben desplegar políticas basadas en eBPF con Cilium, asegurando que solo pods y servicios explícitamente autorizados puedan comunicarse a través de mTLS y Layer 7.

### Código / Laboratorio Ejecutable
```python
# cilium_zero_trust_policy.yaml
# Manifiesto de microsegmentación eBPF para aislar sistemas SCADA y BDs críticas
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "scada-isolation-zerotrust"
  namespace: "critical-infrastructure"
spec:
  endpointSelector:
    matchLabels:
      app: "scada-core-service"
  ingress:
  - fromEndpoints:
    - matchLabels:
        role: "authorized-operator-hmi"
    toPorts:
    - ports:
      - port: "502"
        protocol: TCP
      rules:
        http: []
  egress:
  - toEndpoints:
    - matchLabels:
        app: "telemetry-timescale-db"
    toPorts:
    - ports:
      - port: "5432"
        protocol: TCP
```

---

## Recursos Multimedia Oficiales

* [📺 Ver Ponencia en Video Oficial (Día 1 · Minuto 9:20:00)](https://www.youtube.com/watch?v=PEqWRTb1idE&t=9h20m00s)
* [▶️ Escuchar Podcast Resumen](../../assets/audio/dia1_09_evirtus_redes.mp3)

---

[⬅️ Lección Anterior](08-bonnaire-agentes-ia.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](../03-dia2-seminario/01-caceres-blue-team-ia.md)
