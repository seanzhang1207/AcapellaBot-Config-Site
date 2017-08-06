import asyncio
import datetime
import random
import websockets
import json
import time

MODE = 'config'
REALSENSE = False
SERIAL = False
AUDIO_IN = False
BATON = False
REALSENSE_SERIAL = False
AUDIO_ANALYZER = False
ACAPELLA = False
BATON_RECV = False
STAGE = 0

def make_status_report():
    global MODE, REALSENSE, SERIAL, AUDIO_IN, BATON, REALSENSE_SERIAL, AUDIO_ANALYZER, ACAPELLA, BATON_RECV, STAGE
    status = {
        "type": "status",
        "mode": MODE,
        "realsense": REALSENSE,
        "serial": SERIAL,
        "audio_in": AUDIO_IN,
        "baton": BATON,
        "realsense_serial": REALSENSE_SERIAL,
        "audio_analyzer": AUDIO_ANALYZER,
        "acapella": ACAPELLA,
        "baton_recv": BATON_RECV,
        "stage": STAGE,
    }
    return json.dumps(status)

async def server(websocket, path):
    global MODE, REALSENSE, SERIAL, AUDIO_IN, BATON, REALSENSE_SERIAL, AUDIO_ANALYZER, ACAPELLA, BATON_RECV, STAGE
    await websocket.send(make_status_report())
    while True:
        data = await websocket.recv()
        data = json.loads(data)
        if data['type'] == "cmd":
            print("Received {} command.".format(data['cmd']))

            if data['cmd'] == "set-mode":
                MODE = data['value']
                time.sleep(1)
                await websocket.send(make_status_report())

            if data['cmd'] == "start-realsense":
                #Start realsense to serial thread here
                REALSENSE_SERIAL = True
                time.sleep(1)
                await websocket.send(make_status_report())

            if data['cmd'] == "start-audioana":
                #Start realsense to serial thread here
                AUDIO_ANALYZER = True
                time.sleep(1)
                await websocket.send(make_status_report())

            if data['cmd'] == "start-acapella":
                #Start realsense to serial thread here
                ACAPELLA = True
                time.sleep(1)
                await websocket.send(make_status_report())

            if data['cmd'] == "start-baton":
                #Start realsense to serial thread here
                BATON_RECV = True
                time.sleep(1)
                await websocket.send(make_status_report())

            if data['cmd'] == "interactions-toggle":
                pass

            if data['cmd'] == "roaming-toggle":
                pass

            if data['cmd'] == "face-toggle":
                pass

            if data['cmd'] == "songs-toggle":
                pass

            if data['cmd'] == "acapella-toggle":
                pass

            if data['cmd'] == "conducting-toggle":
                pass



start_server = websockets.serve(server, '0.0.0.0', 8091)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
