# -*- coding: utf-8 -*-
import boto3
import datetime

class orderResponseOne:
    def __init__(self):
        self.response = {}
        self.response["message"] = "Which size do you want? 1. Slide, 2. Small, 3. Medium, 4. Large, 5. X-Large"

    def getResponse(self):
        return self.response

class orderResponseTwo:
    def __init__(self):
        self.response= {}

    def formulateResponse(self,cost):
        self.response["message"] = "Your order costs "+cost+". We will email you when the order is ready. Thank you!"

    def getResponse(self):
        return self.response

def getMenuInfo(table,menu_id):
    response = table.get_item(Key={
            "menu_id" : menu_id
        })
    item = response['Item']
    return item

def getOrderInfo(table,event):
    response = table.get_item(Key={
            "order_id" : event["order_id"]
        })
    item = response['Item']
    return item

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',aws_access_key_id='your_key', aws_secret_access_key='your_key')

    tableOrder = dynamodb.Table('order')
    tableMenu = dynamodb.Table('menu')

    orderTableData = getOrderInfo(tableOrder,event)#order_id will be in the request body
    menuTableData = getMenuInfo(tableMenu,orderTableData["menu_id"])
    
    if not orderTableData.get("order"):
        orderTableData["order"] = {}

    if orderTableData["sequence"] == 1:
        selection = menuTableData["selection"][event["input"] -1 ]
        orderTableData["order"]["selection"] = selection
        orderTableData["sequence"] = 2
        response = orderResponseOne().getResponse()
    elif orderTableData["sequence"] == 2:
        size = menuTableData["size"][event["input"] -1 ]
        price =menuTableData["price"][event["input"] -1 ]
        date = datetime.datetime.now()

        orderTableData["order"]["size"] = size
        orderTableData["order"]["price"] = price
        orderTableData["order"]["date"] = str(date)

        response = orderResponseTwo()
        response.formulateResponse(menuTableData["price"][event["input"] -1])
        response=response.getResponse()

    tableOrder.put_item(Item = orderTableData)

    return response
