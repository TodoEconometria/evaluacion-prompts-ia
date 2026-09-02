# Guia de Entregas - Sistema por PROMPTS

Esta guia explica como entregar tus trabajos usando el sistema de evaluacion por PROMPTS.

---

## Resumen en 30 segundos

```
1. Trabajas en TU fork (tu copia del repositorio)
2. Documentas tus prompts de IA en PROMPTS.md
3. Tomas capturas de pantalla de los prompts
4. Subes con: git add . && git commit -m "mensaje" && git push
5. Listo! El sistema evalua automaticamente tu PROMPTS.md
```

**NO necesitas crear Pull Request.**

---

## El Archivo Mas Importante: PROMPTS.md

Este archivo es **LO QUE SE EVALUA**. No el codigo, no el resultado final.

### Estructura:

```markdown
# Prompts de IA - Mi Proyecto

## Prompt A: [Titulo]
**IA usada:** ChatGPT
**Prompt exacto:**
> como ago q python lea un archivo csv muy grande

**Captura:** Ver capturas/prompt_A.png

---

## Prompt B: [Titulo]
[Mismo formato...]

---

## Blueprint Final
[Resumen tecnico generado por la IA]
```

### Reglas importantes:

1. **NO limpies tus prompts** - Si escribiste con errores, pega con errores
2. **Minimo 3 prompts** - A, B, y C como minimo
3. **Capturas obligatorias** - Screenshot de cada prompt importante
4. **Blueprint al final** - Pide a la IA un resumen tecnico

---

## Paso a Paso

### 1. Hacer Fork (solo una vez)

1. Ve al repositorio del curso
2. Click en "Fork" (arriba a la derecha)
3. Ahora tienes tu copia en `github.com/TU_USUARIO/nombre-repo`

### 2. Clonar a tu PC (solo una vez)

```bash
git clone https://github.com/TU_USUARIO/nombre-repo.git
cd nombre-repo
```

### 3. Trabajar y Documentar

Mientras trabajas con IA:

1. Copia cada prompt importante a `PROMPTS.md`
2. Toma captura de pantalla
3. Guarda la captura en `capturas/`

### 4. Subir tu Trabajo

```bash
git add .
git commit -m "Entrega [nombre del ejercicio]"
git push
```

### 5. Verificar

1. Ve a tu fork en GitHub
2. Verifica que `PROMPTS.md` esta completo
3. Verifica que las capturas estan en `capturas/`

---

## Como se Evalua

El sistema automatico analiza:

| Criterio | Que busca |
|----------|-----------|
| **Autenticidad** | Prompts con errores humanos (no perfectos) |
| **Completitud** | Minimo 3 prompts + blueprint |
| **Coherencia** | Blueprint coincide con codigo entregado |
| **Evidencia** | Capturas de pantalla presentes |

### Alertas automaticas:

- **DESTACADO** - Trabajo excepcional, posible bonus
- **NORMAL** - Cumple requisitos
- **REVISAR** - Algo no cuadra, verificacion manual
- **RECHAZADO** - Copia detectada o requisitos no cumplidos

---

## Errores Comunes

### "No tengo PROMPTS.md"

Crea el archivo copiando la plantilla:

```bash
cp plantilla/PROMPTS.md tu_carpeta/PROMPTS.md
```

### "Mis prompts son muy cortos"

El sistema espera minimo 500 palabras totales en PROMPTS.md.
Incluye mas detalle en "Que obtuviste" y "Que aprendiste".

### "Olvide tomar capturas"

Si ya cerraste la conversacion con la IA, reconstruye el prompt
y toma la captura. Pero es mejor tomarlas en el momento.

---

## FAQ

**P: Puedo usar cualquier IA?**
R: Si. ChatGPT, Claude, Copilot, Gemini, cualquiera. Solo indica cual usaste.

**P: Cuantos prompts debo documentar?**
R: Minimo 3 (A, B, C). Si usaste mas, incluye los mas importantes.

**P: Que pasa si mi codigo no funciona?**
R: No importa. Evaluamos tu proceso de aprendizaje, no si el codigo corre.

**P: Puedo editar PROMPTS.md despues de entregar?**
R: Si, puedes hacer push multiples veces. Se evalua la ultima version.

---

## Recursos

- [Template de PROMPTS.md](../templates/PROMPTS.md)
- [Metodologia completa](../docs/metodologia.md)

---

**Ultima actualizacion:** 2026-02-04
