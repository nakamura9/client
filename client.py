import json
import sys

from cefpython3 import cefpython as cef

CONFIG = None
with open("config.json", "r") as f:
    CONFIG  = json.load(f)

def main():
    sys.excepthook = cef.ExceptHook

    cef.Initialize()
    cef.CreateBrowserSync(url=CONFIG["serverHost"],
                        window_title="Suave Business Tools")

    cef.MessageLoop()
    cef.Shutdown()


if __name__ == "__main__":
    main()