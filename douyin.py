import  json

def response(flow):
    if 'http://aaaa' in flow.request.url:
       res = json.load(flow.response.text)
       print(res)