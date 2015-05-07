"""
Creates an ec2 instance on AWS, downloading the ssh key.

Configuration:

    make sure you set up your aws credentials on the 'tsid-test'
    profile

Usage:

    python create_machine.py <key_name>

**NOTE** key name must be unique among all participants

"""
import botocore.session


def create_machine(key_name, create_security_group=False):
    # Use the tsid-test auth credentials
    session = botocore.session.Session(
        session_vars={'profile': (None, None, 'tsid-test')}
    )
    ec2 = session.create_client('ec2', region_name='eu-west-1')
    if create_security_group:
        # Firewall rules
        ec2.create_security_group(
            GroupName='project-work-1',
            Description='project work sec group 1'
        )
        ec2.authorize_security_group_ingress(
            GroupName='project-work-1',
            IpProtocol='tcp', FromPort=22, ToPort=22,
            CidrIp='0.0.0.0/0'
        )
    kp = ec2.create_key_pair(KeyName=key_name)
    with open('key_{}.pem'.format(key_name), 'x') as key_file:
        key_file.write(kp['KeyMaterial'])
    instances = ec2.run_instances(
        ImageId='ami-00b11177',
        KeyName=key_name,
        SecurityGroups=['project-work-1'],
        InstanceType='t1.micro',
        MinCount=1, MaxCount=1
    )
    instance_id = instances['Instances'][0]['InstanceId']
    with open('instance_id_{}.txt'.format(key_name), 'w') as info_file:
        info_file.write(instance_id)
    ec2.describe_instances(InstanceIds=['i-047f42e2'])


if __name__ == '__main__':
    import sys
    create_machine(sys.argv[1])
