import http.client
conn = http.client.HTTPConnection("perencanaan.unhas.ac.id:8080")
conn.request("GET", "/login")
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()
print(data)