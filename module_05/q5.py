import subprocess

image_name = "agrigorev/zoomcamp-model:2025"

result = subprocess.run(
    ['docker', 'images', image_name, '--format', '{{.Size}}'],
    capture_output=True,
    text=True
)

size = result.stdout.strip()
print(f"Size: {size}")