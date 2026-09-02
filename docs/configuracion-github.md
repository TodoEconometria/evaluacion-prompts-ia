# Configuracion de GitHub para Evaluacion por PROMPTS

Esta guia explica como configurar tu repositorio de GitHub para usar el sistema.

---

## 1. GitHub Action para Cerrar PRs

### Copiar el archivo

```bash
mkdir -p .github/workflows
cp github-actions/cerrar-prs.yml .github/workflows/
```

### Personalizar el mensaje

Edita `.github/workflows/cerrar-prs.yml` y actualiza:
- URLs a tu documentacion
- Mensaje de bienvenida
- Recursos especificos de tu curso

### Verificar permisos

El Action necesita permisos para:
- Comentar en PRs
- Cerrar PRs

Esto se configura en el archivo con:
```yaml
permissions:
  pull-requests: write
```

---

## 2. Template de Pull Request

### Copiar el archivo

```bash
cp templates/PULL_REQUEST_TEMPLATE.md .github/
```

### Proposito

Cuando alguien intente crear un PR, vera este mensaje ANTES de crearlo.
Explica que no se aceptan PRs y como entregar correctamente.

---

## 3. Branch Protection (Opcional)

Puedes agregar proteccion adicional a la rama main:

1. Ve a Settings > Branches
2. Add rule para `main`
3. Configura:
   - Require pull request reviews (aunque los cierres)
   - Restrict who can push

Esto previene que alguien haga push directo a main.

---

## 4. Configuracion de Issues

### Deshabilitar Issues (Opcional)

Si no quieres que abran issues:

1. Settings > General
2. Features > Uncheck "Issues"

### O usar templates

Si quieres permitir issues pero guiarlos:

```bash
mkdir -p .github/ISSUE_TEMPLATE
```

Crea templates para:
- Preguntas sobre el curso
- Reportar errores en el material
- etc.

---

## 5. README del Repositorio

Actualiza tu README.md principal con:

```markdown
## Como Entregar

Este repositorio usa **evaluacion por PROMPTS**, no Pull Requests.

1. Trabaja en tu fork
2. Documenta tus prompts en `PROMPTS.md`
3. Sube con `git push`

Ver [Guia de Entregas](link) para mas detalles.

> Los PRs seran cerrados automaticamente.
```

---

## 6. Verificar que Funciona

### Test de la Action

1. Crea un fork de tu propio repo (con otra cuenta o pide a alguien)
2. Abre un PR de prueba
3. Verifica que:
   - Se agrega el comentario explicativo
   - El PR se cierra automaticamente

### Ver logs

1. Ve a Actions en tu repositorio
2. Busca "Cerrar PRs Automaticamente"
3. Revisa los logs de ejecucion

---

## 7. Problemas Comunes

### "Action no se ejecuta"

Verifica que:
- El archivo esta en `.github/workflows/`
- El nombre termina en `.yml`
- La sintaxis YAML es correcta

### "No tiene permisos"

Verifica que la Action tiene:
```yaml
permissions:
  pull-requests: write
```

### "El mensaje no aparece"

El PR target debe ser hacia tu repositorio, no hacia el fork.
`pull_request_target` se ejecuta en el contexto del repo base.

---

## 8. Seguridad

### pull_request_target vs pull_request

Usamos `pull_request_target` porque:
- Se ejecuta en el contexto del repo base
- Tiene permisos para modificar PRs
- Funciona con PRs desde forks

**Riesgo:** El codigo del workflow viene del repo base, no del PR.
Esto es seguro porque no ejecutamos codigo del PR.

### No ejecutar codigo del PR

El workflow solo:
- Lee metadatos del PR (numero, usuario)
- Escribe un comentario
- Cambia el estado a cerrado

Nunca ejecuta codigo del PR, asi que es seguro.

---

## Recursos

- [GitHub Actions Security](https://docs.github.com/en/actions/security-guides)
- [pull_request_target](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target)
- [Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
