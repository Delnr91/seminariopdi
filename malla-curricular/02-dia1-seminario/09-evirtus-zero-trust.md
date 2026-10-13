# Especialista en Redes · Seguridad en la Red: Hacia una infraestructura crítica resiliente
**Institución:** E-Virtus | **Nivel:** Intermedio

### 🎧 Audio-Clase (1 Minuto)
<audio controls src="../../assets/audio/dia1_09_evirtus_redes.mp3">
  Tu dispositivo no soporta audio nativo. <a href="../../assets/audio/dia1_09_evirtus_redes.mp3">Descargar MP3</a>
</audio>

---

### 💡 La Idea en Palabras Simples
> Es como diseñar un gran barco transatlántico dividido en compartimentos estancos herméticos. En los barcos antiguos, si un iceberg rompía una esquina del casco, el agua entraba y llenaba todo el barco hasta hundirlo. En un barco moderno con compartimentos cerrados, el agua inunda únicamente una pequeña habitación aislada, mientras el resto del barco sigue navegando con total seguridad.

El especialista de E-Virtus aborda el diseño arquitectónico de redes bajo la premisa de Confianza Cero (Zero Trust). Durante décadas, las empresas construyeron su seguridad bajo el modelo perimetral tradicional de castillo y foso: quien lograba conectarse a la red interna era considerado de confianza total. Hoy, con el trabajo remoto y la infiltración de credenciales, asumir que la red interna es segura es un error fatal.

La solución radica en la microsegmentación de red, donde cada servidor, estación de trabajo y dispositivo industrial vive en su propia celda aislada con políticas de acceso mínimo estricto. Toda comunicación entre máquinas debe autenticarse, autorizarse y cifrarse continuamente. Así, si un virus o intruso infecta una computadora en el área comercial, le resulta imposible saltar hacia las redes de control de las bombas de agua o generadores eléctricos.

---

### 🛠️ Lo que Debes Aprender
* Fin del perímetro tradicional: Todo el tráfico, tanto externo como interno, debe considerarse hostil hasta que se demuestre lo contrario.
* Microsegmentación granular: Dividir la red en zonas lógicas independientes frena el movimiento lateral de ciberdelincuentes y ransomware.
* Principio de privilegio mínimo (Least Privilege): Cada usuario y aplicación solo tiene acceso a los puertos y recursos indispensables para su función específica.

---

### 📋 Lista de Chequeo Preventiva
- [ ] Implementar autenticación y autorización continua basada en identidad para cada sesión de usuario y comunicación entre servidores.
- [ ] Segmentar la red interna en zonas independientes mediante cortafuegos de próxima generación (NGFW) y políticas de microsegmentación.
- [ ] Bloquear por defecto todo tráfico este-oeste (entre computadores de la misma red) que no esté explícitamente autorizado en una lista blanca.

---

### ❓ Autoevaluación Rápida
**¿Cuál es la diferencia fundamental entre el modelo perimetral tradicional y el modelo Zero Trust?**
<details>
<summary>▶️ Toca aquí para ver la respuesta</summary>

El modelo tradicional confía ciegamente en todo lo que está dentro de la red corporativa tras cruzar el firewall perimetral; en cambio, Zero Trust asume que la red interna ya está comprometida y exige verificar de manera estricta y continua la identidad de cada usuario y dispositivo en cada petición.
</details>

---

### 📚 Enlaces y Video
* 📺 [Video Oficial YouTube Día 1](https://www.youtube.com/watch?v=PEqWRTb1idE)
* 📄 [Sitio PDI Ciberseguridad](https://www.pdichile.cl/seminariociberseguridad); [E-Virtus Arquitecturas Resilientes](https://e-virtus.com)
