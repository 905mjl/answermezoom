import speech_recognition as sr
snow_path = "C:\\Users\\mlf05\\Desktop\\answermezoom"
jarv_path = "C:\\Users\\mlf05\\Desktop\\answermezoom\\snowboy\\resources\\models\\jarvis.umdl"
r = sr.Recognizer()
m = sr.Microphone()
r.pause_threshold = .7
keyword = "hey computer"

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source:
            audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            val_str = format(value)
            if keyword in val_str:
                print("keyword detected")
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
