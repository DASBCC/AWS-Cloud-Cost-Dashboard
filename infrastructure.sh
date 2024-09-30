#EDIT RESOURCES LIKE:
#YOUR AMI ID, INSTANCE NAME, OWNER NAME
aws ec2 run-instances \
  --image-id ami-xxxxxxxxxxxxxx \
  --count 1 \
  --instance-type t2.micro \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=YourInstanceName},{Key=Project,Value=CloudCostOptimization},{Key=Environment,Value=Development},{Key=Owner,Value=YourName}]'