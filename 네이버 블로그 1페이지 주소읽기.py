import urllib.request
import re
import urllib.parse
import time

infile=open("키워드.txt",'r')
keyword=infile.read()
keyword=keyword.strip()
keyword=keyword.split("\n")

for k in keyword:
    blog="https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_jum&query="
    blog=blog.strip()
    key=blog+urllib.parse.quote_plus(k)
    key=key.strip()
    blog1=urllib.request.urlopen(key)
    blogword=blog1.read()
    blogstr=blogword.decode("utf-8")
    outfile=open(str(k)+".html","w",encoding="utf-8")
    time.sleep(7)
    outfile.write(blogstr)
    outfile.close()
infile.close()
outfile=open("결과.txt","w") #요기만 날짜별로 정해서 하면 매일 색다른 결과를 얻을 수 있습니당 (결과를 날짜로 바꾸든 그냥 하든 상관없어용)

for word in keyword:
    try:    
        readfile=open(str(word)+".html","r",encoding="utf-8")
    except:
        break
    line=readfile.read()
    address=re.findall('<a href="[\D]+://([m.]*[\S]*[.][\D]+[.]*[\D]*[/]*[\S]*)[/]+[\d]*" onClick="return goOtherCR',line)
    print(len(address), str(word)+" - 주의사항: 여기 결과값이 15가 아니면 연락주세용")

    addressrank=address[0:5]
    addressrank2=address[0:10]

    number=0
    for i in addressrank:
        key2=open('블로그주소.txt','r')
        key2=key2.read()
        key2=key2.split("\n")
        for i2 in key2:
            if i==i2:
                number=number+1

    count=0
    for j in addressrank2:
        key3=open('블로그주소.txt','r')
        key3=key3.read()
        key3=key3.split("\n")
        for j2 in key3:
            if j==j2:
                count=count+1
    print("{word} 상위 5위이내 일치하는 주소 숫자는 {a}개, 10위이내 일치하는 주소 숫자는 {b}개 입니당.".format(word=word,a=number,b=count))
    outfile.write(word+"- 5위이내 일치하는 주소개수:"+str(number)+" "+"& 10위이내 일치하는 주소개수:"+str(count)+"\n")
    
     
readfile.close()
outfile.close()
   



