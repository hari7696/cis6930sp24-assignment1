something03/09/2024 16:12:44 - root - INFO - Args parsed (Namespace(), ['--input', 'text_files/*.txt', '--names', '--dates', '--phones', '--address', '--output', 'files/', '--stats', 'stdout'])
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from creating-client-class.iot-data to creating-client-class.iot-data-plane
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from before-call.apigateway to before-call.api-gateway
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from request-created.machinelearning.Predict to request-created.machine-learning.Predict
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.autoscaling.CreateLaunchConfiguration to before-parameter-build.auto-scaling.CreateLaunchConfiguration
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.route53 to before-parameter-build.route-53
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from request-created.cloudsearchdomain.Search to request-created.cloudsearch-domain.Search
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from docs.*.autoscaling.CreateLaunchConfiguration.complete-section to docs.*.auto-scaling.CreateLaunchConfiguration.complete-section
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.logs.CreateExportTask to before-parameter-build.cloudwatch-logs.CreateExportTask
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from docs.*.logs.CreateExportTask.complete-section to docs.*.cloudwatch-logs.CreateExportTask.complete-section
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from before-parameter-build.cloudsearchdomain.Search to before-parameter-build.cloudsearch-domain.Search
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Changing event name from docs.*.cloudsearchdomain.Search.complete-section to docs.*.cloudsearch-domain.Search.complete-section
03/09/2024 16:12:44 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\endpoints.json
03/09/2024 16:12:44 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\sdk-default-configuration.json
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event choose-service-name: calling handler <function handle_service_name_alias at 0x00000222A731EAC0>
03/09/2024 16:12:44 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\s3\2006-03-01\service-2.json.gz
03/09/2024 16:12:44 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\s3\2006-03-01\endpoint-rule-set-1.json.gz
03/09/2024 16:12:44 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\partitions.json
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event creating-client-class.s3: calling handler <function add_generate_presigned_post at 0x00000222A7283600>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event creating-client-class.s3: calling handler <function lazy_call.<locals>._handler at 0x00000222A73C5800>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event creating-client-class.s3: calling handler <function add_generate_presigned_url at 0x00000222A7283380>
03/09/2024 16:12:44 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: environment_service
03/09/2024 16:12:44 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: environment_global
03/09/2024 16:12:44 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: config_service
03/09/2024 16:12:44 - botocore.configprovider - DEBUG - Looking for endpoint for s3 via: config_global
03/09/2024 16:12:44 - botocore.configprovider - DEBUG - No configured endpoint found.
03/09/2024 16:12:44 - botocore.endpoint - DEBUG - Setting s3 timeout as (60, 60)
03/09/2024 16:12:44 - botocore.loaders - DEBUG - Loading JSON file: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\botocore\data\_retry.json
03/09/2024 16:12:44 - botocore.client - DEBUG - Registering retry handlers for service: s3
03/09/2024 16:12:44 - botocore.utils - DEBUG - Registering S3 region redirector handler
03/09/2024 16:12:44 - botocore.utils - DEBUG - Registering S3Express Identity Resolver
03/09/2024 16:12:44 - boto3.s3.transfer - DEBUG - Opting out of CRT Transfer Manager. Preferred client: auto, CRT available: False, Instance Optimized: False.
03/09/2024 16:12:44 - boto3.s3.transfer - DEBUG - Using default client. pid: 1944, thread: 12624
03/09/2024 16:12:44 - s3transfer.utils - DEBUG - Acquiring 0
03/09/2024 16:12:44 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x00000222A7C56E70>}) about to wait for the following futures []
03/09/2024 16:12:44 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x00000222A7C56E70>}) done waiting for dependent futures
03/09/2024 16:12:44 - s3transfer.tasks - DEBUG - Executing task UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x00000222A7C56E70>}) with kwargs {'client': <botocore.client.S3 object at 0x00000222A6A94AD0>, 'config': <boto3.s3.transfer.TransferConfig object at 0x00000222A6A976E0>, 'osutil': <s3transfer.utils.OSUtils object at 0x00000222A7B463F0>, 'request_executor': <s3transfer.futures.BoundedExecutor object at 0x00000222A640F890>, 'transfer_future': <s3transfer.futures.TransferFuture object at 0x00000222A7C56E70>}
03/09/2024 16:12:44 - s3transfer.futures - DEBUG - Submitting task PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-161244', 'extra_args': {}}) to executor <s3transfer.futures.BoundedExecutor object at 0x00000222A640F890> for transfer request: 0.
03/09/2024 16:12:44 - s3transfer.utils - DEBUG - Acquiring 0
03/09/2024 16:12:44 - s3transfer.tasks - DEBUG - PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-161244', 'extra_args': {}}) about to wait for the following futures []
03/09/2024 16:12:44 - s3transfer.utils - DEBUG - Releasing acquire 0/None
03/09/2024 16:12:44 - s3transfer.tasks - DEBUG - PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-161244', 'extra_args': {}}) done waiting for dependent futures
03/09/2024 16:12:44 - s3transfer.tasks - DEBUG - Executing task PutObjectTask(transfer_id=0, {'bucket': 'deassignment', 'key': '20240309-161244', 'extra_args': {}}) with kwargs {'client': <botocore.client.S3 object at 0x00000222A6A94AD0>, 'fileobj': <s3transfer.utils.ReadFileChunk object at 0x00000222A5FA6000>, 'bucket': 'deassignment', 'key': '20240309-161244', 'extra_args': {}}
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function validate_ascii_metadata at 0x00000222A73414E0>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function sse_md5 at 0x00000222A73407C0>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function convert_body_to_file_like_object at 0x00000222A7341EE0>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function validate_bucket_name at 0x00000222A7340720>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function remove_bucket_from_url_paths_from_model at 0x00000222A7342840>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.annotate_request_context of <botocore.utils.S3RegionRedirectorv2 object at 0x00000222A646ECC0>>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.inject_signing_cache_key of <botocore.utils.S3ExpressIdentityResolver object at 0x00000222A640E8A0>>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function generate_idempotent_uuid at 0x00000222A7340540>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <function customize_endpoint_resolver_builtins at 0x00000222A7342A20>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <bound method S3RegionRedirectorv2.redirect_from_cache of <botocore.utils.S3RegionRedirectorv2 object at 0x00000222A646ECC0>>
03/09/2024 16:12:44 - botocore.regions - DEBUG - Calling endpoint provider with parameters: {'Bucket': 'deassignment', 'Region': 'us-east-2', 'UseFIPS': False, 'UseDualStack': False, 'ForcePathStyle': False, 'Accelerate': False, 'UseGlobalEndpoint': False, 'Key': '20240309-161244', 'DisableMultiRegionAccessPoints': False, 'UseArnRegion': True}
03/09/2024 16:12:44 - botocore.regions - DEBUG - Endpoint provider result: https://deassignment.s3.us-east-2.amazonaws.com
03/09/2024 16:12:44 - botocore.regions - DEBUG - Selecting from endpoint provider's list of auth schemes: "sigv4". User selected auth scheme is: "None"
03/09/2024 16:12:44 - botocore.regions - DEBUG - Selected auth type "v4" as "v4" with signing context params: {'region': 'us-east-2', 'signing_name': 's3', 'disableDoubleEncoding': True}
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function conditionally_calculate_checksum at 0x00000222A6FD4180>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function add_expect_header at 0x00000222A7340AE0>
03/09/2024 16:12:44 - botocore.handlers - DEBUG - Adding expect 100 continue header to request.
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.apply_signing_cache_key of <botocore.utils.S3ExpressIdentityResolver object at 0x00000222A640E8A0>>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function add_recursion_detection_header at 0x00000222A731F9C0>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function inject_api_version_header_if_needed at 0x00000222A7342020>
03/09/2024 16:12:44 - botocore.endpoint - DEBUG - Making request for OperationModel(name=PutObject) with params: {'url_path': '/20240309-161244', 'query_string': {}, 'method': 'PUT', 'headers': {'User-Agent': 'Boto3/1.34.59 md/Botocore#1.34.59 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.2 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.59', 'Content-MD5': 'OZplqOr21vYCdETr+vWC9g==', 'Expect': '100-continue'}, 'body': <s3transfer.utils.ReadFileChunk object at 0x00000222A5FA6000>, 'auth_path': '/deassignment/20240309-161244', 'url': 'https://deassignment.s3.us-east-2.amazonaws.com/20240309-161244', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x00000222A64DCAA0>, 'has_streaming_input': True, 'auth_type': 'v4', 's3_redirect': {'redirected': False, 'bucket': 'deassignment', 'params': {'Bucket': 'deassignment', 'Key': '20240309-161244', 'Body': <s3transfer.utils.ReadFileChunk object at 0x00000222A5FA6000>}}, 'S3Express': {'bucket_name': 'deassignment'}, 'signing': {'region': 'us-east-2', 'signing_name': 's3', 'disableDoubleEncoding': True}, 'endpoint_properties': {'authSchemes': [{'disableDoubleEncoding': True, 'name': 'sigv4', 'signingName': 's3', 'signingRegion': 'us-east-2'}]}}}
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_not_transferring at 0x00000222A7BCA340>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x00000222A6A97A70>>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event choose-signer.s3.PutObject: calling handler <function set_operation_specific_signer at 0x00000222A7340400>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <function remove_arn_from_signing_path at 0x00000222A7342980>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.resolve_s3express_identity of <botocore.utils.S3ExpressIdentityResolver object at 0x00000222A640E8A0>>
03/09/2024 16:12:44 - botocore.auth - DEBUG - Calculating signature using v4 auth.
03/09/2024 16:12:44 - botocore.auth - DEBUG - CanonicalRequest:
PUT
/20240309-161244

