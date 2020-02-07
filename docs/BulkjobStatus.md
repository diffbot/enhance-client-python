# BulkjobStatus

Bulkjob status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Bulkjob Id | [optional] 
**message** | **str** | Bulkjob status message | [optional] 
**jobs_total** | **int** | Number of jobs in bulkjob | [optional] 
**jobs_completed** | **int** | Number of jobs completed in bulkjob. | [optional] 
**status** | **str** | Status of Bulkjob. One of {NOT_STARTED, IN_PROCESS, COMPLETE, COMPLETE_WITH_FAILURES, STOPPED, ERROR_FINALIZING, UNKNOWN} | [optional] 
**estimate_remaining_time** | **int** | Estimated remaining time for bulkjob to complete (in seconds). &#x60;null&#x60; if job is completed or not started. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


