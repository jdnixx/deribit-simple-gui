BOOK_SIDE_ORDERTYPE = {
    'buy': 'bids',
    'sell': 'asks'
}

class Order:
    # must set these class properties before instantiating a subclass
    instrument = None
    client = None

    def _make_order(self, side, *args, **kwargs):
        # assert isinstance(__class__, )
        if side == 'buy':
            # self.client.buy(self.instrument, *args, **kwargs)
            return print("ok we did it", self.instrument, self.client)
        elif side == 'sell':
            return self.client.sell(self.instrument, *args, **kwargs)
        else:
            raise ValueError("'side' parameter must be either 'buy' or 'sell'")

class MarketOrder(Order):
    def __init__(self, side, amt):
        # blah blah make a market order
        super()._make_order(side, "market", amt)   # TODO: qty()