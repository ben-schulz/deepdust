watch:
	. env/bin/activate && python3 deepdust/test/watcher.py --project deepdust deepdust/jsonld deepdust/io deepdust/test --tests deepdust/test --pattern test_*.py

test:
	. env/bin/activate && python3 -m unittest discover -s deepdust/test -p "test_*.py"

.PHONY: test watch
