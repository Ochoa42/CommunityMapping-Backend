# CommunityMappingBackend


## STEP 1
### Create a virtual env and activate

```sh
python -m venv env
```

```sh
source env/Scripts/activate
```

## STEP 2
### Install dependencies
```sh
python -m pip install -r  requirements.txt
```

## STEP 3
### Levantar la api 

```sh
python -m uvicorn main:app --reload --port 8001
```

### Para testear los endpoints ir al endpoint "/docs

