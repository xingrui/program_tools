import urlparse
import base64
U='net.rayjump.com/request?p=eyJzbnIiOiJpbnRlcnN0aXRpYWwiLCJvdCI6MSwibnQiOjIsInNuIjoiMDU2MmIzOWE2MDhmMTg1%0AOWNmZjE2MThkZTQxNDcxYTEiLCJvdiI6IjQuNC4yIiwibWNjIjoiNDA1IiwiYXQiOiJmdWxsX3Nj%0AcmVlbiIsImRpZCI6IjFiOTQ5YjFjYjlhZWM3ODUiLCJsIjoiZW4iLCJtYWMiOiIwMDI3MTU4OTQ5%0AMzIiLCJhaWQiOjEsImltIjoiOTExNDI3NTAyNzU0NDk1Iiwidm4iOiIyLjAiLCJwZiI6ImFuZHJv%0AaWQiLCJ0eiI6IkdNVCswNTozMCIsInQiOiIxNDU2MjQ5OTUxIiwiYW4iOjEsImRtIjoiQTM1OSIs%0AInVhIjoiTW96aWxsYVwvNS4wIChMaW51eDsgQW5kcm9pZCA0LjQuMjsgQTM1OSBCdWlsZFwvS09U%0ANDlIKSBBcHBsZVdlYktpdFwvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvblwvNC4w%0AIENocm9tZVwvMzAuMC4wLjAgTW9iaWxlIFNhZmFyaVwvNTM3LjM2Iiwic3YiOiJTQS4xLjQuMSIs%0AIm1uYyI6IjgxOSIsInNzIjoiMzIweDQ4MCIsInZjIjozLCJwbiI6ImNvbS5seWgucG9wYmlyZCJ9%0A'
res=urlparse.urlparse(U)
#print res
params = urlparse.parse_qs(res.query,True) 
p = params['p'][0]
print base64.decodestring(p)
