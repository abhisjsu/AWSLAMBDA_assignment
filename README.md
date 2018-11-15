# ORDER PIZZA
Backend Logic, REST endpoints created and deployed leveraging on the AWS Services

## Technologies Involved

```
1. AWS Lamda
2. AWS DynamoDB
3. AWS Api Gateway
```

## REST Endpoint Testing
1. POST /menu
(exam-venv) Abhisheks-MacBook-Pro:final abhishekchaudhary$ curl -H "Content-Type: application/json" -X POST -d '{     "menu_id": "menu1",     "store_name": "Pizza Hut",     "selection": [         "Cheese",         "Pepperoni"     ],     "size": [         "Slide", "Small", "Medium", "Large", "X-Large"     ],     "price": [         "3.50", "7.00", "10.00", "15.00", "20.00"     ],     "store_hours": {         "Mon": "10am-10pm",         "Tue": "10am-10pm",         "Wed": "10am-10pm",         "Thu": "10am-10pm",         "Fri": "10am-10pm",         "Sat": "11am-12pm",         "Sun": "11am-12pm"     } }' https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/menu
"OK"

2. GET /menu/{menu-id}
(exam-venv) Abhisheks-MacBook-Pro:final abhishekchaudhary$ curl -X GET -H "Content-type: application/json" -H "Accept: application/json" https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/menu/menu1
{"menu_id": "menu1", "selection": ["Cheese", "Pepperoni"], "price": ["3.50", "7.00", "10.00", "15.00", "20.00"], "store_hours": {"Wed": "10am-10pm", "Sun": "11am-12pm", "Fri": "10am-10pm", "Tue": "10am-10pm", "Mon": "10am-10pm", "Thu": "10am-10pm", "Sat": "11am-12pm"}, "store_name": "Pizza Hut", "size": ["Slide", "Small", "Medium", "Large", "X-Large"]}

3. PUT /menu/{menu-id}
(exam-venv) Abhisheks-MacBook-Pro:final abhishekchaudhary$ curl -H "Content-Type: application/json" -X PUT -d '{"selection": ["Cheese","Pepperoni","Vegetable"]  }' https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/menu/menu1
"OK"

4. Post /order
(exam-venv) Abhisheks-MacBook-Pro:final abhishekchaudhary$ curl -H "Content-Type: application/json" -X POST -d '{"menu_id": "menu1","order_id": "order1","omer_name": "John Smith","customer_email":"foobar@gmail.com" }' https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/order
{"message": "Hi John Smith, please choose one of these selection:  1. Cheese, 2. Pepperoni, 3.Vegetable"}

 5. PUT /order/{order-id}
(exam-venv) Abhisheks-MacBook-Pro:final abhishekchaudhary$ curl -H "Content-Type: application/json" -X PUT -d '{"input": "1"}' https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/order/order1
{"message": "Which size do you want? 1. Slide, 2. Small, 3. Medium, 4. Large, 5. X-Large"}

 6. PUT /order/{order-id}
(exam-venv) Abhisheks-MacBook-Pro:final abhishekchaudhary$ curl -H "Content-Type: application/json" -X PUT -d '{"input": "2"}' https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/order/order1
{"message": "Your order costs 7.00. We will email you when the order is ready. Thank you!"}


 7. GET /order/{order-id}
curl -X GET -H "Content-type: application/json" -H "Accept: application/json" https://441popqhr5.execute-api.us-west-2.amazonaws.com/LambdaDynamoDB/order/order1
{"menu_id": "menu1", "customer_email": "foobar@gmail.com", "order_id": "order1", "order": {"date": "2017-05-24 17:41:08.158745", "price": "7.00", "selection": "Cheese", "size": "Small"}, "customer_name": "John Smith"}





