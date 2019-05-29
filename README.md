# Deribit Simple Gui

## Description

An experimental GUI interface, with a few useful features, for cryptocurrency trading on [Deribit.](https://www.deribit.com)

Uses Deribit API v1. (soon to be deprecated; need to integrate v2 eventually)

Deribit API docs:
https://www.deribit.com/docs/api/

### Usage

The program is started from any of the `starter.py` files.

Modify the variables `path_to_keyfile` and  `market` inside
it, to set the relative path to the .txt file containing your API keys, and your desired perpetual contract,
respectively:
```
path_to_keyfile = './deribit_keys.txt'     # see ordermanger_interface.py for API key syntax
market = 'btc'                             # either 'btc' or 'eth'
```

The example above starts the program for the BTC-PERPETUAL swap instrument, using API keys in `deribit_keys.txt`,
located in the same (root) directory.

### Keyfile

The contents of your keyfile should be 2 separate lines. On the first is your API key, and the second, your API secret.
```
ABzGtz9QGVeN
URT2ZLHGG6WTK6XZWKTVZSJLQCXZES46
test
```
For use on the [testnet](https://www.test.deribit.com), add a third line containing only the text `test` (as in 
above example).

For live usage, leave the third line off completely.