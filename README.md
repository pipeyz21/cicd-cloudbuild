# .cloudbuild

Pipelines de Cloud Build para el ciclo de vida de DAGs en Cloud Composer.

## Archivos

| Archivo | Trigger | Descripción |
|---|---|---|
| `composer/test-pr.yaml` | PR a `main` | Linting con flake8 y tests unitarios con pytest |
| `composer/validate-for-prod.yaml` | Pre-merge a `main` | Ejecuta DAGs modificados en DEV y genera informe de validación |
| `composer/deploy.yaml` | Merge a `main` | Despliega DAGs al bucket de Composer y verifica el despliegue |

## Flujo

```
PR abierto → test-pr → validate-for-prod → (aprobación) → deploy
```
