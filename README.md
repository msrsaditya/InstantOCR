## Clone this repository

```cd /path/to/project```

```git clone https://github.com/msrsaditya/InstantOCR```

## Install Dependencies

```brew install tesseract```

#### Create a Virtual Environment

```python3 -m venv venv```

```source venv/bin/activate```

#### Install Flask Framework

```pip install flask```

## Run the Flask Server

```python3 app.py```

- Go to [Local Host](http://localhost:5000/) in Your Browser.
- For the TTS Engine to Work, You Need to be Running MacOS.
- If no output is visible, it means the OCR failed in recognizing the text.
- The OCR can't recognize handwritten text, it only works well with printed text.
