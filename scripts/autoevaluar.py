#!/usr/bin/env python3
"""
Autoevaluacion de un PROMPTS.md (lector o alumno por su cuenta, sin lista de alumnos)
====================================================================================

Aplica los mismos criterios que evaluar_prompts.py (cuenta de prompts, capturas, blueprint,
palabras y alertas) a uno o varios ficheros y escribe un informe en Markdown. Pensado para la
GitHub Action del fork: sin servidor, sin modelos de IA, sin coste. Es una orientacion para quien
aprende, no una nota oficial: el juicio humano sigue siendo irreducible (ver el paper, «Alcance»).

Uso:
    python autoevaluar.py ruta/PROMPTS.md [otra/PROMPTS.md ...] > informe.md

Parte del sistema de Evaluacion por PROMPTS (MIT)
https://github.com/TodoEconometria/evaluacion-prompts-ia
"""
import sys
import types
from pathlib import Path

# evaluar_prompts.py importa config.py (lista de alumnos de una clase); aqui no hace falta
sys.modules.setdefault("config", types.SimpleNamespace(
    ALUMNOS=[], REPO_ORIGINAL="", RUTA_PROMPTS="", CRITERIOS={}))
sys.path.insert(0, str(Path(__file__).parent))
import evaluar_prompts as ev  # noqa: E402

CONSEJOS = {
    "prompts": "Documenta cada prompt con su encabezado («## Prompt A», «## Prompt B»...): al menos 3.",
    "capturas": "Añade capturas de lo que obtuviste (carpeta capturas/ y enlaces .png).",
    "blueprint": "Cierra con un blueprint o resumen técnico de lo que construiste y por qué.",
    "palabras": "Explica más: qué pediste, qué te respondió la IA, qué corregiste tú (500+ palabras).",
}


def evaluar(ruta: Path) -> tuple[ev.ResultadoEvaluacion, list[str]]:
    contenido = ruta.read_text(encoding="utf-8", errors="ignore")
    num = ev.contar_prompts(contenido)
    r = ev.ResultadoEvaluacion(
        alumno=ruta.parent.name, github_user="", tiene_prompts=True, num_prompts=num,
        tiene_capturas=ev.verificar_capturas(contenido), tiene_blueprint=ev.verificar_blueprint(contenido),
        total_palabras=len(contenido.split()), alertas=ev.detectar_alertas(contenido, num),
        nota_sugerida=0.0, categoria="")
    r.nota_sugerida = ev.calcular_nota(r)
    r.categoria = ev.categorizar(r.nota_sugerida, r.alertas)
    consejos = [CONSEJOS[k] for k, falta in (("prompts", num < 3), ("capturas", not r.tiene_capturas),
                                             ("blueprint", not r.tiene_blueprint),
                                             ("palabras", r.total_palabras < 500)) if falta]
    return r, consejos


def informe(rutas: list[Path]) -> str:
    out = ["# Autoevaluación por PROMPTS", "",
           "Orientación automática con los criterios del curso. No es una nota oficial.", ""]
    for ruta in rutas:
        r, consejos = evaluar(ruta)
        out += [f"## `{ruta.as_posix()}`", "",
                "| Prompts | Capturas | Blueprint | Palabras | Puntuación | Categoría |",
                "|---|---|---|---|---|---|",
                f"| {r.num_prompts} | {'sí' if r.tiene_capturas else 'no'} | "
                f"{'sí' if r.tiene_blueprint else 'no'} | {r.total_palabras} | "
                f"{r.nota_sugerida:.0f}/100 | {r.categoria} |", ""]
        out += [f"- {a}" for a in r.alertas] + ([""] if r.alertas else [])
        if consejos:
            out += ["**Para mejorar:**", ""] + [f"- {c}" for c in consejos] + [""]
    return "\n".join(out)


if __name__ == "__main__":
    rutas = [Path(p) for p in sys.argv[1:] if Path(p).is_file()]
    if not rutas:
        print("Sin PROMPTS.md que evaluar.")
        sys.exit(0)
    print(informe(rutas))
