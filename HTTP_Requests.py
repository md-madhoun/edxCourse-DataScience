import requests
import os 
from PIL import Image
from IPython.display import IFrame

'''
url='https://flash-toons.com'
r=requests.get(url)
print(r.status_code)
print(r.request.headers)
print("request body:", r.request.body)
header=r.headers
print(r.headers)
print(header['date'])
print(header['Content-Type'])
print( r.encoding)
print(r.text[0:100])

'''



for i in range(0,50):
    url_post='https://english.flash-toons.com/contact/#contact-form-197'
    payload={"g197-name":"MohD","g197-email":"mm@mm.com","g197":"Boddddy","contact-form-id":"197","action":"grunion-contact-form","contact-form-hash":"d8dc1fa6df5ed9ba1a999c4df567d298c63fe91b"}
    r_post=requests.post(url_post,data=payload)
    print(r_post.status_code)
    print("POST request URL:",r_post.url )
    print("POST request body:",r_post.request.body)
    #r_post.json()['form']
    i=i+1