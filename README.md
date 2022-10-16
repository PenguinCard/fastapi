```shell
# create virtual env
python -m venv .venv

# run virtual env
source ./.venv/bin/activate

# get virtual env and save
pip freeze >> requirements.txt

# stop virtual env
deactivate

# run server
python server.py
```
