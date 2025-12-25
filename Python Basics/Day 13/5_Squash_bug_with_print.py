# print() is your BEST Friend
# use print to debug 

pages = 0
words_per_page =0
pages = int(input("enter  pages: "))
print("bwfore: ", words_per_page)
words_per_page = int(input("enter wordsperpage:")) #instead == use = 
print("after",words_per_page)
total_words = pages * words_per_page
# print(pages)
# print(words_per_page)
print(total_words)

# here == equals checks , we need to updte the values



#  pages = int("enter  pages: ")
# ValueError: invalid literal for int() with base 10: 'enter  pages: '