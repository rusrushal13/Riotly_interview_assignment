# Riotly Backend Test

The implementation extracts the files, parses them, converts them, merges them and uploads a zip file to the cloud storage.

## Usage

### Using command line

```bash
pip3 install -r requirements.py

export GOOGLE_APPLICATION_CREDENTIALS=credentials.json

python3 riotly-etl.py
```

### Using Docker Container(Docker needs to be installed)

```Docker
docker build --rm -t riotly . && docker run --rm --it riotly
```

## Time Spent

* 10 Min - Going through the problem statement

* 1 Hour - Learning about the google cloud storage

* 2 Hour - Implementation

* 30-45 Min - Writing Readme