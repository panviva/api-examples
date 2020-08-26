# get-doc-direct-api

## Prerequisites

- Open the `settings.json` file in project directory and make sure you provide valid PANVIVA api settings and save the file.

    ```JSON
    {
        "BaseUrl" : "https://{correctEnvironment}.panviva.com", 
        "Instance" :"--Instance--",
        "ApiKey" : "--Api key--"
    }
    ```

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
