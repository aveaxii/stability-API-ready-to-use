import * as Generation from "./generation/generation_pb";
import { GenerationServiceClient } from "./generation/generation_pb_service";
import { grpc as GRPCWeb } from "@improbable-eng/grpc-web";
import { NodeHttpTransport } from "@improbable-eng/grpc-web-node-http-transport";

// This is a NodeJS-specific requirement - browsers implementations should omit this line.
GRPCWeb.setDefaultTransport(NodeHttpTransport());

// Authenticate using your API key, don't commit your key to a public repository!
export const metadata = new GRPCWeb.Metadata();
metadata.set("Authorization", "Bearer {your_key_here}");

// Create a generation client to use with all future requests
export const client = new GenerationServiceClient("https://grpc.stability.ai", {});