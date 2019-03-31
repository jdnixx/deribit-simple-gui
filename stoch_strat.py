import time
from pyti import stochastic as stoch

from deribit_api import RestClient
client = RestClient("AHoDez9QDVyM", "UQT5ZLCGE4WTF6XYSKTJZSJKOCXQES35", "https://test.deribit.com")  # key, secret, URL
client.index()
client.account()
# print(client.positions())


INSTRUMENT = "BTC-PERPETUAL"



data = [4087.56, 4086.82, 4086.12] #whatever
period = 3

K = stoch.percent_k(data, period)
D = stoch.percent_d(data, period)


class StochStrat:
	#def __init__(self):

		# Nothing



	def run_loop(self):
		while True:
			print(client.positions())

			data =
			print("%s \n %s" % (K, D))

			time.sleep(1)

	#def calc_stoch(self):
	#	data =



'''
Startup Behavior
'''

ss = StochStrat()
ss.run_loop()