# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import gadgettracermanager_pb2 as gadgettracermanager__pb2


class GadgetTracerManagerStub(object):
  """Methods called by bcc scripts
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddTracer = channel.unary_unary(
        '/gadgettracermanager.GadgetTracerManager/AddTracer',
        request_serializer=gadgettracermanager__pb2.AddTracerRequest.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.TracerID.FromString,
        )
    self.RemoveTracer = channel.unary_unary(
        '/gadgettracermanager.GadgetTracerManager/RemoveTracer',
        request_serializer=gadgettracermanager__pb2.TracerID.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.RemoveTracerResponse.FromString,
        )
    self.TracerSubscribeContainers = channel.unary_stream(
        '/gadgettracermanager.GadgetTracerManager/TracerSubscribeContainers',
        request_serializer=gadgettracermanager__pb2.TracerSubscribeContainersRequest.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.TracerSubscribeContainersResponse.FromString,
        )
    self.AddContainer = channel.unary_unary(
        '/gadgettracermanager.GadgetTracerManager/AddContainer',
        request_serializer=gadgettracermanager__pb2.ContainerDefinition.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.AddContainerResponse.FromString,
        )
    self.RemoveContainer = channel.unary_unary(
        '/gadgettracermanager.GadgetTracerManager/RemoveContainer',
        request_serializer=gadgettracermanager__pb2.ContainerDefinition.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.RemoveContainerResponse.FromString,
        )
    self.DumpState = channel.unary_unary(
        '/gadgettracermanager.GadgetTracerManager/DumpState',
        request_serializer=gadgettracermanager__pb2.DumpStateRequest.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.Dump.FromString,
        )


class GadgetTracerManagerServicer(object):
  """Methods called by bcc scripts
  """

  def AddTracer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveTracer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TracerSubscribeContainers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddContainer(self, request, context):
    """Methods called by OCI Hooks

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveContainer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DumpState(self, request, context):
    """Methods called for debugging

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GadgetTracerManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddTracer': grpc.unary_unary_rpc_method_handler(
          servicer.AddTracer,
          request_deserializer=gadgettracermanager__pb2.AddTracerRequest.FromString,
          response_serializer=gadgettracermanager__pb2.TracerID.SerializeToString,
      ),
      'RemoveTracer': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveTracer,
          request_deserializer=gadgettracermanager__pb2.TracerID.FromString,
          response_serializer=gadgettracermanager__pb2.RemoveTracerResponse.SerializeToString,
      ),
      'TracerSubscribeContainers': grpc.unary_stream_rpc_method_handler(
          servicer.TracerSubscribeContainers,
          request_deserializer=gadgettracermanager__pb2.TracerSubscribeContainersRequest.FromString,
          response_serializer=gadgettracermanager__pb2.TracerSubscribeContainersResponse.SerializeToString,
      ),
      'AddContainer': grpc.unary_unary_rpc_method_handler(
          servicer.AddContainer,
          request_deserializer=gadgettracermanager__pb2.ContainerDefinition.FromString,
          response_serializer=gadgettracermanager__pb2.AddContainerResponse.SerializeToString,
      ),
      'RemoveContainer': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveContainer,
          request_deserializer=gadgettracermanager__pb2.ContainerDefinition.FromString,
          response_serializer=gadgettracermanager__pb2.RemoveContainerResponse.SerializeToString,
      ),
      'DumpState': grpc.unary_unary_rpc_method_handler(
          servicer.DumpState,
          request_deserializer=gadgettracermanager__pb2.DumpStateRequest.FromString,
          response_serializer=gadgettracermanager__pb2.Dump.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gadgettracermanager.GadgetTracerManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TracerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateContainers = channel.unary_unary(
        '/gadgettracermanager.Tracer/UpdateContainers',
        request_serializer=gadgettracermanager__pb2.UpdateContainersRequest.SerializeToString,
        response_deserializer=gadgettracermanager__pb2.UpdateContainersResponse.FromString,
        )


class TracerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateContainers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TracerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateContainers': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateContainers,
          request_deserializer=gadgettracermanager__pb2.UpdateContainersRequest.FromString,
          response_serializer=gadgettracermanager__pb2.UpdateContainersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gadgettracermanager.Tracer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
