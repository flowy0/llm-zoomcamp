

Create the python env
```
micromamba create -n llmzoomcamp python=3.10 -c conda-forge
micromamba activate llmzoomcamp
micromamba install tqdm notebook==7.1.2 openai elasticsearch -c conda-forge
```

Run Jupyter notebook
```
micromamba run jupyter notebook
```

Run Elastic Search using Docker
```
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
 ``` 


Download the documents using this command
```
wget https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json
```

# Docker Compose

I have modified the docker compose from https://github.com/alexeygrigorev/llm-rag-workshop/tree/main to run streamlit and an additional indexer.

Use the docker compose file to run the following, ollama, elasticsearch, streamlit, indexer.
- run `docker compose up`
- Current workarounds:
  - At the moment, the indexing and ollama model pull is done manually
  - Run the following commands inside the docker container once its up
    - for the container `indexer` 
        ```
          docker exec -it indexer bash
          python create_index.py
        ```
    - for container ollama, 
        ```
        docker exec -it ollama
        ollama pull llama3
        ```
- Access the UI at http://localhost:8501

