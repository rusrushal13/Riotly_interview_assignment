from google.cloud import storage
from collections import OrderedDict
from constants import ZIP_NAME, FIELD_NAMES, DATE_REGEX
from datetime import datetime
import os, csv, json, re, zipfile

def parse_dates(date):
    data = re.match(DATE_REGEX, date)
    if data:
        epoch = float(data.group(1))
        timezone = data.group(2)
        utc_timing = datetime.utcfromtimestamp(epoch/1000.0)
        data_with_tz = utc_timing.isoformat() + timezone # considering timezone
        user_date = datetime.strptime(data_with_tz, "%Y-%m-%dT%H:%M:%S%z") # user local time
        return user_date.date() # return the date

def process_fields(data, name):
    field_data = {}
    for entry in data:
        date = parse_dates(entry['<CurrentDate>k__BackingField'])
        num_per_day = entry['<NumberPerDay>k__BackingField']
        if date not in field_data:
            field_data[date] = 0
        field_data[date] += num_per_day
    return field_data

def process_json(name, json_string, writer):
    
    json_data = json.loads(json_string)
    userdata = {}

    for field_name in FIELD_NAMES.keys():
        if field_name == 'user' or field_name == 'date':
            continue
        map_name = FIELD_NAMES[field_name]
        userdata[map_name] = process_fields(json_data[field_name], field_name)
    
    userdata_date = {}

    for field in userdata:
        for date in userdata[field]:
            if not date in userdata_date:
                userdata_date[date] = {
                    'user': name,
                    'date': date,
                }
            
            userdata_date[date][field] = userdata[field][date]
    
    for row in userdata_date.values():
        writer.writerow(row)

def zip_directory(filepath, zobj):
    for root, directory, files in os.walk(filepath):
        for file in files:
            if file == ZIP_NAME:
                continue
            zobj.write(os.path.join(root, file))

def main():
    storage_client = storage.Client(project='riotly-interview')
    bucket = storage_client.get_bucket('riotly-interview-test')
    blobs = bucket.list_blobs(prefix='data/', delimiter='/')

    with open('merged.csv', 'w') as f:
        write = csv.DictWriter(f, fieldnames=FIELD_NAMES.values())
        write.writeheader()
    
        for blob in blobs:
            filename, file_extension = os.path.splitext(blob.name)
            
            if file_extension == '.json':
                json_string = blob.download_as_string().decode('utf-8')
                name = os.path.basename(filename)
                process_json(name, json_string, write)
    
    with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zobj:
        zip_directory('.', zobj)

    blob = bucket.blob('output/{}'.format(ZIP_NAME))
    blob.upload_from_filename(filename=ZIP_NAME)

if __name__ == '__main__':
    main()