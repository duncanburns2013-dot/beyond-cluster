import json, ssl, urllib.parse, urllib.request

BASE = "https://cthru.data.socrata.com/resource/pegc-naaa.json"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

def q(**params):
    url = BASE + "?" + urllib.parse.urlencode({("$" + k if k in
          ("select","where","group","order","limit","offset","q","having") else k): v
          for k, v in params.items()})
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
        return json.loads(r.read().decode())

def f(x):
    try: return float(x)
    except (TypeError, ValueError): return 0.0
