# -*- coding: utf-8 -*-
import boto3

def getInformation(table,event):
    response = table.get_item(Key={
            "menu_id": event["menu_id"]
        })
    item = response['Item']
    return item

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',aws_access_key_id='your_key', aws_secret_access_key='your_key')
    table = dynamodb.Table('menu')
    data = getInformation(table,event)
    return data
