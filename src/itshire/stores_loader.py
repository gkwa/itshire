import importlib.resources
import json
import logging


def load_stores() -> list[str]:
    data = importlib.resources.files("itshire.data").joinpath("stores.json").read_text()
    parsed = json.loads(data)
    stores = [entry["name"] for entry in parsed.get("stores", [])]
    logging.debug(f"Loaded {len(stores)} stores from heatedhornet data")
    return stores
