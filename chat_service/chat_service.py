import asyncio
import websockets
import json
import requests

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            message_data = json.loads(message)
            user_id = message_data.get('user_id')
            user = requests.get(f'http://user-service:5000/users/{user_id}').json()
            broadcast_message = f"{user['name']}: {message_data['content']}"
            tasks = [asyncio.create_task(client.send(broadcast_message)) for client in connected_clients]
            await asyncio.gather(*tasks)
    except json.JSONDecodeError:
        print("Received message is not in JSON format.")
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(handler, "0.0.0.0", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
