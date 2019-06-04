# Instrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_currency** | **str** | The currency in which the instrument prices are quoted. | 
**kind** | **str** | Instrument kind, &#x60;\&quot;future\&quot;&#x60; or &#x60;\&quot;option\&quot;&#x60; | 
**tick_size** | **float** | specifies minimal price change and, as follows, the number of decimal places for instrument prices | 
**contract_size** | **int** | Contract size for instrument | 
**is_active** | **bool** | Indicates if the instrument can currently be traded. | 
**option_type** | **str** | The option type (only for options) | [optional] 
**min_trade_amount** | **float** | Minimum amount for trading. For perpetual and futures - in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. | 
**instrument_name** | **str** | Unique instrument identifier | 
**settlement_period** | **str** | The settlement period. | 
**strike** | **float** | The strike value. (only for options) | [optional] 
**base_currency** | **str** | The underlying currency being traded. | 
**creation_timestamp** | **int** | The time when the instrument was first created (milliseconds) | 
**expiration_timestamp** | **int** | The time when the instrument will expire (milliseconds) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


