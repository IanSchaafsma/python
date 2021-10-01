import webbrowser 
import time
tijd = 1000
while tijd > 0:
    print(tijd)
    tijd = tijd -1
    time.sleep(0.01)
else:
    print("gefeliciteerd, je hebt je tijd vernaggeld!")
    webbrowser.open("https://www.youtube.com/watch?v=U_WLzCLZeJw&ab_channel=ColeTrain")