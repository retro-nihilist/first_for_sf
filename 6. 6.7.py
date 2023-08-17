def get_unique_words(words_list):  return sorted(set(words_list))


words_list_example = ['and', 'take', 'the', 'most', 'special', 'care',
 'that', 'you', 'locate', "muad'dib", 'in', 'his', 'place', 'the', 
 'planet', 'arrakis', 'do', 'not', 'be', 'deceived', 'by', 'the', 
 'fact', 'that', 'he', 'was', 'born', 'on', 'caladan', 'and', 'lived', 
 'his', 'first', 'fifteen', 'years', 'there', 'arrakis', 'the', 
 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
print(get_unique_words(words_list=words_list_example))
"""


print(get_unique_words(words_list=words_list_example))
## ['and', 'arrakis', 'as', 'be', 'born', 'by', 'caladan', 'care', 
'deceived', 'do', 'dune', 'fact', 'fifteen', 'first', 'forever', 'he',
 'his', 'in', 'is', 'known', 'lived', 'locate', 'most', "muad'dib", 'not',
   'on', 'place', 'planet', 'special', 'take', 'that', 'the', 'there', 'was',
     'years', 'you']"""