from requests import get as GET
response = GET('http://3ss.mobvista.com/offer/orm?id=486223', params =  {"client_id": "qXJSJzzsGDPdYXR1"}, headers =  {"Authorization": "Basic Ozg5P5nB8qegPBhH"})
print response.content
