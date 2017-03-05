from ..dao.ESDao import ESDao

class MiddlewareData():

    def get_data(self, queryFilter):
        esClass = ESDao()
        results = esClass.search(queryFilter)
        results = results.to_dict()
        data = []

        for result in results['hits']['hits']:
            data.append(result['_source'])
        return data