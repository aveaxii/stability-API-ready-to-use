import io
import os
import warnings

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://platform.stability.ai/

# Click on the following link once you have created an account to be taken to your API Key.
# https://platform.stability.ai/account/keys

# Paste your API Key below.

os.environ['STABILITY_KEY'] = 'your_key_here'


# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-xl-1024-v1-0", # Set the engine to use for generation.
    # Check out the following link for a list of available engines: https://platform.stability.ai/docs/features/api-parameters#engine

)


# Set up our initial generation parameters.
answers = stability_api.generate(
    prompt="expansive landscape rolling greens with blue daisies and weeping willow trees under a blue alien sky, masterful, ghibli",
    seed=123126, # If a seed is provided, the resulting generated image will be deterministic.
                 # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
                 # Note: This isn't quite the case for CLIP Guided generations.
    steps=50, # Step Count defaults to 30 if not specified here.
    cfg_scale=7.0, # Influences how strongly your generation is guided to match your prompt. Setting this value higher increases the strength in which it tries to match your prompt. Defaults to 7.0 if not specified.
    width=512, # Generation width, defaults to 512 if not included.
    height=512, # Generation height, defaults to 512 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2S_ANCESTRAL, # Choose which sampler we want to denoise our generation with. Defaults to k_dpmpp_2s_ancestral. CLIP Guidance only supports ancestral samplers.
                                                     # (Available Samplers: ddim, k_euler_ancestral, k_dpm_2_ancestral, k_dpmpp_2s_ancestral)
    # guidance_preset=generation.GUIDANCE_PRESET_FAST_BLUE # Enables CLIP Guidance.
                                                         # (Available Presets: _NONE, _FAST_BLUE, _FAST_GREEN)
)


# Set up our initial generation parameters.
answers = stability_api.generate(
    prompt="expansive landscape rolling greens with blue daisies and weeping willow trees under a blue alien sky, masterful, ghibli",
    seed=123126, # Note: Seeded CLIP Guided generations will attempt to stay near its original generation.
                 # However unlike non-clip guided inference, there's no way to guarantee a deterministic result, even with the same seed.
    steps=50, # Step Count defaults to 30 if not specified here.
    cfg_scale=7.0, # Influences how strongly your generation is guided to match your prompt. Setting this value higher increases the strength in which it tries to match your prompt. Defaults to 7.0 if not specified.
    width=512, # Generation width, defaults to 512 if not included.
    height=512, # Generation height, defaults to 512 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2S_ANCESTRAL, # Choose which sampler we want to denoise our generation with. Defaults to k_dpmpp_2s_ancestral. CLIP Guidance only supports ancestral samplers.
                                                     # (Available Samplers: ddim, k_euler_ancestral, k_dpm_2_ancestral, k_dpmpp_2s_ancestral)
    guidance_preset=generation.GUIDANCE_PRESET_FAST_BLUE # Enables CLIP Guidance.
                                                         # (Available Presets: _NONE, _FAST_BLUE, _FAST_GREEN)
)

# Set up our warning to print to the console if the adult content classifier is tripped. If adult content classifier is not tripped, save generated image.
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save(str(artifact.seed)+ ".png") # Save our generated images with their seed number as the filename.