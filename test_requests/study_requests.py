import requests

# param = {"shouji":"13456755448","appkey":"0c818521d38759e1"}
# resp = requests.get(url = "http://api.binstd.com/shouji/query",params=param)
# print(resp.status_code)
# print(resp.headers)
# print(resp.json())

# params传参
# param = {
#     "word":"hello",
#     "lang":"en"
# }
# re = requests.get(url="http://youdao.com/result",params=param)
# print(re.headers)
# print(re.text)

# 表单传参关键字data
# resp = requests.post(url = "https://dict.youdao.com/keword/key",data={"text":"hello"})
# print(resp.status_code)
# print(resp.headers)

# 有请求头
def test_get_douban():
    url = "https://m.douban.com/rexxar/api/v2/movie/36766358/verify_users"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "referer": "https://movie.douban.com/subject/36766358/"
    }
    param = {
        "start": 0,
        "count": 2,
        "ck": ""
    }
    resp = requests.get(url=url, params=param, headers=header)
    json_data = resp.json()
    assert resp.status_code == 200
    assert json_data['count'] == 2
    assert json_data['start'] ==0
    assert json_data.get('total') == 0
    assert json_data.get('verify_users') == []

