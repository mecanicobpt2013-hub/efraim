
from fastapi import FastAPI

app = FastAPI(
    title="Minha API",
    description="Minha primeira API criada no GitHub",
    version="1.0"
)

@app.get("/")
def inicio():
    return {
        "mensagem": "API funcionando!",
        "status": "online"
    }

@app.get("/usuario")
def usuario():
    return {
        "nome": "Efraim",
        "status": "ativo"
    }

@app.get("/teste")
def teste():
    return {
        "resultado": "Sucesso"
    }
