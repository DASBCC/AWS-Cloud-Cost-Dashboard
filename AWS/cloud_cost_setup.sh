#EDIT RESOURCES LIKE:
#YOUR AMI ID, INSTANCE NAME, OWNER NAME
aws ec2 run-instances \
  --image-id ami-xxxxxxxxxxxxxx \
  --count 1 \
  --instance-type t2.micro \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=YourInstanceName},{Key=Project,Value=CloudCostOptimization},{Key=Environment,Value=Development},{Key=Owner,Value=YourName}]'

#CHECK IF TAGS WERE CREATED SUCCESFULLY
aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=YourInstanceName" \
  --query 'Reservations[*].Instances[*].[InstanceId,Tags]'

#YOU CAN REMOVE END IF YOU WANT THE COST AND USAGE TO MATCH YOUR ACTUAL DATE
#IF YOU USE TIME PERIOD, ENSURE THE END DATE IS LOWER OR EQUAL THAN YOUR ACTUAL DATE
  aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-12-31\
  --granularity MONTHLY \
  --metrics "AmortizedCost" \
  --group-by Type=DIMENSION,Key=LINKED_ACCOUNT \
  --group-by Type=TAG,Key=Project
