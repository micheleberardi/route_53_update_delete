# route_53_update_delete

 This script contains three functions:

list_hosted_zones(): lists all the hosted zones in your AWS account.
find_and_remove_ip_from_records(hosted_zone_id, ip_address): searches for a specific IP address in a hosted zone and removes it from the respective A record.
update_route53_record(hosted_zone_id, domain_name, action, ip_address, ttl=300): adds, updates, or removes an IP address from an A record in a Route 53 hosted zone.
Replace the ip_address_to_remove variable with the IP address you want to remove. The script will search all hosted zones in your AWS account and remove the IP address from any A records where it is found.
