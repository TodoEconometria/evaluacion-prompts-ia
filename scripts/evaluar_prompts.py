#!/usr/bin/env python3
"""
Sistema de Evaluacion Automatica por PROMPTS
=============================================

Evalua los archivos PROMPTS.md de los alumnos en sus forks de GitHub.

Uso:
    python evaluar_prompts.py

Configuracion:
    Edita config.py con la lista de alumnos y criterios.

Parte del sistema de Evaluacion por PROMPTS
https://github.com/TodoEconometria/evaluacion-prompts-ia

Autor:  Juan Marcelo Gutierrez Miranda | TodoEconometria
Cita:   Gutierrez Miranda, J. M. (2026). Evaluacion por prompts: desplazar la
        evaluacion del producto al proceso en la ensenanza de la programacion
        en la era de la IA generativa. Preprint. TodoEconometria.
Licencia: MIT
"""
__author__ = "Juan Marcelo Gutierrez Miranda"
__license__ = "MIT"
__project__ = "https://github.com/TodoEconometria/evaluacion-prompts-ia"

import os
import re
import json
import subprocess
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

# Importar configuracion
try:
    from config import ALUMNOS, REPO_ORIGINAL, RUTA_PROMPTS, CRITERIOS
except ImportError:
    print("ERROR: No se encontro config.py")
    print("Copia config.example.py a config.py y edita la lista de alumnos")
    exit(1)


@dataclass
class ResultadoEvaluacion:
    """Resultado de evaluar un alumno"""
    alumno: str
    github_user: str
    tiene_prompts: bool
    num_prompts: int
    tiene_capturas: bool
    tiene_blueprint: bool
    total_palabras: int
    alertas: list
    nota_sugerida: float
    categoria: str  # DESTACADO, NORMAL, REVISAR, RECHAZADO


def clonar_fork(github_user: str, temp_dir: Path) -> Optional[Path]:
    """Clona el fork de un alumno a una carpeta temporal"""
    repo_url = f"https://github.com/{github_user}/{REPO_ORIGINAL.split('/')[-1]}.git"
    destino = temp_dir / github_user

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(destino)],
            capture_output=True,
            timeout=60
        )
        return destino if destino.exists() else None
    except Exception as e:
        print(f"  Error clonando {github_user}: {e}")
        return None


def leer_prompts_md(ruta_fork: Path) -> Optional[str]:
    """Lee el archivo PROMPTS.md del fork"""
    ruta_completa = ruta_fork / RUTA_PROMPTS
    if ruta_completa.exists():
        return ruta_completa.read_text(encoding='utf-8', errors='ignore')
    return None


def contar_prompts(contenido: str) -> int:
    """Cuenta cuantos prompts hay documentados"""
    # Busca patrones como "## Prompt A", "### Prompt B", etc.
    patron = r'#+\s*Prompt\s+[A-Z]'
    return len(re.findall(patron, contenido, re.IGNORECASE))


def verificar_capturas(contenido: str) -> bool:
    """Verifica si menciona capturas de pantalla"""
    patrones = [
        r'captura',
        r'screenshot',
        r'\.png',
        r'\.jpg',
        r'capturas/',
    ]
    for patron in patrones:
        if re.search(patron, contenido, re.IGNORECASE):
            return True
    return False


def verificar_blueprint(contenido: str) -> bool:
    """Verifica si tiene blueprint final"""
    patrones = [
        r'blueprint',
        r'resumen\s+tecnico',
        r'resumen\s+final',
        r'parte\s*2',
    ]
    for patron in patrones:
        if re.search(patron, contenido, re.IGNORECASE):
            return True
    return False


def detectar_alertas(contenido: str, num_prompts: int) -> list:
    """Detecta posibles problemas o destacados"""
    alertas = []

    # Alerta: prompts muy "limpios" (sin errores humanos)
    # Los prompts reales suelen tener errores, abreviaciones, etc.
    palabras_formales = ['implementar', 'desarrollar', 'utilizar', 'mediante']
    palabras_informales = ['como', 'que', 'ago', 'necesito', 'ayuda']

    formales = sum(1 for p in palabras_formales if p in contenido.lower())
    informales = sum(1 for p in palabras_informales if p in contenido.lower())

    if formales > informales * 2 and num_prompts >= 3:
        alertas.append("SOSPECHOSO: Prompts muy formales (posiblemente editados)")

    # Alerta: contenido muy corto
    if len(contenido.split()) < 300:
        alertas.append("REVISAR: Contenido muy corto")

    # Alerta: sin errores de ortografia (sospechoso)
    # Los humanos cometen errores tipicos

    # Destacado: contenido extenso y detallado
    if len(contenido.split()) > 1000 and num_prompts >= 5:
        alertas.append("DESTACADO: Documentacion muy completa")

    return alertas


def calcular_nota(resultado: ResultadoEvaluacion) -> float:
    """Calcula nota sugerida basada en criterios"""
    nota = 0.0

    # Tiene PROMPTS.md (obligatorio)
    if not resultado.tiene_prompts:
        return 0.0

    # Numero de prompts (max 30 puntos)
    nota += min(resultado.num_prompts * 10, 30)

    # Tiene capturas (20 puntos)
    if resultado.tiene_capturas:
        nota += 20

    # Tiene blueprint (20 puntos)
    if resultado.tiene_blueprint:
        nota += 20

    # Palabras totales (max 30 puntos)
    palabras_score = min(resultado.total_palabras / 50, 30)
    nota += palabras_score

    # Penalizaciones por alertas
    for alerta in resultado.alertas:
        if "SOSPECHOSO" in alerta:
            nota -= 20
        elif "REVISAR" in alerta:
            nota -= 10

    # Bonus por destacado
    for alerta in resultado.alertas:
        if "DESTACADO" in alerta:
            nota += 10

    return min(max(nota, 0), 100)


