#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sorted_by_second_word(url):
  match = re.search(r"-(\w+)-(\w+).jpg",url)
  if match:
    return match.group(2)
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  mylist = []
  f = open(filename,'r')
  server_match = re.search(r"_(\S+.com)",filename)
  if server_match:
    server = "http://"+server_match.group(1)
  for line in f:
    match = re.search(r"GET\s(\S*puzzle\S*)\sHTTP",line)
    if match:
      mylist.append(server+match.group(1))
  
  mylist = sorted(mylist,key=sorted_by_second_word)
  prev = ""
  i =0
  while i<len(mylist):
    if prev == mylist[i]:
      del mylist[i]
    else:
      prev = mylist[i]
      i = i+1

  print '\n'.join(mylist)
  return mylist

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  html_file = open(os.path.join(dest_dir,"index.html"),'w')
  html_file.write("<verbatim>\n")
  html_file.write("<html>\n<body>\n")

  i=0
  for url in img_urls:
    print "Retrieve the %d stripe" % i
    urllib.urlretrieve(url,os.path.join(dest_dir,"img"+str(i)))

    html_file.write('<img src="%s">' % ("img"+str(i)))
    i += 1

  html_file.write("\n</body>\n</html>\n")

  html_file.close()
  return

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
