from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
import time

outfile=open("naver_blog_text.txt","w",encoding='utf-8')

headers = {'User-Agernt':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

word=input("단어를 입력해주세요- ")
word=urllib.parse.quote_plus(word)
number=int(input("보고 싶은 개수는요? - "))
count=1
while count<number:
    blog="https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query="+word+"&sm=tab_pge&srchby=all&st=sim&where=post&start="+str(count)
    blog_address=requests.get(blog, headers=headers)
    blog_html=blog_address.text
    blog_soup=BeautifulSoup(blog_html,'html.parser')

    address_list=[]
    final_naver_address_list=[]
    for naver_address in blog_soup.select('dd.txt_block > span > a.url'):
        naver_address=str(naver_address).split(" ")
        naver_address=naver_address[2][6:]
        naver_address=naver_address[:-1]
        address_list.append(naver_address)
    for naver_address_list in address_list:
        if '?' in naver_address_list:
            naver_address1=naver_address_list.split("?")[0]
            naver_address2=naver_address_list.split("?")[1]
            final_naver_address=naver_address1+"/"+naver_address2.split("=")[2]
            final_naver_address_list.append(final_naver_address)
        else:
            final_naver_address_list.append(naver_address_list)    
    

    final_blog_naver_address_list=[]
    for final_address in final_naver_address_list:
        if 'naver' in final_address:
            final_final_address=final_address.split("/")
            final_blog_naver_address="https://"+"blog.naver.com/"+"PostView.nhn?blogId="+final_final_address[3]+"&logNo="+final_final_address[4]
            final_blog_naver_address_list.append(final_blog_naver_address)
        elif final_address.split(".")[1]=="blog":
            final_final_address1=final_address.split(".")[0]
            final_final_address1=final_final_address1[8:]
            final_final_address2=final_address.split("/")[3]
            final_blog_naver_address1="https://"+"blog.naver.com/"+"PostView.nhn?blogId="+final_final_address1+"&logNo="+final_final_address2
            final_blog_naver_address_list.append(final_blog_naver_address1)
        else:
            final_blog_naver_address_list.append(final_address)

    print("숫자가 10이 아니면 이상한겁니다용 - "+str(len(final_blog_naver_address_list)))

    for html in final_blog_naver_address_list:
        blog_address_html=requests.get(html, headers=headers)
        blog_html=blog_address_html.text
        blog_soup=BeautifulSoup(blog_html,'html.parser')

        outfile.write(html+"\t")

        contents = []

        for tag in blog_soup.select('div[id=postViewArea]') or blog_soup.select('div[class=se_editArea]') or blog_soup.select('div[class=se_sectionArea]') or blog_soup.select('div[id=postListBody]') or blog_soup.select('div[class=se_textView]') or blog_soup.select('div[class=se_editArea]') or blog_soup.select("h3[class=se_textArea]"):
            tag_text=tag.text
            tag_text=tag_text.strip("\n\r")
            tag_text=tag_text.replace(",",":").replace('\n', '').replace('\r', '')
            contents.append(tag_text)

        content = " ".join(contents)
        outfile.write(content + "\n")
    count=count+10
    
    time.sleep(7)
    
outfile.close()

        
            
