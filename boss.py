import requests
import lxml.etree
import time
import csv
csv_file = open('./boss_msg.csv','a',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['职位名称','公司名称','公司信息','薪资','经验要求','jd详情'])
headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip,deflate,br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Host":"www.zhipin.com",
    "Cookie":"t=0GuYnMvn5Ir753Dh; wt=0GuYnMvn5Ir753Dh; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1598354465,1598365985,1598422177,1598665954; lastCity=100010000; __c=1598665953; __l=l=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E7%25AB%259E%25E5%2593%2581%26unit%3D%25E6%2599%25BA%25E8%2581%2594-2%26keyword%3Dwww.hugoboss.cn%26bd_vid%3D4645570595134235086%26csource%3Dboctb&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0f00000uEDLSpLgiC9xwq8G9koHQv3EkSelv7H47z47uonxpHOs2mETEPOQazPGmwSpvUurfQkgdPx3htCW0Ju0PlM6xtEBMHnPZaKEKz9FMiOIdyQYi7QMCQNs_zOVA-p78_8hyS4tixdoE6wWBq9gAm1ZyeRuWxWz0IWmj-4nCwAZ2v2X5-jQTYgTb3EAByTJBCpOLUtip_11pTdA8q8CgOWrR.Db_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMks4OgSWS534Oqo4yunOogEOtZV_zyUr1oWC_knmx5u9qVXZutrZ1en5o_seOU9tqvZvSXZxeT5MY3IMVseqvxj4SrZvS8Zx43x5I9LtTrzEo6BxfmsSxH9Let5oeT5M_se2trO_14rEpMwsrh8m3rj6tJ_AGdeC3SHojAeKPa-BqYPaOonh4tzmpj7Na9WWOqmcrj635Q9JxWxDBaPrha81hGyAp7WGzu2e70.U1Yk0ZDqmhq1TsKspynqn0KY5yFETLn0pyYqnWcd0ATqTZn10ZNG5yF9pywd0ZKGujYk0APGujYs0AdY5HDsnH-xnH0kPdtknjc1g1DsPjwxn1msnfKopHYs0ZFY5HR3nfKBpHYkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PHf3P1n3rjwxnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWI0KGuAnqiDFK0Zw9ThI-IjYvndtsg1nsn0KYIgnqPWTdPjTvnHc3n1T4PWRLn1m4nfKzug7Y5HDdrH6vPWR4PH0srHc0Tv-b5HbLPvmknjNhnj0kPhR1PyD0mLPV5Rf4PRmYPYR3fRc3fbf4wjR0mynqnfKYIgfqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1KxnH0YP-ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1f1nH04rHNxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0KlTAkdT1Ys0A7buhk9u1Y30Akhm1Ys0AwWmvfq0Zwzmyw-5HTvnjcsn6KBuA-b5RmLnbc1nHc4fWParj6snH9jwjKjrjKawWu7fHDYrDRk0AqW5HD0mMfqn0KEmgwL5H00ULfqnfKETMKY5HcWnanknanzc1bzrjDYrjmvc1nknj0sc1nknj0sQW0snj0snankc1cWnanVc108nj0snj0sc1D8nj0snj0s0Z7xIWYsQWbsg108njKxna3sn7tsQWmdg108rj7xna31nfKBTdqsThqbpyfqn0KWThnqPjR1PHm%26ck%3D7632.1.106.328.179.328.179.165%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26us%3D1.0.1.0.1.0.0%26wd%3D%26bc%3D110101&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E7%25AB%259E%25E5%2593%2581%26unit%3D%25E6%2599%25BA%25E8%2581%2594-2%26keyword%3Dwww.hugoboss.cn%26bd_vid%3D4645570595134235086%26csource%3Dboctb&friend_source=0&friend_source=0; __a=75833049.1598343523.1598422177.1598665953.72.3.5.5; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1598666505; __zp_stoken__=523ebOHhUSXlybFZYKBxwaDQsWj4tYC9Ydx9JdUctX0IIL0o9J2VcP3gVWEBYDlJ5fm4lIC1NX0cod08uKWVUAW0jJWw7MRUmB38%2BQ3UWAXZKNiAYG3YkPQgyZjccbwBfeD9YRm1ELU5dflFNOQ%3D%3D; __zp_sseed__=MMgUvVBtS2cPg6dMa7ZTdS2FQkcWoQ3NBGOhnNbPzZo=; __zp_sname__=393d5208; __zp_sts__=1598666865782",
    #要实时的cookies
    "Referer":"https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=",
    "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/84.0.4147.135Safari/537.36",
}
msg_list = []
for i in range(1,5):
    url = 'https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page={}'.format(i)
    #query后面的参数为职位
    res = requests.get(url,headers=headers)
    print(res)
    soul = lxml.etree.HTML(res.text)
    job_list = soul.xpath('//div[@class="job-list"]/ul/li/div[@class="job-primary"]')
    for item in job_list:
        title = item.xpath('./div//div[@class="job-title"]/span/a/@title')[0]#名字
        company = item.xpath('./div//div[@class="info-company"]//h3/a/text()')[0]#公司
        scale = item.xpath('./div//div[@class="info-company"]//p//text()')  # 公司规模
        salary = item.xpath('./div/div/div/div[2]/span/text()')[0]#薪水
        exprience = item.xpath('./div/div/div/div[2]/p//text()')#经验
        href = 'https://www.zhipin.com' +item.xpath('./div//div[@class="job-title"]/span/a/@href')[0]#详情
        print("title:",title,"company:",company,"scale:",scale,"salary:",salary,"exprience:",exprience,"href:",href,)
        time.sleep(1)
        msg_list.append([title,company,scale,salary,exprience,href])
# print(msg_list)
for row in msg_list:
        writer.writerow(row)
csv_file.close()
print('DONE---------------------------------------------------------------------------------------------------------------------------------------')