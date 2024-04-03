import cv2
import numpy as np
import asyncio
import websockets
import predictor

async def echo(websocket, path):
    async for message in websocket:
        # Assuming the message is a binary frame (blob sent from the frontend)
        nparr = np.frombuffer(message, np.uint8)
    # Decode image
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # frame is now in BGR format suitable for OpenCV
        char = predictor.runCamera(frame)
        print("Received character: " + char)

        # Send a confirmation back to the client
        await websocket.send(char)

async def main():
    async with websockets.serve(echo, "localhost", 4000):
        print("WebSocket server started on ws://localhost:4000")
        await asyncio.Future()  # run forever


    
if __name__ == "__main__":
    asyncio.run(main())

