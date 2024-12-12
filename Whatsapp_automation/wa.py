import pywhatkit as kit
import datetime
from TextToSpeech.Fast_DF_TTS import speak
from os import getcwd

now = datetime.datetime.now()
hour = now.hour
minute = now.minute

def clear_file():
    with open(f"{getcwd()}\\input.txt","w") as file:
        file.truncate(0)
        
raj = "+8448223378"

def send_msg_wa():
    speak("who do you wanna send the message sir ?")
    output_txt = ""
    while True:
        with open("input.txt","r") as file:
            input_txt = file.read().lower()
        if input_txt != output_txt:
            output_txt = input_txt
            if  output_txt.startswith("send to") or output_txt.startswith("send tu"):
                output_txt.replace("send tu","")
                output_txt.replace("send to","")
                if "raj" in output_txt:
                    speak("By the way what is the message for raj , sir ??")
                    while True:
                         with open("input.txt","r") as file:
                             input_txt = file.read().lower()
                             if output_txt != input_txt:
                                output_txt = input_txt
                                if output_txt.startswith("message is"):
                                    message = output_txt.replace("message is","")
                                    kit.sendwhatmsg(raj,message,hour,minute+1)
                                    speak("message send successfully")
                                 