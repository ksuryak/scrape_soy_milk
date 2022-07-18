f = open('Soy_Milk_Url.txt','w+')

url = 'https://www.amazon.com/s?k=soy+milk"&"crid=1H6WFKJAWQH4M"&"qid=1658109000"&"sprefix=soy+milk%2Caps%2C275"&"ref=sr_pg_1'
f.write(url)
f.write('\n')


for i in range(2,8):
    url = 'https://www.amazon.com/s?k=soy+milk&page='+str(i)+'&crid=1H6WFKJAWQH4M&qid=1658108738&sprefix=soy+milk%2Caps%2C275&ref=sr_pg_'+ str(i)
    f.write(url)
    f.write('\n')
    
f.close()
