
# enemies = 1

# def battle():
#     enemies = 5
#     print(enemies)
# battle()   # 5

# print(enemies) # 1
# # -----------

# # Local Scope
# def drink():
#     ltr = 2 # loacl var
#     print("LOCAL SCOPE - var is valid only inside the function if you created inside the the fucntion ")
#     print(ltr)
# drink()

# # print(ltr) # NameError: name 'ltr' is not defined.
# # -------------

# # Global Scope
# actual_bmi = 22  # globl
# def bmi():
#     actual_bmi = 25 # local
#     print("inside function actual bmi: ", actual_bmi)
# bmi() 
# print("outside bmi actucal bmi: ", actual_bmi)
# print("global are availabel within or inside and outside function !")
# ------------------------


# # how to modify GLobl scope ?
score = 10 # gloabl
def update_score():
    #score = += 2 #SyntaxError: invalid syntax - Because we cant modify like this inside the how?
    global score
    score += 5 # loacl
    print("Updated score : " , score) #15
update_score()
print("Orig score : ", score) #15

print("alternative way without using Global")
# without using global method :
score2 = 10 # global
def update_score_alternative_way():
    return score2 + 5 # local upd
score2 = update_score_alternative_way()
print("upadted score2 using return: ", score2)

# Global CONSTANTS
PI = 3.141 # this cant be chagned in the code or modified so use UPPERCASE eg.PI, URL, API

# def calc():
#     pi 