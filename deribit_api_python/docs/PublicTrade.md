# PublicTrade

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Trade direction of the taker | 
**tick_direction** | **int** | Direction of the \&quot;tick\&quot; (&#x60;0&#x60; &#x3D; Plus Tick, &#x60;1&#x60; &#x3D; Zero-Plus Tick, &#x60;2&#x60; &#x3D; Minus Tick, &#x60;3&#x60; &#x3D; Zero-Minus Tick). | 
**timestamp** | **int** | The timestamp of the trade | 
**price** | **float** | The price of the trade | 
**trade_seq** | **int** | The sequence number of the trade within instrument | 
**trade_id** | **str** | Unique (per currency) trade identifier | 
**iv** | **float** | Option implied volatility for the price (Option only) | [optional] 
**index_price** | **float** | Index Price at the moment of trade | 
**amount** | **float** | Trade amount. For perpetual and futures - in USD units, for options it is amount of corresponding cryptocurrency contracts, e.g., BTC or ETH. | 
**instrument_name** | **str** | Unique instrument identifier | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


