import pyautogui
import json
import datetime
import requests
import time
import threading
from lib.email import Email

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

em = Email() # sending email

# https://pyautogui.readthedocs.io/en/latest/
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

cDate = datetime.datetime.now() 

SAVED_DATA = "./settings/settings.json"

def save_data(data):
    with open(SAVED_DATA, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            return  json.load(f)
    except:
        return {}

def sendEmail():
    html = f"""
        <html>
            <body>
                <h2>Date: {f"{cDate.month} / {cDate.day} / {cDate.year}"}</h2>
                <h2>Time: {cDate.strftime('%Y/%m/%d %I:%M:%S')} </h2>
            </body>
        </html>
    """

def checkForCcleaner():
    print("ccleaner")


def checkForMalwareBytes():
    print("MalwareBytes")


def downLoadCcleaner(): # downloading ccleaner
    url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
  
    # URL of the image to be downloaded is defined as image_url
    r = requests.get(url) # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open("python_logo.png",'wb') as f:
    
        # Saving received content as a png file in
        # binary format
    
        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)


def downLoadMalwareBytes(): # downloading ccleaner
    url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
  
    # URL of the image to be downloaded is defined as image_url
    r = requests.get(url) # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open("python_logo.png",'wb') as f:
    
        # Saving received content as a png file in
        # binary format
    
        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)


def mainProgram():
    print("placeholder")


def runFirst():
    data  = load_data(SAVED_DATA)

    if data["computer-name"] == None:

        computerName = input("input computer:\t")

        settings = {
            "program-version": "0.0.1",
            "computer-name": computerName,
            "date": f"{cDate.month} / {cDate.day} / {cDate.year}",
            "time": cDate.strftime('%Y/%m/%d %I:%M:%S')
        }

        print("\n\nSaving\n\n")
        save_data(settings)
        time.sleep(1.05)
        print("\n\nSaved\n\n")
        time.sleep(1.05)
        mainProgram()

    else:
        mainProgram()


if __name__ == "__main__":
    runFirst()