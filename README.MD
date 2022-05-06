#### Python and Visual C++ Setup

1. Install [Python 3.10.1+ (64-bit)](https://www.python.org/downloads/windows/).
2. (possibly optional) Install [Visual C++ 14.0 build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools).
   Make sure to select **C++ build tools** in the setup screen.

#### Virtual Environment Setup

Execute the following commands to create a virtual environment:

```
$ py -3.10 -m venv .env
$ .env\Scripts\activate.bat
$ pip install -r requirements.txt
$ python setup.py develop
```


#### Running the Script
 
 1. Open `gstiming\timing_test.py` in an editor
 2. Modify parameters at the top of the file to best simulate a spectrum
 3. Run the timing_test.py, results printed to the console