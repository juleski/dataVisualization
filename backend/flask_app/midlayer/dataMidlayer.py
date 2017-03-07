
class DataMidlayer():

    def __init__(self, DataEsDao):
        self.esDao = DataEsDao()

    def get_data(self, queryFilter):
        results = self.esDao.search(queryFilter)
        results = results.to_dict()
        data = []

        for result in results['hits']['hits']:
            data.append(result['_source'])
        return data

    def get_ports(self):
        results = self.esDao.get_ports()
        results = results.to_dict()
        data = []
        for result in results['hits']['hits']:
            data.append(result['_source'])
        return data