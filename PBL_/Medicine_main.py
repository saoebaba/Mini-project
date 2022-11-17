import time
from plyer import notification

def Medicine(name,message):
    notification.notify(
        title=name,
        message=message,
        app_icon="D:\PBL_\Icons-Land-Medical-People-Doctor-Male.ico",
        timeout=5,
    )

def drinkwater(name,message):
    notification.notify(
        title=name,
        message=message,
        app_icon="D:\PBL_\icon.ico.ico",
        timeout=5,
    )
def work(name,message):
    notification.notify(
        title=name,
        message=message,
        app_icon="D:\PBL_\Vcferreira-Firefox-Os-Clock.ico",
        timeout=5,
    )
if __name__ == '__main__':
    while True:
        Medicine("Medicine reminder","Paracetamol\nTake your medicine on time")
        time.sleep(6)
        drinkwater("Drink Water","Hey user it's time to drink some water!!!")
        time.sleep(20)
        work("Take Break !!!","Hey user you are working continuously make some walk")
        time.sleep(30)