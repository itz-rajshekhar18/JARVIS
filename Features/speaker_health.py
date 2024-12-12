import numpy as np
import pyaudio
import time
from scipy import signal
from TextToSpeech.Fast_DF_TTS import speak

def play_tone(frequency, duration=2, volume=0.5, sample_rate=44100):
    """Plays a single tone of a specific frequency through a speaker ."""
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    
    audio_data = (tone * volume * 32767).astype(np.int16)
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    
    stream.write(audio_data.tobytes())
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
def play_sweep(duration=5, volume=0.5, sample_rate=44100, start_freq=20, end_freq=20000):
    """Plays a frequency sweep from start_freq to end_freq throught the speaker. Useful for testing the full frequency range of the speaker."""
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    sweep = signal.chirp(t, start_freq, t[-1], end_freq, method='logarithmic')
    
    audio_data = (sweep * volume * 32767).astype(np.int16)
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    
    stream.write(audio_data.tobytes())
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
def speaker_health_test():
    """This function plays different tones and sweeps to test the speaker's health. It returns a speaker health percentage based on the tone coverage."""
    
    speak("Playing test tones...")
    health_score = 0
    
    speak("Playing 100Hz tone...")
    play_tone(100, duration=2)
    time.sleep(1)
    health_score += 25
    
    speak("Playing 1000 Hz tone...")
    play_tone(1000, duration=2)
    time.sleep(1)
    health_score += 25
    
    speak("Playing 5000 Hz tone...")
    play_tone(5000, duration=2)
    time.sleep(1)
    health_score += 50
    
    speak("Playing 10,000 Hz tone...")
    play_tone(10000, duration=2)
    time.sleep(1)
    health_score += 15
    
    speak("Playing freuency sweep from 20 Hz to 20,000 Hz...")
    play_sweep(duration=5)
    time.sleep(1)
    health_score += 15
    
    speak("\nSpeaker health test complete.")
    
    speak(f"\nSpeaker Health: {health_score}%")
    if health_score == 100:
        speak("The speaker is in excellent condition!")
    elif 80 <= health_score < 100:
        speak("The speaker is in good condition.")
    elif 60 <= health_score < 80:
        speak("The speaker is in ab=verage condition")
    else:
        speak("The speaker might be in poor condition.")