import urllib.request
import json
import time

url = 'https://marupulgasstore-default-rtdb.firebaseio.com/maru_store/products.json'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read())

items = data.get('items', [])
seen_ids = set()
for i, item in enumerate(items):
    if not item:
        continue
    if 'id' not in item or item['id'] in seen_ids:
        # Give it a new unique id
        new_id = int(time.time() * 1000) + i
        item['id'] = new_id
        seen_ids.add(new_id)
    else:
        seen_ids.add(item['id'])

data['items'] = items
data['_ts'] = int(time.time() * 1000)

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), method='PUT')
req.add_header('Content-Type', 'application/json')
with urllib.request.urlopen(req) as response:
    print("Successfully updated database. Response:", response.read().decode('utf-8')[:100])
