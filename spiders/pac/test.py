import requests
import urllib3
urllib3.disable_warnings()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Host': 'epay.ecnu.edu.cn',
    'charset': 'utf-8',
    'xweb_xhr': '1',
    'sw-Authorization': '',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx8baadd3d2289f1a7/13/page-frame.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
me_data = '{}'
elc_data = '{"elcsysid":1,"areaid":"1","roomid":"8415_ZB_15_138","buildid":"new-15_ZB"}'
token_data = '{"custname":"","stuempno":"10224804419","code":"0c3cay100hhwYQ1ZqH200aK4RZ1cay1R","paypwd":"wangbangbang666.","model":"microsoft"}'

token_response = requests.post('https://epay.ecnu.edu.cn/openservice/wechatauth/bindaccount', headers=headers, data=token_data, verify=False)
token = token_response.json()['data']['token']
headers['sw-Authorization'] = token
print(token)
# me_response = requests.post('https://epay.ecnu.edu.cn/openservice/miniprogram/wxlayout', headers=headers, data=me_data, verify=False)
# elc_response = requests.post('https://epay.ecnu.edu.cn/openservice/miniprogram/queryroominfo', headers=headers, data=elc_data, verify=False)
# now_elc = elc_response.json()['data']['restElecDegree']
# buy_elc_data = '{"elcsysid":1,"areaid":"102","roomid":"8415_ZB_15_138","buildid":"new-15_ZB","roomname":"用电缴费，楼宇名称：中北8舍，房间号：8415房间，缴费前电量：'+f'{now_elc}'+'度","amount":100}'
# print(buy_elc_data)