# VoiceExample - Text-to-Speech with Piper

A Python application that demonstrates text-to-speech synthesis using the Piper TTS engine. This project supports both English and Vietnamese voice synthesis with high-quality neural voice models.

## 🎯 Features

- **Multi-language Support**: English and Vietnamese text-to-speech
- **High-Quality Voices**: Uses neural voice models for natural-sounding speech
- **Easy Configuration**: Simple language switching via configuration
- **Audio Playback**: Automatic audio playback on Windows
- **File Output**: Saves synthesized speech as WAV files

## 📋 Prerequisites

- Python 3.8 or higher
- Windows operating system (for audio playback functionality)
- Internet connection (for downloading voice models)

## 🚀 Quick Start

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd VoiceExample
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Voice Models

The project requires voice model files. Download them from the [Piper releases page](https://github.com/rhasspy/piper/releases):

**For English:**
- Download `en_US-lessac-medium.onnx`
- Download `en_US-lessac-medium.onnx.json`

**For Vietnamese:**
- Download `vi_VN-vais1000-medium.onnx`
- Download `vi_VN-vais1000-medium.onnx.json`

Place all downloaded files in the project root directory.

### 4. Run the Application

```bash
python main.py
```

## ⚙️ Configuration

### Language Selection

Edit the `LANGUAGE` variable in `main.py`:

```python
LANGUAGE = "en"  # For English
# or
LANGUAGE = "vi"  # For Vietnamese
```

### Custom Text

Modify the `text` variable in `main.py` to synthesize your own text:

```python
text = "Your custom text here"
```

## 📁 Project Structure

```
VoiceExample/
├── main.py                              # Main application file
├── requirements.txt                     # Python dependencies
├── README.md                           # This file
├── en_US-lessac-medium.onnx            # English voice model
├── en_US-lessac-medium.onnx.json       # English voice config
├── vi_VN-vais1000-medium.onnx          # Vietnamese voice model
├── vi_VN-vais1000-medium.onnx.json     # Vietnamese voice config
├── output_en.wav                       # Generated English audio
└── output_vi.wav                       # Generated Vietnamese audio
```

## 🔧 Dependencies

- **piper-tts**: Core text-to-speech engine
- **soundfile**: Audio file handling
- **langdetect**: Language detection utilities
- **numpy**: Numerical operations

## 📖 Usage Examples

### Basic Usage

```python
from piper import PiperVoice
import wave

# Load voice model
voice = PiperVoice.load("en_US-lessac-medium.onnx")

# Synthesize text
text = "Hello, this is a text-to-speech example!"
with wave.open("output.wav", "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)
```

### Switching Languages

```python
# For English
LANGUAGE = "en"
text = "What is an infinite loop in programming?"

# For Vietnamese
LANGUAGE = "vi"
text = "Vòng lặp vô hạn trong lập trình là gì?"
```

## 🎵 Output

The application generates:
- **Audio files**: `output_en.wav` or `output_vi.wav`
- **Console output**: Processing status and audio information
- **Automatic playback**: Audio plays automatically on Windows

## 🛠️ Troubleshooting

### Common Issues

1. **Model Loading Error**
   ```
   Error: Could not load voice model
   ```
   **Solution**: Ensure both `.onnx` and `.onnx.json` files are in the project directory.

2. **Missing Dependencies**
   ```
   ModuleNotFoundError: No module named 'piper'
   ```
   **Solution**: Run `pip install -r requirements.txt`

3. **Audio Playback Issues**
   - Ensure you're running on Windows
   - Check that audio output is working
   - Verify the generated WAV file exists

### Getting Help

- Check the [Piper TTS documentation](https://github.com/rhasspy/piper)
- Verify your Python version: `python --version`
- Ensure all dependencies are installed: `pip list`

## 📝 License

This project is for educational purposes. Please check the license terms of the Piper TTS engine and voice models.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📚 Additional Resources

- [Piper TTS GitHub Repository](https://github.com/rhasspy/piper)
- [Piper Voice Models](https://github.com/rhasspy/piper/releases)
- [Text-to-Speech Documentation](https://github.com/rhasspy/piper/wiki)

---

**Note**: This project is designed for Windows systems. For other operating systems, you may need to modify the audio playback functionality.
