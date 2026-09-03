# Preguntas Frecuentes (FAQ)

> **Idioma:** Español · [English](faq.en.md)

### ¿Los alumnos pueden mentir en sus prompts?

Pueden, pero mantener coherencia entre prompts inventados, capturas, blueprint y codigo es
costoso. El sistema busca **inconsistencias** entre esas cuatro fuentes (ver
[`anti-trampa.md`](anti-trampa.md)). Fabricar un caso coherente cuesta casi tanto como
hacer el trabajo.

### ¿Qué pasa si un alumno no usa IA?

Documenta su proceso igual: busquedas en Google, StackOverflow, documentacion, prueba y
error. El formato de `PROMPTS.md` es el mismo; lo que se evalua es el **razonamiento**, no
la herramienta concreta.

### ¿Cómo manejo alumnos sin cuenta de GitHub?

Necesitan crearla: forma parte de la alfabetizacion profesional. Como alternativa, la misma
estructura (`PROMPTS.md` + capturas + blueprint) puede entregarse por el aula virtual / LMS
para quien no pueda o no quiera exponer su trabajo en publico (ver privacidad mas abajo).

### ¿Funciona para trabajos en grupo?

Sí. Cada integrante documenta **sus** prompts en el mismo `PROMPTS.md`, identificando quien
hizo que. Asi la contribucion individual queda trazable dentro del trabajo colectivo.

### ¿La nota del script es la nota final?

No. Es una **señal de triaje** para ordenar las entregas y marcar las dudosas. La
calificacion final la decide el profesor; los pesos son editables en `config.py`. Ver
"Criterios de Puntuacion" en el README.

### ¿No es injusto publicar el trabajo de los alumnos?

Por eso el consentimiento informado y la alternativa privada son **obligatorios**. Nadie
debe ser forzado a exponer su trabajo. Ver la seccion de privacidad en
[`metodologia.md`](metodologia.md#privacidad-y-consentimiento) (RGPD / FERPA).

### ¿El detector de trampa da falsos positivos?

Sí, y a proposito prefiere marcar de mas (mandar a revisar) que de menos. Un alumno de
estilo formal puede disparar la alerta `SOSPECHOSO` sin haber copiado. Por eso la alerta
lleva a una **conversacion**, no a una sancion automatica.

### ¿Puedo usar esto fuera de programacion?

El principio —evaluar el proceso de pensamiento en vez del entregable que la IA puede
generar— es general. La implementacion concreta (forks, `PROMPTS.md`, blueprint tecnico)
esta pensada para asignaturas tecnicas; adaptarla a ensayos o diseño requiere cambiar el
formato de evidencia, no la filosofia.

### ¿Dónde está el fundamento academico?

En [`metodologia.md`](metodologia.md) y en las referencias del README (evaluacion autentica
de Wiggins 1990; juicio evaluativo de Tai et al. 2018; integridad academica y ChatGPT de
Cotton et al. 2024). El whitepaper completo esta en `paper/preprint.pdf`.
