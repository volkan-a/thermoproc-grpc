# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coolprop.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x63oolprop.proto\"W\n\x12\x43\x61lculationRequest\x12#\n\x0cpropertyPair\x18\x01 \x01(\x0e\x32\r.PropertyPair\x12\r\n\x05value\x18\x02 \x01(\x01\x12\r\n\x05\x66luid\x18\x03 \x01(\t\"\xba\x01\n\x0f\x46luidProperties\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x10\n\x08pressure\x18\x02 \x01(\x02\x12\x16\n\x0especificVolume\x18\x03 \x01(\x02\x12\x1e\n\x16specificInternalEnergy\x18\x04 \x01(\x02\x12\x18\n\x10specificEnthalpy\x18\x05 \x01(\x02\x12\x17\n\x0fspecificEntropy\x18\x06 \x01(\x02\x12\x15\n\rvaporFraction\x18\x07 \x01(\x02\"@\n\x13\x43\x61lculationResponse\x12)\n\x0f\x66luidProperties\x18\x01 \x01(\x0b\x32\x10.FluidProperties*8\n\x0cPropertyPair\x12\x06\n\x02TP\x10\x00\x12\x07\n\x03TVF\x10\x01\x12\x07\n\x03PVF\x10\x02\x12\x06\n\x02PH\x10\x03\x12\x06\n\x02PS\x10\x04\x32N\n\x12\x43\x61lculationService\x12\x38\n\tCalculate\x12\x13.CalculationRequest\x1a\x14.CalculationResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'coolprop_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROPERTYPAIR._serialized_start=362
  _PROPERTYPAIR._serialized_end=418
  _CALCULATIONREQUEST._serialized_start=18
  _CALCULATIONREQUEST._serialized_end=105
  _FLUIDPROPERTIES._serialized_start=108
  _FLUIDPROPERTIES._serialized_end=294
  _CALCULATIONRESPONSE._serialized_start=296
  _CALCULATIONRESPONSE._serialized_end=360
  _CALCULATIONSERVICE._serialized_start=420
  _CALCULATIONSERVICE._serialized_end=498
# @@protoc_insertion_point(module_scope)
