"""
Minimal Python solution example following the platform contract.

Contract:
  - Reads /run/input.json to get input data.
  - Prints a single JSON object to stdout.
  - Must complete within 10 seconds.
  - No network access is available.

This example: sums all numeric values in the input JSON.
"""

import json
import sys


def solve(data: dict) -> dict:
    """Add all numeric values found at the top level of the input dict.

    Args:
        data: Parsed input JSON.

    Returns:
        Dict with 'sum' key and the computed total.
    """
    total = sum(v for v in data.values() if isinstance(v, (int, float)))
    return {"sum": total, "input_keys": list(data.keys())}


def main() -> None:
    with open("/run/input.json") as f:
        data = json.load(f)
    result = solve(data)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
