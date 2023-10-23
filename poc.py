from Cryptodome.PublicKey import RSA
import requests
from bs4 import BeautifulSoup

nid_login_url = 'https://nid.naver.com/nidlogin.login?url=https://clova-x.naver.com/'

sk = ""
def lenchar(a: str):
    return chr(len(a))

def enc_pw(id, pw):
    sess = requests.session()
    data = sess.get(nid_login_url)

    soup = BeautifulSoup(data.text, 'lxml')

    dynamicKey  = soup.find('input', id= 'dynamicKey').attrs['value']


    data = sess.get(f'https://nid.naver.com/dynamicKey/{dynamicKey}')
    sessionKeys = data.text.split(",")


    sk = sessionKeys[0]
    env_nm = sessionKeys[1]
    pub_e = int(sessionKeys[2], 16)
    pub_n = int(sessionKeys[3], 16)

    ## TODO
    # genereate uuid 
    fuck = """{"a":"38a52ed5-b711-47c7-9916-5cc12b7abad6-0","b":"1.3.9","c":false,"d":[{"i":"id","a":["0,d,i0,65","18,d,i1,83","34,d,i2,68","63,d,i3,70","19,u,i0,65","27,u,i1,83","91,u,i2,68","106,u,i3,70"],"b":{"a":["0,a","15,as","34,asd","65,asdf"],"b":3},"c":"","d":"asdf","e":false,"f":false},{"i":"pw","a":["0,d,i0,","12,d,i1,","32,d,i2,","31,u,i0,","103,u,i1,","132,u,i2,"],"b":{"a":["0,","11,","33,"],"b":2},"c":"","d":"","e":true,"f":false}],"e":{"a":{"a":444,"b":444,"c":444},"b":{"a":444,"b":444,"c":444}},"f":{"a":{"a":{"a":444,"b":444,"c":444},"b":{"a":444,"b":444,"c":444}},"b":{"a":{"a":444,"b":444,"c":444},"b":{"a":444,"b":444,"c":444}}},"g":{"a":["0|2|587|41","0|1|0|-1","0|8|0|-2","0|21|0|-2","0|9|0|-1","0|89|0|-2","0|29|0|-1","0|37|0|-1","0|6|0|-1","0|81|-2|0","0|16|-1|3","0|16|-2|7","0|2224|-148|297","0|8|-17|1","0|8|-10|1","0|8|-4|0","0|8|-1|0","0|106|3|0","0|7|3|-6","0|8|5|-7","0|8|4|-7","0|9|5|-8","0|7|3|-5","0|8|2|-5","0|8|4|-6","0|9|1|-2","0|7|1|-4","0|8|1|-2","0|9|0|-2","0|15|0|-1","0|16|0|-1","0|24|0|-1","1|67|0|0","0|6|0|0","2|94|0|0","0|48|-1|-1","0|48|-1|0","0|16|0|3","0|8|0|9","0|8|0|10","0|9|0|8","0|8|0|8","0|9|0|5","0|11|2|6","0|4|0|3","0|8|1|2","0|7|2|2","0|8|0|1","0|7|1|1","0|77|2|0","0|6|0|-1","0|9|0|-1","0|7|1|-4","0|7|3|-3","0|8|0|-1","0|7|1|-3","0|8|1|-2","0|8|1|-1","0|8|0|-1","1|101|0|0","2|107|0|0","0|48|0|4","0|8|1|9","0|8|1|8","0|8|1|8","0|8|3|10","0|8|2|10","0|8|4|8","0|8|4|9","0|8|2|5","0|8|4|9","0|8|2|6","0|8|3|5","0|8|2|9","0|8|4|7","0|9|1|3","0|8|2|6","0|8|1|3","0|9|1|3","0|7|0|1","0|10|0|3","0|6|2|2","0|9|0|1","0|7|0|1","0|8|0|2","0|17|1|0","0|48|0|1","0|15|0|2","0|8|0|1","0|8|0|2","0|16|0|1","0|17|0|2","0|40|0|1","0|24|0|2","0|8|0|1","0|24|0|2","1|60|0|0","2|114|0|0"],"b":97,"c":488,"d":469,"e":4170,"f":0},"j":100,"h":"1248c886fb7bbabd96716fd5be065d30","i":{"a":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36","b":"ko-KR","c":24,"d":1,"e":1,"f":5,"g":[1075,1010],"h":[1075,1010],"i":-540,"j":1,"k":1,"l":1,"z":1,"m":"unknown","n":"Win32","o":"unknown","aa":["1iZMOHL::Puf2j4FCgQIECozZzCBfXyZz4k5kx3j::~q0i","com.adobe.pdf Display::Portable Document Format::application/x-google-chrome-pdf~pdf","268eu2Eh::AIr0iZMOHLkaVKs9eu26GDJEKFpUSRQv::~gQI","Browser Portable Document Format Plugin::::application/pdf~pdf"],"p":"d439a64af4188c27587a1438882301f1","q":"a23202eedc8f949c89d7994eae76d3ed","r":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) UHD Graphics 630 (0x00003E92) Direct3D11 vs_5_0 ps_5_0, D3D11)","s":false,"t":false,"u":false,"v":false,"w":false,"x":[0,false,false],"aca":"x86","acb":"","acc":"64","acd":"Windows","ace":"10.0.0","acf":"118.0.0.0","acg":["{\\"brand\\":\\"Chromium\\",\\"version\\":\\"118.0.0.0\\"}","{\\"brand\\":\\"Brave\\",\\"version\\":\\"118.0.0.0\\"}","{\\"brand\\":\\"Not=A?Brand\\",\\"version\\":\\"99.0.0.0\\"}"],"ach":false,"aci":false,"ad":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36","ae":"true","af":"true","ak":"default|prompt","ag":"1","aj":"1075|1010","ah":"false","ai":"","am":"landscape","an":"false","al":"","y":["Arial","Arial Black","Arial Narrow","Calibri","Cambria","Cambria Math","Comic Sans MS","Consolas","Courier","Courier New","Georgia","Helvetica","Impact","Lucida Console","Lucida Sans Unicode","Microsoft Sans Serif","MS Gothic","MS PGothic","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times New Roman","Trebuchet MS","Verdana","Wingdings"]}}"""
    #replace fuck uuid
    # lzstring bscz
    print(pub_e, pub_n)
    rsa = RSA.RsaKey(e = pub_e, n = pub_n)
    encpw = lenchar(sk) + sk + lenchar(id) + id + lenchar(pw) + pw
    enc = rsa.export_key(format="DER", passphrase=encpw)
    print("\nhex\n")
    print(enc)


# SetCookie on Success!








