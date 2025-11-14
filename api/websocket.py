import asyncio
import websockets
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections = set()

    async def connect(self, websocket):
        self.active_connections.add(websocket)

    async def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data):
        if self.active_connections:  # Check if there are any active connections
            message = json.dumps(data)
            await asyncio.wait([
                connection.send(message) for connection in self.active_connections
            ])


manager = ConnectionManager()

async def websocket_endpoint(websocket, path):
    # Connect the client
    await manager.connect(websocket)
    try:
        while True:
            # Listening for incoming messages
            message = await websocket.recv()
            data = json.loads(message)
            # Here you can handle messages sent by the client
            print(f"Received message: {data}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        await manager.disconnect(websocket)


async def start_server():
    server = websockets.serve(websocket_endpoint, "localhost", 8000)
    await server
    print("WebSocket server started at ws://localhost:8000")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()

# Creator Information
# Name: Thamer Aljadaan (CyberX)
# Email: frankly.sa@gmail.com
# Phone: +966597778968
# Date Created: 2025-11-14 18:56:56 UTC
