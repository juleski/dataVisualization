from dataEsDao import *

class DataMiddleware():

    def get_data(self, queryFilter):
        esClass = DataEsDao()
        results = esClass.search(queryFilter)
        results = results.to_dict()
        data = []

        for result in results['hits']['hits']:
            data.append(result['_source'])
        return data