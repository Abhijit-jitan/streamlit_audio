# import streamlit as st
# import sounddevice as sd
# import soundfile as sf
# import numpy as np
# import speech_recognition as sr

# def record_audio(duration):
#     sample_rate = 44100
#     frames = int(sample_rate * duration)

#     recording = sd.rec(frames, samplerate=sample_rate, channels=1, blocking=True)
#     recording = recording.squeeze()  # Remove unnecessary dimensions
#     recording /= np.abs(recording).max()  # Normalize the audio data
#     recording_scaled = np.int16(recording * 32767)  # Rescale and convert to 16-bit integer
#     return recording_scaled, sample_rate

# def save_audio(recording, sample_rate, filename):
#     sf.write(filename, recording, sample_rate)

# def speech_to_text(filename):
#     r = sr.Recognizer()
#     with sr.AudioFile(filename) as source:
#         audio = r.record(source)
#     try:
#         text = r.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         return "Could not understand audio"
#     except sr.RequestError as e:
#         return f"Error: {e}"

# def main():
#     st.title("Audio Recorder")

#     if st.button("Start Recording"):
#         duration = 5  # Specify the duration of the recording in seconds
#         st.write("Recording started. Please speak into your microphone.")
#         st.write("Mic is active now")
#         recording, sample_rate = record_audio(duration)
#         st.write("Recording finished.")

#         st.audio(recording, format='audio/wav', sample_rate=sample_rate)

#         #if st.button("Save Recording"):
#         filename = "voice.wav"  # Specify the filename for saving the recording
#         save_audio(recording, sample_rate, filename)
#         st.success(f"Recording saved as {filename}")

#         st.write("Converting speech to text...")
#         text = speech_to_text(filename)
#         st.write("Speech to text conversion finished.")
#         st.write(f"Text: {text}")

# if __name__ == '__main__':
#     main()





# import streamlit as st
# import sounddevice as sd
# import numpy as np
# import speech_recognition as sr

# def record_audio(duration):
#     sample_rate = 44100
#     frames = int(sample_rate * duration)

#     recording = sd.rec(frames, samplerate=sample_rate, channels=1, blocking=True)
#     recording = recording.squeeze()  # Remove unnecessary dimensions
#     recording /= np.abs(recording).max()  # Normalize the audio data
#     recording_scaled = np.int16(recording * 32767)  # Rescale and convert to 16-bit integer
#     return recording_scaled, sample_rate

# def speech_to_text(audio_data, sample_rate):
#     r = sr.Recognizer()
#     audio = sr.AudioData(audio_data.tobytes(), sample_rate, sample_width=2)  # Create audio data from numpy array
#     try:
#         text = r.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         return "Could not understand audio"
#     except sr.RequestError as e:
#         return f"Error: {e}"

# def main():
#     st.title("Audio Recorder")

#     if st.button("Start Recording"):
#         duration = 5  # Specify the duration of the recording in seconds
#         st.write("Recording started. Please speak into your microphone.")
#         st.write("Mic is active now")
#         recording, sample_rate = record_audio(duration)
#         st.write("Recording finished.")

#         st.audio(recording, format='audio/wav', sample_rate=sample_rate)

#         st.write("Converting speech to text...")
#         text = speech_to_text(recording, sample_rate)
#         st.write("Speech to text conversion finished.")
#         st.write(f"Text: {text}")

# if __name__ == '__main__':
#     main()




import streamlit as st
import sounddevice as sd
import numpy as np
import speech_recognition as sr

def record_audio(duration):
    sample_rate = 44100
    frames = int(sample_rate * duration)

    recording = sd.rec(frames, samplerate=sample_rate, channels=1, blocking=True)
    recording = recording.squeeze()  # Remove unnecessary dimensions
    recording /= np.abs(recording).max()  # Normalize the audio data
    recording_scaled = np.int16(recording * 32767)  # Rescale and convert to 16-bit integer
    return recording_scaled, sample_rate

def speech_to_text(audio_data, sample_rate):
    r = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), sample_rate, sample_width=2)  # Create audio data from numpy array
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {e}"

def main():
    st.title("Audio Recorder")

    if st.button("Start Recording"):
        duration = 5  # Specify the duration of the recording in seconds
        st.write("Recording started. Please speak into your microphone.")
        st.write("Mic is active now")
        recording, sample_rate = record_audio(duration)
        st.write("Recording finished.")

        st.audio(recording, format='audio/wav', sample_rate=sample_rate)

        st.write("Converting speech to text...")
        text = speech_to_text(recording, sample_rate)
        st.write("Speech to text conversion finished.")
        st.write(f"Text: {text}")

if __name__ == '__main__':
    main()
