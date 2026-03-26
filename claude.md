## Coding Standards
- Add error handling in every function
- Add logging to all pipelines
- Use camel case for variable and function names
- Use pytest for test cases
- Add docstrings to every function
- Use type hints in function parameters
- Keep functions small and single purpose
- Use constants instead of hardcoded values

## Logging Standards
- Use Python logging module (not print statements)
- Log start and end of every pipeline
- Log record counts after each transformation
- Log errors with full traceback

## Testing Standards
- Write at least one test per function
- Test happy path and edge cases
- Use mock data for PySpark tests
- Test file should be named test_<filename>.py