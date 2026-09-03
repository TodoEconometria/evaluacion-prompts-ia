# Guía de despliegue: implanta la evaluación por prompts en tu curso

> **Idioma:** Español · [English](deployment-guide.md)

Esta guía te lleva de principio a fin con un **ejemplo genérico** que puedes copiar
y adaptar a tus propios materiales. No asume tu asignatura ni tu stack: el método es
independiente del lenguaje o la tecnología que enseñes. Para el detalle mecánico de
GitHub (permisos, `pull_request_target`, branch protection) ver
[`configuracion-github.md`](configuracion-github.md).

## Antes de empezar: el cambio de contrato

Estás cambiando **qué se entrega y qué se evalúa**. Antes: el código, revisado por
PR. Ahora: el **proceso** —los prompts que el estudiante dirigió a la IA, sus
capturas y un *blueprint* técnico final—, con el código como ancla de coherencia.
Comunica este cambio de contrato el primer día; la resistencia habitual desaparece
cuando el alumnado entiende que **no se prohíbe la IA, se evalúa cómo la usa**.

---

## Ejemplo genérico (adáptalo)

Supongamos una asignatura ficticia, **"Procesamiento de datos con Python"**, con un
trabajo final: *"construye un pipeline que ingiera un CSV grande, lo limpie y
publique una tabla agregada"*. Sustituye el dominio por el tuyo (una API REST, un
modelo de ML, un dashboard, un contrato en Solidity: da igual).

### Paso 1 — Prepara el repositorio del curso

1. Crea el repo `mi-curso-datos` (el alumnado hará **fork**, no PR).
2. Copia la acción que cierra PRs y personaliza su mensaje:
   ```bash
   mkdir -p .github/workflows
   cp github-actions/cerrar-prs.yml .github/workflows/
   cp templates/PULL_REQUEST_TEMPLATE.md .github/
   ```
3. Copia la plantilla que el alumnado rellenará y la guía de entregas:
   ```bash
   mkdir -p plantilla
   cp templates/PROMPTS.md plantilla/
   cp templates/guia-entregas.md plantilla/
   ```
4. En el `README.md` del curso, deja claro el flujo (fork → `PROMPTS.md` →
   `git push`, sin PR) y enlaza la guía de entregas.

### Paso 2 — Define el entregable en `PROMPTS.md`

Pide, como mínimo:

- **3+ prompts reales**, copiados tal cual (con erratas: son la huella humana).
- **Una captura** por prompt clave.
- **Un blueprint final**: el resumen técnico que la IA redacta a petición del
  alumno (stack, arquitectura, decisiones) y que demuestra que entiende lo que
  construyó.
- El **código** resultante en su fork.

> La rúbrica **no** valora "que el código funcione" (lo genera la IA), sino la
> **calidad de la descomposición** en prompts, la **capacidad de iterar** ante
> errores, la **coherencia** prompts↔captura↔blueprint↔código y la **comprensión**
> al explicar decisiones. Ver los pesos exactos en el README (sección "Criterios de
> Puntuación") y el fundamento en [`metodologia.md`](metodologia.md).

### Paso 3 — El alumnado trabaja y entrega

```
1. Fork del repo del curso
2. Trabaja con la IA que prefiera, documentando prompts MIENTRAS trabaja
3. Captura los prompts importantes
4. Pide a la IA el blueprint final
5. git push a su fork  (no hay PR que crear)
```

### Paso 4 — Cribado automático

Configura la lista de forks y corre el evaluador (es una **señal de triaje**, no la
nota final):

```bash
cp scripts/config.example.py scripts/config.py   # config.py NO se versiona
# edita ALUMNOS, REPO_ORIGINAL y RUTA_PROMPTS
python scripts/evaluar_prompts.py
```

Genera un informe con ranking y categorías (destacado / normal / **revisar** /
rechazado). El evaluador está sesgado a la **sensibilidad**: prefiere marcar de más.
Los umbrales viven en `config.py` y se ajustan a tu curso.

### Paso 5 — Revisión humana donde importa

Acepta directamente los `normal`/`destacado` sin alertas. Dedica tu tiempo a los
`revisar`: **2–3 preguntas orales sobre su propio blueprint** distinguen enseguida
al que entendió del que ensambló sin comprender. La máquina prioriza; **tú
calificas**.

---

## Adaptar a tus propios materiales

- **Otro lenguaje/stack**: no cambia nada. El entregable es el proceso, no el
  código; sirve igual para SQL, R, Rust o un notebook.
- **Trabajo en grupo**: cada integrante documenta **sus** prompts en el mismo
  `PROMPTS.md`, identificando quién hizo qué.
- **Sin GitHub**: el mismo tríptico (`PROMPTS.md` + capturas + blueprint) se entrega
  por el aula virtual / LMS. Imprescindible para quien no quiera exponer su trabajo
  (ver privacidad).
- **Ajustar la exigencia**: sube `min_prompts`/`min_palabras` en `CRITERIOS` para
  cursos avanzados; baja el umbral de la alerta de "contenido escaso" para
  principiantes.

## Privacidad (obligatorio)

El método publica prompts y capturas en forks públicos. **Consentimiento informado**
+ **alternativa privada** sin penalización + instruir para que **oculten datos
personales** de las capturas + cumplir RGPD/FERPA. Detalle en
[`metodologia.md`](metodologia.md#privacidad-y-consentimiento).

---

## Cómo citar y atribuir este trabajo

Si usas el método o las herramientas —en tu curso, en una charla, en un artículo o
al derivar tu propia versión—, **cita la autoría** y **conserva la atribución**:

**Cita académica (preprint):**

> Gutierrez Miranda, J. M. (2026). *Evaluación por prompts: desplazar la evaluación
> del producto al proceso en la enseñanza de la programación en la era de la IA
> generativa*. Preprint. TodoEconometria.
> https://github.com/TodoEconometria/evaluacion-prompts-ia

**Software / toolkit:** ver [`CITATION.cff`](../CITATION.cff) (GitHub muestra el
botón "Cite this repository"). Autor: **Juan Marcelo Gutierrez Miranda | TodoEconometria**.

**Licencia MIT:** puedes usar, modificar y redistribuir libremente; la única
condición es **conservar el aviso de copyright y la atribución al autor** en las
copias y derivados. No elimines las cabeceras de autoría de los scripts.
