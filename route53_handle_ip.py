import boto3

def list_hosted_zones():
    client = boto3.client('route53')
    paginator = client.get_paginator('list_hosted_zones')
    hosted_zones = []

    for page in paginator.paginate():
        hosted_zones.extend(page['HostedZones'])

    return hosted_zones

def find_and_remove_ip_from_records(hosted_zone_id, ip_address):
    client = boto3.client('route53')
    paginator = client.get_paginator('list_resource_record_sets')
    
    for page in paginator.paginate(HostedZoneId=hosted_zone_id):
        for record_set in page['ResourceRecordSets']:
            if record_set['Type'] == 'A':
                for record in record_set['ResourceRecords']:
                    if record['Value'] == ip_address:
                        print(f"Removing IP {ip_address} from record {record_set['Name']}")
                        update_route53_record(hosted_zone_id, record_set['Name'], 'DELETE', ip_address, record_set['TTL'])

def update_route53_record(hosted_zone_id, domain_name, action, ip_address, ttl=300):
    client = boto3.client('route53')

    if action not in ('UPSERT', 'DELETE'):
        print("Invalid action. Use 'UPSERT' to add/update or 'DELETE' to remove.")
        return

    change_record = {
        'Action': action,
        'ResourceRecordSet': {
            'Name': domain_name,
            'Type': 'A',
            'TTL': ttl,
            'ResourceRecords': [
                {
                    'Value': ip_address
                },
            ],
        }
    }

    try:
        response = client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': [change_record]
            }
        )
        print(f"Change submitted: {response['ChangeInfo']['Id']}")
    except Exception as e:
        print(f"Error updating the record: {e}")

ip_address_to_remove = '1.2.3.4'

hosted_zones = list_hosted_zones()
for zone in hosted_zones:
    print(f"Searching in hosted zone: {zone['Name']}")
    find_and_remove_ip_from_records(zone['Id'], ip_address_to_remove)
