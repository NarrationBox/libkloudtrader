install:
	pipenv install --dev

lint:
	pipenv run pylint libkloudtrader

format:
	pipenv run yapf -i --recursive libkloudtrader

test:
	pipenv run pytest -s -v tests/test_stocks.py

git:
	pipenv run yapf -i --recursive libkloudtrader
	git add -A
	git commit -m "$(message)"
	git push

safe:
	pipenv run safety check

typecheck:
	pipenv run pyre --source-directory libkloudtrader check

run:
	pipenv run python algo.py

tox:
	pipenv run tox

algo:
	pipenv run python algo.py