content-md5:OZplqOr21vYCdETr+vWC9g==
host:deassignment.s3.us-east-2.amazonaws.com
x-amz-content-sha256:UNSIGNED-PAYLOAD
x-amz-date:20240309T211244Z

content-md5;host;x-amz-content-sha256;x-amz-date
UNSIGNED-PAYLOAD
03/09/2024 16:12:44 - botocore.auth - DEBUG - StringToSign:
AWS4-HMAC-SHA256
20240309T211244Z
20240309/us-east-2/s3/aws4_request
25abcc0a12b315928b87d099a61ad5b95c286afcf6ce02a11a927c063568db9b
03/09/2024 16:12:44 - botocore.auth - DEBUG - Signature:
a780a02628bf7f7da2aebc9b5ca9fa60fbeb64536097ad2ce6935c09b9368c0f
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_transferring at 0x00000222A7BCA3E0>
03/09/2024 16:12:44 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function add_retry_headers at 0x00000222A73427A0>
03/09/2024 16:12:44 - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=PUT, url=https://deassignment.s3.us-east-2.amazonaws.com/20240309-161244, headers={'User-Agent': b'Boto3/1.34.59 md/Botocore#1.34.59 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.2 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.59', 'Content-MD5': b'OZplqOr21vYCdETr+vWC9g==', 'Expect': b'100-continue', 'X-Amz-Date': b'20240309T211244Z', 'X-Amz-Content-SHA256': b'UNSIGNED-PAYLOAD', 'Authorization': b'AWS4-HMAC-SHA256 Credential=***REMOVED***/20240309/us-east-2/s3/aws4_request, SignedHeaders=content-md5;host;x-amz-content-sha256;x-amz-date, Signature=a780a02628bf7f7da2aebc9b5ca9fa60fbeb64536097ad2ce6935c09b9368c0f', 'amz-sdk-invocation-id': b'52f683b8-2c45-427b-a5b4-a3afc13d5a1c', 'amz-sdk-request': b'attempt=1', 'Content-Length': '5947'}>
03/09/2024 16:12:44 - botocore.httpsession - DEBUG - Certificate path: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\certifi\cacert.pem
03/09/2024 16:12:44 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): deassignment.s3.us-east-2.amazonaws.com:443
03/09/2024 16:12:45 - botocore.awsrequest - DEBUG - Waiting for 100 Continue response.
03/09/2024 16:12:45 - botocore.awsrequest - DEBUG - Received a non 100 Continue response from the server, NOT sending request body.
03/09/2024 16:12:45 - botocore.awsrequest - DEBUG - send() called, but response already received. Not sending data.
03/09/2024 16:12:45 - urllib3.connectionpool - DEBUG - https://deassignment.s3.us-east-2.amazonaws.com:443 "PUT /20240309-161244 HTTP/1.1" 301 None
03/09/2024 16:12:45 - botocore.parsers - DEBUG - Response headers: {'x-amz-bucket-region': 'us-east-1', 'x-amz-request-id': 'V85ZRZSGS2E2PYWQ', 'x-amz-id-2': 'odPY3GnLB9rDuzQJSnPEB55FL/p5m9cVeI0Lffm0uPHXVxdUz5MisYOLKJsbmcLLEqR1MxeSNFiCyjXeScpdCA==', 'Content-Type': 'application/xml', 'Transfer-Encoding': 'chunked', 'Date': 'Sat, 09 Mar 2024 21:12:45 GMT', 'Server': 'AmazonS3', 'Connection': 'close'}
03/09/2024 16:12:45 - botocore.parsers - DEBUG - Response body:
b'<?xml version="1.0" encoding="UTF-8"?>\n<Error><Code>PermanentRedirect</Code><Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message><Endpoint>s3.amazonaws.com</Endpoint><Bucket>deassignment</Bucket><RequestId>V85ZRZSGS2E2PYWQ</RequestId><HostId>odPY3GnLB9rDuzQJSnPEB55FL/p5m9cVeI0Lffm0uPHXVxdUz5MisYOLKJsbmcLLEqR1MxeSNFiCyjXeScpdCA==</HostId></Error>'
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <botocore.retryhandler.RetryHandler object at 0x00000222A7B46F60>
03/09/2024 16:12:45 - botocore.retryhandler - DEBUG - No retry needed.
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.redirect_from_error of <botocore.utils.S3RegionRedirectorv2 object at 0x00000222A646ECC0>>
03/09/2024 16:12:45 - botocore.utils - DEBUG - S3 client configured for region us-east-2 but the bucket deassignment is in region us-east-1; Please configure the proper region to avoid multiple unnecessary redirects and signing attempts.
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <function customize_endpoint_resolver_builtins at 0x00000222A7342A20>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <bound method S3RegionRedirectorv2.redirect_from_cache of <botocore.utils.S3RegionRedirectorv2 object at 0x00000222A646ECC0>>
03/09/2024 16:12:45 - botocore.regions - DEBUG - Calling endpoint provider with parameters: {'Bucket': 'deassignment', 'Region': 'us-east-1', 'UseFIPS': False, 'UseDualStack': False, 'ForcePathStyle': False, 'Accelerate': False, 'UseGlobalEndpoint': False, 'Key': '20240309-161244', 'DisableMultiRegionAccessPoints': False, 'UseArnRegion': True}
03/09/2024 16:12:45 - botocore.regions - DEBUG - Endpoint provider result: https://deassignment.s3.us-east-1.amazonaws.com
03/09/2024 16:12:45 - botocore.utils - DEBUG - Updating URI from https://deassignment.s3.us-east-2.amazonaws.com/20240309-161244 to https://deassignment.s3.us-east-1.amazonaws.com/20240309-161244
03/09/2024 16:12:45 - botocore.regions - DEBUG - Selecting from endpoint provider's list of auth schemes: "sigv4". User selected auth scheme is: "None"
03/09/2024 16:12:45 - botocore.regions - DEBUG - Selected auth type "v4" as "v4" with signing context params: {'region': 'us-east-1', 'signing_name': 's3', 'disableDoubleEncoding': True}
03/09/2024 16:12:45 - botocore.endpoint - DEBUG - Response received to retry, sleeping for 0 seconds
03/09/2024 16:12:45 - botocore.awsrequest - DEBUG - Rewinding stream: <s3transfer.utils.ReadFileChunk object at 0x00000222A5FA6000>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_not_transferring at 0x00000222A7BCA340>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x00000222A6A97A70>>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event choose-signer.s3.PutObject: calling handler <function set_operation_specific_signer at 0x00000222A7340400>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <function remove_arn_from_signing_path at 0x00000222A7342980>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.resolve_s3express_identity of <botocore.utils.S3ExpressIdentityResolver object at 0x00000222A640E8A0>>
03/09/2024 16:12:45 - botocore.auth - DEBUG - Calculating signature using v4 auth.
03/09/2024 16:12:45 - botocore.auth - DEBUG - CanonicalRequest:
PUT
/20240309-161244

