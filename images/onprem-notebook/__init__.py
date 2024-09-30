import IPython.display as ipd
from rtboost import audio as rtaudio
from pathlib import Path

def play(audio_p, st=None, ed=None):
    
    """
    st, ed : (sec)
    """
    
    if not isinstance(audio_p, Path):
        audio_p = Path(audio_p)
    
    assert audio_p.exists()
    
    audio, sr = rtaudio.load(audio_p)    
    print(sr)
    if st is not None:
        audio = audio[int(st * sr): int(ed * sr)]
    audio = ipd.Audio(audio, rate=sr)
    ipd.display(audio)
    
def play_record(record, sr=8000):
    wav = record[0].wav
    audio, sr = rtaudio.load(wav, sr=sr)
    for utt in record:
        audio_seg = audio[int(sr * utt.st) : int(sr * utt.ed)]
        audio_seg = ipd.Audio(audio_seg, rate=sr)
        display(audio_seg)
        print(utt.text)
def play_utterance(utt, sr=8000):
    audio, sr = rtaudio.load(utt.wav, sr=sr)
    audio_seg = audio[int(sr * utt.st) : int(sr * utt.ed)]
    audio_seg = ipd.Audio(audio_seg, rate=sr)
    display(audio_seg)
    print(utt.text)