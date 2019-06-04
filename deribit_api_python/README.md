# Deribit API clients

## About
Interact with the Deribit API from the comfort of your favorite programming language.   
The client libraries are automatically generated and cover the REST endpoints of the API.

These clients interface with the Deribit API v2.   
[Find the documentation here](https://docs.deribit.com/v2/#deribit-api-v2-0-0)

##### Important
The access token is valid for a certain time, read more about the scope of access tokens, their validity time and how to refresh them [here](https://docs.deribit.com/v2/#authentication-2).

## Currently supported

* Android
* ASP.NET Core
* C
* Clojure
* C++ Qt5
* C++ REST SDK
* C#
* Erlang
* Go
* Java
* JavaScript
* Kotlin
* Objective-C
* PHP
* Python
* R
* Ruby
* Scala (Akka)
* Swift 4
* TypeScript


## Examples

Following are example code snippets on how to do authentication (using `client_credentials`) with the Python and PHP client libraries

##### Python
```python
    # Setup configuration instance
    conf = configuration.Configuration()
    # Setup unauthenticated client
    client = api_client.ApiClient(conf)
    publicApi = public_api.PublicApi(client)
    # Authenticate with API credentials
    response = publicApi.public_auth_get('client_credentials', '', '', 'API_ACCESS_KEY', 'API_SECRET_KEY', '', '', '', scope='session:test wallet:read')
    access_token = response['result']['access_token']

    conf_authed = configuration.Configuration()
    conf_authed.access_token = access_token
    # Use retrieved authentication token to setup private endpoint client
    client_authed = api_client.ApiClient(conf_authed)
    privateApi = private_api.PrivateApi(client_authed)

    response = privateApi.private_get_transfers_get(currency='BTC')
    print(response['result']['data'][0]['amount'])
    response = privateApi.private_get_current_deposit_address_get(currency='BTC')
    print(response['result']['address'])
```
##### PHP
```php
  <?php
  $configuration = new Configuration();
  $publicApi = new PublicApi($client = null, $configuration);
  // Authenticate with API credentials
  $authData = $publicApi->publicAuthGet('client_credentials', '', '', 'API_ACCESS_KEY', 'API_SECRET_KEY', '', '', '', null, null, 'session:test wallet:read');
  $authDataParsed = json_decode($authData[0], true);
  $accessToken = $authDataParsed['result']['access_token'];

  // Use retrieved authentication token to setup private endpoint client
  $authedConfig = new Configuration();
  $authedConfig->setAccessToken($accessToken);
  $privateApi = new PrivateApi(null, $authedConfig);

  $accountSummaryBTC = $privateApi->privateGetAccountSummaryGet('BTC');
  var_dump($accountSummaryBTC);
  $currentDepositAddressBTC = $privateApi->privateGetCurrentDepositAddressGet('BTC');
  var_dump($currentDepositAddressBTC);
  $transfersBTC = $privateApi->privateGetTransfersGet('BTC');
  var_dump($transfersBTC);
```

## Found a bug or have a question?
Please open an issue and it will be addressed.
