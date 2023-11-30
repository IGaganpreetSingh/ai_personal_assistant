
import pvporcupine
import struct
import pyaudio
import time

def wake():
    porcupine = None
    pa = None
    audio_stream = None
    
    print("J.A.R.V.I.S. version 1.2 - Online and Ready!")
    print("*******************************************************")
    print("J.A.R.V.I.S.: Awaiting for your call")
    
    try: 
        porcupine = pvporcupine.create(keywords=["jarvis", "computer"], access_key= "NtqEZ0ofxQDO9uv4K3H/tZrj9lrgMsBLU4LOgmIFQrb7nnEDHqNBkQ==")
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate = porcupine.sample_rate,
            channels = 1,
            format = pyaudio.paInt16,
            input = True,
            frames_per_buffer= porcupine.frame_length
        )
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword Detected..", end = "")
                time.sleep(1)
                print("J.A.R.V.I.S.: Awaiting for your call")
    
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()

