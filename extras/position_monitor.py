"""
Position Watcher - operations for monitoring & taking action on the current Deribit position
"""

import asyncio


# interval (in seconds) to pull API data
INTERVAL_FOR_RATELIMIT = 0.05   # make sure it's >10ms

class Monitor:
    om = None   # OrderManager instance
    def __init__(self):
        self.om = __class__.om
        self.position = self.om.get_position()

    async def run(self):
        await self.run_mon_loop()

    async def run_mon_loop(self):
        while True:
            print("Monitor loop executing! Position: ")
            self.position = self.om.get_position()    # constantly update position
            print(self.position)

            # await self.run_check_triggers()

            await asyncio.sleep(INTERVAL_FOR_RATELIMIT)

    async def run_check_triggers(self):
        """
        sub-loop to perform a few crucial checks, called 'triggers', conditions which
        initialize new looping coroutines upon becoming true. Such as:
        -limit chase order fell off the top of the book
        -liquidation price changed (so doomsday stop should be moved)
        -
        """


        await asyncio.sleep(0)


    def stop_loss_monitor(self):
        raise NotImplementedError("TODO")

    async def limit_chaser_adjustments(self, orderid):
        """
        Takes an order ID and tracks that order, chasing it up/down the orderbook.

        e.g. if it's a BUY LIMIT, and someone places an order at a price $0.01 above us, we'll adjust
        our order to be on top.
        """
        orderid = orderid
