import pyttsx3

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate:int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'{i + 1} Name : {voice.name},  Age : {voice.age}, ID : [{voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)
        print('I am speaking...')

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()


# voice - HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0


if __name__ == '__main__':
    tts = TextToSpeech('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0', 200, 1.0)
    # tts.list_available_voices()
    text = """
    Within the hour we’d arrived at Batavia Downs, an old-school harness
horse race track, the type where jockeys ride behind the horses in
lightweight buggies. My dad grabbed a racing form as soon we stepped
through the gate. For hours, the three of us watched him place bet after bet,
chain smoke, drink scotch, and raise holy hell as every pony he bet on
finished out of the money. With my dad raging at the gambling gods and
acting a fool, I tried to make myself as small as possible whenever people
walked by, but I still stuck out. I was the only kid in the stands dressed like
a Cub Scout. I was probably the only black Cub Scout they’d ever seen, and
my uniform was a lie. I was a pretender.
    """
    tts.text_to_speech(text)