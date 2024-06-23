import json
from elasticsearch import Elasticsearch

def load_docs(file):

    with open(file, 'rt') as f_in:
        documents_file = json.load(f_in)

    documents = []

    for course in documents_file:
        course_name = course['course']

        for doc in course['documents']:
            doc['course'] = course_name
            documents.append(doc)

    return documents

def check_es_connection(es_host):
    es = Elasticsearch(es_host)
    es.info()

def create_index(es_host, documents):    
    es = Elasticsearch(es_host)
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"} 
            }
        }
    }

    index_name = "course-questions"
    response = es.indices.create(index=index_name, body=index_settings)

    print(response)

    for doc in documents:
        es.index(index=index_name, document=doc)


def main():
    documents = load_docs(file="./documents.json")
    print(check_es_connection(es_host="http://elasticsearch:9200"))
    create_index(es_host="http://elasticsearch:9200",documents=documents)


if __name__ == "__main__":
    main()