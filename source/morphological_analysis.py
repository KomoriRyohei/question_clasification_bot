import MeCab

def mecab_analyze(text):
    mecab = MeCab.Tagger("-Ochasen")
    node = mecab.parseToNode(text)
    words_list = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            words_list.append(node.surface)
        elif node.feature.split(",")[0] == "形容詞":
            words_list.append(node.feature.split(",")[6])
        elif node.feature.split(",")[0] == "動詞":
            words_list.append(node.feature.split(",")[6])
        node = node.next

    return words_list