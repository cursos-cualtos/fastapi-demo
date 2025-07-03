from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379, db=1)

@app.get("/config")
async def root():
    return [{item: r.get(item)} for item in r.keys()]

@app.put("/config/add/{setting_name}/")
async def add(setting_name: str, setting_value: str):
    r.set(setting_name, setting_value)
    return {setting_name: setting_value}

@app.get("/config/get/{setting_name}")
async def get(setting_name):
    return {setting_name: r.get(setting_name)}

@app.get("/hello")
async def hello():
    return {"message": "Hola Mundo!"}