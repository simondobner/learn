import json
import random
import sys
import uuid

import boto3


def get_stream():
    return random.choice(['Red', 'Green', 'Blue', 'Foo', 'Brown'])


sqs = boto3.resource('sqs', endpoint_url='http://localhost:4576')

queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# # Create a new message
# response = queue.send_message(MessageBody='world')
#
# # The response is NOT a resource, but gives you a message ID and MD5
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

# build a batch of 5 records
message_set = []
for x in range(5):
    message = {'Id': str(x),
               'MessageBody': json.dumps({'Record_id': str(uuid.uuid4()),
                                          'record_stream': get_stream(),
                                          'record_value': random.randint(0, 10000000)}),
               # 'MessageAttributes': json.dumps(
               #     {'Author': {
               #         'Name': 'Simon',
               #         'DataType': 'Record'
               #     }})
               }
    # message_set.append(json.dumps(message))
    message_set.append(message)

print('message_set is : {}'.format(message_set))

# send the batch

response = queue.send_messages(Entries=message_set)

# Print out any failures
print('failed meassages:{}'.format(response.get('Failed')))

# print('message_set is : {}'.format(json.dumps(message_set)))

#
# # send message with custom attributes
# queue.send_message(MessageBody='boto3', MessageAttributes={
#     'Author': {
#         'StringValue': 'Simon',
#         'DataType': 'String'
#     }
# })
#
# # send a batch
#
# response = queue.send_messages(Entries=[
#     {
#         'Id': '1',
#         'MessageBody': 'world'
#     },
#     {
#         'Id': '2',
#         'MessageBody': 'boto3',
#         'MessageAttributes': {
#             'Author': {
#                 'StringValue': 'Simon (double batched message)',
#                 'DataType': 'String'
#             }
#         }
#     }
# ])
#
# # Print out any failures
# print('failed meassages:{}'.format(response.get('Failed')))
