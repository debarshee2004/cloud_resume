"""
Azure Function: GetResumeCounter

This module defines an Azure Function App with an HTTP-triggered function `GetResumeCounter`. 
The function responds to HTTP requests by returning a personalized greeting if a 'name' parameter 
is provided, either in the query string or in the request body.

Functions:
    GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
        Processes HTTP requests and returns a personalized greeting if a 'name' parameter is provided.
"""

import azure.functions as func
import logging

# Create a Function App instance with HTTP authentication level set to FUNCTION
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetResumeCounter")
def GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered function to return a personalized greeting.

    This function processes an HTTP request and returns a greeting message. 
    If a 'name' parameter is provided in the query string or in the request body, 
    the function returns a personalized greeting. Otherwise, it returns a default message.

    Args:
        req (func.HttpRequest): The HTTP request object.

    Returns:
        func.HttpResponse: The HTTP response object containing the greeting message.
    """
    logging.info('Python HTTP trigger function processed a request.')

    # Attempt to get the 'name' parameter from the query string
    name = req.params.get('name')
    if not name:
        # If not found in the query string, attempt to get 'name' from the request body
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # Return a personalized greeting if 'name' is provided
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        # Return a default message if 'name' is not provided
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
