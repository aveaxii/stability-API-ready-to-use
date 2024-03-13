import * as fs from "fs";
import * as Generation from "./generation/generation_pb";
import {
    buildGenerationRequest,
    executeGenerationRequest,
    onGenerationComplete,
} from "./helpers";
import {client, metadata} from "./client";

const request = buildGenerationRequest("stable-diffusion-xl-1024-v0-9", {
    type: "image-to-image-masking",
    initImage: fs.readFileSync("./init_image.png"),
    maskImage: fs.readFileSync("./mask_image.png"),
    prompts: [
        {
            text: "big man with cool haircut",
        },
    ],
    seed: 44332211,
    samples: 1,
    cfgScale: 8,
    steps: 50,
    sampler: Generation.DiffusionSampler.SAMPLER_K_DPMPP_2M,
});

executeGenerationRequest(client, request, metadata)
    .then(onGenerationComplete)
    .catch((error) => {
        console.error("Failed to make image-to-image-masking request:", error);
    });