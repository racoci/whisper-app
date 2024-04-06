from flet import *
import sounddevice as sd
import scipy.io.wavfile as wav
import requests

BASE_URL = "http://127.0.0.1:8000"


def main(current_page: Page):
    def on_record_click(e):
        current_page.snack_bar = SnackBar(
            Text("Começe a gravar agora...", size=20, weight=FontWeight.BOLD),
            bgcolor="blue"
        )
        current_page.open = True
        current_page.update()

        freq = 44100
        duration = 5
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait()
        file_name = "recording.wav"
        wav.write(file_name, freq, recording)
        url = f'{BASE_URL}/api/upload-audio/'
        files = {'file': ('recording.wav', open(file_name, 'rb'), 'audio/wav')}
        response = requests.post(url, files=files)
        print(response.status_code)

    current_page.add(
        Column([
            Text("Grave um audio", size=30, weight=FontWeight.BOLD),
            Divider(),
            Text("Grave um audio de 5 segundos", size=20, weight=FontWeight.BOLD),
            ElevatedButton("Grave Aqui", bgcolor="red", color="white", on_click=on_record_click)
        ])
    )


app(target=main)
