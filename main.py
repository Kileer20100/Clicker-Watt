from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# Подключение директорий со статическими файлами
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/css", StaticFiles(directory="static/css"), name="css")
app.mount("/image", StaticFiles(directory="static/image"), name="image")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Загрузка HTML-файла и возврат его как ответа
    html_file = Path("static/index.html").read_text()
    return HTMLResponse(content=html_file)

@app.get("/bost", response_class=HTMLResponse)
async def read_bost():
    html_file = Path("static/Bost.html").read_text()
    return HTMLResponse(content=html_file)



@app.get("/task", response_class=HTMLResponse)
async def read_task():
    html_file = Path("static/task.html").read_text()
    return HTMLResponse(content=html_file)

@app.get("/invite", response_class=HTMLResponse)
async def read_invite():
    html_file = Path("static/invite.html").read_text()
    return HTMLResponse(content=html_file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
