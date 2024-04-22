from keywords import SYNONYMS, IGNORE, CV, NLP, DATA_ENGINEER, BACKEND, FRONT, MOBILE, BLOCK_CHAIN, FINANCE, SYSTEM, SECURITY, METABERS

class Preprocess():
    def __init__(self):
        pass

    def preprocess(self, df):
        df['fields'] = df['fields'].apply(lambda x: ', '.join(x))
        return df