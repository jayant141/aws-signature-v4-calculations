import hmac
import hashlib

def signA(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).hexdigest()

def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning
    
key = '51xdlikN46zil/fxY9n5nJ44Dz/DDn394LR1vd3v'
dateStamp = '20200914'
regionName = 'ap-south-1'
serviceName = 's3'
sign = getSignatureKey(key, dateStamp, regionName, serviceName)
kSign = signA(sign,'eyAiZXhwaXJhdGlvbiI6ICIyMDIwLTA5LTE0VDEyOjAwOjAwLjAwMFoiLA0KICAiY29uZGl0aW9ucyI6IFsNCiAgICB7ImJ1Y2tldCI6ICJqYXlhbnRwcm9qZWN0In0sDQogICAgWyJzdGFydHMtd2l0aCIsICIka2V5IiwgInByb2plY3QvdXBsb2Fkcy8iXSwNCiAgICB7ImFjbCI6ICJwdWJsaWMtcmVhZCJ9LA0KICAgIHsic3VjY2Vzc19hY3Rpb25fcmVkaXJlY3QiOiAiaHR0cHM6Ly9qYXlhbnRwcm9qZWN0LnMzLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbS93ZWJzaXRlL3N1Y2Nlc3NmdWxfdXBsb2FkLmh0bWwifSwNCiAgICBbInN0YXJ0cy13aXRoIiwgIiRDb250ZW50LVR5cGUiLCAiaW1hZ2UvIl0sDQogICAgeyJ4LWFtei1tZXRhLXV1aWQiOiAiMTQzNjUxMjM2NTEyNzQifSwNCiAgICB7IngtYW16LXNlcnZlci1zaWRlLWVuY3J5cHRpb24iOiAiQUVTMjU2In0sDQogICAgWyJzdGFydHMtd2l0aCIsICIkeC1hbXotbWV0YS10YWciLCAiIl0sDQoNCiAgICB7IngtYW16LWNyZWRlbnRpYWwiOiAiQUtJQVFTS1dDNjNIM0tLVkRGN1EvMjAyMDA5MTQvYXAtc291dGgtMS9zMy9hd3M0X3JlcXVlc3QifSwNCiAgICB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sDQogICAgeyJ4LWFtei1kYXRlIjogIjIwMjAwOTE0VDAwMDAwMFoiIH0NCiAgXQ0KfQ==')
print(kSign)