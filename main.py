# ================================================================
# Assignment 07: Text-to-Speech with Piper
# ================================================================

# Step 1: Install dependencies before running (in terminal)
# pip install piper-tts soundfile

# Step 2: Import required libraries
from piper import PiperVoice
import wave
import soundfile as sf
import winsound

# Step 3: Configuration - Choose your language and voice model
# Available models: "vi" for Vietnamese, "en" for English
LANGUAGE = "en"  # Change to "en" for English

# Voice model paths
VOICE_MODELS = {
    "vi": "vi_VN-vais1000-medium.onnx",      # Vietnamese voice
    "en": "en_US-lessac-medium.onnx"      # English voice
}

# Step 4: Prepare input text
text = "Vòng lặp vô hạng trong ngôn ngữ lập trình và ứng dụng của nó là gì?" if LANGUAGE == "vi" else \
    "What is an infinite loop in the Python programming language and its applications?"
print("=" * 70)
print("Text-to-Speech with Piper")
print("=" * 70)
print(f"Language: {LANGUAGE.upper()}")
print(f"Input text: {text}")

# Step 5: Load the selected Piper voice model
print(f"\nLoading {LANGUAGE.upper()} voice model...")
voice_path = VOICE_MODELS[LANGUAGE]
print(f"  Model: {voice_path}")

try:
    voice = PiperVoice.load(voice_path)
    print("  ✅ Voice model loaded successfully!")
except Exception as e:
    print(f"  ❌ Error: Could not load {voice_path}")
    print(f"     {e}")
    print(f"\n  Please ensure:")
    print(f"  1. Download the model from: https://github.com/rhasspy/piper/releases")
    print(f"  2. Place both .onnx and .onnx.json files in this directory")
    exit(1)

# Step 6: Synthesize speech using Piper
output_file = f"output_{LANGUAGE}.wav"
print(f"\nGenerating speech and saving to '{output_file}'...")

# Synthesize speech and write to WAV file
with wave.open(output_file, "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

# Step 7: Get audio info
audio_data, sampling_rate = sf.read(output_file)

# Step 8: Play the audio (Windows only)
print("Playing audio...")
winsound.PlaySound(output_file, winsound.SND_FILENAME)

print("\n" + "=" * 70)
print("✅ Text-to-Speech completed successfully!")
print("=" * 70)
print(f"📁 Output file: {output_file}")
print(f"📊 Duration: {len(audio_data) / sampling_rate:.2f} seconds")
print(f"🔊 Sampling rate: {sampling_rate} Hz")
print("\nYou can now play the audio file in any media player!")
