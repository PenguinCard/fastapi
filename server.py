import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'Hello': 'World!'}


if __name__ == '__main__':
    uvicorn.run("server:app", port=5000, log_level="info")
