03/09/2024 16:40:56 - root - INFO - Args parsed Namespace(input='text_files/testdatesin', names=True, dates=True, phones=True, address=True, output='gradescopetestsout/', stats='stdout')
03/09/2024 16:40:56 - root - DEBUG - spacy model loaded
03/09/2024 16:40:56 - root - DEBUG - text preprocessing done
03/09/2024 16:40:56 - root - DEBUG - entity extraction with spacy done
03/09/2024 16:40:56 - assignment1.regex_helper - DEBUG - regex matching started
03/09/2024 16:40:56 - assignment1.regex_helper - DEBUG - regex matching initial dictionary <class 'list'>
03/09/2024 16:40:56 - root - DEBUG - entity extraction with regex done
03/09/2024 16:40:56 - root - DEBUG - censoring done
03/09/2024 16:40:56 - root - DEBUG - for file text_files/testdatesin censoring dictionary: {'PERSON': [(268, 283, 'Phillip K Allen'), (290, 302, 'Tim Belden <'), (302, 312, 'Tim Belden'), (357, 370, 'Phillip Allen'), (381, 418, "Allen  Phillip K. 'Sent Mail\nX-Origin"), (420, 427, 'Allen-P'), (440, 446, 'pallen'), (36, 50, 'JavaMail.evans'), (108, 121, 'phillip.allen'), (136, 146, 'tim.belden'), (306, 318, 'Belden/Enron')], 'DATE': [(69, 80, '14 May 2001'), (81, 89, '16:39:00'), (69, 75, '14 May'), (181, 184, '1.0'), (371, 378, 'Jan2002')], 'PHONE': [(13, 35, '18782981.1075855378110'), (75, 83, ' 2001 16'), (87, 95, '00 -0700')], 'ADDRESS': [(157, 164, 'Subject')]}
03/09/2024 16:40:56 - root - DEBUG - preprocessed text Message-ID: <18782981.1075855378110.JavaMail.evans@thyme>
Date: Mon  14 May 2001 16:39:00 -0700 (PDT)
From: phillip.allen@enron.com
To: tim.belden@enron.com
Subject: 
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Phillip K Allen
X-To: Tim Belden <Tim Belden/Enron@EnronXGate>
X-cc: 
X-bcc: 
X-Folder:  Phillip Allen Jan2002 1 Allen  Phillip K. 'Sent Mail
X-Origin: Allen-P
X-FileName: pallen (Non-Privileged).pst

