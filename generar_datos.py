import json
import os

datos = {
    "total_lecciones": 19,
    "lecciones": [
        {
            "id": "dia1_01_wong",
            "carpeta": "02-dia1-seminario",
            "archivo": "01-wong-ia-cibercrimen.md",
            "speaker": "Subprefecto Marcelo Wong Cea",
            "institucion": "Jefatura Nacional de Cibercrimen, PDI Chile",
            "titulo": "Adversarios digitales IA y el nuevo escenario de amenazas a la infraestructura crítica",
            "dificultad": "Principiante",
            "analogia": "Imagina que un ladrón común antes tenía que probar las cerraduras de una casa una por una caminando por la calle. Ahora, ese delincuente tiene un dron invisible equipado con rayos X que recorre toda la ciudad en tres segundos, detectando qué ventana tiene el pestillo suelto y además imitando la voz de tu hermano para pedirte que le abras la puerta principal.",
            "explicacion": "El Subprefecto Marcelo Wong expone cómo la delincuencia digital ha dado un salto evolutivo al adoptar herramientas de Inteligencia Artificial generativa y automatización masiva. Los atacantes ya no necesitan semanas de planeación manual; hoy despliegan algoritmos capaces de escanear redes enteras de empresas de electricidad, agua y finanzas en busca de vulnerabilidades en tiempo récord, generando correos trampa con lenguaje natural impecable.\n\nAnte esta amenaza simétrica, la PDI recalca que la respuesta policial y corporativa no puede ser artesanal. Proteger la infraestructura crítica exige elevar las capacidades de ciberinvestigación científica con analítica avanzada, cooperación multisectorial y una cultura ciudadana de verificación rigurosa, desconfiando de comunicaciones que parezcan legítimas pero utilicen canales atípicos.",
            "puntos_clave": [
                "Automatización ofensiva: Los ciberdelincuentes utilizan IA para ejecutar reconocimiento masivo y ataques dirigidos con mínima inversión de tiempo.",
                "Ingeniería social hiperrealista: La síntesis de voz y los modelos de lenguaje eliminan las faltas ortográficas típicas del phishing tradicional, volviendo creíbles las suplantaciones.",
                "Investigación científica y predictiva: La ciberdefensa requiere telemetría continua y modelos analíticos de la policía para anticipar patrones delictivos."
            ],
            "checklist": [
                "- [ ] Implementar un protocolo de verificación fuera de banda (por otra vía) para cualquier orden ejecutiva o financiera recibida por correo o mensajería.",
                "- [ ] Configurar filtros de correo electrónico con detección heurística e inspección de autenticación SPF, DKIM y DMARC.",
                "- [ ] Realizar pruebas periódicas de simulación de ingeniería social asistida por IA para todo el personal operativo de infraestructura crítica."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué la Inteligencia Artificial hace que los ataques de phishing sean mucho más peligrosos que antes?",
                "respuesta": "Porque permite a los delincuentes redactar mensajes perfectamente contextualizados y libres de errores gramaticales a escala masiva, e incluso clonar voces y rostros (deepfakes), haciendo casi imposible distinguir el fraude a simple vista sin una verificación secundaria."
            },
            "guion_audio": "¡Hola! Bienvenidos a esta cápsula de ciberseguridad. Hoy abordamos la ponencia del Subprefecto Marcelo Wong de la PDI, sobre cómo los ciberdelincuentes usan la Inteligencia Artificial. Imagina a un adversario que no duerme, capaz de probar miles de cerraduras digitales en un segundo y copiar la voz de tu jefe para que le entregues las llaves de los sistemas eléctricos o de agua potable. Frente a esto, la intuición ya no basta. La regla de oro es simple: nunca confirmes una orden urgente o inusual solo porque el mensaje se ve formal o creíble. Establece siempre una llamada de confirmación por una línea segura. La tecnología avanza rápido, pero el criterio humano y la verificación rigurosa siguen siendo nuestro escudo principal.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "Jefatura Nacional de Cibercrimen PDI", "url": "https://www.pdichile.cl"}
            ]
        },
        {
            "id": "dia1_02_lama",
            "carpeta": "02-dia1-seminario",
            "archivo": "02-lama-infraestructura-dns.md",
            "speaker": "Guillermo Lama",
            "institucion": "NIC Chile (Universidad de Chile)",
            "titulo": "Infraestructura de Internet: Seguridad, Continuidad y Resiliencia",
            "dificultad": "Principiante",
            "analogia": "Imagina la guía telefónica y el mapa central de una gran metrópolis. Cada vez que tomas un autobús o buscas una dirección, consultas ese mapa. Si alguien borrara o cambiara las señales en todas las esquinas al mismo tiempo, los vehículos chocarían o se detendrían, las ambulancias no llegarían a los hospitales y nadie encontraría su casa. Eso es el DNS para Internet.",
            "explicacion": "Guillermo Lama explica la función vital del Sistema de Nombres de Dominio (DNS), especialmente para el dominio nacional .cl administrado por NIC Chile. El DNS traduce nombres legibles para los humanos (como el de tu banco o centro de salud) en números de coordenadas que las computadoras entienden (direcciones IP). Sin este servicio en funcionamiento continuo, la red queda virtualmente inaccesible para los ciudadanos.\n\nLa charla detalla cómo se blinda esta columna vertebral mediante arquitecturas Anycast, servidores distribuidos geográficamente en varios continentes y protocolos de seguridad criptográfica como DNSSEC. Gracias a esta redundancia masiva, aunque un centro de datos sufra un ataque masivo de denegación de servicio (DDoS), las consultas de los usuarios son absorbidas por réplicas operativas, garantizando la continuidad de Chile en la red global.",
            "puntos_clave": [
                "El DNS como servicio esencial: Es el cimiento sobre el cual opera toda la economía digital, la banca, la salud y las telecomunicaciones nacionales.",
                "Arquitectura Anycast y redundancia: Distribuir copias operativas de los servidores raíz y de nivel superior en múltiples regiones mitiga ataques de saturación masiva.",
                "Validación criptográfica con DNSSEC: Impide que atacantes intermedios falsifiquen respuestas de resolución y desvíen a usuarios a sitios web fraudulentos."
            ],
            "checklist": [
                "- [ ] Activar DNSSEC en todos los nombres de dominio institucionales para certificar la autenticidad de las respuestas DNS.",
                "- [ ] Configurar servidores DNS redundantes alojados en redes y ubicaciones geográficas físicamente independientes.",
                "- [ ] Monitorear en tiempo real los tiempos de resolución y picos anómalos de tráfico hacia los servidores autoritativos de la entidad."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál es el principal beneficio de desplegar una arquitectura Anycast en los servidores DNS?",
                "respuesta": "Permite que múltiples servidores en distintas partes del mundo compartan la misma dirección IP, de modo que el tráfico se reparte automáticamente al nodo más cercano y un ataque masivo de denegación de servicio queda disperso y neutralizado sin botar el servicio global."
            },
            "guion_audio": "¿Te has preguntado cómo llega tu computador a la página web correcta en milésimas de segundo? En esta sesión revisamos la infraestructura de internet con Guillermo Lama de NIC Chile. El sistema DNS es como el mapa de navegación de nuestro país en internet: traduce cada nombre de dominio punto cl a la dirección exacta del servidor correspondiente. Si este servicio falla, los bancos, hospitales y servicios de emergencia quedan desconectados. Para evitarlo, se utiliza redundancia Anycast, lo que significa colocar copias de estos mapas en servidores de todo el mundo. Si uno es atacado o falla, los demás responden de inmediato. La lección para toda organización es clara: jamás dependas de un único punto de falla en tus sistemas críticos.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "NIC Chile - Centro de Información de Redes", "url": "https://www.nic.cl"}
            ]
        },
        {
            "id": "dia1_03_fernandez_manu",
            "carpeta": "02-dia1-seminario",
            "archivo": "03-fernandez-crimen-ia.md",
            "speaker": "Manu Fernández",
            "institucion": "TRM - IAFIS",
            "titulo": "El lado práctico del crimen con IA",
            "dificultad": "Intermedio",
            "analogia": "Es como un imitador profesional con una máscara de silicona hiperrealista que entra a una sucursal bancaria imitando a la perfección los gestos, la voz y la firma del dueño de la cuenta para retirar los fondos de emergencia, mientras por teléfono llama a los empleados con la voz idéntica de la junta directiva diciendo que liberen el dinero inmediatamente.",
            "explicacion": "Manu Fernández aterriza las amenazas de la Inteligencia Artificial a la práctica cotidiana del cibercrimen financiero y corporativo. Demuestra cómo delincuentes con herramientas de bajo costo clonan timbres vocales a partir de videos públicos de ejecutivos y crean avatares hiperrealistas capaces de participar en videollamadas para autorizar transferencias millonarias hacia cuentas en el extranjero.\n\nAdemás, la presentación expone la debilidad de los métodos biométricos convencionales cuando no cuentan con algoritmos de detección de vida (liveness detection). Ante este panorama, se exige a las organizaciones redefinir sus procesos de validación de identidad, incorporando autenticaciones contextuales, palabras clave fuera de canal y una cultura de tolerancia cero a la precipitación ante órdenes urgentes.",
            "puntos_clave": [
                "Suplantación de voz y video en tiempo real: Los deepfakes ya no son solo teóricos; se usan en estafas del CEO y fraudes corporativos en vivo.",
                "Evasión de biometría sin prueba de vida: Fotografías 3D o máscaras generadas por IA pueden burlar cámaras si los algoritmos no exigen desafíos dinámicos reales.",
                "Quiebre de la urgencia psicológica: Los atacantes combinan la perfección técnica del engaño con un ambiente de extrema presión para evitar que la víctima verifique."
            ],
            "checklist": [
                "- [ ] Implementar un canal secundario obligatorio y telefónico directo para autorizar transferencias monetarias o cambios de cuentas bancarias.",
                "- [ ] Actualizar los sistemas de autenticación facial y dactilar con módulos de detección activa de prueba de vida (liveness detection).",
                "- [ ] Definir palabras de paso o códigos secretos verbales entre directivos clave para validar instrucciones confidenciales en caso de duda."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Qué es una prueba de vida (liveness detection) y por qué es indispensable ante el uso de IA?",
                "respuesta": "Es una tecnología que verifica si la persona frente a la cámara es un ser humano real presente en ese instante (mediante parpadeo, movimiento o patrones de luz), impidiendo que videos pregrabados o deepfakes sintéticos engañen al sistema de biometría."
            },
            "guion_audio": "¿Creerías si tu gerente general te pide una transferencia urgente por videollamada? En esta lección, Manu Fernández de TRM IAFIS nos muestra el lado más peligroso del fraude digital actual: el cibercrimen con Inteligencia Artificial. Con unos pocos segundos de audio extraído de redes sociales, los estafadores clonan voces reales y crean videos falsos tan convincentes que burlan a cualquiera. Para proteger a nuestras instituciones, la regla de oro es nunca permitir que la prisa anule los protocolos. Implementa palabras de paso secretas y valida siempre cualquier movimiento financiero a través de una segunda vía de comunicación independiente. Si una orden huele a apuro extraordinario, detente, respira y verifica. En ciberseguridad, dudar a tiempo salva millones.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "TRM - IAFIS Biometrics", "url": "https://www.iafis.com"}
            ]
        },
        {
            "id": "dia1_04_bordachar",
            "carpeta": "02-dia1-seminario",
            "archivo": "04-bordachar-anci-regulacion.md",
            "speaker": "Michelle Bordachar",
            "institucion": "Agencia Nacional de Ciberseguridad (ANCI)",
            "titulo": "Ciberseguridad y Resiliencia: Un Desafío Nacional",
            "dificultad": "Principiante",
            "analogia": "Es similar a la creación del código de construcción y la inspección oficial de edificios tras un gran terremoto: ya no se deja al criterio de cada constructor si coloca o no vigas antisísmicas; la ley establece normas obligatorias, exige simulacros periódicos y castiga severamente a quien ponga en riesgo la vida de los vecinos por ahorrar en cemento.",
            "explicacion": "Michelle Bordachar detalla el hito institucional de Chile con la promulgación de la Ley Marco de Ciberseguridad y la puesta en marcha de la Agencia Nacional de Ciberseguridad (ANCI). Este marco legal transforma la ciberseguridad de ser una recomendación técnica optativa a convertirse en una obligación de Estado con fuerza de ley para entidades públicas y privadas.\n\nLa exposición se centra en la figura de los Operadores de Importancia Vital (OIV), aquellos cuya interrupción afectaría gravemente servicios esenciales como salud, energía, transporte y telecomunicaciones. Estos actores están legalmente obligados a implementar estándares de gestión de riesgos, realizar auditorías y reportar incidentes graves en plazos perentorios de pocas horas, bajo apercibimiento de cuantiosas multas.",
            "puntos_clave": [
                "Creación de la ANCI: Una autoridad rectora con facultades de fiscalización, sanción y coordinación técnica para la protección nacional.",
                "Operadores de Importancia Vital (OIV): Designación formal de entidades estratégicas obligadas a mantener estándares estrictos de ciberseguridad y continuidad.",
                "Obligatoriedad de notificación de incidentes: El reporte rápido a la autoridad permite emitir alertas tempranas y proteger al resto del ecosistema chileno."
            ],
            "checklist": [
                "- [ ] Determinar si la organización clasifica como Operador de Importancia Vital (OIV) bajo los criterios de la Ley Marco chilena.",
                "- [ ] Establecer un protocolo interno con plazos definidos para reportar incidentes de ciberseguridad a la ANCI en menos de tres horas.",
                "- [ ] Asignar formalmente la responsabilidad legal y de gobernanza de ciberseguridad a nivel del Directorio y la Gerencia General."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál es el cambio de paradigma principal que introduce la Ley Marco de Ciberseguridad y la ANCI en Chile?",
                "respuesta": "Eleva la ciberseguridad de un problema puramente informático a un asunto de gobernanza corporativa y seguridad nacional obligatoria, con deberes de reporte legal e importantes sanciones económicas para directivos y empresas estratégicas."
            },
            "guion_audio": "Chile cuenta con un nuevo escudo legal. En esta lección repasamos la presentación de Michelle Bordachar sobre la Agencia Nacional de Ciberseguridad, la ANCI, y la Ley Marco de Ciberseguridad. Proteger los sistemas informáticos ya no es un favor ni una opción técnica: es una exigencia legal para todas las empresas de servicios esenciales, conocidas como Operadores de Importancia Vital. Si una planta de agua, una distribuidora eléctrica o un hospital sufre un ciberataque, la ley exige reportarlo de inmediato para alertar y blindar al resto del país. La ciberseguridad se sienta ahora en la mesa del directorio. Cumplir con las normativas y mitigar riesgos es hoy un deber ciudadano y corporativo fundamental para la resiliencia de nuestra nación.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "Agencia Nacional de Ciberseguridad de Chile (ANCI)", "url": "https://www.gob.cl"}
            ]
        },
        {
            "id": "dia1_05_evirtus_incidentes",
            "carpeta": "02-dia1-seminario",
            "archivo": "05-evirtus-efecto-domino.md",
            "speaker": "Representante Técnico Sectorial",
            "institucion": "E-Virtus",
            "titulo": "Un Incidente, Múltiples Impactos: La Criticidad de la Ciberseguridad",
            "dificultad": "Intermedio",
            "analogia": "Piensa en una hilera de fichas de dominó dispuestas en espiral. La primera ficha es un pequeño taller que suministra tornillos; la última es el aeropuerto internacional de la capital. Si un niño empuja la ficha del taller, la caída se propaga ficha por ficha hasta apagar la torre de control del aeropuerto, a pesar de que el aeropuerto nunca conoció directamente al pequeño taller de tornillos.",
            "explicacion": "El especialista de E-Virtus ilustra el fenómeno del efecto dominó y la vulnerabilidad en la cadena de suministro industrial. En la economía digital actual, las grandes corporaciones de infraestructura crítica están blindadas internamente, por lo que los atacantes seleccionan como blanco a pequeños proveedores externos de software, climatización o soporte técnico que poseen accesos directos a la red corporativa.\n\nA través de incidentes sectoriales reales, se evidencia cómo la paralización de un único sistema logístico de transporte de combustible puede detener ambulancias, dejar sin energía térmica a hospitales y paralizar la distribución de alimentos frescos. La lección primordial es que la superficie de ataque de una entidad no termina en sus propias oficinas, sino que abarca a todos los socios tecnológicos conectados a su ecosistema.",
            "puntos_clave": [
                "Ataques a la cadena de suministro (Supply Chain Attacks): El eslabón más débil de tus proveedores es la puerta de entrada a tu red principal.",
                "Interdependencia de infraestructuras: La caída de telecomunicaciones o logística impacta inmediatamente en energía, salud y transporte público.",
                "Auditoría de accesos de terceros: Se requiere revocar privilegios permanentes y aplicar el principio de mínimo privilegio a contratistas externos."
            ],
            "checklist": [
                "- [ ] Levantar un inventario exhaustivo de todos los proveedores y contratistas con conexiones de red remotas o cuentas activas.",
                "- [ ] Exigir contractualmente cláusulas de ciberseguridad mínima y derecho a auditoría técnica a todos los proveedores externos.",
                "- [ ] Aislar y restringir los accesos de soporte técnico mediante redes dedicadas y autenticación multifactor temporal (Just-In-Time)."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué los atacantes prefieren vulnerar a un pequeño proveedor externo en lugar de atacar directamente a la gran empresa de infraestructura crítica?",
                "respuesta": "Porque los proveedores medianos suelen tener menos presupuesto y controles de ciberdefensa más débiles, pero conservan conexiones VPN o credenciales de confianza que permiten al atacante saltar directamente al corazón de la empresa principal."
            },
            "guion_audio": "Todo está conectado, y esa es nuestra mayor fortaleza pero también nuestro mayor riesgo. En esta sesión de E-Virtus exploramos el efecto dominó de los ciberataques. Cuando pensamos en defender una gran empresa eléctrica o bancaria, solemos vigilar su fachada principal. Sin embargo, los atacantes modernos buscan la puerta trasera: vulneran al pequeño proveedor de mantenimiento, limpieza o software de facturación para colarse a los servidores centrales. Un simple incidente en una empresa de transporte puede dejar sin combustible a los generadores de un hospital. Tu nivel de seguridad real es el de tu proveedor más vulnerable. Por eso, auditar a terceros, restringir accesos temporales y vigilar la cadena de suministro es imprescindible para evitar que una pequeña chispa incendie todo el bosque.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "E-Virtus Ciberseguridad Industrial", "url": "https://e-virtus.com"}
            ]
        },
        {
            "id": "dia1_06_fernandez_victor",
            "carpeta": "02-dia1-seminario",
            "archivo": "06-fernandez-dispositivos-medicos.md",
            "speaker": "Víctor Fernández",
            "institucion": "Biohacking Village (DEF CON)",
            "titulo": "Anatomía de un dispositivo médico conectado: explorando sus superficies de ataque",
            "dificultad": "Avanzado",
            "analogia": "Imagina un marcapasos o un suero en el brazo de un paciente que tiene una pequeña antena de radio para que la enfermera ajuste la dosis desde su escritorio. Si esa antena no tiene llave y está conectada a la misma red pública de internet que usan las visitas de la sala de espera para ver videos, cualquier intruso con un teléfono podría cambiar la medicina sin levantarse de su silla.",
            "explicacion": "Víctor Fernández desmenuza la arquitectura de hardware y software del Internet de las Cosas Médicas (IoMT). Equipos como bombas de infusión de insulina, monitores fetales y respiradores artificiales fueron diseñados históricamente para operar en ambientes hospitalarios aislados, pero hoy incorporan módulos WiFi y Bluetooth que exponen puertos de depuración física (JTAG, UART) y firmwares vulnerables sin cifrar.\n\nEl expositor demuestra cómo un atacante con acceso a la red hospitalaria puede explotar vulnerabilidades de memoria en estos dispositivos para alterar parámetros de dosificación farmacológica o generar alarmas falsas, poniendo en riesgo directo la vida del paciente. Se concluye que la ciberseguridad biomédica requiere segmentación de red estricta mediante VLANs médicas dedicadas y auditorías de seguridad desde la fase de diseño industrial.",
            "puntos_clave": [
                "Riesgo ciberfísico en salud: En IoMT, una falla de seguridad informática se traduce inmediatamente en un daño físico o desenlace fatal para el paciente.",
                "Superficies de ataque de hardware: Puertos de mantenimiento físico, contraseñas de fábrica predeterminadas y firmwares obsoletos sin firmar criptográficamente.",
                "Microsegmentación clínica: Los dispositivos médicos conectados deben residir en redes aisladas sin acceso a la internet pública ni a computadores administrativos."
            ],
            "checklist": [
                "- [ ] Aislar todos los dispositivos biomédicos en una red VLAN clínica dedicada, con bloqueo estricto de tráfico hacia internet.",
                "- [ ] Modificar todas las contraseñas predeterminadas de fábrica en bombas de infusión, monitores y equipamiento hospitalario.",
                "- [ ] Deshabilitar interfaces inalámbricas (Bluetooth/WiFi) y puertos de diagnóstico físico que no se utilicen activamente en la atención del paciente."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál es el peligro de mantener dispositivos médicos conectados en la misma red de computadores de administración hospitalaria?",
                "respuesta": "Que un malware o ransomware que infecte una computadora administrativa por un correo engañoso puede propagarse lateralmente hacia las bombas de infusión o monitores de signos vitales, alterando su funcionamiento y amenazando la vida de los pacientes."
            },
            "guion_audio": "Cuando la ciberseguridad falla en un banco, se pierde dinero; pero cuando falla en un hospital, se pierden vidas humanas. Víctor Fernández de Biohacking Village nos lleva al quirófano para analizar los dispositivos médicos conectados. Hoy, bombas de infusión de medicamentos, respiradores y monitores cardíacos se comunican por redes inalámbricas. Muchos de estos equipos fueron fabricados sin defensas digitales sólidas y conservan contraseñas de fábrica que cualquiera podría vulnerar. Imagina el impacto de alterar remotamente la dosis de morfina de un paciente. Para frenar esta pesadilla, los hospitales deben aislar estos aparatos en redes privadas exclusivas y exigir a los fabricantes estándares de ciberseguridad estrictos. Defender la tecnología médica es, literalmente, salvar vidas.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "Biohacking Village DEF CON", "url": "https://www.village.bio"}
            ]
        },
        {
            "id": "dia1_07_panel_multisectorial",
            "carpeta": "02-dia1-seminario",
            "archivo": "07-panel-sectores-criticos.md",
            "speaker": "Panel Multisectorial (Soledad Bastías, Patricio Leyton, Juan Huechucura, Cristián Bravo)",
            "institucion": "Codelco, Coordinador Eléctrico Nacional, Aguas Andinas, CSIRT de Gobierno",
            "titulo": "Protegiendo lo Esencial: Ciberseguridad y Resiliencia en Sectores Críticos",
            "dificultad": "Intermedio",
            "analogia": "Imagina una junta de vecinos donde conviven la compañía de agua, la central de bomberos, la cuadrilla eléctrica y la comisaría. Si una banda de asaltantes comienza a merodear por las casas de la izquierda, la única forma de que no saqueen el barrio entero es que el primer vecino que los vea toque la alarma comunitaria al instante, en lugar de quedarse callado por vergüenza.",
            "explicacion": "En este panel de alto nivel, los líderes de ciberseguridad de Codelco, el Coordinador Eléctrico Nacional, Aguas Andinas y el CSIRT Gubernamental analizan los desafíos reales de proteger las Tecnologías Operativas (OT) e industriales de Chile. A diferencia de las oficinas corporativas, las válvulas de agua, subestaciones eléctricas y fundiciones mineras utilizan controladores industriales (PLC) que operan las 24 horas y no admiten reinicios ni parches de seguridad intempestivos.\n\nLos panelistas enfatizan que los atacantes son oportunistas y no discriminan entre sectores públicos o privados. La clave de la ciberresiliencia nacional radica en la colaboración interinstitucional y el intercambio oportuno de indicadores de compromiso (IoCs). El secreto o el recelo ante un incidente digital solo beneficia al adversario, mientras que la transparencia técnica fortalece la defensa de todo el país.",
            "puntos_clave": [
                "Brecha entre TI y TO: Los sistemas industriales priorizan disponibilidad y seguridad física; no se pueden parchar de la misma forma que un computador de oficina.",
                "Cooperación público-privada: El intercambio rápido de alertas e incidentes a través del CSIRT frena ataques coordinados antes de que escalen.",
                "Planes de contingencia manual: Toda infraestructura crítica debe mantener la capacidad operativa de maniobra analógica y manual en caso de apagón cibernético total."
            ],
            "checklist": [
                "- [ ] Establecer un canal formal y seguro de compartición de amenazas con el CSIRT Nacional y empresas pares del sector.",
                "- [ ] Realizar simulacros semestrales de operación en modo manual o degradado ante una eventual caída total de los sistemas digitales.",
                "- [ ] Separar rigurosamente las redes corporativas (IT) de las redes de control y automatización industrial (OT) bajo el modelo Purdue."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué en los sistemas industriales (OT) no se pueden aplicar parches de seguridad de forma automática e inmediata como en las computadoras personales?",
                "respuesta": "Porque detener un controlador industrial para reiniciarlo puede apagar turbinas eléctricas, cortar el suministro de agua o detener hornos mineros, provocando daños materiales multimillonarios y cortes de servicios básicos a miles de personas."
            },
            "guion_audio": "¿Qué tienen en común una mina de cobre, una represa de agua y una subestación eléctrica? Todas dependen de computadoras industriales que hacen girar motores, abrir válvulas y alimentar a nuestras ciudades. En este panel de expertos con Codelco, el Coordinador Eléctrico Nacional, Aguas Andinas y el CSIRT, aprendimos que los ciberdelincuentes buscan paralizar los servicios que hacen funcionar a Chile. En el mundo industrial, los sistemas no se pueden reiniciar de un momento a otro. Por eso, el arma defensiva más poderosa no es un software mágico, sino la colaboración: si Aguas Andinas detecta una amenaza, debe avisar al instante al sector eléctrico y al gobierno. Compartir información a tiempo es lo que mantiene la luz encendida y el agua corriendo.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "CSIRT de Gobierno de Chile", "url": "https://www.csirt.gob.cl"},
                {"nombre": "Coordinador Eléctrico Nacional", "url": "https://www.coordinador.cl"}
            ]
        },
        {
            "id": "dia1_08_bonnaire",
            "carpeta": "02-dia1-seminario",
            "archivo": "08-bonnaire-agentes-ia.md",
            "speaker": "Dr. Xavier Bonnaire",
            "institucion": "Departamento de Informática, Universidad Técnica Federico Santa María (USM)",
            "titulo": "Agentes IA e infraestructura crítica: entre la falla operativa y el arma de ciberguerra",
            "dificultad": "Avanzado",
            "analogia": "Es como instalar un piloto automático supersónico en un autobús escolar repleto de niños, pero sin volante, sin freno de emergencia manual y sin que el chofer humano tenga permiso para pisar el pedal si el sistema confunde una sombra en el pavimento con un abismo y decide doblar bruscamente hacia el río.",
            "explicacion": "El Dr. Xavier Bonnaire profundiza en los riesgos inherentes de delegar decisiones autónomas a agentes de Inteligencia Artificial en entornos de infraestructura crítica. La integración de modelos de lenguaje y agentes autónomos para regular flujos de energía o balance de químicos introduce el peligro de alucinaciones probabilísticas, ataques de inyección de prompts y envenenamiento de datos que pueden provocar fallas operativas catastróficas.\n\nLa entrevista distingue con agudeza entre la falla fortuita por error de diseño del modelo y el ataque deliberado de ciberguerra patrocinado por estados hostiles. El académico concluye que la IA debe concebirse exclusivamente como un asistente de apoyo a la decisión para los operadores humanos, y nunca como un decisor terminal no supervisado (human-in-the-loop), preservando mecanismos de anulación manual irrenunciables.",
            "puntos_clave": [
                "Principio de Human-in-the-Loop: Las decisiones de impacto físico o vital en infraestructuras críticas deben requerir siempre la validación de un operador humano competente.",
                "Vulnerabilidades de modelos autónomos: Inyección indirecta de instrucciones, envenenamiento de conjuntos de datos de entrenamiento y comportamientos no deterministas.",
                "Ciberguerra versus falla técnica: La ambigüedad en el comportamiento de la IA dificulta determinar si un fallo fue un accidente algorítmico o un sabotaje digital dirigido."
            ],
            "checklist": [
                "- [ ] Garantizar un interruptor de parada de emergencia físico e independiente (kill-switch) que desconecte el agente de IA de los actuadores de planta.",
                "- [ ] Auditar las fuentes de datos y canales de entrada de los modelos de IA para impedir inyecciones de comandos maliciosos o datos envenenados.",
                "- [ ] Mantener entrenamiento continuo para los operadores humanos en resolución de fallas manuales sin dependencia de herramientas de IA."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Qué significa el concepto de 'Human-in-the-Loop' en la automatización con IA para infraestructuras críticas?",
                "respuesta": "Significa que un ser humano calificado debe estar integrado obligatoriamente en el ciclo de toma de decisiones para revisar, autorizar y eventualmente cancelar cualquier acción crítica propuesta por el algoritmo de IA antes de que se ejecute en la planta real."
            },
            "guion_audio": "¿Dejarías que un programa de computador decida por sí solo si abre una compuerta hidráulica o apaga un reactor químico? El Dr. Xavier Bonnaire de la Universidad Santa María nos plantea un dilema crucial: el uso de agentes de Inteligencia Artificial en infraestructura crítica. La IA es una herramienta maravillosa para detectar patrones y optimizar recursos, pero también puede cometer errores imprevistos, alucinar o ser engañada por atacantes externos. Si le entregamos el control absoluto sin supervisión humana, un simple error de cálculo puede transformarse en una catástrofe de ciberguerra. La regla indiscutible es mantener siempre al operador humano al mando. La tecnología debe aconsejar y asistir, pero el juicio, la ética y el botón de freno siempre deben pertenecer a las personas.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "Departamento de Informática USM", "url": "https://inf.utfsm.cl"}
            ]
        },
        {
            "id": "dia1_09_evirtus_redes",
            "carpeta": "02-dia1-seminario",
            "archivo": "09-evirtus-zero-trust.md",
            "speaker": "Especialista en Redes",
            "institucion": "E-Virtus",
            "titulo": "Seguridad en la Red: Hacia una infraestructura crítica resiliente",
            "dificultad": "Intermedio",
            "analogia": "Es como diseñar un gran barco transatlántico dividido en compartimentos estancos herméticos. En los barcos antiguos, si un iceberg rompía una esquina del casco, el agua entraba y llenaba todo el barco hasta hundirlo. En un barco moderno con compartimentos cerrados, el agua inunda únicamente una pequeña habitación aislada, mientras el resto del barco sigue navegando con total seguridad.",
            "explicacion": "El especialista de E-Virtus aborda el diseño arquitectónico de redes bajo la premisa de Confianza Cero (Zero Trust). Durante décadas, las empresas construyeron su seguridad bajo el modelo perimetral tradicional de castillo y foso: quien lograba conectarse a la red interna era considerado de confianza total. Hoy, con el trabajo remoto y la infiltración de credenciales, asumir que la red interna es segura es un error fatal.\n\nLa solución radica en la microsegmentación de red, donde cada servidor, estación de trabajo y dispositivo industrial vive en su propia celda aislada con políticas de acceso mínimo estricto. Toda comunicación entre máquinas debe autenticarse, autorizarse y cifrarse continuamente. Así, si un virus o intruso infecta una computadora en el área comercial, le resulta imposible saltar hacia las redes de control de las bombas de agua o generadores eléctricos.",
            "puntos_clave": [
                "Fin del perímetro tradicional: Todo el tráfico, tanto externo como interno, debe considerarse hostil hasta que se demuestre lo contrario.",
                "Microsegmentación granular: Dividir la red en zonas lógicas independientes frena el movimiento lateral de ciberdelincuentes y ransomware.",
                "Principio de privilegio mínimo (Least Privilege): Cada usuario y aplicación solo tiene acceso a los puertos y recursos indispensables para su función específica."
            ],
            "checklist": [
                "- [ ] Implementar autenticación y autorización continua basada en identidad para cada sesión de usuario y comunicación entre servidores.",
                "- [ ] Segmentar la red interna en zonas independientes mediante cortafuegos de próxima generación (NGFW) y políticas de microsegmentación.",
                "- [ ] Bloquear por defecto todo tráfico este-oeste (entre computadores de la misma red) que no esté explícitamente autorizado en una lista blanca."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál es la diferencia fundamental entre el modelo perimetral tradicional y el modelo Zero Trust?",
                "respuesta": "El modelo tradicional confía ciegamente en todo lo que está dentro de la red corporativa tras cruzar el firewall perimetral; en cambio, Zero Trust asume que la red interna ya está comprometida y exige verificar de manera estricta y continua la identidad de cada usuario y dispositivo en cada petición."
            },
            "guion_audio": "Antiguamente, los castillos se defendían con una muralla alta y un foso de agua; pero si un invasor lograba cruzar la puerta con un disfraz, tenía vía libre para saquear todas las habitaciones. En esta lección, el especialista de E-Virtus nos enseña el modelo Zero Trust o Confianza Cero. En el mundo digital moderno, nunca debemos asumir que alguien es de confianza solo porque está conectado a la red de la oficina. Diseñar redes resilientes significa dividir nuestros sistemas en compartimentos herméticos, como en los submarinos. Si un virus infecta el computador de recepción, las barreras internas impiden que avance hacia las salas de control eléctrico o servidores bancarios. Verifica siempre, nunca confíes a ciegas y aísla tus activos críticos.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Video Oficial YouTube Día 1", "url": "https://www.youtube.com/watch?v=PEqWRTb1idE"},
                {"nombre": "E-Virtus Arquitecturas Resilientes", "url": "https://e-virtus.com"}
            ]
        },
        {
            "id": "dia2_01_caceres",
            "carpeta": "03-dia2-seminario",
            "archivo": "01-caceres-blue-team-ia.md",
            "speaker": "Diego Cáceres",
            "institucion": "Investigador y especialista en ciberdefensa (Ganador Call for Papers)",
            "titulo": "Blue team aumentado por inteligencia artificial: modelos de ciberdefensa y resiliencia para infraestructuras críticas",
            "dificultad": "Intermedio",
            "analogia": "Imagina a un guardia de seguridad humano que tiene que revisar 500 pantallas de cámaras de vigilancia a la vez durante el turno de noche. Rápidamente se cansará y pestañeará. Ahora dale un asistente de inteligencia artificial que monitorea los 500 monitores sin parpadear jamás, detecta de inmediato si una sombra extraña cruza un pasillo en penumbra y le avisa al guardia en milisegundos indicándole exactamente en qué puerta colocar el cerrojo.",
            "explicacion": "Diego Cáceres, ganador del Call for Papers del seminario, presenta cómo potenciar al Blue Team (el equipo defensor de ciberseguridad) utilizando modelos de aprendizaje automático y agentes autónomos defensivos. Los centros de operaciones de seguridad (SOC) reciben diariamente millones de eventos y registros de actividad (logs), provocando fatiga de alertas y demoras críticas en la detección de intrusiones complejas.\n\nEl expositor demuestra cómo los modelos de IA aumentada pueden correlacionar telemetría de red, detectar anomalías sutiles en el tráfico y orquestar respuestas automatizadas (SOAR) para aislar equipos comprometidos en segundos. Esto transforma la labor defensiva de una postura reactiva y saturada a una estrategia proactiva, reduciendo drásticamente el tiempo medio de detección (MTTD) y contención (MTTR) frente a ataques contra infraestructuras críticas.",
            "puntos_clave": [
                "Reducción de fatiga de alertas: La IA filtra el ruido y prioriza incidentes reales para que los analistas humanos se enfoquen en amenazas graves.",
                "Detección de comportamiento anómalo: Los modelos de aprendizaje no supervisado identifican movimientos inusuales de datos que escapan a las firmas tradicionales.",
                "Orquestación y respuesta automatizada (SOAR): Aislamiento inmediato de hosts comprometidos y revocación de credenciales antes de que el ataque se expanda."
            ],
            "checklist": [
                "- [ ] Implementar herramientas de correlación de eventos con capacidades de aprendizaje automático (SIEM/XDR con IA).",
                "- [ ] Diseñar libros de jugadas automatizados (playbooks) para contener y aislar equipos infectados en menos de un minuto.",
                "- [ ] Entrenar a los analistas del SOC en la interpretación y auditoría de decisiones sugeridas por herramientas automatizadas."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cómo ayuda la IA a resolver el problema de la fatiga de alertas en un Centro de Operaciones de Seguridad (SOC)?",
                "respuesta": "Analizando y correlacionando automáticamente millones de registros por segundo para descartar falsos positivos y destacar únicamente aquellos patrones sospechosos que representan un riesgo real para la infraestructura."
            },
            "guion_audio": "En ciberdefensa, cada segundo cuenta. Imagina recibir diez mil alertas de seguridad por hora en tu pantalla; ningún equipo humano puede procesar semejante avalancha sin cometer errores. En esta sesión, Diego Cáceres nos demuestra cómo la Inteligencia Artificial puede convertirse en el mejor aliado del Blue Team, nuestro equipo de guardianes digitales. Los modelos inteligentes pueden analizar millones de conexiones en tiempo real, filtrar el ruido irrelevante y detectar cuando un intruso intenta moverse en silencio por la red. Al empoderar a nuestros especialistas con asistentes de IA, logramos contener infecciones en segundos en lugar de semanas. La velocidad es la clave absoluta entre un susto pasajero y un apagón nacional. Defensores humanos con herramientas inteligentes marcan la diferencia.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "Investigación Call for Papers USM", "url": "https://usm.cl"}
            ]
        },
        {
            "id": "dia2_02_fuentes",
            "carpeta": "03-dia2-seminario",
            "archivo": "02-fuentes-threat-intelligence.md",
            "speaker": "Omar Fuentes",
            "institucion": "SEK",
            "titulo": "Cyber Threat Intelligence (CTI)",
            "dificultad": "Intermedio",
            "analogia": "Es como tener un servicio de inteligencia meteorológica y radares militares antes de una expedición marítima: en lugar de esperar en cubierta a que una tormenta azote el barco o a que piratas aborden en plena noche, tus vigías interceptan los mapas y planes de los asaltantes días antes, sabiendo con qué armas vienen y por cuál bahía intentarán entrar.",
            "explicacion": "Omar Fuentes expone el rol estratégico de la Inteligencia de Ciberamenazas (CTI, por sus siglas en inglés). La CTI recolecta, analiza y sintetiza información proveniente de la web superficial, foros clandestinos (dark web) y telemetría global para identificar las tácticas, técnicas y procedimientos (TTPs) de grupos de amenazas avanzadas persistentes (APTs) que apuntan activamente a sectores industriales y gubernamentales.\n\nLa conferencia enseña que la seguridad no consiste en parcharlo todo a ciegas, lo cual resulta económicamente inviable, sino en priorizar la protección en base a inteligencia accionable. Al correlacionar marcos como MITRE ATT&CK con las vulnerabilidades reales de la organización, los directores de seguridad pueden tomar decisiones informadas de inversión y blindar las puertas exactas que los adversarios están intentando forzar hoy.",
            "puntos_clave": [
                "Niveles de inteligencia (Estratégico, Operacional y Táctico): Traducir datos técnicos complejos en decisiones ejecutivas comprensibles para la alta dirección.",
                "Mapeo mediante MITRE ATT&CK: Categorizar las fases del adversario para identificar brechas de visibilidad y control en la propia infraestructura.",
                "Inteligencia accionable: Descartar feeds de datos masivos estériles y enfocarse en amenazas dirigidas contra tu industria y región geográfica específica."
            ],
            "checklist": [
                "- [ ] Suscribir la organización a fuentes de inteligencia de amenazas específicas para el sector industrial o geográfico correspondiente.",
                "- [ ] Mapear las defensas y controles actuales contra las técnicas de ataque del marco MITRE ATT&CK más empleadas por los actores adversarios.",
                "- [ ] Generar informes periódicos de inteligencia ejecutiva en lenguaje de negocio para orientar las inversiones de la alta gerencia."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué es fundamental que la Inteligencia de Amenazas (CTI) entregue reportes a nivel estratégico y no solo táctico?",
                "respuesta": "Porque los directores y tomadores de decisiones de negocio necesitan comprender el impacto financiero, legal y operativo del riesgo para asignar presupuestos y recursos, mientras que el nivel puramente táctico solo contiene datos técnicos (como hashes o IPs) útiles para los ingenieros."
            },
            "guion_audio": "Para ganar una batalla, primero debes conocer a tu oponente. Omar Fuentes de SEK nos enseña el valor de la Inteligencia de Ciberamenazas, conocida como CTI. En lugar de blindar cada ventana y rincón a ciegas gastando fortunas, la CTI actúa como un radar avanzado que investiga foros clandestinos y movimientos globales para advertirte: ¿quiénes son los atacantes que apuntan a tu sector?, ¿qué técnicas usarán? y ¿cuáles puertas intentarán abrir? Con esta información privilegiada, las organizaciones pueden anticiparse, cerrar las brechas antes de que sean explotadas y justificar con claridad sus inversiones ante la gerencia. En el ciberespacio, la información oportuna es el arma defensiva más poderosa. No esperes el golpe: anticípalo.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "SEK Cybersecurity Intelligence", "url": "https://sek.com"}
            ]
        },
        {
            "id": "dia2_03_cordero",
            "carpeta": "03-dia2-seminario",
            "archivo": "03-cordero-resiliencia-hardware.md",
            "speaker": "César Cordero",
            "institucion": "Lenovo",
            "titulo": "El Rol de la Tecnología en la Continuidad y Resiliencia Operacional",
            "dificultad": "Intermedio",
            "analogia": "Imagina que compras una caja fuerte blindada para guardar tus ahorros. Puedes ponerle la cerradura digital más sofisticada del mundo en la puerta, pero si quien fabricó la caja le instaló una tapa trasera de cartón o un chip espía escondido en las bisagras desde la fábrica, ningún código secreto podrá evitar que te roben.",
            "explicacion": "César Cordero destaca la trascendencia de la seguridad a nivel de hardware, microcódigo y cadena de suministro físico. Con frecuencia, las estrategias defensivas se concentran en el software operativo (antivirus, cortafuegos), descuidando la capa más profunda: la BIOS y el firmware de los computadores y servidores. Si un atacante compromete esta capa inicial de arranque, adquiere control absoluto del equipo de manera persistente e invisible al sistema operativo.\n\nLa sesión aborda cómo los fabricantes líderes integran tecnologías como raíces de confianza de hardware (Root of Trust), chips de seguridad criptográfica TPM y plataformas de auto-recuperación de firmware que restauran el equipo a un estado limpio si detectan manipulación. Asimismo, se exploran soluciones para garantizar la continuidad del negocio, permitiendo restaurar entornos de trabajo completos en la nube en cuestión de minutos ante desastres físicos o ciberataques.",
            "puntos_clave": [
                "Seguridad por debajo del sistema operativo: Blindar la BIOS y el firmware contra amenazas persistentes avanzadas (bootkits/rootkits).",
                "Raíz de confianza en hardware (Hardware Root of Trust): Validación criptográfica del arranque seguro desde el encendido inicial del procesador.",
                "Cadenas de suministro íntegras y trazables: Certificar que los componentes no hayan sido alterados o interceptados durante la fabricación y despacho."
            ],
            "checklist": [
                "- [ ] Activar Secure Boot y verificación criptográfica de BIOS/firmware en todos los servidores y terminales de trabajo.",
                "- [ ] Implementar dispositivos con módulos TPM 2.0 y capacidades de auto-recuperación de firmware ante ataques de bajo nivel.",
                "- [ ] Validar con los proveedores de hardware las certificaciones de seguridad física y trazabilidad en la cadena de suministro."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué un ataque al firmware o BIOS de un computador es mucho más peligroso que una infección típica de software en el sistema operativo?",
                "respuesta": "Porque reside por debajo del sistema operativo y los antivirus, logrando sobrevivir al formateo o cambio del disco duro y manteniendo el control oculto y persistente de la máquina en cada reinicio."
            },
            "guion_audio": "Solemos pensar que los virus solo viven en las aplicaciones o en el correo electrónico, pero el peligro más silencioso se esconde mucho más abajo: en el hardware. En esta lección, César Cordero de Lenovo nos enseña que la verdadera resiliencia comienza en la fábrica del computador. Si un atacante logra infectar la memoria BIOS de un equipo, podrá formatear el disco mil veces y el espía seguirá allí escondido. La tecnología moderna combate esto con raíces de confianza de hardware y chips criptográficos que comprueban que el equipo esté intacto antes de encender la pantalla. Asegurar la cadena de suministro de tus computadores y servidores es tan crucial como instalar un buen antivirus. Blindar la base física garantiza la continuidad de tu operación.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "Lenovo ThinkShield Security", "url": "https://www.lenovo.com"}
            ]
        },
        {
            "id": "dia2_04_alli",
            "carpeta": "03-dia2-seminario",
            "archivo": "04-alli-salud-ciberseguridad.md",
            "speaker": "Nina Alli",
            "institucion": "Biohacking Village",
            "titulo": "Ciberseguridad en Salud: Protegiendo la Infraestructura que Protege Vidas",
            "dificultad": "Principiante",
            "analogia": "Imagina la sala de urgencias de un hospital en medio de una tormenta. De repente, una banda desconecta la energía de los respiradores, cambia las etiquetas de sangre en los refrigeradores del banco de sangre y bloquea con cadenas las puertas del pabellón de cirugías. No buscan dinero de inmediato; han paralizado la máquina que mantiene con vida a tus seres queridos.",
            "explicacion": "Nina Alli, directora de Biohacking Village, expone en esta entrevista magistral la cruda realidad del cibercrimen cuando golpea al sector sanitario. Cuando un ataque de ransomware secuestra las fichas clínicas de un hospital, el impacto no es contable: las ambulancias deben ser derivadas a otras ciudades, las sesiones de quimioterapia se cancelan de emergencia y los cirujanos pierden acceso a los antecedentes alérgicos de pacientes en la mesa de operaciones.\n\nLa expositora hace un llamado ético y urgente a transformar la cultura de seguridad en salud mediante la empatía y la educación práctica, desterrando el lenguaje técnico intimidante que aleja al personal médico y de enfermería. Promueve la colaboración estrecha con comunidades de hackers éticos para descubrir brechas en el equipamiento clínico antes de que sean explotadas por organizaciones criminales.",
            "puntos_clave": [
                "La ciberseguridad en salud es seguridad humana: El secuestro de registros clínicos y equipos asistenciales pone en riesgo inminente vidas humanas.",
                "Pedagogía adaptada al personal médico: La capacitación debe centrarse en flujos clínicos reales, sin culpabilizar a doctores ni enfermeras.",
                "Divulgación coordinada de vulnerabilidades (CVD): Alianzas con hackers éticos y fabricantes para parchar equipos hospitalarios de forma segura."
            ],
            "checklist": [
                "- [ ] Establecer un protocolo clínico de contingencia en papel para mantener la atención médica ante una caída total de las fichas electrónicas.",
                "- [ ] Brindar capacitaciones breves y empáticas sobre higiene digital adaptadas al personal de enfermería y médicos de guardia.",
                "- [ ] Mantener respaldos aislados (offline) e inmutables de los registros clínicos y sistemas de dispensación farmacológica."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué los hospitales son un blanco tan frecuente y vulnerable para los atacantes de ransomware?",
                "respuesta": "Porque manejan datos confidenciales y, al tratarse de servicios críticos donde minutos de interrupción amenazan vidas humanas, los delincuentes calculan que la presión para pagar el rescate rápidamente será mucho más alta."
            },
            "guion_audio": "En un hospital, cada segundo cuenta para salvar una vida; pero ¿qué pasa cuando un ciberataque apaga los monitores de urgencia? Nina Alli, líder de Biohacking Village, nos abre los ojos ante la dimensión más humana y desgarradora de la ciberseguridad: la protección de la salud. Cuando el ransomware bloquea las fichas médicas electrónicas, los cirujanos operan a ciegas y las ambulancias deben desviarse con pacientes graves a bordo. La seguridad digital hospitalaria no es un trámite de oficina; es el soporte vital de nuestros seres queridos. Necesitamos capacitar a médicos y enfermeras con empatía y sencillez, aliarnos con investigadores éticos y blindar los sistemas sanitarios. Porque en salud, una contraseña fuerte o un respaldo seguro salvan vidas todos los días.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "Biohacking Village Health Security", "url": "https://www.village.bio"}
            ]
        },
        {
            "id": "dia2_05_albuquerque",
            "carpeta": "03-dia2-seminario",
            "archivo": "05-albuquerque-deteccion-respuesta.md",
            "speaker": "Tales Albuquerque",
            "institucion": "Sophos",
            "titulo": "Seguridad Digital: Prevención, Detección y Respuesta ante Ciberamenazas",
            "dificultad": "Intermedio",
            "analogia": "Es como un intruso sigiloso que no rompe la ventana con estrépito para robar la televisión, sino que encuentra una copia de la llave que dejaste olvidada bajo el felpudo. Entra silenciosamente de noche, se esconde en el ático durante dos meses estudiando tus horarios y costumbres, y cuando finalmente se decide a actuar, vacía la casa entera en diez minutos.",
            "explicacion": "Tales Albuquerque desmitifica la idea de que los ataques cibernéticos y el ransomware ocurren en un parpadeo. En incidentes contra infraestructuras críticas y grandes empresas, los adversarios suelen permanecer un promedio de semanas o meses infiltrados en la red interna (dwell time). Durante este período exploran directorios, roban credenciales con privilegios y neutralizan los respaldos de seguridad antes de detonar el cifrado masivo.\n\nLa ponencia promueve la adopción de servicios gestionados de detección y respuesta (MDR), donde cazadores de amenazas humanos monitorean la telemetría las 24 horas del día. Albuquerque resalta el peligro de las técnicas Living off the Land (LotL), donde los intrusos utilizan las propias herramientas legítimas del sistema operativo (como PowerShell o WMI) para moverse sin levantar sospechas en los antivirus convencionales.",
            "puntos_clave": [
                "Tiempo de permanencia silenciosa (Dwell Time): Los atacantes estudian la víctima durante semanas antes de cifrar los datos; la detección temprana es crucial.",
                "Técnicas Living off the Land: Uso malicioso de herramientas administrativas nativas para eludir antivirus basados en firmas estáticas.",
                "Cacería activa de amenazas (Threat Hunting 24/7): No basta con alarmas pasivas; se requiere personal experto investigando anomalías de forma continua."
            ],
            "checklist": [
                "- [ ] Activar autenticación multifactor (MFA) obligatoria en todas las conexiones remotas (VPN, RDP) y cuentas de administración.",
                "- [ ] Implementar monitoreo de comportamiento continuo con agentes EDR/XDR con capacidad de bloqueo y respuesta inmediata.",
                "- [ ] Auditar y restringir el uso de consolas de comandos y herramientas administrativas del sistema solo a administradores autorizados."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿En qué consiste la técnica de ataque conocida como 'Living off the Land' (LotL)?",
                "respuesta": "Consiste en que los atacantes utilizan utilitarios y programas legítimos ya instalados en el sistema operativo (como PowerShell o utilidades de red) para ejecutar sus acciones, evitando descargar herramientas sospechosas que alertarían a los antivirus."
            },
            "guion_audio": "¿Crees que tu computador está seguro solo porque el antivirus no muestra alertas rojas? Tales Albuquerque de Sophos nos advierte sobre una realidad inquietante: los atacantes modernos no golpean al instante. Suelen pasar semanas o meses dentro de tus redes, estudiando tus movimientos en completo silencio mediante credenciales robadas y herramientas legítimas del propio sistema. Cuando finalmente detonan el secuestro de información, el daño ya es total. Para ganarles la partida, debemos cazar activamente las amenazas las 24 horas del día, observando comportamientos anómalos antes de que sea tarde. La prevención tradicional ya no basta; la capacidad de detectar a tiempo y responder en minutos es la verdadera frontera de la ciberseguridad moderna.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "Sophos MDR & Threat Research", "url": "https://www.sophos.com"}
            ]
        },
        {
            "id": "dia2_06_norman",
            "carpeta": "03-dia2-seminario",
            "archivo": "06-norman-amenazas-hibridas.md",
            "speaker": "James Norman",
            "institucion": "FCDO (Foreign, Commonwealth & Development Office, Reino Unido)",
            "titulo": "Amenazas híbridas en la era digital",
            "dificultad": "Principiante",
            "analogia": "Imagina que un día se corta la electricidad en todo tu barrio por una avería en un transformador. Al mismo instante, miles de cuentas en redes sociales comienzan a difundir rumores falsos de que el agua corriente está envenenada y que hay turbas saqueando las tiendas, provocando histeria colectiva, carreras al supermercado y colapso de las líneas telefónicas, todo sin disparar una sola bala.",
            "explicacion": "James Norman, diplomático y experto del Ministerio de Asuntos Exteriores británico, expone el concepto de amenazas híbridas en el escenario geopolítico moderno. Una amenaza híbrida orquesta simultáneamente tácticas cibernéticas (como ataques a redes eléctricas o portuarias) con campañas de desinformación masiva en redes sociales y presiones económicas coordinadas por actores estatales o grupos afines.\n\nLa conferencia enseña que el objetivo de estas agresiones no es únicamente destruir infraestructura física, sino debilitar la confianza ciudadana en las instituciones democráticas y sembrar el caos social. La resiliencia nacional frente a la guerra híbrida exige no solo firewalls e ingenieros, sino una ciudadanía dotada de pensamiento crítico, cooperación diplomática internacional y una comunicación gubernamental transparente y veloz.",
            "puntos_clave": [
                "Convergencia de sabotaje cibernético y desinformación: Los apagones informáticos se combinan con falsos rumores para potenciar el pánico social.",
                "Guerra de zona gris: Ataques diseñados deliberadamente por debajo del umbral de un acto de guerra convencional para dificultar la atribución legal.",
                "El pensamiento crítico como ciberdefensa: La alfabetización mediática y la verificación ciudadana son escudos esenciales para la soberanía democrática."
            ],
            "checklist": [
                "- [ ] Establecer canales oficiales de comunicación de crisis verificados para informar rápidamente a la ciudadanía en caso de incidentes.",
                "- [ ] Implementar programas de concientización y alfabetización digital que enseñen a identificar campañas de manipulación y desinformación.",
                "- [ ] Coordinar protocolos de intercambio de información de seguridad nacional y diplomática con aliados internacionales."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál es el objetivo principal de una 'amenaza híbrida' frente a un ciberataque tradicional?",
                "respuesta": "No busca solo desconectar un servidor o robar datos, sino combinar el impacto del ciberataque con desinformación masiva para desestabilizar la confianza pública, sembrar caos y debilitar la gobernanza democrática de una nación."
            },
            "guion_audio": "En el siglo XXI, las batallas no se libran únicamente en tierra, mar o aire; hoy el frente de combate está en las redes y en la opinión pública. James Norman, de la cancillería británica, nos explica las amenazas híbridas. Imagina que un apagón en una subestación eléctrica viene acompañado de una ola de noticias falsas en redes sociales para sembrar histeria colectiva y desconfianza en las instituciones. Ese cóctel de sabotaje digital y manipulación psicológica busca fracturar a la sociedad desde adentro. Frente a esto, nuestra mejor defensa colectiva es el pensamiento crítico. La ciberseguridad es hoy un pilar de la democracia: verificar las noticias antes de compartirlas es tan importante como proteger nuestras contraseñas.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "UK Foreign, Commonwealth & Development Office", "url": "https://www.gov.uk/fcdo"}
            ]
        },
        {
            "id": "dia2_07_abbas",
            "carpeta": "03-dia2-seminario",
            "archivo": "07-abbas-academia-talento.md",
            "speaker": "Nadezda Abbas",
            "institucion": "Universidad Bernardo O'Higgins (UBO)",
            "titulo": "Transformación Digital y Ciberresiliencia: El Rol de la Academia",
            "dificultad": "Principiante",
            "analogia": "Imagina que un país compra los aviones de rescate y los camiones de bomberos más modernos y veloces del planeta para proteger a sus ciudades, pero se olvida de abrir academias para formar pilotos y bomberos. Cuando ocurre la emergencia, las máquinas millonarias quedan inmóviles en los hangares porque no hay nadie que sepa conducirlas.",
            "explicacion": "Nadezda Abbas resalta el rol insustituible de la educación superior en la construcción de la ciberresiliencia del país. Existe a nivel global y en Chile una severa escasez de talento calificado en ciberseguridad, lo que deja a instituciones públicas y privadas desprotegidas no por falta de software o presupuesto, sino por falta de especialistas humanos capaces de interpretar y responder ante las amenazas.\n\nLa académica promueve una profunda transformación en la formación universitaria: dejar atrás la enseñanza puramente teórica para adoptar laboratorios de simulación en vivo, competencias de Capture The Flag (CTF) y proyectos interdisciplinarios vinculados a las necesidades reales de la industria. Asimismo, recalca la urgencia de fomentar la inclusión de mujeres y jóvenes de regiones en carreras STEM para enriquecer la diversidad y capacidad analítica del país.",
            "puntos_clave": [
                "Cierre de la brecha de talento: La educación en ciberseguridad es una inversión crítica para la seguridad nacional y el desarrollo económico.",
                "Metodología basada en la práctica: La formación debe apoyarse en ciberejercicios reales, análisis de incidentes y laboratorios interactivos (CTF).",
                "Diversidad e inclusión en STEM: Impulsar la participación femenina y regional para construir equipos de ciberdefensa multidisciplinarios y robustos."
            ],
            "checklist": [
                "- [ ] Integrar laboratorios prácticos y competencias de Capture The Flag (CTF) en los programas formativos y mallas curriculares.",
                "- [ ] Fomentar alianzas estratégicas entre universidades, organismos estatales (como la PDI) y empresas para pasantías reales.",
                "- [ ] Implementar programas de becas e incentivos para incorporar activamente a mujeres en carreras de ciberseguridad y tecnologías de información."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Por qué la formación puramente teórica resulta insuficiente para preparar profesionales de ciberseguridad hoy en día?",
                "respuesta": "Porque las ciberamenazas evolucionan en tiempo real, por lo que los defensores necesitan adquirir experiencia práctica resolviendo incidentes simulados, utilizando herramientas reales y pensando tácticamente bajo presión en laboratorios y competencias."
            },
            "guion_audio": "Puedes tener el presupuesto más grande del mundo y comprar la mejor tecnología, pero sin personas capacitadas para manejarla, estás indefenso. En esta lección, Nadezda Abbas de la Universidad Bernardo O'Higgins nos recuerda el papel vital de la educación. El mundo enfrenta una escasez dramática de especialistas en ciberseguridad. Proteger a Chile exige formar a una nueva generación de defensores digitales con mentalidad ética, curiosidad científica y experiencia práctica en laboratorios reales y torneos de hacking ético. Además, abrir las puertas a más mujeres y jóvenes de todas las regiones es indispensable para enriquecer la visión de nuestros equipos. La mejor inversión en tecnología siempre será el talento humano. Formar personas es blindar el futuro de nuestra sociedad.",
            "enlaces": [
                {"nombre": "Sitio PDI Ciberseguridad", "url": "https://www.pdichile.cl/seminariociberseguridad"},
                {"nombre": "Canal Oficial YouTube PDI Chile", "url": "https://www.youtube.com/@PDIChileOficial"},
                {"nombre": "Universidad Bernardo O'Higgins (UBO)", "url": "https://www.ubo.cl"}
            ]
        },
        {
            "id": "intl_01_eeuu_uk",
            "carpeta": "04-comparativa-internacional",
            "archivo": "01-nist-cisa-ncsc.md",
            "speaker": "Marco CISA / NIST & NCSC",
            "institucion": "CISA / NIST (EE.UU.) & NCSC (Reino Unido)",
            "titulo": "Marco NIST CSF 2.0 y Guías de Ciberresiliencia CISA/NCSC",
            "dificultad": "Intermedio",
            "analogia": "Es como un manual universal de aviación comercial desarrollado por los mejores pilotos del mundo: no importa si vuelas un avión pequeño o un jet transcontinental, todos siguen una lista estandarizada y rigurosa para antes del despegue, durante el vuelo y en casos de emergencia, garantizando que tripulación y pasajeros lleguen siempre a salvo a su destino.",
            "explicacion": "El modelo anglosajón liderado por el NIST (National Institute of Standards and Technology) con su marco NIST Cybersecurity Framework 2.0 (CSF 2.0), junto a CISA en EE.UU. y el NCSC en el Reino Unido, representa el estándar de oro en ciberresiliencia global. La actualización 2.0 añade formalmente la función de Gobernar (Govern) a las clásicas Identificar, Proteger, Detectar, Responder y Recuperar, situando la gestión del riesgo cibernético al nivel de la estrategia ejecutiva y la cadena de suministro.\n\nEste enfoque promueve una sinergia ágil público-privada sustentada en la arquitectura de Confianza Cero (Zero Trust Architecture según NIST SP 800-207) y normativas de reporte rápido obligatorio como la ley estadounidense CIRCIA (que exige informar ataques significativos en 72 horas y pagos de rescate en 24 horas). En el Reino Unido, el NCSC complementa esto con el Cyber Assessment Framework (CAF), ofreciendo un modelo medible de madurez de seguridad para operadores esenciales.",
            "puntos_clave": [
                "Estructura integral del NIST CSF 2.0: Las seis funciones esenciales (Govern, Identify, Protect, Detect, Respond, Recover) cubren todo el ciclo de vida del riesgo.",
                "Mandatos de reporte CIRCIA y colaboración con CISA: Reportes rápidos obligatorios combinados con colaboración voluntaria y compartición de indicadores.",
                "Ciberdefensa activa del NCSC británico (ACD): Protección automatizada a escala nacional contra phishing y ataques a DNS para todo el sector público."
            ],
            "checklist": [
                "- [ ] Alinear el programa corporativo de ciberseguridad con las seis funciones del Marco NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover).",
                "- [ ] Implementar los Objetivos de Desempeño de Ciberseguridad Intersectoriales (CPGs) definidos por CISA para infraestructura crítica.",
                "- [ ] Establecer un mecanismo de reporte ágil capaz de cumplir con plazos de notificación de incidentes graves antes de 72 horas (estándar CIRCIA)."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál fue la función principal incorporada en la versión 2.0 del Marco de Ciberseguridad del NIST (NIST CSF 2.0)?",
                "respuesta": "La función 'Gobernar' (Govern), que establece cómo las organizaciones toman decisiones, definen su apetito de riesgo corporativo y asignan responsabilidades estratégicas de ciberseguridad a nivel del directorio y la cadena de suministro."
            },
            "guion_audio": "¿Cómo se protegen las superpotencias ante un colapso digital? En este módulo exploramos el modelo anglosajón liderado por el marco NIST 2.0 de Estados Unidos y las directrices de CISA y el NCSC británico. Este marco organiza la defensa en seis pilares fundamentales: Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar. Ya no se trata solo de levantar barreras técnicas, sino de una gobernanza estratégica donde directores y gerentes lideran la gestión del riesgo. Además, leyes como CIRCIA exigen a las empresas de servicios esenciales reportar cualquier ataque grave en menos de setenta y dos horas para coordinar la respuesta colectiva. Un modelo ágil, transparente y probado que guía hoy la ciberresiliencia en todo el planeta.",
            "enlaces": [
                {"nombre": "NIST Cybersecurity Framework 2.0", "url": "https://www.nist.gov/cyberframework"},
                {"nombre": "CISA - Cross-Sector Cybersecurity Performance Goals", "url": "https://www.cisa.gov/cpgs"},
                {"nombre": "UK National Cyber Security Centre (NCSC)", "url": "https://www.ncsc.gov.uk"}
            ]
        },
        {
            "id": "intl_02_china",
            "carpeta": "04-comparativa-internacional",
            "archivo": "02-china-cii-cac.md",
            "speaker": "Administración del Ciberespacio de China (CAC)",
            "institucion": "CAC / MPS (República Popular China)",
            "titulo": "Reglamento de Infraestructura de Información Crítica (CII 2021) y Soberanía de Datos",
            "dificultad": "Avanzado",
            "analogia": "Es como una gran muralla moderna con aduanas e inspectores gubernamentales en cada portón del reino: ningún producto extranjero entra a las fábricas del estado sin pasar por un laboratorio de inspección de seguridad nacional, y toda la información valiosa de los ciudadanos tiene prohibido cruzar las fronteras sin una visa oficial concedida directamente por el emperador.",
            "explicacion": "El modelo de la República Popular China está sustentado en el Reglamento de Protección de Seguridad de Infraestructuras de Información Crítica (CII Regulations de 2021), promulgado por el Consejo de Estado bajo la tutela de la Administración del Ciberespacio de China (CAC - 国家互联网信息办公室) y el Ministerio de Seguridad Pública (MPS). Este esquema define con extrema precisión los sectores estratégicos (energía, finanzas, transporte, defensa, agua y telecomunicaciones), imponiendo la doctrina de la soberanía digital absoluta.\n\nEl régimen chino exige la localización forzosa de datos dentro de su territorio según la Ley de Seguridad de Datos y la Ley de Protección de Información Personal (PIPL), prohibiendo transferencias transfronterizas sin evaluaciones oficiales rigurosas. Además, a través del esquema de protección multi-nivel (MLPS 2.0 / 等保2.0), todo producto de red, software o hardware importado debe someterse a revisiones de seguridad nacional para descartar puertas traseras y favorecer la sustitución tecnológica por componentes de desarrollo nacional.",
            "puntos_clave": [
                "Doctrina de Soberanía Digital: Control territorial estricto del ciberespacio nacional y subordinación de las redes a los intereses de seguridad del Estado.",
                "Localización obligatoria de datos: Almacenamiento local de datos operativos y personales recopilados en infraestructura crítica china.",
                "Esquema MLPS 2.0 y revisión de suministros: Certificación gubernamental exhaustiva de hardware y software extranjero para prevenir espionaje o sabotaje externo."
            ],
            "checklist": [
                "- [ ] Evaluar los requisitos de localización de datos y restricciones de transferencia transfronteriza si se opera en el ecosistema digital chino.",
                "- [ ] Cumplir con las auditorías anuales obligatorias de seguridad según el nivel correspondiente del esquema MLPS 2.0 (等级保护).",
                "- [ ] Implementar canales de reporte inmediato a los departamentos de supervisión de la CAC y al MPS ante cualquier brecha de seguridad."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Cuál es el requisito clave que impone la normativa china de Infraestructura de Información Crítica (CII) sobre el hardware y software extranjero?",
                "respuesta": "Exige someter todos los productos y servicios de red de proveedores externos a rigurosas revisiones de seguridad nacional por parte de la CAC antes de su compra e instalación, para verificar que no contengan puertas traseras ni riesgos para la soberanía del país."
            },
            "guion_audio": "En el gigante asiático, el ciberespacio se rige bajo una filosofía muy clara: soberanía digital absoluta. En este módulo analizamos el modelo de China, regulado por la Administración del Ciberespacio de China, la CAC, y el Reglamento de Infraestructura de Información Crítica de 2021. Para el gobierno chino, cualquier red que gestione energía, transporte o finanzas es una extensión de la soberanía nacional. Por ley, todos los datos estratégicos deben permanecer almacenados estrictamente dentro del país. Además, cualquier tecnología extranjera debe superar minuciosas inspecciones de seguridad nacional para descartar puertas traseras antes de conectarse a los sistemas del Estado. Un enfoque centralizado y de control total donde la seguridad nacional y la sustitución tecnológica priman por sobre todo.",
            "enlaces": [
                {"nombre": "CAC - Administración del Ciberespacio de China", "url": "http://www.cac.gov.cn"},
                {"nombre": "Ministerio de Seguridad Pública de China (MPS)", "url": "https://www.mps.gov.cn"},
                {"nombre": "Directrices MLPS 2.0 (Multi-Level Protection Scheme)", "url": "http://www.tc260.org.cn"}
            ]
        },
        {
            "id": "intl_03_rusia",
            "carpeta": "04-comparativa-internacional",
            "archivo": "03-rusia-187fz-fstec.md",
            "speaker": "Servicio Federal de Control Técnico y Exportaciones (FSTEC / FSB)",
            "institucion": "FSTEC / NKTsKI (Federación Rusa)",
            "titulo": "Ley Federal N° 187-FZ de Seguridad de Infraestructura Crítica y GosSOPKA",
            "dificultad": "Avanzado",
            "analogia": "Es como una ciudadela fortificada en el invierno siberiano, conectada a una red de telégrafos interna completamente cerrada que no toca las líneas exteriores. Si los puentes hacia el resto del mundo se dinamitan o quedan bloqueados por tormentas, la ciudadela puede activar sus propios generadores, cerrar sus compuertas herméticas y seguir funcionando de manera 100% autosuficiente con sus propios recursos locales.",
            "explicacion": "El marco de la Federación Rusa se articula en torno a la Ley Federal N° 187-FZ (Sobre la Seguridad de la Infraestructura de Información Crítica), supervisada por el Servicio Federal de Control Técnico y de Exportaciones (FSTEC - ФСТЭК России) y el Centro Nacional de Coordinación de Incidentes Informáticos (NKTsKI - НКЦКИ) dependiente del FSB. Este marco clasifica a los sujetos de infraestructura crítica en tres categorías de significancia según el impacto potencial sobre la defensa, salud, economía y seguridad del Estado.\n\nEl pilar operacional ruso es el sistema GosSOPKA (ГосСОПКА), una red estatal unificada para la detección, prevención y mitigación de ciberataques a la que todos los operadores críticos deben conectarse obligatoriamente para compartir telemetría en tiempo real. Este modelo se complementa con la doctrina del Runet soberano y decretos presidenciales que obligan a reemplazar todo el software, hardware y criptografía extranjera por soluciones rusas certificadas bajo estándares GOST.",
            "puntos_clave": [
                "Integración obligatoria con GosSOPKA: Conexión técnica directa de centros de seguridad corporativos con la red estatal de alerta del FSB/NKTsKI.",
                "Categorización de importancia crítica (187-FZ): Clasificación formal de objetos de infraestructura para asignar niveles obligatorios de control técnico.",
                "Aislamiento y sustitución de importaciones (Import Substitution): Migración obligatoria a software, criptografía certificada GOST y sistemas operativos nacionales."
            ],
            "checklist": [
                "- [ ] Realizar la categorización formal de todos los objetos de infraestructura crítica de acuerdo a los criterios de la Ley 187-FZ.",
                "- [ ] Configurar la integración y envío automatizado de incidentes y telemetría de red al sistema estatal GosSOPKA (НКЦКИ).",
                "- [ ] Diseñar e implementar planes de sustitución de software y hardware importado por alternativas nacionales o independientes certificadas."
            ],
            "pregunta_autoevaluacion": {
                "pregunta": "¿Qué es el sistema GosSOPKA en el marco de ciberseguridad de la Federación Rusa?",
                "respuesta": "Es el Sistema Estatal de Detección, Prevención y Eliminación de Consecuencias de Ataques Informáticos, una plataforma centralizada obligatoria del FSB donde todos los operadores de infraestructura crítica deben reportar incidentes y coordinar su defensa técnica."
            },
            "guion_audio": "Cruzamos ahora hacia el modelo de la Federación Rusa, guiado por la Ley Federal 187-FZ y normativas del organismo técnico FSTEC. En Rusia, la protección de las redes esenciales se basa en dos conceptos clave: desconexión soberana y centralización total. Todos los operadores estratégicos de energía, transporte y gobierno están obligados a integrarse al sistema GosSOPKA, una red estatal coordinada que monitorea ciberataques en tiempo real a nivel nacional. Además, tras las tensiones geopolíticas, la ley rusa exige la sustitución obligatoria de software y componentes extranjeros por tecnología nacional y algoritmos de criptografía propios. Un esquema diseñado para que, incluso si el país quedara completamente aislado de la internet global, su infraestructura crítica continúe operando sin interrupción.",
            "enlaces": [
                {"nombre": "FSTEC de Rusia (ФСТЭК России)", "url": "https://fstec.ru"},
                {"nombre": "Centro Nacional de Coordinación de Incidentes Informáticos (NKTsKI)", "url": "http://safe-surf.ru"},
                {"nombre": "Portal Oficial de Información Legal de Rusia (Ley 187-FZ)", "url": "http://pravo.gov.ru"}
            ]
        }
    ]
}

target_file = "/home/dani/proyectos/seminario-pdi/datos_seminario.json"
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)

print(f"Archivo guardado exitosamente en {target_file}")
print(f"Total lecciones guardadas: {len(datos['lecciones'])}")
for idx, l in enumerate(datos["lecciones"], 1):
    words = len(l["guion_audio"].split())
    print(f"{idx:02d}. [{l['id']}] Palabras audio: {words} | Checklist: {len(l['checklist'])} | Claves: {len(l['puntos_clave'])}")
