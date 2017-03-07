
class DataMidlayer():

    def __init__(self, DataEsDao):
        self.esDao = DataEsDao()

    def get_data(self, queryFilter):
        results = self.esDao.get_data(queryFilter)
        return self.format_results(results)


    def get_ports(self):
        results = self.esDao.get_ports()
        return self.format_results(results)

    def format_results(self, results):
        results = results.to_dict()
        data = []
        for result in results['hits']['hits']:
            data.append(result['_source'])
        return data