Here is our forecast

 
03/09/2024 16:40:56 - root - DEBUG - printing stats to stdout/ ouput directory
03/09/2024 16:40:56 - root - DEBUG - censored file written to output directory
03/09/2024 16:40:56 - root - INFO - censoring done
03/09/2024 16:40:56 - root - INFO - output dir ['testdatesin.censored']
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from creating-client-class.iot-data to creating-client-class.iot-data-plane
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from before-call.apigateway to before-call.api-gateway
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from request-created.machinelearning.Predict to request-created.machine-learning.Predict
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.autoscaling.CreateLaunchConfiguration to before-parameter-build.auto-scaling.CreateLaunchConfiguration
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.route53 to before-parameter-build.route-53
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from request-created.cloudsearchdomain.Search to request-created.cloudsearch-domain.Search
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from docs.*.autoscaling.CreateLaunchConfiguration.complete-section to docs.*.auto-scaling.CreateLaunchConfiguration.complete-section
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.logs.CreateExportTask to before-parameter-build.cloudwatch-logs.CreateExportTask
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from docs.*.logs.CreateExportTask.complete-section to docs.*.cloudwatch-logs.CreateExportTask.complete-section
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.cloudsearchdomain.Search to before-parameter-build.cloudsearch-domain.Search
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Changing event name from docs.*.cloudsearchdomain.Search.complete-section to docs.*.cloudsearch-domain.Search.complete-section
03/09/2024 16:40:56 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\endpoints.json
03/09/2024 16:40:56 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\sdk-default-configuration.json
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event choose-service-name: calling handler <function handle_service_name_alias at 0x000001CE2801AA20>
03/09/2024 16:40:56 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\s3\2006-03-01\service-2.json.gz
03/09/2024 16:40:56 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\s3\2006-03-01\endpoint-rule-set-1.json.gz
03/09/2024 16:40:56 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\partitions.json
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event creating-client-class.s3: calling handler <function add_generate_presigned_post at 0x000001CE27D8B560>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event creating-client-class.s3: calling handler <function lazy_call.<locals>._handler at 0x000001CE281AEAC0>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event creating-client-class.s3: calling handler <function add_generate_presigned_url at 0x000001CE27D8B2E0>
03/09/2024 16:40:56 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: environment_service
03/09/2024 16:40:56 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: environment_global
03/09/2024 16:40:56 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: config_service
03/09/2024 16:40:56 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: config_global
03/09/2024 16:40:56 - botocore.configprovider - DEBUG - No configured endpoint found.
03/09/2024 16:40:56 - botocore.endpoint - DEBUG - Setting s3 timeout as (60, 60)
03/09/2024 16:40:56 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\_retry.json
03/09/2024 16:40:56 - botocore.client - DEBUG - Registering retry handlers for service: s3
03/09/2024 16:40:56 - botocore.utils - DEBUG - Registering S3 region redirector handler
03/09/2024 16:40:56 - botocore.utils - DEBUG - Registering S3Express Identity Resolver
03/09/2024 16:40:56 - boto3.s3.transfer - DEBUG - Opting out of CRT Transfer Manager. Preferred client: auto, CRT available: False, Instance Optimized: False.
03/09/2024 16:40:56 - boto3.s3.transfer - DEBUG - Using default client. pid: 9336, thread: 1664
03/09/2024 16:40:56 - s3transfer.utils - DEBUG - Acquiring 0
03/09/2024 16:40:56 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x000001CE292DEE40>}) about to wait for the following futures []
03/09/2024 16:40:56 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x000001CE292DEE40>}) done waiting for dependent futures
03/09/2024 16:40:56 - s3transfer.tasks - DEBUG - Executing task UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x000001CE292DEE40>}) with kwargs {'client': <botocore.client.S3 object at 0x000001CE282F0980>, 'config': <boto3.s3.transfer.TransferConfig object at 0x000001CE28D43D10>, 'osutil': <s3transfer.utils.OSUtils object at 0x000001CE286D8980>, 'request_executor': <s3transfer.futures.BoundedExecutor object at 0x000001CE292DF8F0>, 'transfer_future': <s3transfer.futures.TransferFuture object at 0x000001CE292DEE40>}
03/09/2024 16:40:56 - s3transfer.futures - DEBUG - Submitting task PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-164056', 'extra_args': {}}) to executor <s3transfer.futures.BoundedExecutor object at 0x000001CE292DF8F0> for transfer request: 0.
03/09/2024 16:40:56 - s3transfer.utils - DEBUG - Acquiring 0
03/09/2024 16:40:56 - s3transfer.tasks - DEBUG - PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-164056', 'extra_args': {}}) about to wait for the following futures []
03/09/2024 16:40:56 - s3transfer.tasks - DEBUG - PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-164056', 'extra_args': {}}) done waiting for dependent futures
03/09/2024 16:40:56 - s3transfer.utils - DEBUG - Releasing acquire 0/None
03/09/2024 16:40:56 - s3transfer.tasks - DEBUG - Executing task PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-164056', 'extra_args': {}}) with kwargs {'client': <botocore.client.S3 object at 0x000001CE282F0980>, 'fileobj': <s3transfer.utils.ReadFileChunk object at 0x000001CE28340FE0>, 'bucket': 'deassignment', 'key': '20240309-164056', 'extra_args': {}}
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function validate_ascii_metadata at 0x000001CE28041440>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function sse_md5 at 0x000001CE28040720>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function convert_body_to_file_like_object at 0x000001CE28041E40>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function validate_bucket_name at 0x000001CE28040680>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function remove_bucket_from_url_paths_from_model at 0x000001CE280427A0>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.annotate_request_context of <botocore.utils.S3RegionRedirectorv2 object at 0x000001CE28340A10>>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.inject_signing_cache_key of <botocore.utils.S3ExpressIdentityResolver object at 0x000001CE27A60260>>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function generate_idempotent_uuid at 0x000001CE280404A0>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <function customize_endpoint_resolver_builtins at 0x000001CE28042980>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <bound method S3RegionRedirectorv2.redirect_from_cache of <botocore.utils.S3RegionRedirectorv2 object at 0x000001CE28340A10>>
03/09/2024 16:40:56 - botocore.regions - DEBUG - Calling endpoint provider with parameters: {'Bucket': 'deassignment', 'Region': 'us-east-2', 'UseFIPS': False, 'UseDualStack': False, 'ForcePathStyle': False, 'Accelerate': False, 'UseGlobalEndpoint': False, 'Key': '20240309-164056', 'DisableMultiRegionAccessPoints': False, 'UseArnRegion': True}
03/09/2024 16:40:56 - botocore.regions - DEBUG - Endpoint provider result: https://deassignment.s3.us-east-2.amazonaws.com
03/09/2024 16:40:56 - botocore.regions - DEBUG - Selecting from endpoint provider's list of auth schemes: "sigv4". User selected auth scheme is: "None"
03/09/2024 16:40:56 - botocore.regions - DEBUG - Selected auth type "v4" as "v4" with signing context params: {'region': 'us-east-2', 'signing_name': 's3', 'disableDoubleEncoding': True}
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function conditionally_calculate_checksum at 0x000001CE27CD40E0>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function add_expect_header at 0x000001CE28040A40>
03/09/2024 16:40:56 - botocore.handlers - DEBUG - Adding expect 100 continue header to request.
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.apply_signing_cache_key of <botocore.utils.S3ExpressIdentityResolver object at 0x000001CE27A60260>>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function add_recursion_detection_header at 0x000001CE2801B920>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function inject_api_version_header_if_needed at 0x000001CE28041F80>
03/09/2024 16:40:56 - botocore.endpoint - DEBUG - Making request for OperationModel(name=PutObject) with params: {'url_path': '/20240309-164056', 'query_string': {}, 'method': 'PUT', 'headers': {'User-Agent': 'Boto3/1.34.59 md/Botocore#1.34.59 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.2 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.59', 'Content-MD5': 'vMqbr7/CUpboUSDIPHGYfQ==', 'Expect': '100-continue'}, 'body': <s3transfer.utils.ReadFileChunk object at 0x000001CE28340FE0>, 'auth_path': '/deassignment/20240309-164056', 'url': 'https://deassignment.s3.us-east-2.amazonaws.com/20240309-164056', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x000001CE282F19A0>, 'has_streaming_input': True, 'auth_type': 'v4', 's3_redirect': {'redirected': False, 'bucket': 'deassignment', 'params': {'Bucket': 'deassignment', 'Key': '20240309-164056', 'Body': <s3transfer.utils.ReadFileChunk object at 0x000001CE28340FE0>}}, 'S3Express': {'bucket_name': 'deassignment'}, 'signing': {'region': 'us-east-2', 'signing_name': 's3', 'disableDoubleEncoding': True}, 'endpoint_properties': {'authSchemes': [{'disableDoubleEncoding': True, 'name': 'sigv4', 'signingName': 's3', 'signingRegion': 'us-east-2'}]}}}
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_not_transferring at 0x000001CE2C4705E0>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x000001CE280DD940>>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event choose-signer.s3.PutObject: calling handler <function set_operation_specific_signer at 0x000001CE28040360>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <function remove_arn_from_signing_path at 0x000001CE280428E0>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.resolve_s3express_identity of <botocore.utils.S3ExpressIdentityResolver object at 0x000001CE27A60260>>
03/09/2024 16:40:56 - botocore.auth - DEBUG - Calculating signature using v4 auth.
03/09/2024 16:40:56 - botocore.auth - DEBUG - CanonicalRequest:
PUT
/20240309-164056

