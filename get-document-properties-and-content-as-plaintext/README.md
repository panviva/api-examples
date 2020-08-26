# get-document-properties-and-content-as-plaintext

A simple Python example to show how to get the metadata and content of a document from Panviva's APIs, utilizing `GET Document` and `GET Document Containers`

## Prerequisites

### Configure Application

You will require `instance name` and `API key` from the [previous instructions](../README.md#how-to-get-credentials)
Entered the acquired credentials in the configuration file (`config.ini`)

### Setup Python Virutal Environment and Install required packages

Change Directory into the folder this README is contained.

```bash
virtualenv venv # Create a python virutal environment folder named `venv`, to hold python interpreter, pip and python packages
source venv/bin/activate # activate your virutal environment in current shell
pip install -r requirements.txt # install all required python packages into virtual environment
```

## Running the Application

```bash
# Assuming you've activated your virtual environment (source venv/bin/active)
python app.py
```
