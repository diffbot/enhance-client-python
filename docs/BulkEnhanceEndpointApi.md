# enhance_client.BulkEnhanceEndpointApi

All URIs are relative to *https://kg.diffbot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkjob_status**](BulkEnhanceEndpointApi.md#bulkjob_status) | **GET** /kg/enhance_endpoint/bulk/{bulkjobId}/status | Bulk Enhance Status Endpoint
[**enhance_bulkjob**](BulkEnhanceEndpointApi.md#enhance_bulkjob) | **POST** /kg/enhance_endpoint/bulk | Bulk Enhance Endpoint
[**poll_bulkjob**](BulkEnhanceEndpointApi.md#poll_bulkjob) | **GET** /kg/enhance_endpoint/bulk/{bulkjobId} | Bulk Enhance Poll Endpoint
[**stop_bulkjob**](BulkEnhanceEndpointApi.md#stop_bulkjob) | **GET** /kg/enhance_endpoint/bulk/{bulkjobId}/stop | Bulkjob stop


# **bulkjob_status**
> BulkjobStatusResponse bulkjob_status(bulkjob_id, token=token)

Bulk Enhance Status Endpoint

Get status of a bulk Enhance job

### Example

```python
from __future__ import print_function
import time
import enhance_client
from enhance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = enhance_client.BulkEnhanceEndpointApi()
bulkjob_id = 'bulkjob_id_example' # str | Bulkjob Id
token = 'token_example' # str | Diffbot Token (optional)

try:
    # Bulk Enhance Status Endpoint
    api_response = api_instance.bulkjob_status(bulkjob_id, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnhanceEndpointApi->bulkjob_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulkjob_id** | **str**| Bulkjob Id | 
 **token** | **str**| Diffbot Token | [optional] 

### Return type

[**BulkjobStatusResponse**](BulkjobStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bulkjob status |  -  |
**201** | Bulkjob is still executing or is stopped |  -  |
**400** | Invalid bulkjobId |  -  |
**401** | Token not specified or other client errors |  -  |
**404** | Bulkjob not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enhance_bulkjob**
> BulkjobAccepted enhance_bulkjob(token=token, tag=tag, mode=mode, non_canonical_facts=non_canonical_facts, jsonmode=jsonmode, lead_iq_token=lead_iq_token, rocket_reach_token=rocket_reach_token, webhookurl=webhookurl, x_diffbot_request_id=x_diffbot_request_id, request_body=request_body)

Bulk Enhance Endpoint

Enhance endpoint to find person or organization using partial data

### Example

```python
from __future__ import print_function
import time
import enhance_client
from enhance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = enhance_client.BulkEnhanceEndpointApi()
token = 'token_example' # str | Diffbot Token (optional)
tag = ['tag_example'] # list[str] | Tag (optional)
mode = 'mode_example' # str | `mode=refresh` indicates that Diffbot will attempt to recrawl all the origins of the identified entity and reconstruct the returned entity from this refreshed data. (optional)
non_canonical_facts = 'non_canonical_facts_example' # str | `nonCanonicalFacts=true` returns non-canonical facts. (optional)
jsonmode = 'jsonmode_example' # str | `jsonmode=extended` returns origin information for facts. (optional)
lead_iq_token = 'lead_iq_token_example' # str | leadIQ token (optional)
rocket_reach_token = 'rocket_reach_token_example' # str | rocketReach token (optional)
webhookurl = 'webhookurl_example' # str | Webhook URL (optional)
x_diffbot_request_id = 'x_diffbot_request_id_example' # str | Request UUID for tracking. If available, will be set on response. (optional)
request_body = None # list[object] | Bulk query payload (optional)

try:
    # Bulk Enhance Endpoint
    api_response = api_instance.enhance_bulkjob(token=token, tag=tag, mode=mode, non_canonical_facts=non_canonical_facts, jsonmode=jsonmode, lead_iq_token=lead_iq_token, rocket_reach_token=rocket_reach_token, webhookurl=webhookurl, x_diffbot_request_id=x_diffbot_request_id, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnhanceEndpointApi->enhance_bulkjob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Diffbot Token | [optional] 
 **tag** | [**list[str]**](str.md)| Tag | [optional] 
 **mode** | **str**| &#x60;mode&#x3D;refresh&#x60; indicates that Diffbot will attempt to recrawl all the origins of the identified entity and reconstruct the returned entity from this refreshed data. | [optional] 
 **non_canonical_facts** | **str**| &#x60;nonCanonicalFacts&#x3D;true&#x60; returns non-canonical facts. | [optional] 
 **jsonmode** | **str**| &#x60;jsonmode&#x3D;extended&#x60; returns origin information for facts. | [optional] 
 **lead_iq_token** | **str**| leadIQ token | [optional] 
 **rocket_reach_token** | **str**| rocketReach token | [optional] 
 **webhookurl** | **str**| Webhook URL | [optional] 
 **x_diffbot_request_id** | **str**| Request UUID for tracking. If available, will be set on response. | [optional] 
 **request_body** | [**list[object]**](object.md)| Bulk query payload | [optional] 

### Return type

[**BulkjobAccepted**](BulkjobAccepted.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Acknowledgement with bulkjobId |  -  |
**400** | Error parsing request |  -  |
**401** | Token not specified or other client errors |  -  |
**429** | Insufficient credits |  -  |
**500** | Internal Server Error |  -  |
**503** | Request too large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_bulkjob**
> object poll_bulkjob(bulkjob_id, token=token, csvmode=csvmode)

Bulk Enhance Poll Endpoint

Poll a bulk Enhance job

### Example

```python
from __future__ import print_function
import time
import enhance_client
from enhance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = enhance_client.BulkEnhanceEndpointApi()
bulkjob_id = 'bulkjob_id_example' # str | Bulkjob Id
token = 'token_example' # str | Diffbot Token (optional)
csvmode = 'csvmode_example' # str | Return results as csv (optional)

try:
    # Bulk Enhance Poll Endpoint
    api_response = api_instance.poll_bulkjob(bulkjob_id, token=token, csvmode=csvmode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnhanceEndpointApi->poll_bulkjob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulkjob_id** | **str**| Bulkjob Id | 
 **token** | **str**| Diffbot Token | [optional] 
 **csvmode** | **str**| Return results as csv | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enhanced entity |  -  |
**201** | Bulkjob is still executing or is stopped |  -  |
**400** | Invalid bulkjobId |  -  |
**401** | Token not specified or other client errors |  -  |
**404** | Bulkjob not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_bulkjob**
> BulkjobRecoveryStatusResponse stop_bulkjob(bulkjob_id, token=token)

Bulkjob stop

Stop an incomplete job

### Example

```python
from __future__ import print_function
import time
import enhance_client
from enhance_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = enhance_client.BulkEnhanceEndpointApi()
bulkjob_id = 'bulkjob_id_example' # str | Bulkjob Id
token = 'token_example' # str | Diffbot Token (optional)

try:
    # Bulkjob stop
    api_response = api_instance.stop_bulkjob(bulkjob_id, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkEnhanceEndpointApi->stop_bulkjob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulkjob_id** | **str**| Bulkjob Id | 
 **token** | **str**| Diffbot Token | [optional] 

### Return type

[**BulkjobRecoveryStatusResponse**](BulkjobRecoveryStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enhanced entity |  -  |
**400** | Invalid bulkjobId |  -  |
**401** | Token not specified or other client errors |  -  |
**404** | Bulkjob not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

