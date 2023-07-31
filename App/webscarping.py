import  requests 
from bs4 import  BeautifulSoup



# url = 'https://en.wikipedia.org/wiki/Technology'
# url ="https://www.codewithharry.com/"
url ="https://www.simplilearn.com/types-of-technology-article"
r = requests.get(url)

html_content = r.content

# print('---------------',html_content)

soup = BeautifulSoup(html_content, 'html.parser')
# print('---------------',soup.prettify())
soup.prettify()


# para_list = soup.find('p')
h_list = soup.find_all('h')
h_text = [ h.text for h in h_list ]

# print(h_list)

print(len(h_list))

list_of_text  = []
for i in h_text:
    # print(i)
    list_of_text.append(h_text)

print(list_of_text)

para_list = soup.find_all('p')
text_list = [para.text for para in para_list]

# for i in text_list:
#     print(i)

# leng = len(para_list)
# print(leng)


# list2 = []
# list2.append(text_list[0])
# list2.append(text_list)

# # list2[0].replace('<p>','')


# print(list2)





if r.status_code == 200:
    print('yesssssssssssssssssssssssssssssssssssssssssss')