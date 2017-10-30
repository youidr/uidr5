# coding: utf-8
import urllib.request
import json
key = '010f9a4ad93e4d8ca8f94eb0d071f101'
api = 'http://www.tuling123.com/openapi/api'
test_data = {'key':key}
test_data['info'] = '你是谁'
test_data_urlencode = urllib.parse.urlencode(test_data).encode('utf-8')
req = urllib.request.Request(url = api,data =test_data_urlencode)
res_data = urllib.request.urlopen(req)
res = res_data.read()
dic_json = json.loads(res)
msg = dic_json['text']
print(msg)
