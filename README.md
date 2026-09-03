<img src="assets/logofinal.png" align="right" width="120" alt="TodoEconometria"/>

# Evaluacion por PROMPTS: Una alternativa a los Pull Requests en educacion

> **Evalua el proceso de aprendizaje, no el codigo generado por IA**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made for Education](https://img.shields.io/badge/Made%20for-Education-blue)](https://github.com/TodoEconometria)

**Idioma:** Español · [English](README.en.md)

---

## El Problema

En la era de ChatGPT, Copilot y Claude, **revisar codigo ya no tiene sentido**:

```
Alumno A: Copia codigo de ChatGPT → PR perfecto → Nota 10
Alumno B: Aprende de verdad → PR con errores → Nota 7

¿Quien aprendio mas?
```

Los Pull Requests evaluan el **resultado** (codigo), no el **proceso** (aprendizaje).

---

## La Solucion: Evaluar PROMPTS

En lugar de revisar codigo, evaluamos los **prompts de IA** que uso el alumno:

| Antes (PRs) | Ahora (PROMPTS) |
|-------------|-----------------|
| Revisar codigo linea por linea | Leer prompts y capturas |
| Codigo puede ser copiado | Prompts muestran pensamiento real |
| Revision manual (horas) | Evaluacion automatica (minutos) |
| Todos entregan codigo similar | Cada proceso es unico |

### Que evaluamos:

1. **Prompts reales** - Copiados tal cual, con errores de escritura
2. **Capturas de pantalla** - Evidencia de la interaccion con IA
3. **Blueprint final** - Resumen tecnico generado por la IA
4. **Coherencia** - Los prompts deben coincidir con el codigo entregado

---

## Como Funciona

### Para el Alumno

```
1. Trabaja con IA (ChatGPT, Claude, Copilot, etc.)
2. Documenta CADA prompt importante en PROMPTS.md
3. Toma capturas de pantalla de los prompts clave
4. Al final, pide a la IA un "blueprint" tecnico
5. Sube todo a su fork con git push
6. Listo! No hay PR que crear
```

### Para el Profesor

```
1. Ejecuta: python evaluar_prompts.py
2. El script analiza PROMPTS.md de cada alumno
3. Genera reporte con:
   - Ranking automatico
   - Destacados (posible bonus)
   - Sospechosos (verificar en persona)
4. Solo interviene en ~10% de casos especiales
```

---

## Estructura del Archivo PROMPTS.md

```markdown
# Prompts de IA - [Nombre del Proyecto]

## Prompt A: [Titulo descriptivo]

**IA usada:** ChatGPT / Claude / Copilot

**Prompt exacto (copiado tal cual):**
> como ago q spark lea un csv grande sin q se cuelge la memoria

**Captura:** Ver `capturas/prompt_A.png`

**Resultado:** [Breve descripcion de lo que obtuviste]

---

## Prompt B: [Titulo descriptivo]
[Mismo formato...]

---

## Blueprint Final

[Al terminar, pide a la IA:]
> "Resume todo lo que hicimos: stack tecnologico, arquitectura,
> decisiones clave, y como replicar este proyecto desde cero"

[Pega el blueprint aqui]
```

---

## Deteccion de Trampa

El sistema detecta automaticamente:

| Alerta | Que detecta |
|--------|-------------|
| Prompts "limpiados" | Prompts perfectos sin errores humanos |
| Copia del ejemplo | Mismo tema/paises que el profesor |
| Blueprint incoherente | Blueprint no coincide con codigo |
| Contenido escaso | Menos de 500 palabras en PROMPTS.md |

---

## Criterios de Puntuacion

El script `evaluar_prompts.py` sugiere una nota sobre 100 (transparente y reproducible;
el profesor tiene la ultima palabra). Los pesos son:

| Componente | Como se mide | Puntos |
|------------|--------------|--------|
| Numero de prompts | `10 x nº de prompts`, con tope | 0–30 |
| Capturas de pantalla | Menciona capturas / `.png` / `.jpg` | +20 |
| Blueprint final | Menciona blueprint / resumen tecnico | +20 |
| Esfuerzo (palabras) | `palabras / 50`, con tope | 0–30 |

**Ajustes por alerta** (sobre la suma anterior):

- `SOSPECHOSO` (prompts demasiado formales: mas del doble de palabras formales que
  informales con ≥3 prompts) → **−20**
- `REVISAR` (contenido corto: menos de 300 palabras) → **−10**
- `DESTACADO` (>1000 palabras y ≥5 prompts) → **+10**

La nota final se recorta al rango `[0, 100]`. La **categoria** se decide asi: cualquier
alerta `SOSPECHOSO` manda a **REVISAR**; nota 0 → **RECHAZADO**; `DESTACADO` o nota ≥90 →
**DESTACADO**; nota ≥60 → **NORMAL**; el resto → **REVISAR**.

> Estos umbrales son un **punto de partida** editable en `config.py`. La nota es una
> señal de triaje —no una calificacion final— para que el profesor concentre su tiempo
> en el ~10% de casos que de verdad requieren revision humana. Ver
> [`docs/anti-trampa.md`](docs/anti-trampa.md) para el detalle de la deteccion.

---

## Instalacion

### 1. Clonar este repositorio

```bash
git clone https://github.com/TodoEconometria/evaluacion-prompts-ia.git
cd evaluacion-prompts-ia
```

### 2. Copiar archivos a tu repositorio

```bash
# GitHub Action para cerrar PRs
cp github-actions/cerrar-prs.yml TU_REPO/.github/workflows/

# Template de PR (explica el sistema)
cp templates/PULL_REQUEST_TEMPLATE.md TU_REPO/.github/

# Template de PROMPTS.md para alumnos
cp templates/PROMPTS.md TU_REPO/plantilla/

# Script de evaluacion (opcional)
cp scripts/evaluar_prompts.py TU_REPO/.profesor/
```

### 3. Configurar lista de alumnos

Edita `scripts/config.py` con los usernames de GitHub de tus alumnos.

---

## Componentes

### `/github-actions/`
- `cerrar-prs.yml` - Cierra automaticamente cualquier PR con mensaje explicativo

### `/templates/`
- `PROMPTS.md` - Template para que alumnos documenten sus prompts
- `PULL_REQUEST_TEMPLATE.md` - Explica por que no se aceptan PRs
- `guia-entregas.md` - Guia completa para alumnos

### `/scripts/`
- `evaluar_prompts.py` - Script de evaluacion automatica
- `config.example.py` - Plantilla de configuracion. Copiala a `config.py` (ignorado por
  git) y pon ahi la lista real de alumnos y los criterios. `config.py` **nunca** se versiona.

### `/docs/`
- `metodologia.md` - Explicacion detallada del sistema
- `configuracion-github.md` - Como configurar tu repositorio
- `anti-trampa.md` - Tecnicas de deteccion implementadas
- `faq.md` - Preguntas frecuentes

---

## Caso de Uso Real

Este sistema se usa en el curso **Big Data con Python** (230 horas):

- **Repositorio:** [ejercicios-bigdata](https://github.com/TodoEconometria/ejercicios-bigdata)
- **Web:** [todoeconometria.github.io/ejercicios-bigdata](https://todoeconometria.github.io/ejercicios-bigdata/)
- **Alumnos:** 18 estudiantes universitarios
- **Resultado:** Evaluacion de 18 trabajos en 30 minutos (vs 6+ horas con PRs)

---

## Filosofia

> "En la era de la IA, el valor no esta en el codigo que produces,
> sino en las preguntas que sabes hacer."

Este sistema reconoce que:

1. **La IA es una herramienta legitima** - No prohibimos su uso, lo evaluamos
2. **El proceso importa mas que el resultado** - Queremos ver como piensas
3. **La autenticidad es verificable** - Los prompts "reales" tienen errores humanos
4. **La eficiencia beneficia a todos** - Menos tiempo revisando = mas tiempo ensenando

---

## Contribuir

Este proyecto es open source. Puedes:

- Reportar bugs via Issues
- Sugerir mejoras
- Compartir tu experiencia implementandolo
- Traducir a otros idiomas

---

## Licencia

MIT License - Usa, modifica y comparte libremente.

---

## Autor

**Prof. Juan Marcelo Gutierrez Miranda**
- GitHub: [@TodoEconometria](https://github.com/TodoEconometria)
- Web: [todoeconometria.com](https://www.todoeconometria.com)
- LinkedIn: [juangutierrezconsultor](https://www.linkedin.com/in/juangutierrezconsultor/)

---

## Privacidad

Este sistema publica prompts y capturas de los alumnos en forks publicos. Antes de
usarlo: obten **consentimiento informado**, ofrece una alternativa privada, indica que
**recorten datos personales** de las capturas, y cumple la normativa (RGPD / FERPA).
Detalle en [`docs/metodologia.md`](docs/metodologia.md#privacidad-y-consentimiento).

## Referencias

- Anderson, L. W., & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy*. Longman.
- Wiggins, G. (1990). The case for authentic assessment. *Practical Assessment, Research & Evaluation*, 2(2).
- Tai, J., Ajjawi, R., Boud, D., Dawson, P., & Panadero, E. (2018). Developing evaluative judgement in higher education. *Higher Education*, 76, 467-481.
- Cotton, D. R. E., Cotton, P. A., & Shipway, J. R. (2024). Chatting and cheating: Ensuring academic integrity in the era of ChatGPT. *Innovations in Education and Teaching International*, 61(2).
- Hunt, A., & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary ed.). Addison-Wesley.

---

*Hecho con dedicacion para la comunidad educativa*
