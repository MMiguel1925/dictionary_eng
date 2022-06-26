import pandas as pd


class Definition:

    def __init__(self, termo):
        self.termo = termo

    def get(self):
        df = pd.read_csv('data.csv')
        return tuple(df.loc[df['word']==self.termo]['definition'])


# inst_definition = Definition('volleyball')
# print(inst_definition.get())
