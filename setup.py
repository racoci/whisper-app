from setuptools import setup, find_packages

setup(
    name='whisper-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'whisper @ git+https://github.com/openai/whisper.git',
        'librosa'
    ],
    author='Lucas Racoci',
    author_email='racoci.0@gmail.com',
    description='User interface for openai/whisper model',
    url='https://github.com/racoci/whisper-app',
)