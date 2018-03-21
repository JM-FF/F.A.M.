import sys
import os
dir_path = str(os.path.dirname(os.path.realpath(__file__)))
dir_path = dir_path[:-7]
sys.path.insert(0, dir_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'FAM.settings'
import django
django.setup()
from sources.models import StockExchange, OptionExchange, CryptoExchange


""" Add all stock exchanges to StockExchange Database """
def add_stockExchange(name, code):
    exchange = StockExchange()
    exchange.name = name
    exchange.code = code
    exchange.save()

stock_exchanges = StockExchange.objects.all()
exchanges = list((item.name for item in stock_exchanges))

if "NYSE MKT" not in exchanges:
    add_stockExchange("NYSE MKT","A")

if "NASDAQ OMX BX" not in exchanges:
    add_stockExchange("NASDAQ OMX BX","B")

if "National Stock Exchange" not in exchanges:
    add_stockExchange("National Stock Exchange","C")

if "FINRA ADF" not in exchanges:
    add_stockExchange("FINRA ADF","D")

if "Market Independent (Generated by Nasdaq SIP)" not in exchanges:
    add_stockExchange("Market Independent (Generated by Nasdaq SIP)", "E")

if "Mutual Funds/Money Markets (NASDAQ)" not in exchanges:
    add_stockExchange("Mutual Funds/Money Markets (NASDAQ)","F")

if "International Securities Exchange" not in exchanges:
    add_stockExchange("International Securities Exchange","I")

if "Direct Edge A" not in exchanges:
    add_stockExchange("Direct Edge A","J")

if "Direct Edge X" not in exchanges:
    add_stockExchange("Direct Edge X","K")

if "Chicago Stock Exchange" not in exchanges:
    add_stockExchange("Chicago Stock Exchange","M")

if "NYSE" not in exchanges:
    add_stockExchange("NYSE","N")

if "NYSE Arca" not in exchanges:
    add_stockExchange("NYSE Arca","P")

if "NASDAQ OMX" not in exchanges:
    add_stockExchange("NASDAQ OMX","Q")

if "NASDAQ Small Cap" not in exchanges:
    add_stockExchange("NASDAQ Small Cap","S")

if "NASDAQ Int" not in exchanges:
    add_stockExchange("NASDAQ Int","T")

if "OTCBB" not in exchanges:
    add_stockExchange("OTCBB","U")

if "OTC other" not in exchanges:
    add_stockExchange("OTC other","V")

if "CBOE" not in exchanges:
    add_stockExchange("CBOE","W")

if "NASDAQ OMX PSX" not in exchanges:
    add_stockExchange("NASDAQ OMX PSX","X")

if "GLOBEX" not in exchanges:
    add_stockExchange("GLOBEX","G")

if "BATS Y-Exchange" not in exchanges:
    add_stockExchange("BATS Y-Exchange","Y")

if "BATS" not in exchanges:
    add_stockExchange("BATS","Z")


""" Add all option exchanges to OptionExchange Database """
def add_optionExchange(name, code):
    exchange = OptionExchange()
    exchange.name = name
    exchange.code = code
    exchange.save()

option_exchanges = StockExchange.objects.all()
exchanges = list((item.name for item in option_exchanges))

if "NYSE Amex Options" not in exchanges:
    add_optionExchange("NYSE Amex Options","A")

if "BOX Options Exchange" not in exchanges:
    add_optionExchange("BOX Options Exchange","B")

if "CBOE" not in exchanges:
    add_optionExchange("CBOE","C")

if "ISE Gemini" not in exchanges:
    add_optionExchange("ISE Gemini","H")

if "ISE" not in exchanges:
    add_optionExchange("ISE","I")

if "MIAX Options Exchange" not in exchanges:
    add_optionExchange("MIAX Options Exchange","M")

if "NYSE Arca Options" not in exchanges:
    add_optionExchange("NYSE Arca Options","N")

if "OPRA" not in exchanges:
    add_optionExchange("OPRA","O")

if "MIAX PEARL" not in exchanges:
    add_optionExchange("MIAX PEARL","P")

if "NASDAQ Options Market" not in exchanges:
    add_optionExchange("NASDAQ Options Market","Q")

if "NASDAQ OMX BX" not in exchanges:
    add_optionExchange("NASDAQ OMX BX","T")

if "C2 Options Exchange" not in exchanges:
    add_optionExchange("C2 Options Exchange","W")

if "NASDAQ OMX PHLX" not in exchanges:
    add_optionExchange("NASDAQ OMX PHLX","X")

if "BATS Options Market" not in exchanges:
    add_optionExchange("BATS Options Market","Z")


""" Add all cryptocurrency exchanges to CryptoExchange Database """
def add_cryptoExchange(name):
    exchange = CryptoExchange()
    exchange.name = name
    exchange.save()

crypto_exchanges = CryptoExchange.objects.all()
exchanges = list((item.name for item in crypto_exchanges))

if "HitBTC" not in exchanges:
    add_cryptoExchange("HitBTC")

if "Coinbase" not in exchanges:
    add_cryptoExchange("Coinbase")

if "Gemini" not in exchanges:
    add_cryptoExchange("Gemini")

if "Poloniex" not in exchanges:
    add_cryptoExchange("Poloniex")
