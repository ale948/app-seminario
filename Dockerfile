FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependencias primero para aprovechar la caché de capas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Usuario no-root por seguridad
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

# Usa el mismo endpoint /health que ya expone la app
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["python", "app.py"]

CMD ["sh", "-c", "gunicorn --bind ${APP_HOST:-0.0.0.0}:${APP_PORT:-5000} app:app"]