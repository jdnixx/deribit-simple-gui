# Position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | direction, &#x60;buy&#x60; or &#x60;sell&#x60; | 
**average_price_usd** | **float** | Only for options, average price in USD | [optional] 
**estimated_liquidation_price** | **float** | Only for futures, estimated liquidation price | [optional] 
**floating_profit_loss** | **float** | Floating profit or loss | 
**floating_profit_loss_usd** | **float** | Only for options, floating profit or loss in USD | [optional] 
**open_orders_margin** | **float** | Open orders margin | 
**total_profit_loss** | **float** | Profit or loss from position | 
**realized_profit_loss** | **float** | Realized profit or loss | [optional] 
**delta** | **float** | Delta parameter | 
**initial_margin** | **float** | Initial margin | 
**size** | **float** | Position size for futures size in quote currency (e.g. USD), for options size is in base currency (e.g. BTC) | 
**maintenance_margin** | **float** | Maintenance margin | 
**kind** | **str** | Instrument kind, &#x60;\&quot;future\&quot;&#x60; or &#x60;\&quot;option\&quot;&#x60; | 
**mark_price** | **float** | Current mark price for position&#39;s instrument | 
**average_price** | **float** | Average price of trades that built this position | 
**settlement_price** | **float** | Last settlement price for position&#39;s instrument 0 if instrument wasn&#39;t settled yet | 
**index_price** | **float** | Current index price | 
**instrument_name** | **str** | Unique instrument identifier | 
**size_currency** | **float** | Only for futures, position size in base currency | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


