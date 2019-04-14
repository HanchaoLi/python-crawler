import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import os.path
import glob
import os
import time
import multiprocessing

namePath = {}
i = 0
for file in glob.glob('E:/result/*.txt'):
    namePath[i] = file.split('\\')[1].split('.')[0]
    i = i + 1


def get_fiction_worker():
    quote_page = 'https://www.xbiquge.cc/book/42534/'

    mainPage = urllib.request.urlopen(quote_page)

    mainSoup = BeautifulSoup(mainPage, 'html.parser')

    save_path = 'E:/result/'
    while True:
        for currPage in mainSoup.findAll('dd'):

            chapterTitle = currPage.a.text
            if chapterTitle in namePath:
                continue
            chapterLink = quote_page + currPage.a['href']
            try:
                chapterPage = urllib.request.urlopen(chapterLink)
                chapterSoup = BeautifulSoup(chapterPage, 'html.parser')
                fiction_content = chapterSoup.find(
                    'div', attrs={'name': 'content'}).text

                completeName = os.path.join(save_path, chapterTitle + '.txt')
                file = open(completeName, 'w', encoding='utf-8')
                file.write(fiction_content)
                file.close()
            except:
                pass
            time.sleep(1)


if __name__ == '__main__':
    worker_1 = multiprocessing.Process(
        name='worker 1', target=get_fiction_worker)
    worker_2 = multiprocessing.Process(
        name='worker 2', target=get_fiction_worker)
    worker_3 = multiprocessing.Process(
        name='worker 3', target=get_fiction_worker)
    worker_4 = multiprocessing.Process(
        name='worker 4', target=get_fiction_worker)
    worker_5 = multiprocessing.Process(
        name='worker 5', target=get_fiction_worker)

    worker_1.start()
    worker_2.start()
    worker_3.start()
    worker_4.start()
    worker_5.start()
