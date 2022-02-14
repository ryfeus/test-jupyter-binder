import boto3
import json
import io
import os

def handler(event,context):
	return {
		'statusCode': 200,
		'body': 'HelloWorld'
	}