# -*- coding: utf-8 -*-
import boto3

class response:
    def __init__(self,menu_id,selection):
        self.menu_id = menu_id
        self.selection = selection

def updateItemInTable(table,event):
    table.update_item(
        Key={
            "menu_id": event["menu_id"]
        },
        UpdateExpression='SET selection = :val1',
        ExpressionAttributeValues={
            ':val1': event["selection"]
        }
    )

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',aws_access_key_id='your_key', aws_secret_access_key='your_key')
    table = dynamodb.Table('menu')

    updateItemInTable(table,event)

    return "OK"

