# -*- coding: utf-8 -*-
import boto3

class orderResponse:
    def __init__(self,name):
        self.response = {}
        self.response["message"] ="Hi "+name+", please choose one of these selection:  1. Cheese, 2. Pepperoni, 3.Vegetable"

    def getResponse(self):
        return self.response

def getInformation(table,event):
    response = table.get_item(Key={
            "order_id": event["order_id"]
        })
    item = response['Item']
    return item

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',aws_access_key_id='your_key', aws_secret_access_key='your_key')
    table = dynamodb.Table('order')

    table.put_item(Item=event)
    event["sequence"] = 1

    table.put_item(Item=event)
    response = orderResponse(event["customer_name"])

    return response.getResponse()
