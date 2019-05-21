# -*- coding: utf-8 -*-

import time, hashlib, requests_async as requests, base64, sys, asyncio.locks
from collections import OrderedDict

from utils import log
logger = log.setup_custom_logger(__name__)


class RestClient(object):
    def __init__(self, key=None, secret=None, url=None):
        self.key = key
        self.secret = secret
        self.session = requests.Session()

        if url:
            self.url = url
        else:
            self.url = "https://www.deribit.com"

    async def request(self, action, data):
        response = None

        try:
            if action.startswith("/api/v1/private/"):
                if self.key is None or self.secret is None:
                    raise Exception("Key or secret empty")

                signature = self.generate_signature(action, data)
                response = await self.session.post(self.url + action, data=data, headers={'x-deribit-sig': signature}, verify=True)
            else:
                response = await self.session.get(self.url + action, params=data, verify=True)
        except Exception as e:
            print("Error making the request. Probably something to do with asyncio.\nException: ", e)



        if response.status_code != 200:
            raise Exception("Wrong response code: {0}".format(response.status_code))

        json = response.json()

        if json["success"] == False:
            raise Exception("Failed: " + json["message"])

        if "result" in json:
            return json["result"]
        elif "message" in json:
            return json["message"]
        else:
            return "Ok"

    def generate_signature(self, action, data):
        tstamp = int(time.time()* 1000)
        signature_data = {
            '_': tstamp,
            '_ackey': self.key,
            '_acsec': self.secret,
            '_action': action
        }
        signature_data.update(data)
        sorted_signature_data = OrderedDict(sorted(signature_data.items(), key=lambda t: t[0]))


        def converter(data):
            key = data[0]
            value = data[1]
            if isinstance(value, list):
                return '='.join([str(key), ''.join(value)])
            else:
                return '='.join([str(key), str(value)])

        items = map(converter, sorted_signature_data.items())

        signature_string = '&'.join(items)

        sha256 = hashlib.sha256()
        sha256.update(signature_string.encode("utf-8"))
        sig = self.key + "." + str(tstamp) + "." 
        sig += base64.b64encode(sha256.digest()).decode("utf-8")
        return sig

    async def getorderbook(self, instrument):
        return await self.request("/api/v1/public/getorderbook", {'instrument': instrument})

    async def getinstruments(self):
        return await self.request("/api/v1/public/getinstruments", {})


    async def getcurrencies(self):
        return await self.request("/api/v1/public/getcurrencies", {})


    async def getlasttrades(self, instrument, count=None, since=None):
        options = {
            'instrument': instrument
        }

        if since:
            options['since'] = since

        if count:
            options['count'] = count

        return await self.request("/api/v1/public/getlasttrades", options)


    async def getsummary(self, instrument):
        return await self.request("/api/v1/public/getsummary", {"instrument": instrument})


    async def index(self):
        return await self.request("/api/v1/public/index", {})

    
    async def stats(self):
        return await self.request("/api/v1/public/stats", {})


    async def account(self):
        return await self.request("/api/v1/private/account", {})


    async def buy(self, instrument, ordertype, quantity, price=None, stopPx=None, reduce_only=None, postOnly=None,
            label=None):
        options = {
            "instrument": instrument,
            "type": ordertype,
            "quantity": quantity,
        }

        if price:
            options["price"] = price
        if stopPx:
            options["stopPx"] = stopPx
        if reduce_only:
            options["reduce_only"] = reduce_only
        if label:
            options["label"] = label
        if postOnly:
            options["postOnly"] = postOnly

        logger.warning("Buy() order options: ", options)

        return await self.request("/api/v1/private/buy", options)


    async def sell(self, instrument, ordertype, quantity, price=None, stopPx=None, reduce_only=None, postOnly=None,
             label=None):
        options = {
            "instrument": instrument,
            "type": ordertype,
            "quantity": quantity,
        }

        if price:
            options["price"] = price
        if stopPx:
            options["stopPx"] = stopPx
        if reduce_only:
            options["reduce_only"] = reduce_only
        if label:
            options["label"] = label
        if postOnly:
            options["postOnly"] = postOnly

        logger.warning("Sell() order options: ", options)

        return await self.request("/api/v1/private/sell", options)


    async def cancel(self, orderId):
        options = {
            "orderId": orderId
        }  

        return await self.request("/api/v1/private/cancel", options)


    async def cancelall(self, typedef="all"):
        return await self.request("/api/v1/private/cancelall", {"type": typedef})


    async def edit(self, orderId, quantity, price):
        options = {
            "orderId": orderId,
            "quantity": quantity,
            "price": price
        }

        return await self.request("/api/v1/private/edit", options)


    async def getopenorders(self, instrument=None, orderId=None):
        options = {}

        if instrument:
            options["instrument"] = instrument 
        if orderId:
            options["orderId"] = orderId

        return await self.request("/api/v1/private/getopenorders", options)


    async def positions(self) -> object:
        """

        :rtype: object
        """
        return await self.request("/api/v1/private/positions", {})


    async def orderhistory(self, count=None):
        options = {}
        if count:
            options["count"] = count

        return await self.request("/api/v1/private/orderhistory", options)


    async def tradehistory(self, countNum=None, instrument="all", startTradeId=None):
        options = {
            "instrument": instrument
        }
  
        if countNum:
            options["count"] = countNum
        if startTradeId:
            options["startTradeId"] = startTradeId
        
        return await self.request("/api/v1/private/tradehistory", options)


    async def orderstate(self, orderId):
        options = {
            "orderId": orderId
        }

        return await self.request("/api/v1/private/orderstate", options)