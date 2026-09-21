import json, ssl, urllib.parse, urllib.request

BASE = "https://cthru.data.socrata.com/resource/pegc-naaa.json"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

def q(dataset=None, **params):
    base = BASE if dataset is None else BASE.replace("pegc-naaa", dataset)
    url = base + "?" + urllib.parse.urlencode({("$" + k if k in
          ("select","where","group","order","limit","offset","q","having") else k): v
          for k, v in params.items()})
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
        return json.loads(r.read().decode())

def f(x):
    try: return float(x)
    except (TypeError, ValueError): return 0.0
