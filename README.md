# Audio Extraction Tool
Simple Python script to extract audio from videos

## Getting started

1. Make sure you have Python and Git installed on your computer
2. Clone the repository and navigate into the project root
    ```bash
    $ git clone https://github.com/nc1z/audio-extraction-tool.git
    $ cd audio-extraction-tool/
    ```
2. Run the command

    ```bash
    $ pip install moviepy
    ```

3. Place your mp4 videos into `./input`
4. Run the command

    ```bash
    $ python main.py
    ```
5. The extracted audio files will be found in `./output`

## Audio sampling

You might want to split the extracted audio into multiple parts for sampling purposes (e.g. training AI voice models or like <a href="https://github.com/neonbjb/tortoise-tts">Tortoise-tts</a>)

1. Set `num_parts` in `split-audio-sampling.py` to your desired number of samples
2. Run the command

    ```bash
    $ python split-audio-sampling.py
    ```

## Clean up

You might want remove the `output_samples/` directory after you are done saving the sample audio files. Simply run the command:

```bash
$ python split-audio-sampling.py
```

