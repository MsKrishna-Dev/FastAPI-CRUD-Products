import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "data" / "dummy.json"
 
def load_data() ->List[Dict]:
    if not DATA_FILE:
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def get_all_products() -> List[Dict]:
    return load_data()