import random

class DataGenerator:

    def __init__(self):
        pass

    def get_sample_data(self):
        records = []
        for i in range(10):
            records.append(self.create_sample_record())
        return records

    def create_sample_record(self):
        datadict = {}
        datadict["customer"] = random.randint(1,4)
        datadict["revenue"] = random.randint(200, 1000)
        return datadict


