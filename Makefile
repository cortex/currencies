default: currencies.json

iso4217.xml:
	curl http://www.currency-iso.org/dam/downloads/lists/list_one.xml > iso4217.xml

cldr_root.xml:
	curl http://unicode.org/repos/cldr/tags/release-28/common/main/root.xml > cldr_root.xml

currencies.json: iso4217.xml cldr_root.xml
	python3 currencies.py > currencies.json

clean:
	rm iso4217.xml cldr_root.xml currencies.json

