import http.client
conn = http.client.HTTPSConnection("www.bni.co.id")
conn.request("GET", "/id-id/")
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()
print(data)