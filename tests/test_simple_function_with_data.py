import json
from pathlib import Path

import numpy as np

from ees_scientific_software_engineering.simple_function import multiply, rmse

DATA_PATH = Path(__file__).parent / "data"


def test_multiply_from_data():
    with open(DATA_PATH / "test_multiply.json") as f:
        data = json.load(f)
    assert multiply(data["x"], data["y"]) == data["expected"]


def test_rmse_from_data():
    with open(DATA_PATH / "test_rmse.json") as f:
        data = json.load(f)
    assert rmse(np.array(data["x"], dtype=np.float64)) == data["expected"]
