# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/model_evaluation.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1.proto import (
    translation_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/model_evaluation.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoML\\V1\352\002\031Google::Cloud::AutoML::V1"
    ),
    serialized_pb=_b(
        '\n3google/cloud/automl_v1/proto/model_evaluation.proto\x12\x16google.cloud.automl.v1\x1a.google/cloud/automl_v1/proto/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\xf8\x01\n\x0fModelEvaluation\x12^\n\x1etranslation_evaluation_metrics\x18\t \x01(\x0b\x32\x34.google.cloud.automl.v1.TranslationEvaluationMetricsH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x61nnotation_spec_id\x18\x02 \x01(\t\x12/\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x17\x65valuated_example_count\x18\x06 \x01(\x05\x42\t\n\x07metricsB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoML\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_MODELEVALUATION = _descriptor.Descriptor(
    name="ModelEvaluation",
    full_name="google.cloud.automl.v1.ModelEvaluation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="translation_evaluation_metrics",
            full_name="google.cloud.automl.v1.ModelEvaluation.translation_evaluation_metrics",
            index=0,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1.ModelEvaluation.name",
            index=1,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1.ModelEvaluation.annotation_spec_id",
            index=2,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.automl.v1.ModelEvaluation.create_time",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="evaluated_example_count",
            full_name="google.cloud.automl.v1.ModelEvaluation.evaluated_example_count",
            index=4,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="metrics",
            full_name="google.cloud.automl.v1.ModelEvaluation.metrics",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=191,
    serialized_end=439,
)

_MODELEVALUATION.fields_by_name[
    "translation_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2._TRANSLATIONEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["translation_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "translation_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
DESCRIPTOR.message_types_by_name["ModelEvaluation"] = _MODELEVALUATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelEvaluation = _reflection.GeneratedProtocolMessageType(
    "ModelEvaluation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MODELEVALUATION,
        __module__="google.cloud.automl_v1.proto.model_evaluation_pb2",
        __doc__="""Evaluation results of a model.
  
  
  Attributes:
      metrics:
          Output only. Problem type specific evaluation metrics.
      translation_evaluation_metrics:
          Model evaluation metrics for translation.
      name:
          Output only. Resource name of the model evaluation. Format:  `
          `projects/{project_id}/locations/{location_id}/models/{model_i
          d}/modelEvaluations/{model_evaluation_id}``
      annotation_spec_id:
          Output only. The ID of the annotation spec that the model
          evaluation applies to. The The ID is empty for the overall
          model evaluation.
      create_time:
          Output only. Timestamp when this model evaluation was created.
      evaluated_example_count:
          Output only. The number of examples used for model evaluation,
          i.e. for which ground truth from time of model creation is
          compared against the predicted annotations created by the
          model. For overall ModelEvaluation (i.e. with
          annotation\_spec\_id not set) this is the total number of all
          examples used for evaluation. Otherwise, this is the count of
          examples that according to the ground truth were annotated by
          the  [annotation\_spec\_id][google.cloud.automl.v1beta1.ModelE
          valuation.annotation\_spec\_id].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ModelEvaluation)
    ),
)
_sym_db.RegisterMessage(ModelEvaluation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
