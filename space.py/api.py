#!/usr/bin/python3

import requests
"""This program makes requests to a public API and handles exceptions for network errors, invalid responses, and rate limits."""

def make_api_request(url, params=None):
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    # Check response format (e.g JSON) and data validity
    data = response.json()# a JSON response
    return data
  except requests.exceptions.RequestException as e:
    if "Network" in str(e):
      handle_network_error()
    else:
      handle_api_error(e)
  except json.JSONDecodeError:
    handle_invalid_response()
  return None  # Indicate error

def handle_network_error():
  print("Network error. Please check your internet connection.")

def handle_api_error(error):
  print(f"API error: {error}")

def handle_invalid_response():
  print("Invalid response")

# Making a request
api_url = "https://api.example.com/data"
data = make_api_request(api_url)
if data:# Process the retrieved data
  print(data)
else:
  print("An error occurred while fetching data.")
