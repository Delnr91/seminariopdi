# Marco NIST CSF 2.0 y Guías de Ciberresiliencia CISA/NCSC - Marco CISA / NIST & NCSC

## Síntesis Ejecutiva

El modelo de ciberresiliencia desarrollado por la comunidad anglosajona, liderado por el Instituto Nacional de Estándares y Tecnología (NIST) de EE.UU. junto a CISA y el Centro Nacional de Ciberseguridad (NCSC) del Reino Unido, constituye el referente normativo y metodológico más extendido en el mundo corporativo internacional. La publicación del marco NIST Cybersecurity Framework 2.0 (CSF 2.0) introduce una evolución estratégica fundamental al incorporar la función de 'Gobernar' (Govern) de forma transversal a las tradicionales 'Identificar', 'Proteger', 'Detectar', 'Responder' y 'Recuperar', posicionando la gestión del riesgo cibernético como una responsabilidad indivisible de la junta directiva y la alta dirección empresarial.

El paradigma anglosajón se distingue por articular mandatos legales de reporte acelerado con una cultura de colaboración pública y privada altamente coordinada. Instrumentos como los Objetivos de Rendimiento en Ciberseguridad Intersectoriales (CPGs) de CISA y los mandatos de la ley CIRCIA (reporte de incidentes en 72 horas) establecen una línea base de seguridad obligatoria para sectores críticos. A su vez, el Cyber Assessment Framework (CAF) del Reino Unido proporciona una métrica de madurez pragmática para auditar sistemas industriales, complementada con programas de Ciberdefensa Activa (ACD) para neutralizar amenazas a escala nacional.

---

## Conceptos Core

* **NIST CSF 2.0 Core Functions:** Estructura que organiza el ciclo de gestión del riesgo cibernético en seis pilares: Govern (Gobernar), Identify (Identificar), Protect (Proteger), Detect (Detectar), Respond (Responder) y Recover (Recuperar).
* **CISA Cross-Sector Cybersecurity Performance Goals (CPGs):** Conjunto priorizado de prácticas defensivas de alto impacto diseñadas para reducir drásticamente el riesgo de intrusiones en infraestructuras críticas.
* **NCSC Cyber Assessment Framework (CAF 3.2):** Marco sistemático del gobierno británico para evaluar cómo las organizaciones esenciales gestionan la seguridad de la información y la resiliencia operativa.
* **CIRCIA 72h / 24h Mandatory Reporting:** Régimen legal estadounidense que exige a operadores críticos reportar ciberataques significativos ante CISA en menos de 72 horas y pagos de ransomware en 24 horas.

---

## 🧠 Ecosistema de Recursos Globales (Deep Dive)

