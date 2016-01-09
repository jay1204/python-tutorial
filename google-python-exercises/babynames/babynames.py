#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  mylist = []
  f = open(filename,'r')
  content = f.read()
  match_year = re.search(r"Popularity\sin\s(\d\d\d\d)",content)
  if match_year:
    year =  match_year.group(1)
    mylist.append(str(year))
  else:
    print "Can not find the year"
    sys.exit(1)

  names_ranks = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',content)
  names_dict = {}
  if names_ranks:
    for name_rank in names_ranks:
      (rank,male_name,female_name) = name_rank
      if not male_name in names_dict:
        names_dict[male_name] = rank
      if not female_name in names_dict:
        names_dict[female_name] = rank
  else:
    print "can not extract the name-rank"
    sys.exit(1)

  for name in names_dict:
    mylist.append(name+" "+str(names_dict[name]))

  f.close()
  return mylist


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  for filename in args:
    mylist = extract_names(filename)

    result = '\n'.join(mylist)

    if summary:
      outputfile = open(filename+'.summary','w')
      outputfile.write(result+'\n')
      outputfile.close()
    else:
      print result

  
if __name__ == '__main__':
  main()
