# diffbot_enhance.EnhanceLiveEndpointApi

All URIs are relative to *https://kg.diffbot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enhance**](EnhanceLiveEndpointApi.md#enhance) | **GET** /kg/enhance_endpoint | Live Enhance Endpoint


# **enhance**
> EnhanceResponse enhance(token=token, type=type, id=id, name=name, url=url, phone=phone, email=email, description=description, employer=employer, title=title, school=school, location=location, mode=mode, non_canonical_facts=non_canonical_facts, jsonmode=jsonmode, lead_iq_token=lead_iq_token, rocket_reach_token=rocket_reach_token, x_diffbot_request_id=x_diffbot_request_id)

Live Enhance Endpoint

Enhance endpoint to find person or organization using partial data

### Example

```python
from __future__ import print_function
import time
import diffbot_enhance
from diffbot_enhance.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = diffbot_enhance.EnhanceLiveEndpointApi()
token = 'token_example' # str | Diffbot Token (optional)
type = 'type_example' # str | Diffbot entity type (optional)
id = 'id_example' # str | DiffbotId of entity to enhance. Parameter can be used with types `Person` and `Organization` (optional)
name = 'name_example' # str | Name of the entity to enhance. Parameter can be used with types `Person` and `Organization` (optional)
url = 'url_example' # str | Origin or homepage URI of entity to enhance. Parameter can be used with types `Person` and `Organization` (optional)
phone = 'phone_example' # str | Phone of the entity to enhance. Parameter can be used with types `Person` and `Organization` (optional)
email = 'email_example' # str | Email of the entity to enhance. Parameter can be used only with type `Person` (optional)
description = 'description_example' # str | Description of the entity to enhance. Parameter can be used with types `Person` and `Organization` (optional)
employer = 'employer_example' # str | Employer of the entity to enhance. Parameter can be used only with type `Person` (optional)
title = 'title_example' # str | Title of the entity to enhance. Parameter can be used only with type `Person` (optional)
school = 'school_example' # str | School of the entity to enhance. Parameter can be used only with type `Person` (optional)
location = 'location_example' # str | Location of the entity to enhance. Parameter can be used with types `Person` and `Organization` (optional)
mode = 'mode_example' # str | `mode=refresh` indicates that Diffbot will attempt to recrawl all the origins of the identified entity and reconstruct the returned entity from this refreshed data. (optional)
non_canonical_facts = 'non_canonical_facts_example' # str | `nonCanonicalFacts=true` returns non-canonical facts. (optional)
jsonmode = 'jsonmode_example' # str | `jsonmode=extended` returns origin information for facts. (optional)
lead_iq_token = 'lead_iq_token_example' # str | leadIQ token (optional)
rocket_reach_token = 'rocket_reach_token_example' # str | rocketReach token (optional)
x_diffbot_request_id = 'x_diffbot_request_id_example' # str | Request UUID for tracking. If available, will be set on response. (optional)

try:
    # Live Enhance Endpoint
    api_response = api_instance.enhance(token=token, type=type, id=id, name=name, url=url, phone=phone, email=email, description=description, employer=employer, title=title, school=school, location=location, mode=mode, non_canonical_facts=non_canonical_facts, jsonmode=jsonmode, lead_iq_token=lead_iq_token, rocket_reach_token=rocket_reach_token, x_diffbot_request_id=x_diffbot_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnhanceLiveEndpointApi->enhance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Diffbot Token | [optional] 
 **type** | **str**| Diffbot entity type | [optional] 
 **id** | **str**| DiffbotId of entity to enhance. Parameter can be used with types &#x60;Person&#x60; and &#x60;Organization&#x60; | [optional] 
 **name** | **str**| Name of the entity to enhance. Parameter can be used with types &#x60;Person&#x60; and &#x60;Organization&#x60; | [optional] 
 **url** | **str**| Origin or homepage URI of entity to enhance. Parameter can be used with types &#x60;Person&#x60; and &#x60;Organization&#x60; | [optional] 
 **phone** | **str**| Phone of the entity to enhance. Parameter can be used with types &#x60;Person&#x60; and &#x60;Organization&#x60; | [optional] 
 **email** | **str**| Email of the entity to enhance. Parameter can be used only with type &#x60;Person&#x60; | [optional] 
 **description** | **str**| Description of the entity to enhance. Parameter can be used with types &#x60;Person&#x60; and &#x60;Organization&#x60; | [optional] 
 **employer** | **str**| Employer of the entity to enhance. Parameter can be used only with type &#x60;Person&#x60; | [optional] 
 **title** | **str**| Title of the entity to enhance. Parameter can be used only with type &#x60;Person&#x60; | [optional] 
 **school** | **str**| School of the entity to enhance. Parameter can be used only with type &#x60;Person&#x60; | [optional] 
 **location** | **str**| Location of the entity to enhance. Parameter can be used with types &#x60;Person&#x60; and &#x60;Organization&#x60; | [optional] 
 **mode** | **str**| &#x60;mode&#x3D;refresh&#x60; indicates that Diffbot will attempt to recrawl all the origins of the identified entity and reconstruct the returned entity from this refreshed data. | [optional] 
 **non_canonical_facts** | **str**| &#x60;nonCanonicalFacts&#x3D;true&#x60; returns non-canonical facts. | [optional] 
 **jsonmode** | **str**| &#x60;jsonmode&#x3D;extended&#x60; returns origin information for facts. | [optional] 
 **lead_iq_token** | **str**| leadIQ token | [optional] 
 **rocket_reach_token** | **str**| rocketReach token | [optional] 
 **x_diffbot_request_id** | **str**| Request UUID for tracking. If available, will be set on response. | [optional] 

### Return type

[**EnhanceResponse**](EnhanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enhanced entity |  -  |
**400** | Error parsing request |  -  |
**401** | Token not specified or other client errors |  -  |
**429** | Insufficient credits |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

