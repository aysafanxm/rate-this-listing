import json

request_keys = []

with open('./requestkeys.txt', 'rb') as f:
    for l in f:
        l = l.strip().split('=')[0]
        request_keys.append(l)

# print request_keys
d = {
    'props': [],
    'amens': [],
    'neighbs': [],
    'bedtypes': [],
    'roomtypes': [],
    'cancels': [],
    'resps': [],
}

for r in request_keys:
    if 'property_' in r:
        d['props'].append(r)
    elif 'amenities_' in r:
        d['amens'].append(r)
    elif 'neighbourhood_' in r:
        d['neighbs'].append(r)
    elif 'bed_type_' in r:
        d['bedtypes'].append(r)
    elif 'room_type_' in r:
        d['roomtypes'].append(r)
    elif 'cancellation_policy_' in r:
        d['cancels'].append(r)
    elif 'host_response_' in r:
        d['resps'].append(r)
    else:
        print r

for k, v in d.items():
    fname = k+'_props.json'
    with open(fname, 'wb') as f:
        f.write(json.dumps(v))