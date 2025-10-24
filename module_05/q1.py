'''
Question 1

- Install uv
- What's the version of uv you installed?
- Use --version to find out
'''

from importlib.metadata import version

try:
    uv_version = version('uv')
    print(f"uv version: {uv_version}")
except Exception as e:
    print(f"Could not get version: {e}")