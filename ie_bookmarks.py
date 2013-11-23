#!/usr/bin/env python

import sys
import time

from bs4 import BeautifulSoup

class IEBookmarks:
    def __init__(self, filename):
        self.filename = filename

        self.parse()

    def parse(self):
        raw = open(self.filename).read()
        soup = BeautifulSoup(raw)

        self.saved = []

        items = soup.find_all('a')
        for item in items:
            data = {
                'href' : item['href'],
                'add_date' : int(item['add_date']),
                'last_visit' : int(item['last_visit']),
                'last_modified' : int(item['last_modified']),
                'name' : item.string
            }

            self.saved.append(data)

if __name__ == '__main__':
    filename = sys.argv[1]

    bookmarks = IEBookmarks(filename)

    recent = time.time() - 60 * 60 * 24 * 14

    filtered_bookmarks = [x for x in bookmarks.saved if x['add_date'] >= recent]
    for bookmark in filtered_bookmarks:
        timestamp = time.localtime(bookmark['add_date'])
        #print time.asctime(timestamp), bookmark
        print bookmark['href']
