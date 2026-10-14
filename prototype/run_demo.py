from pathlib import Path
import json
import hashlib
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prototype.src.validation import load_inputs
from prototype.src.baseline import baseline
from prototype.src.optimizer import allocate
from prototype.src.metrics import metrics
from prototype.src.reporting import write_report

ROOT = Path(__file__).resolve().parent

def main():
    stock, demand = load_inputs(ROOT/'data/synthetic_stock.csv', ROOT/'data/synthetic_demand.csv', ROOT/'data/synthetic_offcuts.csv')
    result = {'synthetic': True, 'schema_version': 1, 'algorithm_version': '1.0',
              'input_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'data').glob('*.csv'))},
              'kerf_mm': 3, 'min_reusable_mm': 500, 'plans': {}}
    for name, plan in [('baseline', baseline(stock, demand)), ('assisted', allocate(stock, demand))]:
        result['plans'][name] = {'plan': plan, 'metrics': metrics(stock, plan)}
        print(name + ': ' + json.dumps(result['plans'][name]['metrics'], sort_keys=True))
    write_report(ROOT/'results/demo.json', result)
    print('Synthetic demonstration only. No cash savings or production feasibility established.')

if __name__ == '__main__':
    main()
