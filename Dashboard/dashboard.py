import streamlit as st
import boto3
import matplotlib.pyplot as plt
from datetime import datetime

# Dashboard title
st.title('AWS Cost Optimization Dashboard')

# Date range selection for the user
st.sidebar.header("Select the consultation period")
start_date = st.sidebar.date_input("Start date", value=datetime(2024, 1, 1))
end_date = st.sidebar.date_input("End date", value=datetime.now())

# Convert dates to ISO format (YYYY-MM-DD) for AWS API
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# Initialize session state for the AWS response if not defined
if 'response' not in st.session_state:
    st.session_state.response = None

# Button to trigger the AWS cost consultation
if st.sidebar.button("Consult AWS Costs"):
    
    # Initialize boto3 client for Cost Explorer
    aws_client = boto3.client('ce')

    # Fetch AWS cost data from AWS Cost Explorer
    response = aws_client.get_cost_and_usage(
        TimePeriod={'Start': start_date_str, 'End': end_date_str},
        Granularity='MONTHLY',
        Metrics=['AmortizedCost']
    )

    # Store the response in session state
    st.session_state.response = response

# If we have data in session state from a previous query
if st.session_state.response is not None:
    response = st.session_state.response

    # Process cost data
    results_by_time = response['ResultsByTime']
    months = []
    costs = []

    # Extract costs and time periods
    for result in results_by_time:
        start_period = result['TimePeriod']['Start']  # Start date of the month
        amount = float(result['Total']['AmortizedCost']['Amount'])  # Amortized cost
        months.append(start_period)  # Add the date
        costs.append(amount)  # Add the cost

    # Create the bar chart with Matplotlib
    fig, ax = plt.subplots()
    ax.bar(months, costs, color='blue')

    # Set labels for the chart
    ax.set_xlabel('Month')
    ax.set_ylabel('Cost in USD')
    ax.set_title('Monthly Amortized Costs')

    # Rotate the X-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Adjust layout to prevent label overlap
    plt.tight_layout()

    # Display the chart in Streamlit
    st.pyplot(fig)

    # Show the option to display/hide JSON response
    show_json = st.checkbox('Show/Hide JSON')

    if show_json:
        st.subheader('JSON Response')
        st.json(response)
