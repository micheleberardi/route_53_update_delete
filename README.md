# route 53 Update & Delete

 This script contains three functions:

* list_hosted_zones(): lists all the hosted zones in your AWS account.

* find_and_remove_ip_from_records(hosted_zone_id, ip_address): searches for a specific IP address in a hosted zone and removes it from the respective A record.

* update_route53_record(hosted_zone_id, domain_name, action, ip_address, ttl=300): adds, updates, or removes an IP address from an A record in a Route 53 hosted zone.

* Replace the ip_address_to_remove variable with the IP address you want to remove. 

* The script will search all hosted zones in your AWS account and remove the IP address from any A records where it is found.

# HOW TO USE IT

You can save the script in a file, for example route53_remove_ip.py, and then execute it using Python. Follow these steps:

1. Save the script in a file named route53_remove_ip.py.
2. Open a terminal/command prompt.
3. Navigate to the directory containing the route53_remove_ip.py file.
4. Execute the script using the following command:

```
python route53_remove_ip.py
```

This command assumes you have Python installed and the necessary boto3 library. If you haven't installed boto3, you can do so by running pip install boto3. Also, ensure that your AWS credentials are properly configured as described in my earlier response.

When you run the script, it will search for the specified IP address in all hosted zones in your AWS account and remove the IP from any A records where it is found.
