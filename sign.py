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

# the secret will be found in the credientail section of IAM
# The date should be same as that in policy and all other things
key = '<secret access key>'
dateStamp = '20200914'
regionName = 'ap-south-1'
serviceName = 's3'
sign = getSignatureKey(key, dateStamp, regionName, serviceName)
kSign = signA(sign,'<string to sign>')
print(kSign)
