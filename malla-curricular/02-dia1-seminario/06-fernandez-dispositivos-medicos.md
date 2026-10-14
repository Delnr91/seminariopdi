# Anatomía de un Dispositivo Médico Conectado: Explorando sus Superficies de Ataque - Víctor Fernández

## Síntesis Ejecutiva

El despliegue masivo del Internet de las Cosas Médicas (IoMT) en redes hospitalarias contemporáneas ha expandido drásticamente la superficie de ataque ciberfísica en el sector salud. Equipos de soporte vital como bombas de infusión continua, monitores de constantes hemodinámicas y desfibriladores implantables incorporan interfaces inalámbricas (WiFi, BLE) y pilas de red embebidas que fueron concebidas para maximizar la interoperabilidad clínica, postergando con frecuencia los mecanismos básicos de autenticación criptográfica y validación de entrada.

Un compromiso de seguridad en este vector trasciende la filtración de datos clínicos personales: constituye una amenaza directa e inminente para la vida del paciente. Atacantes con presencia en la red local o que explotan vulnerabilidades en firmwares desactualizados pueden alterar remotamente la velocidad de dosificación de fármacos vasoactivos o inducir lecturas diagnósticas falsas en salas de terapia intensiva. Blindar estos entornos exige una estricta microsegmentación de redes clínicas mediante VLANs médicas dedicadas, auditorías continuas de interfaces de hardware (JTAG/UART) y un compromiso formal de los fabricantes con el principio de seguridad por diseño.

---

## Conceptos Core

