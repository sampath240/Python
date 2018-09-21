import sys
table_name=sys.argv[1]
def delete_all_items(table_name):
    # Deletes all items from a DynamoDB table.
    # You need to confirm your intention by pressing Enter.
    import boto3
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = client.describe_table(TableName=table_name)
    keys = [k['AttributeName'] for k in response['Table']['KeySchema']]
    response = table.scan()
    items = response['Items']
    number_of_items = len(items)
    if number_of_items == 0:  # no items to delete
        print("Table '{}' is empty.".format(table_name))
        return
    else:
	#print "Len of items from response:" + str(number_of_items)
	print "Count from respone: " + str(response['Count'])

delete_all_items(table_name)
