# Metodologia de Evaluacion por PROMPTS

## Fundamentos

### El problema de evaluar codigo en la era de la IA

Desde la aparicion de ChatGPT (noviembre 2022), evaluar codigo tiene un problema fundamental:

1. **El codigo puede ser generado** - Un alumno puede pedir a ChatGPT "escribe un pipeline ETL con Spark" y obtener codigo funcional
2. **El codigo no muestra aprendizaje** - Dos alumnos pueden entregar codigo identico, uno copiandolo y otro entendiendolo
3. **La revision manual es ineficiente** - Revisar PRs linea por linea cuando el codigo es generado no tiene sentido

### La solucion: evaluar el proceso

En lugar de evaluar el **resultado** (codigo), evaluamos el **proceso** (como llegaste ahi):

- Los prompts que usaste con la IA
- Las preguntas que hiciste
- Los errores que cometiste y como los resolviste
- Tu entendimiento final del proyecto

---

## Componentes del Sistema

### 1. Archivo PROMPTS.md

Es el entregable principal. Contiene:

**Parte 1: Prompts Reales**
- Minimo 3 prompts copiados TAL CUAL
- Con errores de ortografia, informalidad, todo
- Captura de pantalla de cada uno

**Parte 2: Blueprint Final**
- Resumen tecnico generado por la IA al final
- Muestra que entendiste lo que construiste

### 2. GitHub Action para cerrar PRs

Automaticamente:
- Detecta cuando alguien abre un PR
- Deja un comentario explicando el sistema
- Cierra el PR

### 3. Script de Evaluacion

Analiza automaticamente:
- Si existe PROMPTS.md
- Numero de prompts documentados
- Si hay capturas de pantalla
- Si hay blueprint
- Cantidad de palabras (indicador de esfuerzo)
- Patrones sospechosos

---

## Deteccion de Trampa

### Prompts "limpiados"

Los prompts reales tienen caracteristicas humanas:
- Errores de ortografia ("como ago que...")
- Lenguaje informal ("ayudame con...")
- Preguntas basicas ("que es spark")

Los prompts inventados despues suelen ser:
- Perfectamente escritos
- Muy tecnicos
- Sin errores

### Copia del ejemplo

Si el profesor da un ejemplo con paises X, Y, Z, el sistema detecta si alguien usa los mismos paises.

### Blueprint incoherente

Si el blueprint describe tecnologias que no aparecen en el codigo, algo esta mal.

---

## Flujo de Trabajo

### Para el alumno

```
1. Hacer fork del repositorio
2. Trabajar con IA (cualquiera)
3. Documentar prompts MIENTRAS trabaja
4. Tomar capturas de los prompts importantes
5. Al final, pedir blueprint a la IA
6. git push a su fork
7. Listo (no hay PR)
```

### Para el profesor

```
1. Esperar fecha de entrega
2. Ejecutar: python evaluar_prompts.py
3. Revisar reporte generado
4. Verificar manualmente casos REVISAR
5. Publicar notas
```

---

## Ventajas

| Aspecto | Sistema PRs | Sistema PROMPTS |
|---------|-------------|-----------------|
| Tiempo evaluacion | 6+ horas | 30 minutos |
| Que evalua | Codigo | Proceso |
| Detecta copia | Dificil | Automatico |
| Escala | Mal | Bien |
| Permite IA | Ambiguo | Explicito |

---

## Implementacion

### Requisitos minimos

1. Repositorio en GitHub
2. Permisos para GitHub Actions
3. Lista de usernames de alumnos

### Pasos

1. Copiar `cerrar-prs.yml` a `.github/workflows/`
2. Copiar `PULL_REQUEST_TEMPLATE.md` a `.github/`
3. Crear plantilla de PROMPTS.md para alumnos
4. Actualizar documentacion del curso
5. Explicar el sistema en clase

---

## FAQ

**P: Los alumnos pueden mentir en sus prompts?**

R: Pueden, pero es dificil mantener coherencia entre prompts inventados, capturas, blueprint y codigo. El sistema detecta inconsistencias.

**P: Que pasa si un alumno no usa IA?**

