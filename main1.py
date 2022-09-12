import time
import os
from pymongo import MongoClient
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import re
import json
import pandas as pd


def get_videos(cname:str,nvids:int):
    def scroll_page(driver: Chrome):
        wait = WebDriverWait(driver, 1)
        for item in range(10):
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(2)
    with Chrome(executable_path=r'chromedriver.exe') as driver:
        wait = WebDriverWait(driver,1)
        driver.get(f"https://www.youtube.com/results?search_query={cname.replace(' ','+')}")
        link1 = wait.until(EC.visibility_of_element_located((By.ID,'main-link'))).get_attribute('href')
        driver.get(f"{link1}/videos")
        time.sleep(2)
        scroll_page(driver)
        links = driver.find_elements(By.ID, "thumbnail")
        links1 = set()
        count=1
        for i in links:
            if 'shorts' not in str(i.get_attribute("href")) and count <=nvids and i.get_attribute("href") != None:
                links1.add(i.get_attribute("href"))
                count+=1
    print(links1)
    print(count)
    # os.makedirs(f"./Vid_links/{cname}")
    # with open(f"./Vid_links/{cname}/vid_links_{cname}.json","a") as f:
    #     f.write(json.dumps(links1))
    return links1


session = HTMLSession()
def get_video_info(url):
    response = session.get(url)
    response.html.render(sleep=1,timeout=50)
    soup = bs(response.html.html, "html.parser")
    result = {}
    response.html.render(sleep=1, timeout=50)
    try:
        result["title"] = soup.find("meta", itemprop="name")['content']
    except:
        result["title"] = "none"
    try:
        result["views"] = soup.find("meta", itemprop="interactionCount")['content']
    except:
        result["views"] = "none"
    try:result["description"] = soup.find("meta", itemprop="description")['content']
    except:result["description"] = "none"

    try:result["date_published"] = soup.find("meta", itemprop="datePublished")['content']
    except:result["date_published"] = "none"

    try:result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    except:result["duration"] = "none"

    try:result["tags"] = ', '.join([meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"})])
    except:result["tags"] = "none"

    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)

    try:videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    except:pass

    try:videoSecondaryInfoRenderer =data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']
    except:pass

    try:likes_label =videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
    except:likes_label=0
    try:likes_str = likes_label.split(' ')[0].replace(',', '')
    except:pass
    result["likes"] = '0' if likes_str == 'No' else likes_str

    channel_tag = soup.find("meta", itemprop="channelId")['content']
    channel_name = soup.find("span", itemprop="author").next.next['content']
    channel_url = f"https://www.youtube.com/{channel_tag}"
    channel_subscribers = videoSecondaryInfoRenderer['owner']['videoOwnerRenderer']['subscriberCountText']['accessibility']['accessibilityData']['label']
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

    # os.makedirs(f"./comments/{channel_name}")
    # with open(f"./comments/{channel_name}/comments_{channel_name}.json","a") as f:
    #     f.write(json.dumps(result))
    return result


def get_video_comments(url:str):
    comments_dict = {"name":[],"comment":[]}
    l1 = list()
    l2 = list()
    with Chrome(executable_path=r'chromedriver.exe') as driver:
        wait = WebDriverWait(driver, 1)

        def scroll_page(driver:Chrome):
            for item in range(30):
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
                time.sleep(1)

        driver.get(url)
        time.sleep(2)
        scroll_page(driver)
        # comments_data = pd.DataFrame({"name":[],"comment":[]})

        for comment in wait.until(EC.presence_of_all_elements_located((By.ID,"comment-content"))):
            comments_dict['comment'].append(comment.text)
        for name in wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="author-text"]/span'))):
            comments_dict['name'].append(name.text)

    return comments_dict


def merge(url:str):
    dict1 = get_video_comments(url)
    dict2 = get_video_info(url)
    dict3 = {**dict1,**dict2}

    return dict3


def merge2(d1: dict, d2: dict):
    d1 = {**d1, **d2}
    return d1


def main_run():
    str1 = input("> ")
    n = int(input("how many videos you want: "))
    count = 1
    l1 = list()
    vids1 = get_videos(str1, n)
    for i in vids1:
        one_dict_merged = merge(i)
        l1.append(one_dict_merged)
        print(f"details extracted for vid{count}");
        count += 1

    print(l1)
    print(len(l1))

    l2 = list()
    c1 = 0
    for i in l1:
        df = pd.DataFrame([i])
        df['vid_id'] = f"vid_id_{c1}"
        l2.append(df)
        c1 += 1

    c2 = 0
    main_df = pd.DataFrame()
    for i in l2:
        main_df = pd.concat([main_df, i])
        print(f"{c2} results turned into df")
        c2 += 1

    print(main_df)
    main_df.to_csv(f"./CSVs/main_csv_{str1}.csv")

    def cleaning_csv():
        vids_list = list(vids1)
        df1 = pd.DataFrame({"vids": vids_list, "vid_id": [f"vid_id_{j}" for j in range(len(vids_list))]})
        df2 = pd.read_csv(f"./CSVs/main_csv_{str1}.csv")
        result = pd.merge(df1, df2, how="outer", on=["vid_id", "vid_id"])
        # result = result.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
        df1.to_csv(f"main_csv3_{str1}.csv")

    cleaning_csv()


main_run()