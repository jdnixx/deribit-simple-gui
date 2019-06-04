# Currency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_confirmations** | **int** | Minimum number of block chain confirmations before deposit is accepted. | [optional] 
**min_withdrawal_fee** | **float** | The minimum transaction fee paid for withdrawals | [optional] 
**disabled_deposit_address_creation** | **bool** | False if deposit address creation is disabled | [optional] 
**currency** | **str** | The abbreviation of the currency. This abbreviation is used elsewhere in the API to identify the currency. | 
**currency_long** | **str** | The full name for the currency. | 
**withdrawal_fee** | **float** | The total transaction fee paid for withdrawals | 
**fee_precision** | **int** | fee precision | [optional] 
**withdrawal_priorities** | [**list[CurrencyWithdrawalPriorities]**](CurrencyWithdrawalPriorities.md) |  | [optional] 
**coin_type** | **str** | The type of the currency. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


