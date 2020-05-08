#统计文件中单词出现的个数
def count_word(file_name, top_n):
    word_map = dict()
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines:
        for word in line.split(" "):
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1

    word_list = [[k,v] for k, v in word_map.items]
    word_list.sort(key=lambda word : word[1], reverse = True)
    return [ w[0] for w in word_list[:top_n]]

count_word()