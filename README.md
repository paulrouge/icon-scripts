# scripts using pyenv

## created a pyenv with
```bash
pipenv install --dev
```
```bash
// or, if above fails
pipenv install --python 3.9
```

## run shell in virtualenv
```bash 
pipenv shell
```

## install the ICON SDK
```bash
pipenv install iconsdk
```

Now you should be able the run the script in main.py

If you get a import error, be sure to check if you are in the pipenv shell!

If you want to exit the pipenv shell, just type 'exit' in the terminal.