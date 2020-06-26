# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/iam_credentials_v1/proto/iamcredentials.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.cloud.iam_credentials_v1.proto import (
    common_pb2 as google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/iam_credentials_v1/proto/iamcredentials.proto",
    package="google.iam.credentials.v1",
    syntax="proto3",
    serialized_options=b"\n#com.google.cloud.iam.credentials.v1B\023IAMCredentialsProtoP\001ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\370\001\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n:google/cloud/iam_credentials_v1/proto/iamcredentials.proto\x12\x19google.iam.credentials.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x32google/cloud/iam_credentials_v1/proto/common.proto2\xad\x07\n\x0eIAMCredentials\x12\xec\x01\n\x13GenerateAccessToken\x12\x35.google.iam.credentials.v1.GenerateAccessTokenRequest\x1a\x36.google.iam.credentials.v1.GenerateAccessTokenResponse"f\x82\xd3\xe4\x93\x02@";/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken:\x01*\xda\x41\x1dname,delegates,scope,lifetime\x12\xe4\x01\n\x0fGenerateIdToken\x12\x31.google.iam.credentials.v1.GenerateIdTokenRequest\x1a\x32.google.iam.credentials.v1.GenerateIdTokenResponse"j\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/serviceAccounts/*}:generateIdToken:\x01*\xda\x41%name,delegates,audience,include_email\x12\xb9\x01\n\x08SignBlob\x12*.google.iam.credentials.v1.SignBlobRequest\x1a+.google.iam.credentials.v1.SignBlobResponse"T\x82\xd3\xe4\x93\x02\x35"0/v1/{name=projects/*/serviceAccounts/*}:signBlob:\x01*\xda\x41\x16name,delegates,payload\x12\xb5\x01\n\x07SignJwt\x12).google.iam.credentials.v1.SignJwtRequest\x1a*.google.iam.credentials.v1.SignJwtResponse"S\x82\xd3\xe4\x93\x02\x34"//v1/{name=projects/*/serviceAccounts/*}:signJwt:\x01*\xda\x41\x16name,delegates,payload\x1aQ\xca\x41\x1diamcredentials.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x85\x01\n#com.google.cloud.iam.credentials.v1B\x13IAMCredentialsProtoP\x01ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\xf8\x01\x01\x62\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2.DESCRIPTOR,
    ],
)


_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_IAMCREDENTIALS = _descriptor.ServiceDescriptor(
    name="IAMCredentials",
    full_name="google.iam.credentials.v1.IAMCredentials",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\035iamcredentials.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    create_key=_descriptor._internal_create_key,
    serialized_start=197,
    serialized_end=1138,
    methods=[
        _descriptor.MethodDescriptor(
            name="GenerateAccessToken",
            full_name="google.iam.credentials.v1.IAMCredentials.GenerateAccessToken",
            index=0,
            containing_service=None,
            input_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._GENERATEACCESSTOKENREQUEST,
            output_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._GENERATEACCESSTOKENRESPONSE,
            serialized_options=b'\202\323\344\223\002@";/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken:\001*\332A\035name,delegates,scope,lifetime',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GenerateIdToken",
            full_name="google.iam.credentials.v1.IAMCredentials.GenerateIdToken",
            index=1,
            containing_service=None,
            input_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._GENERATEIDTOKENREQUEST,
            output_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._GENERATEIDTOKENRESPONSE,
            serialized_options=b'\202\323\344\223\002<"7/v1/{name=projects/*/serviceAccounts/*}:generateIdToken:\001*\332A%name,delegates,audience,include_email',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SignBlob",
            full_name="google.iam.credentials.v1.IAMCredentials.SignBlob",
            index=2,
            containing_service=None,
            input_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._SIGNBLOBREQUEST,
            output_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._SIGNBLOBRESPONSE,
            serialized_options=b'\202\323\344\223\0025"0/v1/{name=projects/*/serviceAccounts/*}:signBlob:\001*\332A\026name,delegates,payload',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SignJwt",
            full_name="google.iam.credentials.v1.IAMCredentials.SignJwt",
            index=3,
            containing_service=None,
            input_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._SIGNJWTREQUEST,
            output_type=google_dot_cloud_dot_iam__credentials__v1_dot_proto_dot_common__pb2._SIGNJWTRESPONSE,
            serialized_options=b'\202\323\344\223\0024"//v1/{name=projects/*/serviceAccounts/*}:signJwt:\001*\332A\026name,delegates,payload',
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_IAMCREDENTIALS)

DESCRIPTOR.services_by_name["IAMCredentials"] = _IAMCREDENTIALS

# @@protoc_insertion_point(module_scope)
