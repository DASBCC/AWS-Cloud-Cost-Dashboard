# Cloud-Cost-Optimization-Dashboard

Cloud cost optimization dashboard is a tool that helps you to monitor and optimize your cloud costs. It provides a dashboard that shows the cost of your cloud resources and helps you to identify the resources that are costing you the most money. 

## Requirements

- AWS CLI | CloudShell
- Python 3.6 or higher
- Install the requirements.txt inside ./Dashboard folder

## Execution

  1. If you're in a local environment, you need to log in to your AWS account using the AWS CLI.
    
    Run the command `aws configure` and enter your AWS Access Key ID, Secret Access Key, and region.

  2. Run the first command located in ./AWS/cloud_cost_setup.sh to create an EC2 Instance with the necessary tags.
  3. Go to the Dashboard folder with cd ./Dashboard
  4. run the streamlit app with the command `streamlit run ./dashboard.py`
