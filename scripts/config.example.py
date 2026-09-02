"""
Configuracion del Sistema de Evaluacion por PROMPTS
====================================================

Copia este archivo a config.py y edita los valores.

IMPORTANTE: config.py NO debe subirse a GitHub (esta en .gitignore)
"""

# Repositorio original del curso (sin https://github.com/)
REPO_ORIGINAL = "TodoEconometria/ejercicios-bigdata"

# Ruta al archivo PROMPTS.md dentro del repositorio
# Ajusta segun tu estructura de carpetas
RUTA_PROMPTS = "entregas/trabajo_final/apellido_nombre/PROMPTS.md"

# Lista de alumnos
# Formato: {'nombre': 'Nombre Completo', 'github': 'username'}
ALUMNOS = [
    {'nombre': 'Maria Garcia', 'github': 'mariagarcia'},
    {'nombre': 'Juan Lopez', 'github': 'juanlopez'},
    {'nombre': 'Ana Martinez', 'github': 'anamartinez'},
    # Agrega mas alumnos aqui...
]

# Criterios de evaluacion (ajustables)
CRITERIOS = {
    'min_prompts': 3,           # Minimo de prompts requeridos
    'min_palabras': 500,        # Minimo de palabras en PROMPTS.md
    'requiere_capturas': True,  # Requiere capturas de pantalla
    'requiere_blueprint': True, # Requiere blueprint final
}
