import sounddevice as sd
import numpy as np

threshold = 80.0
Clap = False

def detect_clap(indata,frames,time,status):
    global Clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        print("clapped!")
        Clap = True

def Listen_for_claps():
    with sd.InputStream(callback= detect_clap):
        return sd.sleep(1000)
    
if __name__ == "__main__":
    while True:
        Listen_for_claps()
        if Clap == True:
            break
        
        else:
            pass
        
    