import requests
import ddddocr

ocr = ddddocr.DdddOcr()
url = 'http://epay.ecnu.edu.cn/epay/person/index'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "epay.ecnu.edu.cn",
    "sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "sec-Ch-Ua-Mobile": "?0",
    "sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
session = requests.Session()
response = session.get(url, headers=headers, verify=False)
img_content = session.get(f'https://epay.ecnu.edu.cn/epay/codeimage;jsessionid={response.cookies["JSESSIONID"]}', headers=headers, verify=False)
#response = requests.get(url, headers=headers, verify=False)
print(response.headers)
print(response.text)
#BIGipServerpool_202.120.92.161_80=2707192010.20480.0000
# with open('captcha.png', 'wb') as f:
#     f.write(img_content.content)
# with open('captcha.png', 'rb') as f:
#     img_bytes = f.read()
# res = ocr.classification(img_bytes)

# def get_answer(res):
#     if'+' or '十' in res:
#         zhi =  int(res[0])+int(res[1])
#     if'-' or '一' in res:
#         zhi =  int(res[0])-int(res[1])
#     if'x'in res:
#         zhi =  int(res[0])*int(res[1])
#     if'÷'in res:
#         zhi =  int(res[0])/int(res[1])
#     return zhi
# try:
#     answer = get_answer(res)
# except:
#     answer = 0
# print(answer)