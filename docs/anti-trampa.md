# Deteccion de Trampa (anti-trampa)

> **Idioma:** Español · [English](anti-cheating.md)

Este documento detalla las señales que `evaluar_prompts.py` usa para marcar entregas que
merecen una **revision humana**. Ninguna de estas señales es un veredicto: son
heuristicas baratas para decidir *donde* mirar, no *que nota* poner.

## Filosofia: señal, no sentencia

La premisa del sistema es que evaluar el proceso (los prompts) es mas robusto que evaluar
el producto (el codigo) cuando la IA puede generar el producto. Pero un alumno decidido
tambien puede fabricar un proceso verosimil. Por eso el objetivo no es un detector
infalible —no existe— sino **subir el coste de la trampa** y **concentrar la atencion del
profesor** en el puñado de casos dudosos.

## Señales implementadas

### 1. Prompts "demasiado limpios"

Los prompts reales de alguien que aprende tienen huellas humanas: erratas (*"como ago
que..."*), lenguaje informal (*"ayudame con..."*), preguntas basicas (*"que es spark"*).
Un alumno que copia el codigo primero y redacta los prompts despues tiende a producir
prompts pulcros, muy tecnicos y sin errores.

**Como se mide.** Se cuentan ocurrencias de un pequeño lexico formal
(`implementar`, `desarrollar`, `utilizar`, `mediante`) frente a uno informal (`como`,
`que`, `ago`, `necesito`, `ayuda`). Si lo formal supera al informal en mas del doble y hay
≥3 prompts, se emite la alerta `SOSPECHOSO`.

**Limite.** Es trivial de evadir (basta pedir a la IA que añada erratas). Trátalo como una
invitacion a preguntar en persona, no como prueba.

### 2. Copia del ejemplo del profesor

Si el enunciado da un ejemplo con un dominio concreto (paises X, Y, Z; un dataset
concreto), una entrega que reutiliza exactamente ese dominio sugiere copia superficial en
vez de trabajo propio. Se compara el tema/entidades de la entrega con las del ejemplo.

### 3. Blueprint incoherente

El *blueprint* es el resumen tecnico que la IA genera al final. Si describe tecnologias,
arquitectura o decisiones que **no aparecen** en el codigo entregado, la entrega es
internamente inconsistente: buena señal de que las piezas se ensamblaron sin entenderse.

### 4. Contenido escaso

Menos de ~300 palabras en `PROMPTS.md` (o muy pocos prompts) indica esfuerzo insuficiente
para documentar un proceso real. Genera la alerta `REVISAR`.

## Coherencia cruzada: la verdadera defensa

Ninguna señal aislada es fuerte. La deteccion real vive en la **coherencia entre las
cuatro fuentes**:

```
prompts  ⇄  capturas  ⇄  blueprint  ⇄  codigo
```

Fabricar un caso que sea coherente en las cuatro a la vez —los prompts explican el codigo,
las capturas coinciden con los prompts, el blueprint describe lo que el codigo hace de
verdad— cuesta casi tanto como haber hecho el trabajo. Ese es el punto.

## Que NO detecta

- Un alumno que de verdad usa la IA con destreza y ademas entiende poco: el sistema premia
  el proceso documentado, y eso es deliberado (el objetivo es enseñar a usar la IA bien).
- Colusion entre alumnos con dominios distintos y prompts reescritos.
- Falsos positivos por estilo: un alumno naturalmente formal puede disparar `SOSPECHOSO`.
  Por eso la alerta manda a **revisar**, no a **suspender**.

## Recomendacion de uso

1. Corre el script y ordena por categoria.
2. Acepta directamente los `NORMAL`/`DESTACADO` sin alertas.
3. Dedica la revision manual a los `REVISAR` y `SOSPECHOSO`: 2–3 preguntas orales sobre su
   propio blueprint suelen bastar para distinguir al que entendio del que copio.

Ver tambien: [`metodologia.md`](metodologia.md) · [`faq.md`](faq.md).
