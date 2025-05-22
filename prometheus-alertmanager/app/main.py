from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response
import uvicorn

app = FastAPI()

REQUESTS = Counter("app_requests_total", "Total de requisições")

@app.get("/hello")
def hello():
    REQUESTS.inc()
    return {"message": "Olá, Prometheus!"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
