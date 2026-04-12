from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Resumescence API is running"}


@app.get("/get-projects")
async def get_projects():
    return {"status": "ok", "message": "Test endpoint working"}


@app.get("/get-project/{project_id}")
async def get_project(project_id: str):
    return {"status": "ok", "message": "Test endpoint working"}


@app.get("/get-project/{project_id}/get-components")
async def get_components(project_id: str):
    return {"status": "ok", "message": "Test endpoint working"}


@app.get("/get-component/{component_id}")
async def get_component(component_id: str):
    return {"status": "ok", "message": "Test endpoint working"}


@app.get("/get-component/{component_id}/get-rendered-component")
async def get_rendered_component(component_id: str):
    return {"status": "ok", "message": "Test endpoint working"}
