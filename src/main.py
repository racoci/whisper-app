from flet import *
import flet.fastapi as flet_fastapi
import sounddevice as sd
import scipy.io.wavfile as wav
import requests
import mimetypes
import logging

BASE_URL = "http://127.0.0.1:8001"

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def main(current_page: Page):
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

        # Read file content
        with open(file_name, 'rb') as f:
            file_content = f.read()

        # Determine file mime type
        mime_type, _ = mimetypes.guess_type(file_name)
        mime_type = mime_type or 'application/octet-stream'

        headers = {'Content-Disposition': f'form-data; name="file"; filename="{file_name}"'}
        # Construct multipart/form-data payload
        files = {
            'file': (
                file_name,
                file_content,
                mime_type,
                headers
            )
        }

        # Log the request details
        logger.debug("Sending POST request to: %s", BASE_URL + "/api/upload-audio/")
        logger.debug("Request headers: %s", headers)

        # Send the request with the constructed payload
        response = requests.post(BASE_URL + "/api/upload-audio/", files=files, headers=headers)

        logger.debug("Response status code: %d", response.status_code)

    current_page.add(
        Column([
            Text("Grave um audio", size=30, weight=FontWeight.BOLD),
            Divider(),
            Text("Grave um audio de 5 segundos", size=20, weight=FontWeight.BOLD),
            ElevatedButton("Grave Aqui", bgcolor="red", color="white", on_click=on_record_click)
        ])
    )


app = flet_fastapi.app(main)
