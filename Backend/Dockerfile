FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libffi-dev libssl-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . ./

# Expose Flask port
EXPOSE 8000

# Flask 3 expects module path
ENV PYTHONPATH=/app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000", "--reload"]
