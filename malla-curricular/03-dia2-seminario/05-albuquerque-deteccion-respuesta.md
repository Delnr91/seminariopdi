# Tales Albuquerque · Seguridad Digital: Prevención, Detección y Respuesta ante Ciberamenazas
**Institución:** Sophos | **Nivel:** Intermedio

### 🎧 Audio-Clase (1 Minuto)
<audio controls src="../../assets/audio/dia2_05_albuquerque.mp3">
  Tu dispositivo no soporta audio nativo. <a href="../../assets/audio/dia2_05_albuquerque.mp3">Descargar MP3</a>
</audio>

---

### 💡 La Idea en Palabras Simples
> Es como un intruso sigiloso que no rompe la ventana con estrépito para robar la televisión, sino que encuentra una copia de la llave que dejaste olvidada bajo el felpudo. Entra silenciosamente de noche, se esconde en el ático durante dos meses estudiando tus horarios y costumbres, y cuando finalmente se decide a actuar, vacía la casa entera en diez minutos.

Tales Albuquerque desmitifica la idea de que los ataques cibernéticos y el ransomware ocurren en un parpadeo. En incidentes contra infraestructuras críticas y grandes empresas, los adversarios suelen permanecer un promedio de semanas o meses infiltrados en la red interna (dwell time). Durante este período exploran directorios, roban credenciales con privilegios y neutralizan los respaldos de seguridad antes de detonar el cifrado masivo.

La ponencia promueve la adopción de servicios gestionados de detección y respuesta (MDR), donde cazadores de amenazas humanos monitorean la telemetría las 24 horas del día. Albuquerque resalta el peligro de las técnicas Living off the Land (LotL), donde los intrusos utilizan las propias herramientas legítimas del sistema operativo (como PowerShell o WMI) para moverse sin levantar sospechas en los antivirus convencionales.

---

### 🛠️ Lo que Debes Aprender
* Tiempo de permanencia silenciosa (Dwell Time): Los atacantes estudian la víctima durante semanas antes de cifrar los datos; la detección temprana es crucial.
* Técnicas Living off the Land: Uso malicioso de herramientas administrativas nativas para eludir antivirus basados en firmas estáticas.
* Cacería activa de amenazas (Threat Hunting 24/7): No basta con alarmas pasivas; se requiere personal experto investigando anomalías de forma continua.

---

### 📋 Lista de Chequeo Preventiva
- [ ] Activar autenticación multifactor (MFA) obligatoria en todas las conexiones remotas (VPN, RDP) y cuentas de administración.
- [ ] Implementar monitoreo de comportamiento continuo con agentes EDR/XDR con capacidad de bloqueo y respuesta inmediata.
- [ ] Auditar y restringir el uso de consolas de comandos y herramientas administrativas del sistema solo a administradores autorizados.

---

### ❓ Autoevaluación Rápida
**¿En qué consiste la técnica de ataque conocida como 'Living off the Land' (LotL)?**
<details>
<summary>▶️ Toca aquí para ver la respuesta</summary>

Consiste en que los atacantes utilizan utilitarios y programas legítimos ya instalados en el sistema operativo (como PowerShell o utilidades de red) para ejecutar sus acciones, evitando descargar herramientas sospechosas que alertarían a los antivirus.
</details>

---

### 📚 Enlaces y Video
* 📺 [Canal Oficial YouTube PDI Chile](https://www.youtube.com/@PDIChile)
* 📄 [Sitio PDI Ciberseguridad](https://www.pdichile.cl/seminariociberseguridad); [Sophos MDR & Threat Research](https://www.sophos.com)

---

[⬅ Lección Anterior](04-alli-salud-ciberseguridad.md) | [🏠 Volver a la Malla Curricular](../../README.md) | [Siguiente Lección ➡](06-norman-amenazas-hibridas.md)
