## Prerequisites

- Open the `settings.json` file in project directory and make sure you provide valid PANVIVA api settings and save the file.

    ```JSON
    {
        "BaseUrl" : "https://{correctEnvironment}.panviva.com", 
        "Instance" :"--Instance--",
        "ApiKey" : "--Api key--"
    }
    ```


- Make sure you have [Python](https://www.python.org/downloads/) v3.7 or grater installed in your system
    > you can check this by running the following command.
    ```
    python --version
    ```

## How to start the app

1. cd into project directory.

2. Preferably, create a virtual environment  and activate it. (This step is optional)
    ```
    python -m venv myEnv
    myEnv\Scripts\activate.bat
    ```

3. Next run this command to install all required packages.
    ```
    pip install -r requirements.txt
    ```
4. Next start the [Flask](https://flask.palletsprojects.com/en/1.1.x/) server by running this commands
    ```
    export FLASK_APP=app.py
    flask run
    ```

    > If you are on Windows, the environment variable syntax depends on command line interpreter.
    
    On [Command Prompt](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)

    ```
    set FLASK_APP=app.py
    flask run
    ```

    On [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)

    ```
    $env:FLASK_APP="app.py"
    flask run
    ```