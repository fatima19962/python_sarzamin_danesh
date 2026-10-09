# text="text"
# text.istitle()
# print(text.istitle())
# def my_istitle(s):
#     if not s:
#         return False
#     words = s.split()
#     for word in words:
#         if not (word[0].isupper() and word[1:].islower()):
#             return False
#     return True
# print(my_istitle("Hello World"))  # True
# print(my_istitle("hello World"))  # False
# print(my_istitle(text))  # False

# text2="Text"
# print(text2.isupper())
# def my_isupper(s):
#     if not s:
#         return False
#     for char in s:
#         if char.isalpha() and not char.isupper():
#             return False
#     return True

# print(my_isupper("HELLO"))  # True
# print(my_isupper("Hello"))  # False

text3="hi"
print(text3.isalpha())
def my_isalpha(s):
    if not s:
        return False
    for char in s:
        if not char.isalpha():
            return False
    return True

print(my_isalpha("Hello"))  # True
print(my_isalpha("Hello123"))  # False
print(my_isalpha(text3))  # False