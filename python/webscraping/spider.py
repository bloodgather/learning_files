import requests
from time import sleep
import tqdm
from bs4 import BeautifulSoup
import json
import re
import os

from datetime import date
from datetime import datetime
from datetime import timedelta

from load_config import load_config
import util
import csv

base_Url = r'https://s.weibo.com/weibo?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 '
                  'Safari/537.36',
}
cookies = {
    'SUB': ''
}
params = {
    'suball': '1',
    'scope': 'ori',
    'Refer': 'g',
}

info_trans = {
    '昵称': 'NickName',
    '简介': 'Intro',
    '阳光信用': 'Credit',
    '性别': 'Gender',
    '生日': 'Birthday',
    '省': 'Province',
    '地区': 'City',
    '感情状况': 'Marriage',
}

# 爬取时间间隔，减少并发
TIME_DELAY = 1
# 每次爬取的默认天数间隔
DATE_INTERVAL = 7


def spider():
    config = load_config()
    cookies['SUB'] = config['cookie']
    params['q'] = config['q']
    params['timescope'] = config['timescope']
    assert check_cookie() is True, "Invalid cookie!"

    time_scope = params['timescope'][params['timescope'].find(':') + 1:].split(':')
    begin_date = date.fromisoformat(time_scope[0])
    final_date = date.fromisoformat(time_scope[1])
    final_date = min(final_date, date.today())
    print('Crawl keyword: %s' % params['q'])
    print('Time scope:', begin_date, final_date)

    print('Initializing...')
    period_list = []
    with tqdm.tqdm(total=100) as tq_bar:
        start_date = begin_date
        while start_date <= final_date:
            sleep(TIME_DELAY)

            step_date = min((final_date - start_date).days + 1, DATE_INTERVAL)  # init step_date
            params['timescope'] = util.update_timeScope(start_date, step_date)

            step_date, page_list = check_pageList(start_date, step_date)  # get valid step_date, page_list
            period_list.append(page_list)
            start_date = start_date + timedelta(days=step_date)  # update start_date

            init_process = util.update_initProcess(begin_date, final_date, step_date)  # update tq_bar
            tq_bar.update(init_process)
        tq_bar.update(100 - tq_bar.n)
    print('Initialized! Start crawling, %d period in total' % len(period_list))

    data_collect = []
    for period in tqdm.tqdm(period_list):
        data_collect = spider_single_period(data_collect, period)

    print("Collect %s data in total" % len(data_collect))
    with open('test_data.json', 'w', encoding='UTF-8') as data_file:
        data_file.write(json.dumps(data_collect, indent=4, ensure_ascii=False))


def get_pageList():
    r = requests.request("GET", url=base_Url, headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        page_list = [r'https://s.weibo.com' + page_sp.a['href'] for page_sp in
                     soup.find('ul', class_="s-scroll").find_all('li')]
    except AttributeError:
        if soup.find('div', class_="card-no-result"):
            page_list = []  # no result in this params
        else:
            page_list = [r.url]  # only one-page result

    return page_list


def check_pageList(start_date: date, step_date: int):
    params['timescope'] = util.update_timeScope(start_date, step_date)
    page_list = get_pageList()
    page_num = len(page_list)
    while step_date > 1 and page_num == 50:
        step_date //= 2
        params['timescope'] = util.update_timeScope(start_date, step_date)
        page_list = get_pageList()
        page_num = len(page_list)
    if page_num == 50:
        print('Warning: one-day results may be concealed because of display limit.')
        # 微博最多显示50页搜索结果
    return step_date, page_list


def spider_single_period(data_collect: list, page_list: list):
    for page_url in page_list:
        sleep(TIME_DELAY)
        page_res = spider_single_page(page_url)
        if page_res:
            data_collect += page_res
            out_to_csv(page_res, params['q'])
    return data_collect


def spider_single_page(page_url: str):
    raw_data = []
    r = requests.request("GET", url=page_url, headers=headers, cookies=cookies)
    sp = BeautifulSoup(r.text, 'lxml')

    for blog_sp in sp.find_all('div', class_="content"):
        # user id
        userInfo_sp = blog_sp.find('div', class_='info').find_all('div')[1]
        user_verify = userInfo_sp.find('a', {'href': '//verified.weibo.com/verify'})
        # 仅保留个人认证以及非认证账号
        if user_verify and user_verify['title'] == '微博官方认证': continue
        userId = re.findall(r'weibo.com/(.*?)\?', userInfo_sp.a['href'])[0]
        userNickName = userInfo_sp.a['nick-name']
        # print(userId, userNickName)

        # weibo message
        msg_sp = blog_sp.find('p', class_='txt', attrs={'node-type': "feed_list_content_full"})
        if msg_sp:
            msg = msg_sp.text.strip()
            msg = msg[:msg.find('收起全文')]
        else:
            msg_sp = blog_sp.find('p', class_='txt')
            msg = msg_sp.text.strip()
        # print(msg)

        # weibo date
        time_info = blog_sp.find('p', class_='from').a.text.strip().split()[0]
        date_str = util.format_timeInfo(time_info)
        # print(date_str)

        raw_data.append({'userId': userId, 'userNickName': userNickName, 'msg': msg, 'date': date_str})
    return raw_data


def out_to_csv(data_collect: list, keyword: str):
    base_dir = 'Results' + os.sep + keyword
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir)
    file_path = base_dir + os.sep + keyword + '.csv'
    if not os.path.isfile(file_path):
        is_first_write = 1
    else:
        is_first_write = 0
    if data_collect:
        with open(file_path, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            csv_header = [
                'userId', 'userNickName', 'msg', 'date'
            ]
            if is_first_write:
                writer.writerow(csv_header)
            for data in data_collect:
                writer.writerow([data[key] for key in csv_header])


def check_cookie():
    r = requests.request("GET", url=base_Url, headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(r.text, 'lxml')
    return True if soup.find('div', class_='m-hint') is None else False


def get_userInfo(userId: str):
    url_info = "https://m.weibo.cn/api/container/getIndex?containerid=230283%s_-_INFO" % userId

    info = {'UserId': userId}
    r = requests.request("GET", headers=headers, url=url_info, cookies=cookies, verify=True)
    data_js = r.json()
    if not data_js['ok']:
        print("Error with userId: %s" % userId)
        return info

    data_js = data_js['data']['cards']
    if len(data_js) >= 1 and data_js[0]['card_group'][0]['desc'] == '账号信息':
        # get data in info_trans
        for card in data_js[0]['card_group']:
            item_name = card.get('item_name')
            if item_name in info_trans.keys():
                info[info_trans[item_name]] = card.get('item_content', '')
    if len(data_js) >= 2 and data_js[1]['card_group'][0]['desc'] == '个人信息':
        for card in data_js[1]['card_group']:
            item_name = card.get('item_name')
            # get birthday data
            if item_name == '生日':
                try:
                    birthday = card.get('item_content', '').split()[0]
                    birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
                    info["Birthday"] = birthday.strftime('%Y-%m-%d')
                except (IndexError, ValueError):
                    info["Birthday"] = ""
            # get location data
            elif item_name == '所在地':
                location = card.get('item_content', '').split()
                if location:
                    info["Province"] = location[0]
                    info["City"] = location[1] if len(location) > 1 else ""
                else:
                    info["Province"] = ""
                    info['City'] = ""
            # get other data in info_trans
            elif item_name in info_trans.keys():
                info[info_trans[item_name]] = card.get('item_content', '')

    return info


if __name__ == '__main__':
    spider()
