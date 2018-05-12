import sys
import re

def print_tuple_list(string_tuple_list):
  result = []
  for tup in string_tuple_list:
    result.append('%s %s' % (tup[0], tup[1]))  
  result_file = open('result.txt', 'w+')
  result_file.write('\n'.join(result))
  result_file.close()

def extract_words(s):
  return re.sub("[^\w]", " ",  s).split()

def count_appearances(stringarr):
  d = {}
  for s in stringarr:
    lowered = s.lower()
    if lowered in d:
      d[lowered] += 1
    else:
      d[lowered] = 1
  return d

def count_word_appearances_in_file(filename):
  file_ = open(filename, 'r')
  content = file_.read(999999999)
  file_.close()
  words = extract_words(content)
  return count_appearances(words)

def print_words(filename):  
  word_dict = count_word_appearances_in_file(filename)
  sort = sorted(word_dict.items())
  print_tuple_list(sort)

def print_top(filename):
  word_dict = count_word_appearances_in_file(filename)
  sort = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)[:20]
  print_tuple_list(sort)