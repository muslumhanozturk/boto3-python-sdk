import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0dfd8599c8b93c35d').terminate()