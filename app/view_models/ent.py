class EntSummary:
    def __init__(self, entname, label):
        self.entname = entname
        self.label = label


class EntCollection:
    def __init__(self):
        self.total = 0
        self.ents = []
        self.keyword = None

    def fill(self, ent_Q, keyword):
        # self.total = ent_Q.total
        self.ents = [EntSummary(ent.entname, ent.label) for ent in ent_Q]
        self.keyword = keyword

    def fill_one(self, ent_Q, keyword):
        # self.total = ent_Q.total
        self.ents = [EntSummary(ent_Q.entname, ent_Q.label)]
        self.keyword = keyword
