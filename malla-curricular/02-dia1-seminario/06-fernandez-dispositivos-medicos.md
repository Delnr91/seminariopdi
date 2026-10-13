# Víctor Fernández · Anatomía de un dispositivo médico conectado: explorando sus superficies de ataque
**Institución:** Biohacking Village (DEF CON) | **Nivel:** Avanzado

### 🎧 Audio-Clase (1 Minuto)
<audio controls src="../../assets/audio/dia1_06_fernandez_victor.mp3">
  Tu dispositivo no soporta audio nativo. <a href="../../assets/audio/dia1_06_fernandez_victor.mp3">Descargar MP3</a>
</audio>

---

### 💡 La Idea en Palabras Simples
> Imagina un marcapasos o un suero en el brazo de un paciente que tiene una pequeña antena de radio para que la enfermera ajuste la dosis desde su escritorio. Si esa antena no tiene llave y está conectada a la misma red pública de internet que usan las visitas de la sala de espera para ver videos, cualquier intruso con un teléfono podría cambiar la medicina sin levantarse de su silla.

Víctor Fernández desmenuza la arquitectura de hardware y software del Internet de las Cosas Médicas (IoMT). Equipos como bombas de infusión de insulina, monitores fetales y respiradores artificiales fueron diseñados históricamente para operar en ambientes hospitalarios aislados, pero hoy incorporan módulos WiFi y Bluetooth que exponen puertos de depuración física (JTAG, UART) y firmwares vulnerables sin cifrar.

El expositor demuestra cómo un atacante con acceso a la red hospitalaria puede explotar vulnerabilidades de memoria en estos dispositivos para alterar parámetros de dosificación farmacológica o generar alarmas falsas, poniendo en riesgo directo la vida del paciente. Se concluye que la ciberseguridad biomédica requiere segmentación de red estricta mediante VLANs médicas dedicadas y auditorías de seguridad desde la fase de diseño industrial.

---

### 🛠️ Lo que Debes Aprender
* Riesgo ciberfísico en salud: En IoMT, una falla de seguridad informática se traduce inmediatamente en un daño físico o desenlace fatal para el paciente.
* Superficies de ataque de hardware: Puertos de mantenimiento físico, contraseñas de fábrica predeterminadas y firmwares obsoletos sin firmar criptográficamente.
* Microsegmentación clínica: Los dispositivos médicos conectados deben residir en redes aisladas sin acceso a la internet pública ni a computadores administrativos.

---

### 📋 Lista de Chequeo Preventiva
- [ ] Aislar todos los dispositivos biomédicos en una red VLAN clínica dedicada, con bloqueo estricto de tráfico hacia internet.
- [ ] Modificar todas las contraseñas predeterminadas de fábrica en bombas de infusión, monitores y equipamiento hospitalario.
- [ ] Deshabilitar interfaces inalámbricas (Bluetooth/WiFi) y puertos de diagnóstico físico que no se utilicen activamente en la atención del paciente.

---

### ❓ Autoevaluación Rápida
**¿Cuál es el peligro de mantener dispositivos médicos conectados en la misma red de computadores de administración hospitalaria?**
<details>
<summary>▶️ Toca aquí para ver la respuesta</summary>

Que un malware o ransomware que infecte una computadora administrativa por un correo engañoso puede propagarse lateralmente hacia las bombas de infusión o monitores de signos vitales, alterando su funcionamiento y amenazando la vida de los pacientes.
</details>

---

### 📚 Enlaces y Video
* 📺 [Video Oficial YouTube Día 1](https://www.youtube.com/watch?v=PEqWRTb1idE)
* 📄 [Sitio PDI Ciberseguridad](https://www.pdichile.cl/seminariociberseguridad); [Biohacking Village DEF CON](https://www.villageb.io/)
