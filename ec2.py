import boto3

def lambda_handler(event, context):
    # Create EC2 client
    ec2_client = boto3.client('ec2')
    
    # Get all running instances
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    # Extract instance IDs
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    # Stop instances
    if instance_ids:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print(f"EC2 instances {instance_ids} stopped successfully")
    else:
        print("No running EC2 instances found")

    return {
        'statusCode': 200,
        'body': 'EC2 instances stopped successfully'
    }
