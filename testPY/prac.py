coo = [1, 2, 3]
x, y, z = coo
print(x, y, z)

# phone = input('Phone: ')
# # mapping = {
# #     "1": "One",
# #     "2": "Two",
# #     "3": "Three",
# #     "4": "Four"
# # }
# # output = ''
# # for i in phone:
# #     output += mapping.get(i, "no") + " "
# # print(output)

msg = input(">")
words = msg.split(' ')
emoji = {
    ":)": "🤪"
}
output = ''
for word in words:
    output += emoji.get(word, word) + " "
print(output)