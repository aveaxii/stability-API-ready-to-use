
import * as Generation from "./generation/generation_pb";
import {
    buildGenerationRequest,
    executeGenerationRequest,
    onGenerationComplete,
} from "./helpers";
import {client, metadata} from "./client";

const request = buildGenerationRequest("stable-diffusion-xl-1024-v0-9", {
    type: "text-to-image",
    prompts: [
        {
            text: "sunrise in seoul, cyberpunk",
        },
    ],
    width: 1024,
    height: 1024,
    samples: 1,
    cfgScale: 8,
    steps: 30,
    seed: 4253978046,
    sampler: Generation.DiffusionSampler.SAMPLER_K_DPMPP_2M,
});

executeGenerationRequest(client, request, metadata)
    .then(onGenerationComplete)
    .catch((error) => {
        console.error("Failed to make text-to-image request:", error);
    });