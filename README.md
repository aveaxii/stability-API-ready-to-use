# StabilityAI TypeScript and Python gRPC Implementation

### https://platform.stability.ai/docs/features - utilized documentation (gRPC).

**TypeScript API Implementation:**

- Text to Image 
- Image to Image 
- Inpainting + Masking 
- Image Upscaling

The `package.json` includes necessary dependencies.

**To utilize:**

1. Run `npm install` in the terminal.
2. For all `.ts` files, use `tsc filename.ts`.
3. After `.ts -> .js` conversion for necessary files, use `node filename.js`.

--------

**Python API Implementation:**

- Multiprompting 
- Variants
- CLIP GUIDANCE

The implementation is in `*.py` files.
The `stable-diffusion-xl-1024-v1-0` engine is utilized in the GRID GUIDANCE implementation file.

**To utilize this, follow these steps:**

1. Install Python 3.11.x (3.11.8 is acceptable, 3.11+ is not supported*).
2. Install `stability-sdk` via pip.
3. In the terminal, use `python filename.py` for the necessary files.

*Using Python versions above 3.11 might cause gRPCio errors.*

**File Structure:**

- `...-...-model.ts` or `...-...-model.js` are API implementations.
