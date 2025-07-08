# rasp-web
Mini web platform for raspberry pi

# 🧱 Project Architecture: my-web-platform

## Overview
- Frontend: React + Tailwind CSS
- Backend: FastAPI (Python)
- Ruby execution via REST API
- Deployment: Docker, Nginx, Raspberry Pi

## Folder Structure


## Application Flow
1. User opens React UI
2. Sends requests to backend endpoints (e.g. `/api/ruby/exec`)
3. Backend runs Ruby securely and returns output
4. React UI displays output

## Technologies Used
- React, Tailwind, WebSocket
- FastAPI, uvicorn, python-jose, passlib[bcrypt], pydantic
- Ruby (IRB/script), PTY
- Docker, Nginx, SSL

## Deployment (on Raspberry Pi)
```bash
bash deploy/setup.sh