content-md5:vMqbr7/CUpboUSDIPHGYfQ==
host:deassignment.s3.us-east-2.amazonaws.com
x-amz-content-sha256:UNSIGNED-PAYLOAD
x-amz-date:20240309T214056Z

content-md5;host;x-amz-content-sha256;x-amz-date
UNSIGNED-PAYLOAD
03/09/2024 16:40:56 - botocore.auth - DEBUG - StringToSign:
AWS4-HMAC-SHA256
20240309T214056Z
20240309/us-east-2/s3/aws4_request
fd76cb2d36db1ccac53068ff183ee7ef0ee2841ebdb5de694fd777c57b97be71
03/09/2024 16:40:56 - botocore.auth - DEBUG - Signature:
a5bb247f0a63113284aad59608155bec3a32888d358330dc5e055574c45ef585
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_transferring at 0x000001CE2C470680>
03/09/2024 16:40:56 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function add_retry_headers at 0x000001CE28042700>
03/09/2024 16:40:56 - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=PUT, url=https://deassignment.s3.us-east-2.amazonaws.com/20240309-164056, headers={'User-Agent': b'Boto3/1.34.59 md/Botocore#1.34.59 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.2 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.59', 'Content-MD5': b'vMqbr7/CUpboUSDIPHGYfQ==', 'Expect': b'100-continue', 'X-Amz-Date': b'20240309T214056Z', 'X-Amz-Content-SHA256': b'UNSIGNED-PAYLOAD', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIATNNECNCIQVLW42KP/20240309/us-east-2/s3/aws4_request, SignedHeaders=content-md5;host;x-amz-content-sha256;x-amz-date, Signature=a5bb247f0a63113284aad59608155bec3a32888d358330dc5e055574c45ef585', 'amz-sdk-invocation-id': b'8f9745a3-3f5f-4d1c-a375-560226bf374e', 'amz-sdk-request': b'attempt=1', 'Content-Length': '7970'}>
03/09/2024 16:40:56 - botocore.httpsession - DEBUG - Certificate path: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\certifi\cacert.pem
03/09/2024 16:40:56 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): deassignment.s3.us-east-2.amazonaws.com:443
03/09/2024 16:40:57 - botocore.awsrequest - DEBUG - Waiting for 100 Continue response.
03/09/2024 16:40:57 - botocore.awsrequest - DEBUG - Received a non 100 Continue response from the server, NOT sending request body.
03/09/2024 16:40:57 - botocore.awsrequest - DEBUG - send() called, but response already received. Not sending data.
03/09/2024 16:40:57 - urllib3.connectionpool - DEBUG - https://deassignment.s3.us-east-2.amazonaws.com:443 "PUT /20240309-164056 HTTP/1.1" 301 None
03/09/2024 16:40:57 - botocore.parsers - DEBUG - Response headers: {'x-amz-bucket-region': 'us-east-1', 'x-amz-request-id': 'GD96EW270NPV7JC3', 'x-amz-id-2': 'df8mbNjF/ph0qgDIhollDLRU0AzAVQGaE3VqryLP8ENx3m+yA5YhzBrMCAhwmPgvekLcFq42kwA=', 'Content-Type': 'application/xml', 'Transfer-Encoding': 'chunked', 'Date': 'Sat, 09 Mar 2024 21:40:57 GMT', 'Server': 'AmazonS3', 'Connection': 'close'}
03/09/2024 16:40:57 - botocore.parsers - DEBUG - Response body:
b'<?xml version="1.0" encoding="UTF-8"?>\n<Error><Code>PermanentRedirect</Code><Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message><Endpoint>s3.amazonaws.com</Endpoint><Bucket>deassignment</Bucket><RequestId>GD96EW270NPV7JC3</RequestId><HostId>df8mbNjF/ph0qgDIhollDLRU0AzAVQGaE3VqryLP8ENx3m+yA5YhzBrMCAhwmPgvekLcFq42kwA=</HostId></Error>'
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <botocore.retryhandler.RetryHandler object at 0x000001CE292DFB30>
03/09/2024 16:40:57 - botocore.retryhandler - DEBUG - No retry needed.
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.redirect_from_error of <botocore.utils.S3RegionRedirectorv2 object at 0x000001CE28340A10>>
03/09/2024 16:40:57 - botocore.utils - DEBUG - S3 client configured for region us-east-2 but the bucket deassignment is in region us-east-1; Please configure the proper region to avoid multiple unnecessary redirects and signing attempts.
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <function customize_endpoint_resolver_builtins at 0x000001CE28042980>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <bound method S3RegionRedirectorv2.redirect_from_cache of <botocore.utils.S3RegionRedirectorv2 object at 0x000001CE28340A10>>
03/09/2024 16:40:57 - botocore.regions - DEBUG - Calling endpoint provider with parameters: {'Bucket': 'deassignment', 'Region': 'us-east-1', 'UseFIPS': False, 'UseDualStack': False, 'ForcePathStyle': False, 'Accelerate': False, 'UseGlobalEndpoint': False, 'Key': '20240309-164056', 'DisableMultiRegionAccessPoints': False, 'UseArnRegion': True}
03/09/2024 16:40:57 - botocore.regions - DEBUG - Endpoint provider result: https://deassignment.s3.us-east-1.amazonaws.com
03/09/2024 16:40:57 - botocore.utils - DEBUG - Updating URI from https://deassignment.s3.us-east-2.amazonaws.com/20240309-164056 to https://deassignment.s3.us-east-1.amazonaws.com/20240309-164056
03/09/2024 16:40:57 - botocore.regions - DEBUG - Selecting from endpoint provider's list of auth schemes: "sigv4". User selected auth scheme is: "None"
03/09/2024 16:40:57 - botocore.regions - DEBUG - Selected auth type "v4" as "v4" with signing context params: {'region': 'us-east-1', 'signing_name': 's3', 'disableDoubleEncoding': True}
03/09/2024 16:40:57 - botocore.endpoint - DEBUG - Response received to retry, sleeping for 0 seconds
03/09/2024 16:40:57 - botocore.awsrequest - DEBUG - Rewinding stream: <s3transfer.utils.ReadFileChunk object at 0x000001CE28340FE0>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_not_transferring at 0x000001CE2C4705E0>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x000001CE280DD940>>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event choose-signer.s3.PutObject: calling handler <function set_operation_specific_signer at 0x000001CE28040360>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <function remove_arn_from_signing_path at 0x000001CE280428E0>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.resolve_s3express_identity of <botocore.utils.S3ExpressIdentityResolver object at 0x000001CE27A60260>>
03/09/2024 16:40:57 - botocore.auth - DEBUG - Calculating signature using v4 auth.
03/09/2024 16:40:57 - botocore.auth - DEBUG - CanonicalRequest:
PUT
/20240309-164056

