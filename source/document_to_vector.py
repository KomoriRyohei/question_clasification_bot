from gensim.models.doc2vec import Doc2Vec

model = Doc2Vec.load()
def calc_vector(documents):
    vectors = []
    for document in documents:
        vectors.append(model.infer_vector(mecab_analyze(document)))
    return vectors
