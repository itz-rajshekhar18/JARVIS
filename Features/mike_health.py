import pyaudio
import numpy as np
import time 
from TextToSpeech.Fast_DF_TTS import speak

def get_mic_health(second = 5 , initial_threshold = 500):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    audio = pyaudio.PyAudio()
    
    stream = audio.open(format = FORMAT, channels = CHANNELS,
                        rate = RATE, input = True,
                        frames_per_buffer=True)
    
    print(f"Recording for {second} seconds...")
    time.sleep(1)
    
    sound_count = 0
    total_samples = 0
    noise_floor = 0
    clipping_count = 0
    signal_sum = 0
    noise_sum = 0
    freq_analysis = []
    
    for _ in range(0,int(RATE/CHUNK * seconds)):
        data = np.frombuffer(stream.read(CHUNK),dtype = np.int16)
        volume = np.linalg.norm(data)
        
        freqs = np.fft.fftfreq(len(data))
        fft_spectrum = np.abs(np.fft.fft(data))
        freq_analysis.append(fft_spectrum)
        
        noise_floor = max(noise_floor, np.mean(np.abs(data)) * 1.5)
        
        dynamic_threshold = max(initial_threshold, noise_floor)
        
        if volume > dynamic_threshold:
            sound_count += 1
            signal_sum += volume
        else:
            noise_sum += volume
            
        if np.max(np.abs(data)) >= 32767:
            clipping_count += 1
            
        total_samples += 1
    
    mic_health = (sound_count/ total_samples) * 100
    avg_signal = signal_sum / max(1,sound_count)
    avg_noise = noise_sum/ max(1,(total_samples - sound_count))
    snr = 10 * np.log10(avg_signal / max(1,avg_noise))
    avg_clipping = (clipping_count / total_samples) * 100
    
    avg_fft_spectrum = np.mean(freq_analysis, axis=0)
    freq_range_coverage = np.mean(avg_fft_spectrum > np.median(avg_fft_spectrum)) * 100
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    health_report = {
        'Microphone Health (%)' : mic_health,
        'Average Signal-to-Noise Ratio (dB)' : snr,
        'Clipping percentage (%)' : avg_clipping,
        'Frequency Range coverage (%)' : freq_range_coverage
    }
    
    return health_report

def mike_health():
    health_metrics = get_mic_health(second=5)
    for metric, value in health_metrics.items():
        speak(f"{metric} : {value:.2f}")
        