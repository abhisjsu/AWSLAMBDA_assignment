# -*- coding: utf-8 -*-
import boto3

def putItemInTable(table,event):
    table.put_item(Item=event)

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',aws_access_key_id='your_key', aws_secret_access_key='your_key')
    table = dynamodb.Table('menu')

    putItemInTable(table,event)
    return "OK";
