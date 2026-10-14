# El Lado Práctico del Crimen con IA - Manu Fernández

## Síntesis Ejecutiva

La mercantilización de herramientas generativas avanzadas ha democratizado tácticas de ingeniería social de grado militar para organizaciones delictivas de alcance global. A través de la síntesis neuronal de voz (Voice Cloning) y la generación de avatares sintéticos dinámicos en tiempo real, los ciberdelincuentes están ejecutando con éxito ataques de compromiso de correo corporativo (BEC 3.0) y fraudes de autorización financiera, sorteando los filtros de verificación auditiva y visual tradicionales aplicados por el personal operativo.

Simultáneamente, la fiabilidad de las credenciales biométricas convencionales (reconocimiento facial y huella dactilar) se encuentra en entredicho frente a vectores de ataque de presentación (PAD) construidos con modelos de difusión y máscaras tridimensionales. Neutralizar estas amenazas requiere evolucionar los esquemas de autenticación hacia arquitecturas de confianza cero contextuales, exigiendo desafíos de prueba de vida dinámicos (liveness verification), canales independientes de autorización fuera de banda y una reingeniería profunda de los procesos de autorización corporativa.

---

## Conceptos Core

* **Presentation Attack Detection (PAD):** Conjunto de algoritmos y sensores fisiológicos diseñados para discriminar entre una muestra biométrica humana viva y una suplantación sintética o pregrabada.
* **Business Email Compromise 3.0 (AI-BEC):** Evolución del fraude corporativo donde se integran llamadas y videoconferencias sintéticas hiperrealistas para ordenar transferencias monetarias urgentes.
* **Voice Biometrics Spoofing:** Técnicas adversariales basadas en síntesis de audio texto-a-voz (TTS) condicionadas a muestras acústicas de pocos segundos para burlar IVRs bancarios.
* **Out-of-Band Multi-Factor Authentication (OOB-MFA):** Mecanismo de validación criptográfica que utiliza canales físicos y de red completamente desacoplados para confirmar instrucciones críticas.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [ISO/IEC 30107 (Biometric Presentation Attack Detection Framework)](https://www.iso.org/standard/67381.html): Estándar internacional que regula la evaluación, métricas y pruebas de resistencia frente a ataques de suplantación biométrica.
* [NIST SP 800-63-3: Digital Identity Guidelines](https://pages.nist.gov/800-63-3/): Directrices técnicas del NIST sobre niveles de aseguramiento de identidad (IAL), autenticación (AAL) y federación (FAL).
* [FIDO Alliance Biometric Certification Requirements](https://fidoalliance.org/certification/biometric-component-certification/): Criterios de certificación independiente para garantizar que los sensores y algoritmos biométricos resistan falsificaciones de alta complejidad.
* [MITRE ATT&CK: Technique T1566.002 (Spearphishing Link) & T1656 (Impersonation)](https://attack.mitre.org/techniques/T1656/): Mapeo formal de técnicas de suplantación de identidad e ingeniería social dirigida.

### Papers y Literatura de Frontera
* **IEEE Transactions on Biometrics, Behavior, and Identity Science (2022):** *Deepfake Detection in Biometrics: A Comprehensive Review and Future Directions* ([IEEE Xplore](https://ieeexplore.ieee.org/document/9672074)) — Evaluación de modelos de aprendizaje profundo para identificar anomalías espectrales y micropatrones en rostros sintéticos.
* **arXiv / Computer Vision Foundation (2023):** *Real-Time Deepfake Detection via Physiological Dynamics* ([arXiv:2303.04838](https://arxiv.org/abs/2303.04838)) — Propuesta metodológica para validar la pulsación sanguínea dérmica (fotopletismografía remota) en videollamadas.

### Repositorios y Herramientas (Open Source)
* [FaceForensics++ Toolkit](https://github.com/ondyari/FaceForensics): Benchmark y biblioteca forense de referencia desarrollada por la Universidad Técnica de Múnich para detección de manipulaciones faciales.
* [DeepFaceLab](https://github.com/iperov/DeepFaceLab): Framework de código abierto líder en pipeline de generación neural facial, utilizado por investigadores para diseñar defensas y pruebas de penetración biométrica.
* [OpenFace 2.0](https://github.com/TadasBaltrusaitis/OpenFace): Herramienta de análisis facial open source capaz de capturar microexpresiones y puntos de referencia de mirada para detectar patrones sintéticos anómalos.
* [Canarytokens (Thinkst Canary)](https://github.com/thinkst/canarytokens): Generador de señuelos digitales y trampas de credenciales para alertar tempranamente accesos no autorizados en canales corporativos.

### Ruta de Aprendizaje Autónoma
* [Microsoft Learn: Implementación de Soluciones Biométricas con Azure AI Face](https://learn.microsoft.com/es-es/training/modules/detect-analyze-faces/): Módulo técnico sobre integración de verificación facial, detección de máscaras y prueba de vida.
* [AWS Skill Builder: Architecting Identity and Access Management](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-identity-and-access-management-iam-foundations): Formación sobre políticas de mínimo privilegio, autenticación multifactor contextual y control de accesos federados.
* [TryHackMe: Phishing & Social Engineering Analysis](https://tryhackme.com/module/phishing): Laboratorios interactivos para analizar cabeceras de correo, desarmar señuelos de ingeniería social y desplegar contramedidas en gateways.
* [SANS Cyber Defense Community Curriculum](https://www.sans.org): Recursos abiertos sobre mitigación de fraudes ejecutivos y procedimientos de control interno ante incidentes financieros.

---

## 🧪 Anexo Práctico: Estrategia Operativa y Laboratorio Open Source

### Estrategia Operativa Empresarial
Para blindar las transacciones financieras y órdenes operativas contra suplantaciones mediante voz clonada y deepfakes en videollamadas, se debe implementar una política de 'Desafío Fuera de Banda' (OOB) respaldada por un sistema de palabras clave secretas preacordadas y algoritmos de prueba de vida dinámica.

### Código / Laboratorio Ejecutable
```python
# verificador_liveness_biometrico.py
# Script de análisis de micro-variaciones y parpadeo para detección de avatares sintéticos
import cv2
import numpy as np

def detectar_liveness_stream(simulated_frame_count=30):
    print("[*] Iniciando verificación dinámica de prueba de vida (Liveness Challenge)")
    # En un entorno real se procesa el stream de video de la cámara
    ear_values = []
    for i in range(simulated_frame_count):
        # Simulación de cálculo de Eye Aspect Ratio (EAR)
        simulated_ear = 0.30 if (i < 10 or i > 15) else 0.12  # Cierre de ojos (parpadeo)
        ear_values.append(simulated_ear)
        
    blinks = sum(1 for j in range(1, len(ear_values)) if ear_values[j-1] > 0.25 and ear_values[j] <= 0.15)
    
    if blinks >= 1:
        print(f"[+] Desafío de prueba de vida SUPERADO ({blinks} parpadeos naturales detectados).")
        return True
    else:
        print("[-] ALERTA DE SEGURIDAD: Comportamiento estático o sintético. Posible deepfake.")
        return False

if __name__ == "__main__":
    detectar_liveness_stream()
```

---

## Recursos Multimedia Oficiales

* [📺 Ver Ponencia en Video Oficial (Día 1 · Minuto 2:35:20)](https://www.youtube.com/watch?v=PEqWRTb1idE&t=2h35m20s)
* [▶️ Escuchar Podcast Resumen](../../assets/audio/dia1_03_fernandez_manu.mp3)

---

[⬅️ Lección Anterior](02-lama-infraestructura-dns.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](04-bordachar-anci-regulacion.md)
