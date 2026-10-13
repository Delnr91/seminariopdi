# César Cordero · El Rol de la Tecnología en la Continuidad y Resiliencia Operacional
**Institución:** Lenovo | **Nivel:** Intermedio

### 🎧 Audio-Clase (1 Minuto)
<audio controls src="../../assets/audio/dia2_03_cordero.mp3">
  Tu dispositivo no soporta audio nativo. <a href="../../assets/audio/dia2_03_cordero.mp3">Descargar MP3</a>
</audio>

---

### 💡 La Idea en Palabras Simples
> Imagina que compras una caja fuerte blindada para guardar tus ahorros. Puedes ponerle la cerradura digital más sofisticada del mundo en la puerta, pero si quien fabricó la caja le instaló una tapa trasera de cartón o un chip espía escondido en las bisagras desde la fábrica, ningún código secreto podrá evitar que te roben.

César Cordero destaca la trascendencia de la seguridad a nivel de hardware, microcódigo y cadena de suministro físico. Con frecuencia, las estrategias defensivas se concentran en el software operativo (antivirus, cortafuegos), descuidando la capa más profunda: la BIOS y el firmware de los computadores y servidores. Si un atacante compromete esta capa inicial de arranque, adquiere control absoluto del equipo de manera persistente e invisible al sistema operativo.

La sesión aborda cómo los fabricantes líderes integran tecnologías como raíces de confianza de hardware (Root of Trust), chips de seguridad criptográfica TPM y plataformas de auto-recuperación de firmware que restauran el equipo a un estado limpio si detectan manipulación. Asimismo, se exploran soluciones para garantizar la continuidad del negocio, permitiendo restaurar entornos de trabajo completos en la nube en cuestión de minutos ante desastres físicos o ciberataques.

---

### 🛠️ Lo que Debes Aprender
* Seguridad por debajo del sistema operativo: Blindar la BIOS y el firmware contra amenazas persistentes avanzadas (bootkits/rootkits).
* Raíz de confianza en hardware (Hardware Root of Trust): Validación criptográfica del arranque seguro desde el encendido inicial del procesador.
* Cadenas de suministro íntegras y trazables: Certificar que los componentes no hayan sido alterados o interceptados durante la fabricación y despacho.

---

### 📋 Lista de Chequeo Preventiva
- [ ] Activar Secure Boot y verificación criptográfica de BIOS/firmware en todos los servidores y terminales de trabajo.
- [ ] Implementar dispositivos con módulos TPM 2.0 y capacidades de auto-recuperación de firmware ante ataques de bajo nivel.
- [ ] Validar con los proveedores de hardware las certificaciones de seguridad física y trazabilidad en la cadena de suministro.

---

### ❓ Autoevaluación Rápida
**¿Por qué un ataque al firmware o BIOS de un computador es mucho más peligroso que una infección típica de software en el sistema operativo?**
<details>
<summary>▶️ Toca aquí para ver la respuesta</summary>

Porque reside por debajo del sistema operativo y los antivirus, logrando sobrevivir al formateo o cambio del disco duro y manteniendo el control oculto y persistente de la máquina en cada reinicio.
</details>

---

### 📚 Enlaces y Video
* 📺 [Canal Oficial YouTube PDI Chile](https://www.youtube.com/@PDIChile)
* 📄 [Sitio PDI Ciberseguridad](https://www.pdichile.cl/seminariociberseguridad); [Lenovo ThinkShield Security](https://www.lenovo.com)
