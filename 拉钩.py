import requests
headers = {
    'cookie': 'user_trace_token=20200829101658-87b893ea-ad53-4a96-bfe3-7055742fd90c; _ga=GA1.2.133606921.1598667419; _gat=1; LGSID=20200829101659-d97eb940-5df1-4192-b3cb-5df46fe30121; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.0f0000KqJzKxxTI7ioUDgcmId1Y%5F7ReadBtk3iV1PTdHHh5vNkF-Bl1Ni0xGu7xbUHLVJj83wGJbtxPLWuY-nZPrIUkQHrfMARELT7reJaGwhnF6P0bkuabNdiTiAlUbCgnZQADvH6LZCEsiGORGEPuMJRhWGLUcdSXqcH9kMSTGMbyIyj2aJz-nlKqQSREQvCWD7VvgpotAzPdMh2evxSUam844.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqnfKdThkxpyfqnHRznjfYP1fzr0KVINqGujYkn104PH6YnfKVgv-b5HDsP1czP1T30AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KGuAnqiDFK0APzm1YkrH0LPs%26ck%3D4741.1.91.312.161.308.154.209%26dt%3D1598667416%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tpl%3Dtpl%5F11534%5F22836%5F18980%26l%3D1520447428%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; LGUID=20200829101659-0c59ba73-84e2-4407-87f9-9b11997f2b99; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1598667419; _gid=GA1.2.1063917841.1598667433; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22174380123973e8-00bb604a809804-3323766-1327104-1743801239895%22%2C%22%24device_id%22%3A%22174380123973e8-00bb604a809804-3323766-1327104-1743801239895%22%7D; sajssdk_2015_cross_new_user=1; gate_login_token=fdc41f1dcef165da9959a0df6afa7b41c3b302d4c8e9ef07657356aa9b72c806; LG_LOGIN_USER_ID=59f6cc27c1214d833e64dd94cb1ca95448a88409d999cd340276c38440d1fbe6; LG_HAS_LOGIN=1; _putrc=F9B4A98F0354C9AA123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABIIA39DA5E959BDE0786AB2D5D364F6FDB1; login=true; unick=%E5%B4%94%E6%B5%A9; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=27; privacyPolicyPopup=false; WEBTJ-ID=20200829101748-1743801b0291ed-01b1c3863bc155-3323766-1327104-1743801b02a1e5; RECOMMEND_TIP=true; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; SEARCH_ID=b3592d3ed69240a695d87737dc55120b; X_HTTP_TOKEN=6aaf4a512e8e81f21847668951f5aa63ab59a6b25d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1598667481; LGRID=20200829101826-715fc302-b672-496f-8699-4a9a0826351b',
    #实时cookies
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
# for num in range(1,7):
data = {
    'first': 'false',
    'pn': '1',
    #表示页码，多少页遍历多少次即可
    'kd': '爬虫',
    #搜索关键字
    'sid': '9502bd049e95499c87a5ebdb7fa600d0',
}
res = requests.post(url,headers=headers,data=data).json()
msg_list = res["content"]["positionResult"]["result"]
for item in msg_list:
    name = item["positionName"]
    company = item["companyShortName"]
    time = item["createTime"]
    addr = item["linestaion"]
    salary = item["salary"]
    size = item["companySize"]
    print(name,company,time,addr,salary,size)