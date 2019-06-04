import openapi_client
from openapi_client import Configuration, ApiClient, PublicApi, PrivateApi


class NewClient_v2(ApiClient):
    def __init__(self, path_to_keyfile="../deribit_keys.txt"):
        """
        Deribit Client setup

        Keyfile must have at least 2 lines:
            key on the first line
            secret on the second line
            (optional) "test" on the third line, if using the testnet

        """
        # assumes keyfile is in parent dir

        with open(path_to_keyfile, "r") as f:
            deribit_key = f.readline().strip()
            deribit_secret = f.readline().strip()
            optional_test = f.readline().strip()

            # if optional_test == "test":
            #     deribit_testnet = "https://test.deribit.com"
            # else:
            #     deribit_testnet = None

        ### VANILLA CLIENT SETUP ###
        config = Configuration()
        # set testnet, if specified
        if optional_test == "test":
            config.host = config.get_host_settings()[1]['url']
        super().__init__(config)
        # logger.info('New ApiClient created!')


        ### AUTH ###
        self.publicapi = PublicApi(self)
        resp = self.publicapi.public_auth_get('client_credentials', '', '', 'API KEY HERE',
                                         'API SECRET HERE', '', '', '',
                                         scope='session:test wallet:read')
        access_token = resp['result']['access_token']

        config_authed = Configuration()
        if optional_test == "test":
            config_authed.host = "https://test.deribit.com/api/v2"
        config_authed.access_token = access_token

        # Use retrieved authentication token to setup private endpoint client
        super().__init__(config_authed)

        ### PRIVATE API
        self.privateapi = PrivateApi(self)


    def test_call(self):
        resp = self.privateapi.private_get_transfers_get('btc')
        print(resp['result']['data'][0]['amount'])
        resp = self.privateapi.private_get_current_deposit_address_get(currency='BTC')
        print(resp['result']['address'])


# t = NewClient_v2()
#
# config = Configuration()
# config.host = config.get_host_settings()[1]['url']
#
# client = ApiClient(config)
# publicapi = PublicApi(client)
#
# resp = publicapi.public_auth_get('client_credentials', '', '', 'API KEY HERE',
#                                          'API SECRET HERE', '', '', '', scope='session:test wallet:read')
# access_token = resp['result']['access_token']
#
# config_authed = Configuration()
# config_authed.host = config_authed.get_host_from_settings(1)[1]['url']
# config_authed.access_token = access_token
#
# Use retrieved authentication token to setup private endpoint client
# client_authed = ApiClient(config_authed)
# privateapi = PrivateApi(client_authed)
#
# resp = privateapi.private_get_transfers_get('btc')
# print(resp['result']['data'][0]['amount'])
# resp = privateapi.private_get_current_deposit_address_get(currency='BTC')
# print(resp['result']['address'])