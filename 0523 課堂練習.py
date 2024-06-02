請利用本次上課所提供的2024年總統就職演講稿 speech.txt，讀入檔案後利用Jieba進行斷詞，統計總統在演講裡面用詞的頻率，並輸出成CSV檔案。

with open('speech.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = jieba.cut(content)

    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    with open('stat.csv', 'w', encoding='utf-8') as outf:
        outf.write("word,freq\n")
        for w in d:
            outf.write(f"{w},{d[w]}\n")
