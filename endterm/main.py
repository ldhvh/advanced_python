from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Task2</title>
    </head>
    <body>
        <h1>Webpage</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="txt1" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("txt1")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 0
    while True:
        i+=1
        data = await websocket.receive_text()
        await websocket.send_text(f"The {i} message was: {data}")