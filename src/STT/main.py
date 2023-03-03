import speech_recognition as sr


def getRequest():
    while True:
        listener = sr.Recognizer()

        with sr.Microphone() as raw_voice:

            try:
                print("조정중..........")
                listener.adjust_for_ambient_noise(raw_voice)

                # adjust setting values
                listener.dynamic_energy_adjustment_damping = 0.2
                listener.pause_threshold = 0.6
                listener.energy_threshold = 600

                print("음성 인식 시작!")
                audio = listener.listen(raw_voice)

                voice_data = listener.recognize_google(audio, language='ko')
                print("음성 인식 종료!")
                return voice_data

            except UnboundLocalError:
                pass

            except sr.UnknownValueError:
                print("could not understand audio")
