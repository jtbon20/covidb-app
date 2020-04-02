from selenium import webdriver
from signal import signal, SIGINT
from bs4 import BeautifulSoup
import sys
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def handler():
    driver.close()

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)
    if len(sys.argv) >= 2 and sys.argv[1] == "-h":
        print("Usage:"
              "no args: runs on cached values\n"
              "-h: help\n"
              "-d location of the chrome driver"
              "-c location of the credentials file.")
        sys.exit()
    if "-c" in sys.argv:
        cred = sys.argv[sys.argv.index("-c")+1]
    if "-d" in sys.argv:
        driver_location = sys.argv[sys.argv.index("-d")+1]


    options=webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path=driver_location, options=options)
    driver.get("https://www.arcgis.com/apps/opsdashboard/index.html#/5c7f096096ed482395f6a626150366e2")
    time.sleep(5);
    cred = credentials.Certificate(cred)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    html = BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), features="html.parser")
    text = html.find_all('text')
    res = []
    for t in text:
        res.append(t.contents[0])
    doc_ref = db.collection(u'Live Case Data').document('current')
    doc_ref.set(
        {
            res[0]:res[1],
            res[2]:res[3],
            res[4]:res[5]
        }
    )
    driver.close()
