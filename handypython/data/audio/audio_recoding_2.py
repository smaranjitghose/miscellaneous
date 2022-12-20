# pip install pvrecorder wave struct
# Can read one read one channel and 16kHz samples.
from pvrecorder import PvRecorder
import wave, struct 
import pathlib

# device_index = -1; default microphone
# To check for other microphones: devices = PVRecorder.get_audio_devices()

# Initialize a PvRecorder object
recorder = PvRecorder(device_index=-1, frame_length=512) #(32 milliseconds of 16 kHz audio)
audio = []

WORK_DIR = pathlib.Path(__file__).parent.absolute()
INPUT_DIR = WORK_DIR / "input"
INPUT_DIR.mkdir(exist_ok=True)
FILE_PATH = INPUT_DIR / "recording.wav"

try:
    # Start the recording from the selected microphone
    recorder.start()
    while True:
        frame = recorder.read()
        audio.extend(frame)
except KeyboardInterrupt:
    # Stop recording from the selected microphone
    recorder.stop()
    # Save the recording as a wav file
    with wave.open(FILE_PATH, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))
finally:
    # Clear the Recorder object from memory
    recorder.delete()
