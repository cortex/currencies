import xml.etree.ElementTree as ET
import json
import sys

def na_to_none(v):
    return None if v == "N.A." else v

def maybe_int(v):
    return v if not v else int(v)

iso4217_XML = ET.parse('iso4217.xml')
symbols_XML = ET.parse('cldr_root.xml')
countries = []
symbols = {}
currencies = []

for currency in symbols_XML.findall("./numbers/currencies/currency"):
    symbol = currency.findtext("./symbol[@alt='narrow']")
    symbols[currency.attrib["type"]] = symbol

for country in iso4217_XML.findall("./CcyTbl/CcyNtry"):
    code = country.findtext("Ccy")
    countries.append({
        "Country": country.find("CtryNm").text,
        "Name": country.find("CcyNm").text,
        "Code": code,
        "Number": maybe_int(country.findtext("CcyNbr")),
        "MinorUnits": maybe_int(na_to_none(country.findtext("CcyMnrUnts"))),
        "Symbol": symbols.get(code)
    })

with open("countries.json", "wt") as currencies_file:
    currencies_file.write(json.dumps(countries, indent=4, ensure_ascii=False))

with open("currencies.json", "wt") as currencies_file:
    currencies_file.write(json.dumps(countries, indent=4, ensure_ascii=False))
