import asyncio

from utils import log
logger = log.setup_custom_logger(__name__)

BOOK_SIDE_ORDERTYPE = {
    'buy': 'bids',
    'sell': 'asks'
}

# class aobject(object):
#     """Inheriting this class allows you to define an async __init__.
#
#         So you can create objects by doing something like `await MyClass(params)`
#         """
#
#     async def __new__(cls, *a, **kw):
#         instance = super().__new__(cls)
#         await instance.__init__(*a, **kw)
#         return instance
#
#     async def __init__(self):
#         pass

class Order:
    """
    BASICALLY AN INTERFACE FOR THE SUB-ORDER-TYPES
    """

    # must set these class properties before instantiating a subclass
    # instrument = None
    # client = None
    om = None

    def __init__(self):
        self.side = None
        self.amt = None
        self.order_id = None
        self.order = None
        pass

    async def _make_order(self, side, *args, **kwargs):
        """ Makes an order (buy or sell) and returns a response object from the API """
        logger.info(f"Sending request for client {side} with args={args} and kwargs={kwargs}...")
        if side == 'buy':
            return await self.om.client.buy(self.om.instrument, *args, **kwargs)
        elif side == 'sell':
            return await self.om.client.sell(self.om.instrument, *args, **kwargs)
        else:
            raise ValueError("'side' parameter must be either 'buy' or 'sell'")

    # async def _make_order_OM(self, side, *args, **kwargs):
    #     """ Makes an order (buy or sell) and returns a response object from the API """
    #     if side == 'buy':
    #         return await self.client.buy(self.instrument, *args, **kwargs)
    #     elif side == 'sell':
    #         return await self.client.sell(self.instrument, *args, **kwargs)
    #     else:
    #         raise ValueError("'side' parameter must be either 'buy' or 'sell'")

class MarketOrder(Order):
    # def __init__(self, side, amt):
    def __init__(self):
        super().__init__()

        # blah blah make a market order

    async def make_market_order(self, side, amt):
        resp = await self._make_order(side, 'market', amt)   # sets self.order
        self.order = resp['order']
        logger.info("Market Order made, order:")
        logger.info(self.order)
        return self.order

class LimitOrder(Order):
    def __init__(self):
        super().__init__()
    #
    #     # blah blah make a limit order
    #     resp = await self._make_order(side, 'limit', amt, price, postOnly)
    #     self.order = resp['order']
    #
    #     print("LimitOrder obj self.order: ", self.order)

    async def make_limit_order(self, side, amt, price, postOnly):
        resp = await self._make_order(side, 'limit', amt, price, postOnly)
        self.order = resp['order']
        logger.info("Limit Order made, order: ")
        logger.info(self.order)
        return self.order

class LimitChaser(LimitOrder):
    def __init__(self):
        self.order_current_price = None
        super().__init__()

    # async def make_limitchase_initial_order(self, side, amt, postOnly=True):
    #     self.side = side
    #     self.amt = amt
    #     initialprice = await self.om.get_spread_price(self.side)
    #     await self.make_limit_order(self.side, self.amt, initialprice, postOnly)
    #     # self.order = is now accessible
    #     self.order_id = self.order['orderId']
    #
    #     print("LimitChaser obj self.order: ", self.order)

    async def make_limitchase_initial_order(self, side, amt):
        self.side = side
        self.amt = amt
        initialprice = await self.om.get_spread_price(self.side)
        await self.make_limit_order(self.side, self.amt, initialprice, postOnly=True)

        # self.order = is now accessible
        self.order_id = self.order['orderId']
        logger.info("LimitChaser initial order ran, self.order: ")
        logger.info(self.order)

    async def is_filled(self):
        # updates self.order on every run
        self.order = await self.om.client.orderstate(self.order_id)

        state = self.order['state']
        logger.info("Chceking if order is filled; Order 'state' is: ")
        logger.info(state)
        logger.info("So 'filled' is (true or false):")
        isfilled = state == 'filled'
        logger.info(isfilled)
        return state == 'filled'

    # async def check_spread_and_adjust(self):
    #     self.order_current_price = self.order['price']
    #     current_spread_price = await self.om.get_spread_price(self.side)
    #     quantity = self.order['quantity']
    #     if ((current_spread_price > self.order_current_price) and (self.side is 'buy'))\
    #             or ((current_spread_price < self.order_current_price) and (self.side is 'sell')):
    #         await self.om.client.edit(self.order_id, quantity, current_spread_price)

    async def spam_edit_order(self, price):
        await self.om.client.edit(self.order_id, self.amt, price)