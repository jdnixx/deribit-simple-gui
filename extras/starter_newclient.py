# change these!!!
path_to_keyfile = '../deribit_keys.txt'
market = 'btc'



# begin
# program = Starter(path_to_keyfile, market)



path_to_keyfile = '../../deribit_keys.txt'

from websockets import client as websockets
import asyncio
import json
# from extras import new_deribit_api
# client = new_deribit_api.NewClient_v2(path_to_keyfile)
#
# wsapi = new_deribit_api.openapi_client.WebsocketOnlyApi(client)
# thread = wsapi.public_subscribe_get(["deribit_price_index.btc_usd"], async_req=True)
#
# subapi = new_deribit_api.openapi_client.SubscriptionManagementApi(client)
# threadsub = subapi.public_subscribe_get(["deribit_price_index.btc_usd"], async_req=True)


# Websoccetz
uri = "wss://test.deribit.com/ws/api/v2"
async def authentercate(authmsg):
    ws = await websockets.connect(uri)
    # await ws.send(authmsg)
    # resp = await ws.recv()
    # print(resp)
    return ws
auth = {
    "jsonrpc": "2.0",
     "method": "public/auth",
     # "id": 42,
     "params": {
        "grant_type": "client_credentials",
         "client_id": "API KEY HERE",
         "client_secret": "API SECRETE HERE"
     }
}
privsub = {
    "jsonrpc": "2.0",
     "method": "private/subscribe",
     "id": 42,
     "params": {
        "channels": ["user.portfolio.btc"]}
}
async def go():
    ws = await authentercate(auth)
    resp = await ws.send(json.dumps(auth))
    print(resp)
    # authenticated
    await call(ws, json.dumps(privsub))
async def call(ws, msg):
        await ws.send(msg)
        while ws.open:
            resp = await ws.recv()
            print(resp)
# asyncio.run(call_and_complete(json.dumps(auth)))
asyncio.run(go())
# asyncio.run(call(json.dumps(privsub)))