content-md5:vMqbr7/CUpboUSDIPHGYfQ==
host:deassignment.s3.us-east-1.amazonaws.com
x-amz-content-sha256:UNSIGNED-PAYLOAD
x-amz-date:20240309T214057Z

content-md5;host;x-amz-content-sha256;x-amz-date
UNSIGNED-PAYLOAD
03/09/2024 16:40:57 - botocore.auth - DEBUG - StringToSign:
AWS4-HMAC-SHA256
20240309T214057Z
20240309/us-east-1/s3/aws4_request
29ec000b303349609348519bc2f6a5c0ff241bdb449e8635203334ac622640f0
03/09/2024 16:40:57 - botocore.auth - DEBUG - Signature:
e1c4a9c6afcca02e880ef22278da52c570383dc5ef449173ecc38ed7f01e4558
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_transferring at 0x000001CE2C470680>
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function add_retry_headers at 0x000001CE28042700>
03/09/2024 16:40:57 - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=PUT, url=https://deassignment.s3.us-east-1.amazonaws.com/20240309-164056, headers={'User-Agent': b'Boto3/1.34.59 md/Botocore#1.34.59 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.2 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.59', 'Content-MD5': b'vMqbr7/CUpboUSDIPHGYfQ==', 'Expect': b'100-continue', 'X-Amz-Date': b'20240309T214057Z', 'X-Amz-Content-SHA256': b'UNSIGNED-PAYLOAD', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIATNNECNCIQVLW42KP/20240309/us-east-1/s3/aws4_request, SignedHeaders=content-md5;host;x-amz-content-sha256;x-amz-date, Signature=e1c4a9c6afcca02e880ef22278da52c570383dc5ef449173ecc38ed7f01e4558', 'amz-sdk-invocation-id': b'8f9745a3-3f5f-4d1c-a375-560226bf374e', 'amz-sdk-request': b'ttl=20240309T214157Z; attempt=2; max=5', 'Content-Length': '7970'}>
03/09/2024 16:40:57 - botocore.httpsession - DEBUG - Certificate path: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\certifi\cacert.pem
03/09/2024 16:40:57 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): deassignment.s3.us-east-1.amazonaws.com:443
03/09/2024 16:40:57 - botocore.awsrequest - DEBUG - Waiting for 100 Continue response.
03/09/2024 16:40:57 - botocore.awsrequest - DEBUG - 100 Continue response seen, now sending request body.
03/09/2024 16:40:57 - urllib3.connectionpool - DEBUG - https://deassignment.s3.us-east-1.amazonaws.com:443 "PUT /20240309-164056 HTTP/1.1" 200 0
03/09/2024 16:40:57 - botocore.parsers - DEBUG - Response headers: {'x-amz-id-2': 'H4DrEKU6SkHN5q/62w8SCwYZE0dO4sLHkpVKaCPJaae6m+CX96U3hEGfVCkxLMHPSti2xkujM2o=', 'x-amz-request-id': 'GD9140BG4GEWAE2A', 'Date': 'Sat, 09 Mar 2024 21:40:58 GMT', 'x-amz-server-side-encryption': 'AES256', 'ETag': '"bcca9bafbfc25296e85120c83c71987d"', 'Server': 'AmazonS3', 'Content-Length': '0'}
03/09/2024 16:40:57 - botocore.parsers - DEBUG - Response body:
b''
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <botocore.retryhandler.RetryHandler object at 0x000001CE292DFB30>
03/09/2024 16:40:57 - botocore.retryhandler - DEBUG - No retry needed.
03/09/2024 16:40:57 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.redirect_from_error of <botocore.utils.S3RegionRedirectorv2 object at 0x000001CE28340A10>>
03/09/2024 16:40:57 - botocore.utils - DEBUG - S3 request was previously redirected, not redirecting.
03/09/2024 16:40:57 - s3transfer.utils - DEBUG - Releasing acquire 0/None
