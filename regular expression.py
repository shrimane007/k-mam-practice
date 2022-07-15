# import re
# a=re.compile("shri")
# print(type(a))

# import re
# # a=re.compile("ab")
# reobj=re.finditer("abbabab")
# for i in reobj:
#    print(i.end(),"",i.group())  ##end+1 from start

import re
obj1=re.finditer("a+","a25baacff54g5")  #if ^ add in [abc]then search for other abc letters
for i in obj1:                         #d\D for didgit,\s\S for space
  print(i.start(),"",i.group())       # a+ at least ones
                                       # ? where present


















