// Submit one FLUX 3 Klein image-generation request with Node.js 18+.
const apiKey = process.env.MUAPI_API_KEY;
if (!apiKey) throw new Error("Set MUAPI_API_KEY first.");

const response = await fetch(
  "https://api.muapi.ai/api/v1/flux-3-klein-text-to-image",
  {
    method: "POST",
    headers: {
      "x-api-key": apiKey,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt: "A sculptural glass perfume bottle on a warm limestone plinth, soft editorial light",
      resolution: "2K",
      aspect_ratio: "4:3",
      num_images: 2,
      output_format: "png",
    }),
  },
);

if (!response.ok) {
  throw new Error(`Muapi request failed (${response.status}): ${await response.text()}`);
}

const task = await response.json();
console.log("Poll this task for the image URLs:", task.request_id);
