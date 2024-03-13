import * as fs from "fs";
import * as Generation from "./generation/generation_pb";
import {
    buildGenerationRequest,
    executeGenerationRequest,
    onGenerationComplete,
} from "./helpers";
import {client, metadata} from "./client";

const request = buildGenerationRequest("esrgan-v1-x2plus", {
    type: "upscaling",
    upscaler: Generation.Upscaler.UPSCALER_ESRGAN,
    initImage: fs.readFileSync("./init_image.png"),
});

executeGenerationRequest(client, request, metadata)
    .then(onGenerationComplete)
    .catch((error) => {
        console.error("Failed to upscale image:", error);
    });