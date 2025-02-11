sync:
	uv sync
	
installme:
	uv pip install -e .

test:
	uv run pytest      


.PHONY: sync test installme
