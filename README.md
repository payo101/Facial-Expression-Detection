![Made-In-Python](https://img.shields.io/badge/Made%20In-PYTHON-green?style=for-the-badge&logo=appveyor)

- [About](#about)
  - [Libraries/Modules](#librariesmodules)
- [Pre-Requisites](#pre-requisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributor(s)](#contributors)
# About
The Facial Expression Recognizer detects and classifies the expression of the human face either in a pre-recorded video or a live stream from the camera. As of now, It is capable to recognize 7 different expressions:-
1. **Anger**
2. **Disgust**
3. **Fear**
4. **Happy**
5. **Neutral**
6. **Sad**
7. **Surprised**

This has been trained on the [FER 2013 Dataset](https://www.kaggle.com/msambare/fer2013?select=train).

The architecture of the model is as follows:

## Libraries/Modules
- Python
- Keras
- OpenCV
- Numpy
# Pre-Requisites
**Do install these before running the script**
- Python 3.7+
- Tensorflow
- OpenCV
- Numpy
# Installation
1. First clone the project
```bash
git clone https://github.com/payo101/Facial-Expression-Detection.git
```
1. Start the script
```bash
python3 camera.py
```
# Usage
By Default, It has been programmed to work for live stream. One needs a working camera for that purpose.
# Contributor(s)
1. Piyus Kumar Rout
