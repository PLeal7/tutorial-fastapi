# Execução

Requer Python 3 (testado com 3.14).

## Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
alembic upgrade head
uvicorn main:app --reload
```

## macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn main:app --reload
```

Antes de iniciar a API, substitua o valor de `SECRET_KEY` no `.env` por uma chave própria (por exemplo, a saída de `python -c "import secrets; print(secrets.token_hex(32))"`).

A API fica disponível em http://127.0.0.1:8000 e a documentação em http://127.0.0.1:8000/docs.