content-md5:OZplqOr21vYCdETr+vWC9g==
host:deassignment.s3.us-east-1.amazonaws.com
x-amz-content-sha256:UNSIGNED-PAYLOAD
x-amz-date:20240309T211245Z

content-md5;host;x-amz-content-sha256;x-amz-date
UNSIGNED-PAYLOAD
03/09/2024 16:12:45 - botocore.auth - DEBUG - StringToSign:
AWS4-HMAC-SHA256
20240309T211245Z
20240309/us-east-1/s3/aws4_request
d35e293f12ebe9b09bc59b654fc1a7f4ce9a500a45e9f1614cb5a68ea4254354
03/09/2024 16:12:45 - botocore.auth - DEBUG - Signature:
910ed1efa878145dbfb5c5d63fc1d6b6a40637929f0982382459c4cdb42e2074
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_transferring at 0x00000222A7BCA3E0>
03/09/2024 16:12:45 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function add_retry_headers at 0x00000222A73427A0>
03/09/2024 16:12:45 - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=PUT, url=https://deassignment.s3.us-east-1.amazonaws.com/20240309-161244, headers={'User-Agent': b'Boto3/1.34.59 md/Botocore#1.34.59 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.2 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.59', 'Content-MD5': b'OZplqOr21vYCdETr+vWC9g==', 'Expect': b'100-continue', 'X-Amz-Date': b'20240309T211245Z', 'X-Amz-Content-SHA256': b'UNSIGNED-PAYLOAD', 'Authorization': b'AWS4-HMAC-SHA256 Credential=***REMOVED***/20240309/us-east-1/s3/aws4_request, SignedHeaders=content-md5;host;x-amz-content-sha256;x-amz-date, Signature=910ed1efa878145dbfb5c5d63fc1d6b6a40637929f0982382459c4cdb42e2074', 'amz-sdk-invocation-id': b'52f683b8-2c45-427b-a5b4-a3afc13d5a1c', 'amz-sdk-request': b'ttl=20240309T211345Z; attempt=2; max=5', 'Content-Length': '5947'}>
03/09/2024 16:12:45 - botocore.httpsession - DEBUG - Certificate path: C:\Users\ghari\.virtualenvs\cis6930sp24-assignment1-uWBnGQ1j\Lib\site-packages\certifi\cacert.pem
03/09/2024 16:12:45 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): deassignment.s3.us-east-1.amazonaws.com:443
03/09/2024 16:12:45 - botocore.awsrequest - DEBUG - Waiting for 100 Continue response.
03/09/2024 16:12:46 - botocore.awsrequest - DEBUG - 100 Continue response seen, now sending request body.
03/09/2024 16:12:46 - urllib3.connectionpool - DEBUG - https://deassignment.s3.us-east-1.amazonaws.com:443 "PUT /20240309-161244 HTTP/1.1" 200 0
03/09/2024 16:12:46 - botocore.parsers - DEBUG - Response headers: {'x-amz-id-2': 'w0taPcbYZEHrXXJCbQzeALOvM/6oZlS9UokOuymx2UtWpTweUCflYtfIbYOgY5nfW9w6nkjZTpM=', 'x-amz-request-id': 'V85NMPSKF4M2JZG9', 'Date': 'Sat, 09 Mar 2024 21:12:46 GMT', 'x-amz-server-side-encryption': 'AES256', 'ETag': '"399a65a8eaf6d6f6027444ebfaf582f6"', 'Server': 'AmazonS3', 'Content-Length': '0'}
03/09/2024 16:12:46 - botocore.parsers - DEBUG - Response body:
b''
03/09/2024 16:12:46 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <botocore.retryhandler.RetryHandler object at 0x00000222A7B46F60>
03/09/2024 16:12:46 - botocore.retryhandler - DEBUG - No retry needed.
03/09/2024 16:12:46 - botocore.hooks - DEBUG - Event needs-retry.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.redirect_from_error of <botocore.utils.S3RegionRedirectorv2 object at 0x00000222A646ECC0>>
03/09/2024 16:12:46 - botocore.utils - DEBUG - S3 request was previously redirected, not redirecting.
03/09/2024 16:12:46 - s3transfer.utils - DEBUG - Releasing acquire 0/None
