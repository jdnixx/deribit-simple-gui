BOOK_SIDE_ORDERTYPE = {
    'buy': 'bids',
    'sell': 'asks'
}

class Order:
    # must set these class properties before instantiating a subclass
    instrument = None
    client = None

    def _make_order(self, side, *args, **kwargs):
        """ Makes an order (buy or sell) and returns a response object from the API """
        # assert isinstance(__class__, )
        if side == 'buy':
            return self.client.buy(self.instrument, *args, **kwargs)
        elif side == 'sell':
            return self.client.sell(self.instrument, *args, **kwargs)
        else:
            raise ValueError("'side' parameter must be either 'buy' or 'sell'")

class MarketOrder(Order):
    def __init__(self, side, amt):
        # blah blah make a market order
        super()._make_order(side, 'market', amt)   # TODO: qty()

class LimitOrder(Order):
    def __init__(self, side, amt, price, postOnly):
        # make a limit order
        resp = super()._make_order(side, 'limit', amt, price, postOnly)
        self.order = resp['order']

        print("LimitOrder obj self.order: ", self.order)




class LimitChaser(LimitOrder):
    def __init__(self, side, amt, price, postOnly):
        self.side = side
        self.order_current_price = price
        # set the order itself (instance of LimitOrder)
        super().__init__(side, amt, self.order_current_price, postOnly)
        # self.order = is now accessible
        self.order_id = self.order['orderId']

        print("LimitChaser obj self.order: ", self.order)


    def is_filled(self):
        # updates self.order on every run
        self.order = self.client.orderstate(self.order_id)
        self.order_current_price = self.order['price']
        return self.order['state'] is 'filled'


    def check_spread_and_adjust(self, current_spread_price):
        quantity = self.order['quantity']
        if ((current_spread_price > self.order_current_price) and (self.side is 'buy'))\
                or ((current_spread_price < self.order_current_price) and (self.side is 'sell')):
            self.client.edit(self.order_id, quantity, current_spread_price)
