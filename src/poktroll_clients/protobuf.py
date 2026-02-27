from dataclasses import dataclass
from typing import List

from cffi import FFIError

from poktroll_clients.ffi import ffi


@dataclass
class SerializedProto:
    """
    Represents a serialized protobuf message with its type URL and binary data.
    Handles conversion to C structures while ensuring proper memory management.
    """
    type_url: str
    data: bytes

    def to_c_struct(self) -> ffi.CData:
        """
        Converts the Python protobuf data to a C struct while preserving the underlying memory.
        Returns a C serialized_proto struct pointer.
        """
        serialized_proto = ffi.new("serialized_proto *")

        # Create buffers and store them as instance attributes to prevent GC
        self._type_url_bytes = self.type_url.encode('utf-8')
        self._type_url_buffer = ffi.new("uint8_t[]", self._type_url_bytes)
        self._data_buffer = ffi.new("uint8_t[]", self.data)

        # Assign the buffers to the C struct
        serialized_proto.type_url = self._type_url_buffer
        serialized_proto.type_url_length = len(self._type_url_bytes)
        serialized_proto.data = self._data_buffer
        serialized_proto.data_length = len(self.data)

        return serialized_proto


@dataclass
class ProtoMessageArray:
    """
    Represents an array of serialized protobuf messages.
    Handles conversion to C structures while ensuring proper memory management.
    """
    messages: List[SerializedProto]

    def to_c_struct(self) -> ffi.CData:
        """
        Converts the Python protobuf message array to a C struct while preserving the underlying memory.
        Returns a C serialized_proto_array struct pointer.
        """
        # Create the array structure
        proto_array = ffi.new("serialized_proto_array *")
        proto_array.num_protos = len(self.messages)

        # Allocate the array of message structures
        proto_array.protos = ffi.new("serialized_proto[]", len(self.messages))

        # Convert each message and store C structs as instance attributes
        self._message_structs = []
        for i, msg in enumerate(self.messages):
            # Create and store the C struct for this message
            c_msg = msg.to_c_struct()
            self._message_structs.append(c_msg)

            # Copy the data to the array
            proto_array.protos[i].type_url = c_msg.type_url
            proto_array.protos[i].type_url_length = c_msg.type_url_length
            proto_array.protos[i].data = c_msg.data
            proto_array.protos[i].data_length = c_msg.data_length

        return proto_array


def deserialize_proto(raw_ptr, proto_class):
    """Deserialize a void* (C serialized_proto pointer) into a Python protobuf message."""
    if raw_ptr == ffi.NULL:
        raise FFIError("null serialized_proto pointer")
    c_proto = ffi.cast("serialized_proto *", raw_ptr)
    data_bytes = bytes(ffi.buffer(c_proto.data, c_proto.data_length))
    msg = proto_class()
    msg.ParseFromString(data_bytes)
    return msg


def deserialize_proto_array(raw_ptr, proto_class):
    """Deserialize a void* (C serialized_proto_array pointer) into a list of Python protobuf messages."""
    if raw_ptr == ffi.NULL:
        raise FFIError("null serialized_proto_array pointer")
    c_array = ffi.cast("serialized_proto_array *", raw_ptr)
    results = []
    for i in range(c_array.num_protos):
        data_bytes = bytes(ffi.buffer(c_array.protos[i].data, c_array.protos[i].data_length))
        msg = proto_class()
        msg.ParseFromString(data_bytes)
        results.append(msg)
    return results
