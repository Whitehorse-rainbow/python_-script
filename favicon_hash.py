import mmh3
import requests
response = requests.get('https://baidu.com/favicon.ico')
favicon = response.content.encode('base64')
hash = mmh3.hash(favicon)
print 'http.favicon.hash:'+str(hash)

#需要mmh3，microsoft visual c++ 9.0以上
#https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi
