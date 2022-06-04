import boto3
import pandas as pd
from csv import reader
from io import StringIO

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("Event : ",event)
    # Get the object from the event and show its content type
    source_bucket_name=event['Records'][0]['s3']['bucket']['name']
    print("Bucket Name : ",source_bucket_name)
    
    file_name=event['Records'][0]['s3']['object']['key']
    print("File Name : ",file_name)
    
    files = file_name.split("/")
    
    print(files)
    
    input_file_name = files[3]
    
    print("input file name :",input_file_name)
    
    file_path = source_bucket_name+'/'+file_name
    
    print("input_file_name : ",file_path)
    
    csv_object = s3.get_object(Bucket=source_bucket_name,Key=file_name)
    
    df = pd.read_csv(csv_object['Body'])
    
    print(df)
    
    