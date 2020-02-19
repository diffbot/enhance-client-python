# diffbot_enhance_client
Enhance is an API to find a person or organization in the Knowledge Graph using partial data

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.0.0
- Package version: 1.0.0-rc.05
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/diffbot/enhance-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/diffbot/enhance-client-python.git`)

Then import the package:
```python
import diffbot_enhance_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import diffbot_enhance_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import diffbot_enhance_client
from diffbot_enhance_client.rest import ApiException
from pprint import pprint


# Defining host is optional and default to https://kg.diffbot.com
configuration.host = "https://kg.diffbot.com"
# Enter a context with an instance of the API client
with diffbot_enhance_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = diffbot_enhance_client.BulkEnhanceEndpointApi(api_client)
    bulkjob_id = 'bulkjob_id_example' # str | Bulkjob Id
token = 'token_example' # str | Diffbot Token (optional)

    try:
        # Bulk Enhance Status Endpoint
        api_response = api_instance.bulkjob_status(bulkjob_id, token=token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BulkEnhanceEndpointApi->bulkjob_status: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://kg.diffbot.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BulkEnhanceEndpointApi* | [**bulkjob_status**](docs/BulkEnhanceEndpointApi.md#bulkjob_status) | **GET** /kg/enhance_endpoint/bulk/{bulkjobId}/status | Bulk Enhance Status Endpoint
*BulkEnhanceEndpointApi* | [**enhance_bulkjob**](docs/BulkEnhanceEndpointApi.md#enhance_bulkjob) | **POST** /kg/enhance_endpoint/bulk | Bulk Enhance Endpoint
*BulkEnhanceEndpointApi* | [**poll_bulkjob**](docs/BulkEnhanceEndpointApi.md#poll_bulkjob) | **GET** /kg/enhance_endpoint/bulk/{bulkjobId} | Bulk Enhance Poll Endpoint
*BulkEnhanceEndpointApi* | [**stop_bulkjob**](docs/BulkEnhanceEndpointApi.md#stop_bulkjob) | **GET** /kg/enhance_endpoint/bulk/{bulkjobId}/stop | Bulkjob stop
*EnhanceLiveEndpointApi* | [**enhance**](docs/EnhanceLiveEndpointApi.md#enhance) | **GET** /kg/enhance_endpoint | Live Enhance Endpoint


## Documentation For Models

 - [BulkjobAccepted](docs/BulkjobAccepted.md)
 - [BulkjobRecoveryStatusResponse](docs/BulkjobRecoveryStatusResponse.md)
 - [BulkjobStatus](docs/BulkjobStatus.md)
 - [BulkjobStatusResponse](docs/BulkjobStatusResponse.md)
 - [EnhanceResponse](docs/EnhanceResponse.md)
 - [RequestError](docs/RequestError.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@diffbot.com


