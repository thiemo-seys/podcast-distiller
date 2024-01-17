# Wheels
## OpenAI Whipser
This library has no prepacked wheel, therefore we must create it ourselves so we lose less time when installing our dependencies.

### Creating the wheel

1. Install the dependencies to create wheels
```bash
"pip install wheel setuptools"
```
2. Clone the library repo
```bash
"git clone https://github.com/openai/whisper.git" 
```
3. Create the wheel
```bash
"python setup.py bdist_wheel"
```
