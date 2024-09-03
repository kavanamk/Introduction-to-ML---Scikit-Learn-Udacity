def outlierCleaner(predictions, ages, net_worths):
    """
    Clean away the 10% of points that have the largest
    residual errors (difference between the prediction
    and the actual net worth).

    Return a list of tuples named cleaned_data where 
    each tuple is of the form (age, net_worth, error).
    """
    # Calculate the errors (residuals)
    errors = [abs(nw - pred) for nw, pred in zip(net_worths, predictions)]

    # Combine ages, net_worths, and errors into a list of tuples
    data = list(zip(ages, net_worths, errors))

    # Sort the data by error in descending order
    data_sorted_by_error = sorted(data, key=lambda x: x[2], reverse=True)

    # Determine the number of points to remove (10% of the total data)
    num_points_to_remove = int(len(data_sorted_by_error) * 0.1)

    # Remove the top 10% of points with the largest errors
    cleaned_data = data_sorted_by_error[num_points_to_remove:]

    # Print the indices of the top 10% points for verification (optional)
    print("Indices of points removed:", [data.index(d) for d in data_sorted_by_error[:num_points_to_remove]])

    return cleaned_data
