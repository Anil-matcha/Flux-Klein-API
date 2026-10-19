# FLUX Klein API

Build with FLUX 3 Klein image generation and editing through Muapi's asynchronous image API. This guide documents the two live FLUX 3 Klein routes, supported inputs, per-image pricing, and runnable cURL, Python, and JavaScript examples. It also gives a practical way to compare those routes with the FLUX.2 Klein options in the broader catalog.

Muapi provides one API key and a shared submit-and-poll workflow across image models. Start at [Muapi](https://muapi.ai), read the [FLUX Klein API landing page](https://muapi.ai/flux-klein), try a route in the [image playground](https://muapi.ai/playground/group/text-to-image), or follow the [API quick start](https://muapi.ai/docs/quick-start).

## Related Projects

- [Muapi](https://muapi.ai) — One API for image, video, and audio generation.
- [FLUX Klein API on Muapi](https://muapi.ai/flux-klein) — Compare FLUX 3 Klein generation and editing with FLUX.2 Klein variants, prices, and parameters.
- [FLUX 3 Klein text-to-image playground](https://muapi.ai/playground/flux-3-klein-text-to-image) — Try prompt-based image generation.
- [FLUX 3 Klein image-edit playground](https://muapi.ai/playground/flux-3-klein-edit-image) — Try reference-image editing.
- [FLUX.2 API](https://muapi.ai/flux-2) — Browse FLUX.2 Dev, Flex, Pro, Klein, Turbo, and LoRA routes.
- [FLUX 3 API](https://muapi.ai/flux-3) — Browse the wider FLUX 3 family.
- [FLUX 3 API examples](https://github.com/Anil-matcha/Flux-3-Dev-API) — Examples for other FLUX 3 workflows.
- [Awesome AI image models](https://github.com/Anil-matcha/awesome-ai-image-models) — A broader image-model directory.

## What this API includes

| Workflow | Muapi endpoint | Required inputs | Output options |
| --- | --- | --- | --- |
| Text to image | `flux-3-klein-text-to-image` | `prompt` | 1K, 2K, or 4K; one to four images |
| Image editing | `flux-3-klein-edit-image` | `prompt`, `images_list` | 1K, 2K, or 4K; one to four outputs |

The edit route accepts one to ten public image URLs in `images_list`. Set `aspect_ratio` to `auto` to preserve automatic framing or choose a supported ratio. Both routes accept PNG, JPEG, or WebP output, an optional seed, and prompt enhancement.

## Pricing

Muapi charges per output image. The resolution sets the rate, and `num_images` multiplies the total.

| Resolution | Price per output image |
| --- | ---: |
| 1K | $0.009 |
| 2K | $0.014 |
| 4K | $0.036 |

For example, a request for two 2K outputs costs $0.028. The available API resolution choices are 1K, 2K, and 4K.

## Quick start

Create an API key in the [Muapi dashboard](https://muapi.ai/access-keys). Send it with the `x-api-key` header. Each submit call returns a `request_id`; poll the shared result endpoint until the task completes.

### Text-to-image request

```bash
curl -X POST https://api.muapi.ai/api/v1/flux-3-klein-text-to-image \
  -H "x-api-key: $MUAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A sculptural glass perfume bottle on a warm limestone plinth, soft editorial light",
    "resolution": "2K",
    "aspect_ratio": "4:3",
    "num_images": 2,
    "output_format": "png"
  }'
```

### Image-edit request

```bash
curl -X POST https://api.muapi.ai/api/v1/flux-3-klein-edit-image \
  -H "x-api-key: $MUAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Replace the plain background with a warm limestone studio, preserving the product shape",
    "images_list": ["https://example.com/product.jpg"],
    "resolution": "2K",
    "aspect_ratio": "auto",
    "num_images": 1
  }'
```

### Poll for the result

```bash
curl https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result \
  -H "x-api-key: $MUAPI_API_KEY"
```

When `status` is `completed`, read the generated image URLs from `outputs`. A task may take time to finish, so poll with a short delay and stop on `completed` or `failed`.

## Inputs

| Field | Text to image | Edit | Details |
| --- | :---: | :---: | --- |
| `prompt` | Yes | Yes | Required instruction, up to 5,000 characters |
| `images_list` | — | Yes | One to ten public image URLs |
| `aspect_ratio` | Optional | Optional | `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `16:9`, `9:16`, `21:9`, `9:21`; edit also accepts `auto` |
| `resolution` | Optional | Optional | `1K`, `2K`, or `4K` |
| `output_format` | Optional | Optional | `png`, `jpeg`, or `webp` |
| `num_images` | Optional | Optional | 1–4 outputs; charged per output |
| `seed` | Optional | Optional | Integer from 0 to 2147483647 for reproducible variation |
| `enhance_prompt` | Optional | Optional | Boolean; lets the model refine the prompt |

Only `prompt` is required for text-to-image. The edit endpoint additionally requires at least one `images_list` URL.

## Choosing a FLUX Klein route

| Route family | Good fit when | What to compare |
| --- | --- | --- |
| FLUX 3 Klein | You want the new FLUX 3 Klein prompt-to-image or reference-edit endpoints, with 1K/2K/4K selection | Generation versus editing, resolution, and per-output cost |
| FLUX.2 Klein 4B / 9B | You want to compare the existing FLUX.2 Klein generation and edit variants | 4B versus 9B variants and their available Turbo/LoRA routes |

The model names identify different FLUX generations. Check each route's playground page for its current inputs and availability before switching. The Muapi request lifecycle remains the same: submit, save `request_id`, then poll for `outputs`.

## Python and JavaScript examples

See [`examples/python.py`](examples/python.py) and [`examples/node.js`](examples/node.js). The Python example uses `requests`; install it with `pip install -r requirements.txt`. The JavaScript example uses the built-in `fetch` API in Node.js 18 or newer.

## License

MIT
