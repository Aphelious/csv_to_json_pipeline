from elasticsearch import Elasticsearch, helpers
# from pandas import json_normalize
# from faker import Faker
# fake = Faker()


# Connection and configuration for Elasticsearch/Kibana:
host = 'https://localhost:9200'
ELASTIC_PASSWORD = "password"
cert = cert_path

es = Elasticsearch(host, ca_certs=cert, basic_auth=("elastic", ELASTIC_PASSWORD))


#########################################################################################################


# Inserting a single record into Elasticsearch:

# doc = {
#     "name": fake.name(),
#     "street": fake.street_address(),
#     "city": fake.city(),
#     "zip": fake.zipcode()
# }
#
# res = es.index(index="people", body=doc)    ## Index method is used to write a single record
# print(res['result'])    ## This prints a confirmation message whether the record was successfully written or not


#########################################################################################################


# Inserting many records via the helpers.bulk method:
#
# actions = [
#     {
#     "_index": "people",   ## Column names are preceded with an underscore
#     "_source": {
#         "name": fake.name(),
#         "street": fake.street_address(),
#         "city": fake.city(),
#         "zip": fake.zipcode()
#     }
# }
#     for x in range(998)   ## or for i, r in df.iterrows() - This is the second element in the list
# ]
#
# res = helpers.bulk(es, actions)


#########################################################################################################


# Querying Elasticsearch:
# query = {"match":{"name": "Ashley Morgan"}}
# res = es.search(index="people", size=10, query=query)
# for doc in res['hits']['hits']:
#     print(doc['_source'])


#########################################################################################################


## Print all records returned by a search, accessed at res['hits']['hits']['_source]:
# print(res['hits']['hits']['_source])


#########################################################################################################


# # Can loop through records for more readability:
# for doc in res['hits']['hits']:
#     print(doc['_source'])


#########################################################################################################


## Can load results of a query into Pandas df using json_normalize():
# df = json_normalize(res['hits']['hits'])  ## Remember to import: from pandas import json_normalize
# print(df.head())


#########################################################################################################


## Can 'scroll' through records with a while loop:

# res = es.search(
#   index='people',
#   scroll='20m',
#   size=50,
#   query={"match_all":{}}
# )
# for search_doc in res['hits']['hits']:
#     print(search_doc['_source'])
# sid = res['_scroll_id']
# size = res['hits']['total']['value']
#
# # Start scrolling
#
# while size > 0:
#     print(size)
#     print("--------------------------------------------")
#     res = es.scroll(scroll_id = sid, scroll = '20m')
#
#     sid = res['_scroll_id']
#     size = len(res['hits']['hits'])
#
#     for doc in res['hits']['hits']:
#         print(doc['_source'])