R: Puede documentar su proceso de busqueda en Google, StackOverflow, etc. El formato es el mismo.

**P: Como manejo alumnos sin cuenta GitHub?**

R: Necesitan crearla. Es parte del aprendizaje profesional.

**P: Funciona para grupos?**

R: Si. Cada miembro documenta SUS prompts en el mismo PROMPTS.md, identificando quien hizo que.

---

## Privacidad y consentimiento

Este sistema pide a los alumnos publicar sus prompts y capturas de pantalla en un
fork publico. Antes de aplicarlo:

- **Consentimiento informado**: explica que el trabajo sera publico y obten el
  consentimiento del alumno; ofrece una alternativa privada (repositorio privado o
  entrega por el aula virtual / LMS) para quien no quiera exponer su trabajo.
- **Datos personales en capturas**: las capturas pueden contener nombre, email o la
  interfaz de la cuenta del alumno. Indicales que **recorten/oculten** cualquier dato
  personal antes de subirlas.
- **Normativa**: cumple la proteccion de datos de tu institucion (RGPD en la UE,
  FERPA en EE. UU.). Pseudonimiza cuando sea posible.
- **Retencion**: acuerda cuanto tiempo permaneceran publicos los trabajos y como
  retirarlos a peticion del alumno.

## Alcance: a quien conoces y a quien no

El sistema reduce el tiempo de revision y aumenta la productividad, pero descansa
sobre un supuesto que conviene explicitar. Dentro de un curso o de un equipo de
desarrollo, quien evalua **conoce a su gente**: reconoce la voz de un alumno o
colaborador en sus prompts igual que reconoceria su forma de escribir codigo, y la
coherencia entre el proceso y la persona le resulta verificable casi de un vistazo.
En ese regimen, el cribado automatico libera tiempo precisamente porque el juicio de
fondo se apoya en un conocimiento previo.

La cosa cambia cuando la propuesta llega de **alguien a quien no se conoce** —el
aporte externo a un proyecto publico (open source), que es, no por casualidad, el
escenario para el que nacieron los pull requests—. Ahi no basta con leer los
prompts: hay que leer **entre lineas** como se construyo el razonamiento, **probar**
el aporte y decidir si se acepta o se rechaza aplicando la experiencia y el
conocimiento del oficio. Esa decision conserva una **subjetividad irreducible**: no
puede automatizarse, ni preverse, ni erradicarse, y es exactamente la parte que,
como humanos, seguimos teniendo que gestionar. La evaluacion por prompts desplaza y
reduce el trabajo de revision dentro de una relacion de confianza ya establecida
—el aula, el equipo—, pero **no elimina el juicio humano** alli donde esa confianza
no existe de antemano. Reconocer este limite no debilita el metodo: automatiza el
cribado, no la responsabilidad de decidir.

## Limitaciones

- El detector de "prompts limpiados" es heuristico y **evitable** (un alumno puede
  pedir a la IA que anada erratas). Trata las alertas como senales para revisar en
  persona, no como veredictos.
- La evidencia de eficacia es de un unico despliegue (ver README); no sustituye a un
  estudio con datos de aprendizaje, tasa de falsos positivos y validez.

## Referencias

- Anderson, L. W., & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and
  Assessing: A Revision of Bloom's Taxonomy of Educational Objectives*. Longman.
- Wiggins, G. (1990). The case for authentic assessment. *Practical Assessment,
  Research & Evaluation*, 2(2).
- Tai, J., Ajjawi, R., Boud, D., Dawson, P., & Panadero, E. (2018). Developing
  evaluative judgement in higher education. *Higher Education*, 76, 467-481.
- Cotton, D. R. E., Cotton, P. A., & Shipway, J. R. (2024). Chatting and cheating:
  Ensuring academic integrity in the era of ChatGPT. *Innovations in Education and
  Teaching International*, 61(2), 228-239.
- Hunt, A., & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary ed.).
  Addison-Wesley.
- GitHub Actions Documentation. https://docs.github.com/en/actions

---

**Autor:** Prof. Juan Marcelo Gutierrez Miranda
**Contacto:** @TodoEconometria