def categorizar(nota: float, alertas: list) -> str:
    """Asigna categoria basada en nota y alertas"""
    tiene_sospechoso = any("SOSPECHOSO" in a for a in alertas)
    tiene_destacado = any("DESTACADO" in a for a in alertas)

    if tiene_sospechoso:
        return "REVISAR"
    elif nota == 0:
        return "RECHAZADO"
    elif tiene_destacado or nota >= 90:
        return "DESTACADO"
    elif nota >= 60:
        return "NORMAL"
    else:
        return "REVISAR"


def evaluar_alumno(alumno: dict, temp_dir: Path) -> ResultadoEvaluacion:
    """Evalua un alumno completo"""
    nombre = alumno['nombre']
    github_user = alumno['github']

    print(f"Evaluando: {nombre} (@{github_user})")

    # Valores por defecto
    resultado = ResultadoEvaluacion(
        alumno=nombre,
        github_user=github_user,
        tiene_prompts=False,
        num_prompts=0,
        tiene_capturas=False,
        tiene_blueprint=False,
        total_palabras=0,
        alertas=[],
        nota_sugerida=0.0,
        categoria="RECHAZADO"
    )

    # Clonar fork
    ruta_fork = clonar_fork(github_user, temp_dir)
    if not ruta_fork:
        resultado.alertas.append("ERROR: No se pudo clonar el fork")
        return resultado

    # Leer PROMPTS.md
    contenido = leer_prompts_md(ruta_fork)
    if not contenido:
        resultado.alertas.append("FALTA: No tiene PROMPTS.md")
        return resultado

    # Analizar contenido
    resultado.tiene_prompts = True
    resultado.num_prompts = contar_prompts(contenido)
    resultado.tiene_capturas = verificar_capturas(contenido)
    resultado.tiene_blueprint = verificar_blueprint(contenido)
    resultado.total_palabras = len(contenido.split())
    resultado.alertas = detectar_alertas(contenido, resultado.num_prompts)

    # Calcular nota y categoria
    resultado.nota_sugerida = calcular_nota(resultado)
    resultado.categoria = categorizar(resultado.nota_sugerida, resultado.alertas)

    return resultado


def generar_reporte(resultados: list[ResultadoEvaluacion]) -> str:
    """Genera reporte markdown con todos los resultados"""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    reporte = f"""# Reporte de Evaluacion por PROMPTS

**Fecha:** {fecha}
**Total alumnos:** {len(resultados)}

---

## Resumen

| Categoria | Cantidad |
|-----------|----------|
| DESTACADO | {sum(1 for r in resultados if r.categoria == 'DESTACADO')} |
| NORMAL | {sum(1 for r in resultados if r.categoria == 'NORMAL')} |
| REVISAR | {sum(1 for r in resultados if r.categoria == 'REVISAR')} |
| RECHAZADO | {sum(1 for r in resultados if r.categoria == 'RECHAZADO')} |

---

## Destacados (Posible Bonus)

"""

    destacados = [r for r in resultados if r.categoria == 'DESTACADO']
    if destacados:
        for r in destacados:
            reporte += f"- **{r.alumno}** (@{r.github_user}) - Nota: {r.nota_sugerida:.0f}\n"
    else:
        reporte += "*Ninguno*\n"

    reporte += "\n---\n\n## Requieren Revision Manual\n\n"

    revisar = [r for r in resultados if r.categoria == 'REVISAR']
    if revisar:
        for r in revisar:
            reporte += f"- **{r.alumno}** (@{r.github_user})\n"
            for alerta in r.alertas:
                reporte += f"  - {alerta}\n"
    else:
        reporte += "*Ninguno*\n"

    reporte += "\n---\n\n## Ranking Completo\n\n"
    reporte += "| # | Alumno | GitHub | Prompts | Capturas | Blueprint | Palabras | Nota | Categoria |\n"
    reporte += "|---|--------|--------|---------|----------|-----------|----------|------|----------|\n"

    resultados_ordenados = sorted(resultados, key=lambda r: r.nota_sugerida, reverse=True)
    for i, r in enumerate(resultados_ordenados, 1):
        capturas = "Si" if r.tiene_capturas else "No"
        blueprint = "Si" if r.tiene_blueprint else "No"
        reporte += f"| {i} | {r.alumno} | @{r.github_user} | {r.num_prompts} | {capturas} | {blueprint} | {r.total_palabras} | {r.nota_sugerida:.0f} | {r.categoria} |\n"

    reporte += f"\n---\n\n*Generado automaticamente por evaluacion-prompts-ia*\n"

    return reporte


def main():
    """Funcion principal"""
    print("=" * 60)
    print("SISTEMA DE EVALUACION POR PROMPTS")
    print("=" * 60)
    print()

    # Crear directorio temporal
    temp_dir = Path("temp_evaluacion")
    temp_dir.mkdir(exist_ok=True)

    # Evaluar cada alumno
    resultados = []
    for alumno in ALUMNOS:
        resultado = evaluar_alumno(alumno, temp_dir)
        resultados.append(resultado)
        print(f"  -> {resultado.categoria} (Nota: {resultado.nota_sugerida:.0f})")
        print()

    # Generar reporte
    reporte = generar_reporte(resultados)

    # Guardar reporte
    fecha = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"evaluacion_prompts_{fecha}.md"
    Path(nombre_archivo).write_text(reporte, encoding='utf-8')

    print("=" * 60)
    print(f"Reporte generado: {nombre_archivo}")
    print("=" * 60)

    # Limpiar temporal (opcional)
    # import shutil
    # shutil.rmtree(temp_dir)


if __name__ == "__main__":
    main()
