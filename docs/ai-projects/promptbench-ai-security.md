# PromptBench AI — Security & Secrets Handling

## Security objective

Keep the public AI project reproducible without exposing credentials, tokens, private endpoints, or environment-specific secrets.

## Required controls

### Environment-based secrets

Never hardcode API keys:

```python
import os

api_key = os.getenv("SERVICE_API_KEY")
if not api_key:
    raise RuntimeError("SERVICE_API_KEY is not configured")
```

Use Hugging Face Space **Secrets** for deployed credentials and local environment variables for development.

### `.env.example`

A public repository may include variable names, but never real values:

```text
SERVICE_API_KEY=
MODEL_NAME=
API_BASE_URL=
```

### `.gitignore`

At minimum:

```text
.env
.env.*
!.env.example
__pycache__/
*.pyc
.venv/
venv/
.pytest_cache/
```

### Secret scanning

Before mirroring the Hugging Face source to GitHub:

1. inspect the current source tree for API keys and tokens,
2. inspect test files and examples as well as application code,
3. replace embedded credentials with environment variables,
4. rotate any credential that has ever been committed publicly,
5. enable GitHub secret scanning / push protection where available,
6. run an additional repository scan before publishing.

## AI-specific risks

Prompt/LLM applications should also consider:

- prompt injection,
- untrusted user input,
- excessive token/resource consumption,
- sensitive data included in prompts or logs,
- verbose exception messages leaking configuration,
- third-party API failure handling,
- model output being treated as trusted executable instructions.

## Logging guidance

Logs should record enough information for troubleshooting without storing secrets or unnecessary personal data.

Prefer:

```text
request_id=...
provider=...
model=...
latency_ms=...
status=success|failure
error_type=...
```

Avoid logging:

- full API keys,
- authorization headers,
- complete environment dumps,
- user secrets,
- private prompts unless explicitly required and safely handled.

## Incident response

If a secret is found in repository history:

1. revoke or rotate the secret immediately,
2. remove it from the current source,
3. update the application to use environment variables,
4. inspect repository history and dependent services,
5. document the incident and remediation without republishing the secret.

Removing a secret from the latest commit alone does **not** make an exposed credential safe.
