#!/usr/bin/env python

import os
import sqlite3
from collections import defaultdict
from getpass import getpass
from datetime import datetime
from pprint import pprint
import time
import calendar


header = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!--This is an automatically generated file.
    It will be read and overwritten.
    Do Not Edit! -->
    <Title>Bookmarks</Title>
    <H1>Bookmarks</H1>
    <DL>\n"""
file_ = open('fbm.html', 'w')
file_.write(header)
file_.close()

class Bookmark(object):
  def __init__(self, name, url, add_date, last_visited, last_modified, private=False, tags=[],
                 description=''):
        self.name = name
        self.url = url
        self.add_date = add_date
        self.last_visited = last_visited 
        self.last_modified = last_modified 
        self.private = private
        self.tags = [tags]
        self.description = description

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('db', help="The ybookmarks.sqlite file in firefox "
                        "profile directory")
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)
    curs = conn.cursor()
    curs.execute("select rowid, name, url, shared, description, added_date, last_visited, last_modified from bookmarks")
    bookmarks = dict((id, Bookmark(name=name, url=url,
                                   add_date=added_date/1000000,last_visited=last_visited/1000000,last_modified=last_modified/1000000,
                                   private=(shared != "true"),
                                   description=description))
                     for id, name, url, shared, description, added_date, last_visited, last_modified
                     in curs)
    curs.execute("select rowid, name from tags")
    tags = dict((id, name) for id, name in curs)
    bookmarks_tags = defaultdict(list)
    tags_bookmarks = defaultdict(list)
    curs.execute("select bookmark_id, tag_id from bookmarks_tags")
    for bookmark_id, tag_id in curs:
        bookmarks_tags[bookmark_id].append(tag_id)
        tags_bookmarks[tag_id].append(bookmark_id)

    for bookmark_id, bookmark in bookmarks.items():
        bookmark.tags = [tags[tid] for tid in bookmarks_tags[bookmark_id]]

    folder_count = 0
    bm_count = 0
    false_id_count = 0

    for tg_id in tags_bookmarks:
        folder_count += 1
        tag_name = tags[tg_id].encode('ascii', 'ignore').decode('ascii')
        file_ = open('fbm.html', 'a')
        file_.write("      <DT><H3 FOLDED ADD_DATE=\"\">" + tag_name + "</H3><DL><p>")
        file_.close()
        
        for bm_id in tags_bookmarks[tg_id]:
           if bm_id in bookmarks:
              bm_count += 1
              bm = bookmarks[bm_id]
              bm.name = bm.name.encode('ascii', 'ignore').decode('ascii')
              file_ = open('fbm.html', 'a')
              file_.write("          <DT><A HREF=\"" + bm.url + "\" ADD_DATE=\"" + str(bm.add_date) + "\" LAST_VISIT=\"" + str(bm.last_visited) + "\" LAST_MODIFIED=\"" + str(bm.last_modified) + "\">" + bm.name  + "</A>\n")
              file_.close()
           else:
              false_id_count += 1
   
        file_ = open('fbm.html', 'a')
        file_.write("      </DL><p>\n\n")
        file_.close()

    print "\nSuccessfully exported " + str(folder_count) + " folders and " + str(bm_count) + " bookmarks to fbm.html.\nDisregarded " + str(false_id_count) + " false ids in tag definitions.\n"

if __name__ == '__main__':
    main()

file_ = open('fbm.html', 'a')
file_.write("</DL>")
file_.close()

