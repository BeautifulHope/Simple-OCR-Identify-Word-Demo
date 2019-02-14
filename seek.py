#!/usr/bin/env python3
# -*- coding: utf-8 -*
import re

import requests
from bs4 import BeautifulSoup
from UA import user_agent
from lxml import etree

def iciba(word):

    url = 'http://www.iciba.com/'+word
    ua = user_agent()
    headers = {
        'Host':'www.iciba.com',
        'User-Agent':ua,
        'Upgrade-Insecure-Requests':'1',
        'DNT':'1',
        'Cookie':'iciba_u_rand=65de9865e46d604ff0b3549b6aae5d1e%4060.222.138.212; iciba_u_rand_t=1534828106; is_new_index=1; cbdownload_num=3; cbdownload_time=download; c_word_history=define%2Clook; screen-skin=screen-blue; search-history=define%2Clook'

    }
    html = requests.get(url,headers=headers)
    print(html.status_code)
    # print(html.text)
    soup = BeautifulSoup(html.text, 'lxml')
    seeks = soup.find('div',class_='in-base').find_all('li',class_='clearfix')
    
    print(str(seeks))
    #
    print('-------------------------------')
    for seek in seeks:

        pattern_v = re.compile(r'<span class="prop">(.*?)</span>', re.S)
        pattern = re.compile(r'<span>(.*?)</span>', re.S)

        results_v = re.findall(pattern_v, str(seek))
        results = re.findall(pattern, str(seek))
        for j in results_v:
            print(j)
            for i in results:
                print(i)

    last = seeks[2]
    # print(str(last))
    pattern_type = re.compile(r'<h1 class="base-word abbr chinese change-base">(.*?)</h1>', re.S)
    pattern_change = re.compile(r'<span>(.*?)<a class="shape" href=".*?">(.*?)</a> </span>', re.S)

    results_type = re.findall(pattern_type, str(last))
    results_change = re.findall(pattern_change, str(last))
    print('==============')
    print(results_type[0]+':')

    for change in results_change:
        # print(change)
        print(change[0]+':'+change[1])


if __name__=='__main__':
    word = 'result'
    iciba(word)