### Estándares y Frameworks
* [NIST Cybersecurity Framework 2.0 (CSF 2.0)](https://www.nist.gov/cyberframework): Versión actualizada del marco de ciberseguridad más adoptado del mundo, aplicable a todo tipo de organizaciones y cadenas de suministro.
* [CISA Cross-Sector Cybersecurity Performance Goals (CPGs)](https://www.cisa.gov/cpgs): Guía técnica de controles esenciales de ciberseguridad para operadores de agua, energía, transporte y salud.
* [NCSC Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf): Guía metodológica del Reino Unido para la auditoría técnica y regulatoria bajo las normas NIS.
* [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final): Documento que define la arquitectura y componentes del modelo de Confianza Cero en infraestructuras federales y corporativas.

### Papers y Literatura de Frontera
* **NIST Special Publication 800-53 Rev. 5:** *Security and Privacy Controls for Information Systems and Organizations* ([NIST CSRC](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)) — El catálogo de controles técnicos más exhaustivo del mundo para proteger sistemas contra amenazas avanzadas.
* **UK Cabinet Office (2022):** *National Cyber Strategy 2022: Pioneering a Cyber Resilient Future* ([Gov.uk](https://www.gov.uk/government/publications/national-cyber-strategy-2022)) — Estrategia de estado británica sobre ciberdefensa activa, soberanía tecnológica y resiliencia de servicios públicos esenciales.

### Repositorios y Herramientas (Open Source)
* [CISA CSET (Cyber Security Evaluation Tool)](https://github.com/cisagov/cset): Herramienta oficial de CISA para autoevaluar la postura de ciberseguridad de redes industriales y corporativas frente a múltiples normas (NIST, IEC 62443).
* [NIST CSF 2.0 Reference Tool](https://csrc.nist.gov/Projects/cybersecurity-framework/filters): Explorador interactivo oficial de categorías, subcategorías y ejemplos de implementación del nuevo marco NIST.
* [Lynis (Security Auditing Tool for Unix/Linux)](https://github.com/CISOfy/lynis): Herramienta de auditoría de seguridad open source para comprobar configuraciones del sistema frente a directrices de endurecimiento (hardening).
* [OpenSCAP Platform](https://github.com/OpenSCAP/openscap): Ecosistema de código abierto para automatizar la evaluación de cumplimiento normativo y parches en sistemas operativos empresariales.

### Ruta de Aprendizaje Autónoma
* [NIST CSF 2.0 Online Learning Modules](https://www.nist.gov/cyberframework/online-learning): Recursos oficiales y guías de inicio rápido para implementar la nueva función Govern y mapear controles corporativos.
* [CISA Federal Virtual Training Environment (FedVTE)](https://www.cisa.gov/cyber-training): Plataforma de capacitación gubernamental con cientos de horas de formación en ciberdefensa y análisis de vulnerabilidades.
* [NCSC UK: Certified Cyber Professional (CCP) Knowledge Areas](https://www.ncsc.gov.uk): Guías formativas sobre arquitectura de resiliencia y gestión de incidentes industriales.
* [Coursera / Infosec: NIST Cybersecurity Framework Implementation](https://www.coursera.org): Especialización profesional en planificación e implementación práctica del marco NIST en organizaciones.

---

## 🧪 Anexo Práctico: Estrategia Operativa y Laboratorio Open Source

### Estrategia Operativa Empresarial
Para operacionalizar el marco NIST CSF 2.0 en infraestructura crítica, las entidades deben evaluar automáticamente sus sistemas frente a las seis funciones maestras (GV, ID, PR, DE, RS, RC) utilizando herramientas como CSET y scripts de telemetría de cumplimiento.

### Código / Laboratorio Ejecutable
```python
# evaluador_madurez_nist_csf2.py
# Script de diagnóstico para medir la implementación de las 6 funciones del NIST CSF 2.0
def auditar_madurez_nist(respuestas: dict) -> dict:
    pesos = {"GV": 0.20, "ID": 0.15, "PR": 0.20, "DE": 0.15, "RS": 0.15, "RC": 0.15}
    puntajes = {}
    total = 0.0
    for funcion, peso in pesos.items():
        score = respuestas.get(funcion, 0) # Calificación de 0 a 100
        puntajes[funcion] = score
        total += score * peso
    return {"puntajes_funcion": puntajes, "indice_madurez_global": round(total, 2)}

if __name__ == "__main__":
    datos_evaluacion = {"GV": 85, "ID": 90, "PR": 75, "DE": 70, "RS": 80, "RC": 65}
    resultado = auditar_madurez_nist(datos_evaluacion)
    print(f"[+] Índice de Madurez NIST CSF 2.0: {resultado['indice_madurez_global']}%")
```

---

## Recursos Multimedia Oficiales

* [📺 Ver Masterclass Oficial: NIST Cybersecurity Framework 2.0 Overview](https://www.youtube.com/watch?v=0kH8R5-yUCo)
* [▶️ Escuchar Podcast Resumen](../../assets/audio/intl_01_eeuu_uk.mp3)

---

[⬅️ Lección Anterior](../03-dia2-seminario/07-abbas-academia-talento.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡️](02-china-cii-cac.md)
