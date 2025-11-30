# mini-rag

- This is a minimal implemntation

## Requirements

- Python 3.8 or later

#### Install Python using Conda

1. Download and install anaconda From
2. create a new enviroment using the following command:

```bash
$ conda create -n mini-rag python=3.8
```

3. Activate the enviromnet :

```bash
$ conda activate mini-rag
```

## Installation

### Install the required packages 

```bash 
$ pip install -r requirements.txt
```
### setup the enviroment variables

```bash
$ cp .env.example .env
```

Set your enviroment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection 

Download the POSTMAN collection from [assets/mini-rag-app.postman_collection.json](assets/mini-rag-app.postman_collection.json)