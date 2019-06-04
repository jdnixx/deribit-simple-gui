# Settlement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_profit_loss** | **float** | total value of session profit and losses (in base currency) | 
**mark_price** | **float** | mark price for at the settlement time (in quote currency; settlement and delivery only) | [optional] 
**funding** | **float** | funding (in base currency ; settlement for perpetual product only) | 
**socialized** | **float** | the amount of the socialized losses (in base currency; bankruptcy only) | [optional] 
**session_bankrupcy** | **float** | value of session bankrupcy (in base currency; bankruptcy only) | [optional] 
**timestamp** | **int** | The timestamp (seconds since the Unix epoch, with millisecond precision) | 
**profit_loss** | **float** | profit and loss (in base currency; settlement and delivery only) | [optional] 
**funded** | **float** | funded amount (bankruptcy only) | [optional] 
**index_price** | **float** | underlying index price at time of event (in quote currency; settlement and delivery only) | 
**session_tax** | **float** | total amount of paid taxes/fees (in base currency; bankruptcy only) | [optional] 
**session_tax_rate** | **float** | rate of paid texes/fees (in base currency; bankruptcy only) | [optional] 
**instrument_name** | **str** | instrument name (settlement and delivery only) | 
**position** | **float** | position size (in quote currency; settlement and delivery only) | 
**type** | **str** | The type of settlement. &#x60;settlement&#x60;, &#x60;delivery&#x60; or &#x60;bankruptcy&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


