import json
from pathlib import Path


def write_report(path, result):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(result, indent=2, sort_keys=True), encoding='utf-8')