* **IoMT (Internet of Medical Things):** Ecosistema de dispositivos médicos conectados en red que recopilan, transmiten y actúan sobre datos clínicos en tiempo real.
* **Hardware Attack Surface (JTAG/UART):** Interfaces físicas de depuración en placas de circuitos que, de quedar expuestas o sin bloqueo criptográfico, permiten la extracción directa de firmware y claves privadas.
* **Clinical Network Microsegmentation:** Aislamiento lógico estricto del tráfico de dispositivos médicos respecto de las redes administrativas del hospital y el tráfico de internet de visitas.
* **Coordinated Vulnerability Disclosure (CVD):** Protocolo ético y seguro entre investigadores de seguridad, fabricantes de instrumental médico y agencias reguladoras sanitarias para parchar fallas sin poner en riesgo a los pacientes.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [FDA: Cybersecurity in Medical Devices - Quality System System Regulations](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity): Guía regulatoria obligatoria de la FDA de EE.UU. que exige documentación de ciberseguridad y SBOM para dispositivos médicos conectados.
* [IEC 81001-5-1: Health Software and Health IT Systems Cybersecurity](https://www.iso.org/standard/76503.html): Estándar internacional sobre actividades del ciclo de vida de desarrollo seguro para software e infraestructura médica.
* [NIST SP 800-53: Healthcare Overlay for Information Security Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final): Catálogo de controles de seguridad federales adaptados específicamente a la preservación de la vida en entornos clínicos.
* [MDCG 2019-16: Guidance on Cybersecurity for Medical Devices (Unión Europea)](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en): Marco europeo de cumplimiento para el marcado CE de equipamiento médico digital.

### Papers y Literatura de Frontera
* **Journal of Medical Systems (2021):** *Vulnerability Assessment and Attack Surface Mapping in Connected Infusion Pumps* ([DOI: 10.1007/s10916-021-01789-5](https://link.springer.com/journal/10916)) — Estudio forense experimental sobre explotación de memoria y control remoto en sistemas de dispensación hospitalaria.
* **IEEE Internet of Things Journal (2023):** *Cyber-Physical Security in Connected Healthcare: Threat Modeling, Vulnerabilities, and Countermeasures* ([IEEE Xplore](https://ieeexplore.ieee.org/document/10041235)) — Mapeo integral de vectores de intrusión contra dispositivos IoMT y protocolos propietarios inalámbricos.

### Repositorios y Herramientas (Open Source)
* [Scapy (Packet Manipulation Tool)](https://github.com/secdev/scapy): Potente biblioteca en Python para forjar, decodificar y analizar paquetes de red en protocolos médicos propietarios y diagnósticos HL7/DICOM.
* [Frida (Dynamic Instrumentation Toolkit)](https://github.com/frida/frida): Herramienta de inyección de código para auditoría en caliente de aplicaciones de control médico y depuración de ejecutables embebidos.
* [Ghidra (NSA Reverse Engineering Suite)](https://github.com/NationalSecurityAgency/ghidra): Framework de ingeniería inversa para desensamblar y decompilar imágenes de firmware de dispositivos médicos extraídas por puertos físicos.
* [Wireshark (con Dissectores Médicos HL7/DICOM)](https://github.com/wireshark/wireshark): Analizador de protocolos de red para inspeccionar comunicaciones biomédicas no cifradas y detectar anomalías en tiempo real.

### Ruta de Aprendizaje Autónoma
* [CISA Healthcare and Public Health (HPH) Sector Training](https://www.cisa.gov/topics/critical-infrastructure-sectors/healthcare-and-public-health): Rutas de concientización y aseguramiento de infraestructura clínica para profesionales de IT y biomédica.
* [Biohacking Village DEF CON Open Resources](https://www.villageb.io/): Charlas magistrales, talleres y laboratorios prácticos sobre ingeniería inversa de marcapasos, bombas y resonadores magnéticos.
* [HackTheBox: Hardware & IoT Hacking Tracks](https://www.hackthebox.com): Laboratorios técnicos sobre volcado de memoria Flash, emulación de arquitecturas ARM/MIPS y explotación de puertos UART.
* [TryHackMe: Wireshark Traffic Analysis](https://tryhackme.com/module/network-security): Módulo práctico para adquirir maestría en inspección de paquetes, filtros de captura y detección de balizas maliciosas.

---

## 🧪 Anexo Práctico: Estrategia Operativa y Laboratorio Open Source

### Estrategia Operativa Empresarial
Para proteger dispositivos IoMT en entornos hospitalarios sin interrumpir el cuidado clínico, se debe desplegar un analizador pasivo de tráfico en el switch de la red clínica que alerte inmediatamente sobre comandos de reconfiguración o paquetes broadcast no autorizados dirigidos a bombas de infusión.

### Código / Laboratorio Ejecutable
```python
# sniffer_iomt_anomalias.py
# Monitor pasivo con Scapy para detectar comandos no autorizados hacia dispositivos médicos
from scapy.all import sniff, TCP, IP

IOMT_IP_RANGE = ["192.168.50."]
PUERTOS_CRITICOS = [80, 443, 502, 23, 22] # Puertos de gestión en bombas de infusión

def analizar_paquete_medico(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_dst = packet[IP].dst
        port_dst = packet[TCP].dport
        
        # Verificar si el destino es un equipo IoMT
        if any(ip_dst.startswith(prefix) for prefix in IOMT_IP_RANGE):
            if port_dst in PUERTOS_CRITICOS:
                print(f"[!] ALERTA CLÍNICA: Intento de conexión sospechoso hacia IoMT {ip_dst}:{port_dst} desde {packet[IP].src}")

if __name__ == "__main__":
    print("[*] Iniciando sensor pasivo de tráfico clínico IoMT...")
    # sniff(filter="tcp", prn=analizar_paquete_medico, store=0)
```

---

## Recursos Multimedia Oficiales

* [📺 Ver Ponencia en Video Oficial (Día 1 · Minuto 6:30:20)](https://www.youtube.com/watch?v=PEqWRTb1idE&t=6h30m20s)
* [▶️ Escuchar Podcast Resumen](../../assets/audio/dia1_06_fernandez_victor.mp3)

---

[⬅️ Lección Anterior](05-evirtus-efecto-domino.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](07-panel-sectores-criticos.md)
