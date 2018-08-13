### HUG REST

#### PRÉ REQ

`
Python 3.6 >~
Mongo
`

#### Configure virtualenv

```bash
$ cd hub-rest
$ virtualenv -p python3 venv
$ pip install -r requirements.txt
```

#### RUN

```bash
$ hug -f app.py
```


`Dependecy`

```bash
astroid==2.0.4
certifi==2018.8.13
chardet==3.0.4
falcon==1.4.1
hug==2.4.0
idna==2.7
isort==4.3.4
lazy-object-proxy==1.3.1
mccabe==0.6.1
pylint==2.1.1
pymongo==3.7.1
python-mimeparse==1.6.0
requests==2.19.1
six==1.11.0
typed-ast==1.1.0
urllib3==1.23
wrapt==1.10.11
```