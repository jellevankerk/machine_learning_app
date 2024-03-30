# How to start
1. Create a virtual environment `python -m venv .venv`
2. Install requerements `pip install -r requirements.txt`

## Run simple app
1. to start the application locally run `uvicorn simple:app --reload` the `--reload` makes it so that app gets restarted when the code gets altered
2. run a request e.g `http://127.0.0.1:8000/items/5?q=somequery` or `http://127.0.0.1:8000`

##  Run the Machine Learning app 
1. create a model by running `train_simple_model.py`
2. run `uvicorn machine_learning_app:app --reload --host 0.0.0.0`


##  Run the classification app 
1. run `uvicorn image_classifier_app:app --reload --host 0.0.0.0`
2. test if the api is hosted `http://localhost:8000/docs`
3. fill into browser `http://localhost:8000/classify?url=https://example.com/image.jpg`

## setup local network api
### Open port for firewall Windows
To allow a specific port (e.g., 8000) through the Windows Firewall:


Open Control Panel.
Go to System and Security > Windows Defender Firewall.
On the left, click on Advanced settings. This opens the Windows Defender Firewall with Advanced Security window.
In the left pane, click on Inbound Rules.
On the right, click on New Rule....
Select Port and then click Next.
Ensure TCP is selected and specify the specific port (8000) in the "Specific local ports" field, then click Next.
Choose Allow the connection and click Next.
Leave all the profiles checked or select specific profiles (Domain, Private, Public) as per your requirement, then click Next.
Give the rule a name (e.g., "FastAPI Port 8000") and an optional description, then click Finish.

## Test api connection other devices
1. look up the ip adress of the device you are using to run the api wiht `ipconfig` (look for IPv4)

2. replace the `localhost` with the IPv4 adrres you foind

## API options 
- `/` returns hello world json 
- `classify` GET http://localhost:8000/classify?url=https://example.com/image.jpg
