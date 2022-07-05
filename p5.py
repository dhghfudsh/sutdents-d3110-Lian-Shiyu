from selenium import webdriver
import time
import pandas as pd

start_url = 'https://movie.douban.com/'

def get_driver():
    try:
        return webdriver.PhantomJS()
    except Exception:
        return webdriver.Firefox()


driver = get_driver()
driver.get(start_url)

# 点击“分类”
driver.find_element_by_link_text('分类').click()
time.sleep(1)
# 点击“电影”
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div[1]/div[1]/ul[1]/li[2]/span').click()
time.sleep(1)
# 点击“喜剧”
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div[1]/div[1]/ul[2]/li[3]/span').click()
time.sleep(1)
# 点击“中国大陆”
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div[1]/div[1]/ul[3]/li[2]/span').click()
time.sleep(1)
# 点击“展开列表”
driver.find_element_by_xpath(
    '/html/body/div[3]/div[1]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/a[2]/span').click()
time.sleep(1)
n = 10

for i in range(n):
    driver.find_element_by_class_name('more').click()
    time.sleep(1)


title = driver.find_elements_by_class_name('title')
rating = driver.find_elements_by_class_name('rating')
cast = driver.find_elements_by_class_name('cast')
data = pd.DataFrame({"电影": title, "评分": rating, "导演": cast, "主演": cast})

data['电影'] = data['电影'].apply(lambda x: x.text)
data['评分'] = data['评分'].apply(lambda x: x.text)
data['导演'] = data['导演'].apply(lambda x: x.text.split('\n')[0][3:].split('/'))
data['主演'] = data['主演'].apply(lambda x: x.text.split('\n')[1][3:].split('/'))

outputpath = 'C:/Users/111478/AppData/Roaming/Mozilla/Firefox/Profiles/eec4zuex.default-release-2'
data.to_csv(outputpath, sep=',', index=False, header=True, encoding='utf_8_sig')
