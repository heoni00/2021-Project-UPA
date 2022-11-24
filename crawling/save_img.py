import requests, os, time, re, random
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs

print('ver2')

code = int(input('정해진 파트를 입력해주세요. \n(차헌 : 1, 찬우 : 2, 동욱 : 3, 호준 : 4)\n'))
xlsx = 'id_df_request.xlsx'
split = 4

def save_img(url, name):
        #이미지 url과 저장할 이름을 입력하면 해당 이름으로 저장해주는 함수
        #일단 기본은 10mb까지 저장할 수 있게 해둠

    response = requests.get(url)

    file = open(name + ".png", "wb")
    file.write(response.content)
    file.close()

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        print ('Error: Creating directory. ' +  directory)

class StupidSpider:
    def __init__(self, pth='chromedriver.exe'):        
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        self.driver = webdriver.Chrome(pth, options=options)
        self.driver.maximize_window()
    
    def move(self, pth):
        self.driver.get(pth)
        time.sleep(random.randrange(1,2))
    
    def get(self, xpth):
        self.target = self.driver.find_element_by_xpath(xpth)
        return self.target
    
    def gets(self, xpth):
        return self.driver.find_elements_by_xpath(xpth)
    
    def click(self, xpth="$%&"):
        if xpth != "$%&":
            tmp = self.driver.find_element_by_xpath(xpth)
            tmp.click()
            time.sleep(random.randrange(2,4))
        else:
            self.target.click()
            time.sleep(random.randrange(2,4))
    
    def send(self, key, xpth="$%&"):
        if xpth != "$%&":
            tmp = self.driver.find_element_by_xpath(xpth)
            tmp.send_keys(key)
            time.sleep(random.randrange(2,4))
        else:
            self.target.send_keys(key)
            time.sleep(random.randrange(2,4))
    
    def text(self, xpth="$%&"):
        if xpth != "$%&":
            return self.driver.find_element_by_xpath(xpth).text
        else:
            return self.target.text.replace(' ','')
    
    def get_soup(self, html = '$%&'):
        if html != '$%&':
            res = requests.get(html)
            self.soup = bs.BeautifulSoup(res.text, 'html.parser')
            return self.soup
        else:
            html = self.driver.page_source
            self.soup = bs(html, 'html.parser')
            return self.soup

    def soup_select(self, text):
        return self.soup.select(text)
    
    def get_attribute(self, text):
        return self.target.get_attribute(text)

spider = StupidSpider()

def save_used_car_img(loc):
    loc['id'] = str(loc['id'])
    if loc['site'] == 'encar':
        for i in [1,3]:
            if loc['id'][3] == '0':
                tmp = '10'
            else:
                tmp = '0' + loc['id'][3]
            url = f"https://ci.encar.com/carpicture/carpicture{tmp}/pic{loc['id'][:4]}/{loc['id']}_00{i}.jpg"
            name = f"{loc['회사']}/{loc['모델']}/{loc['id']}_{i}"
            try : 
                save_img(url, name)
            except:
                return
            
    elif loc['site'] == 'kcar':
        for i in [1,3]:
            if loc['id'][3] == '0':
                tmp = '10'
            else:
                tmp = '0' + loc['id'][3]
            url = f"https://img.kcar.com/carpicture/carpicture{tmp}/pic{loc['id'][:4]}/kcarM_{loc['id']}_00{i}.jpg"
            name = f"{loc['회사']}/{loc['모델']}/{loc['id']}_{i}"
            try : 
                save_img(url, name)
            except:
                return


id_df = pd.read_excel(xlsx, index_col = 0)
range_num1 = (len(id_df)//split) * (code - 1) 
range_num2 = (len(id_df)//split) * code 
id_df = id_df.iloc[range_num1:range_num2]
id_df.reset_index(inplace = True)
del id_df['index']

print(f'배당 로우 : {range_num1} ~ {range_num2}')

progress = len(id_df)

for i in range(len(id_df)):
    print(f'id 추출 : ({i+1}/{progress})')
    if id_df.loc[i]['site'] == 'kcar':
        continue
    id_ = id_df.loc[i]['id']
    url = f"http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=normal&carid={id_}"
    spider.move('http://www.encar.com/index.do')
    spider.move(url)
    time.sleep(3)
    try: 
        spider.get('//*[@id="carPic"]/img')
    except:
        try : 
            spider.get('//*[@id="carPic"]/span/img')
        except:
            continue
    url_ = spider.get_attribute('src')
    id_regex = re.compile('[0-9]+_001.jpg')
    try :
        id_ = id_regex.search(url_).group()
    except:
        continue
    id_df.at[i, 'id'] = id_[:-8]

id_df.to_excel('result2.xlsx')

#폴더 생성
for company in id_df['회사'].unique():
    createFolder(company)

for company in id_df['회사'].unique():
    for model in id_df[id_df['회사'] == company]['모델'].unique():
        createFolder(company + '/' + model)

#이미지 다운로드
progress = len(id_df)
for i in range(len(id_df)):
    print(f'img 다운 : ({i+1}/{progress})')
    print(f'{id_df.iloc[i]["차종"]} : {id_df.iloc[i]["모델"]} ({i}/{progress})')
    save_used_car_img(id_df.iloc[i])