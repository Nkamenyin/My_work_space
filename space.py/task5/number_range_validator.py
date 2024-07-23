#!/usr/bin/python3

"""Number Range Validator API:
This file creates an API that checks if a given number (path parameter) falls within a specified range.
Example: /validate_number/5?min=1&max=10 → True"""

from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/validate_number/{number}")
async def validate_number(number: int, min_value: int = Query(..., ge=1), max_value: int = Query(..., ge=min_value)):
      """
        This function checks if a number falls within a specified range provided in query parameters.

          Args:
                number: The number to validate (passed as path parameter).
                      min_value: Minimum allowed value (optional query parameter, defaults to 1, must be greater than or equal to 1).
                            max_value: Maximum allowed value (optional query parameter, must be greater than or equal to min_value).

                              Returns:
                                    JSON response indicating validation result.
                                      """
                                        is_valid = min_value <= number <= max_value
                                          return {"valid": is_valid}
