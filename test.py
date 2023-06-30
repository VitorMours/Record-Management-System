import pyautogui
from time import sleep
class TestAutomation:
    def __init__(self):
        pass

    def initiate(self):
        sleep(1)
        pyautogui.moveTo(113,126,3)

    def get_positions(self):
        while True:
            pass


if __name__ == "__main__":
    tests = TestAutomation()
    tests.initiate()