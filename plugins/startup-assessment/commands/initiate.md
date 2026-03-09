---
description: Scaffold the assessment workspace and save uploaded business case documents
allowed-tools: Bash(python3:*)
model: sonnet
---

Run this Python script immediately and show the output to the user:

```python
import os, shutil, glob

# Discover workspace dynamically — works across all sessions
mounts = glob.glob('/sessions/*/mnt/*/')
if not mounts:
    print("ERROR: No workspace found. Please select a folder in Cowork mode.")
    exit(1)

BASE = os.path.join(mounts[0].rstrip('/'), 'assessment')
UPLOADS = glob.glob('/sessions/*/mnt/uploads')[0] if glob.glob('/sessions/*/mnt/uploads') else ''

print(f"Workspace: {BASE}")

# Create full folder structure
for folder in [
    "business-case-docs",
    "pre-assessment/reports",
    "pre-assessment/data",
    "assessment/reports",
    "assessment/data",
    "sensitivity/reports",
    "sensitivity/data",
    "recommendations/reports",
    "recommendations/data"
]:
    os.makedirs(os.path.join(BASE, folder), exist_ok=True)

print("✅ Folder structure created.")

# Copy uploaded files to business-case-docs
DOCS = os.path.join(BASE, "business-case-docs")
copied, skipped = [], []

if UPLOADS and os.path.isdir(UPLOADS):
    for f in os.listdir(UPLOADS):
        src = os.path.join(UPLOADS, f)
        dst = os.path.join(DOCS, f)
        if not os.path.isfile(src):
            continue
        if os.path.exists(dst):
            skipped.append(f)
        else:
            shutil.copy2(src, dst)
            copied.append(f)
else:
    print("WARNING: uploads folder not found — no files copied.")

print(f"Copied: {copied}")
print(f"Already present (skipped): {skipped}")
print("✅ Assessment workspace ready.")
print("Next step: run /pre-assess")
```
