# ⚡ IT Help Portal

> Enterprise IT Help Portal — migrated from XAMPP to full DevOps stack

## 🚀 Live Demo
https://bias-alberta-amd-collecting.trycloudflare.com

## 🛠 Tech Stack
- **Docker + Nginx** — Containerized web server (replaced XAMPP)
- **Python FastAPI** — AI backend
- **Ollama llama3.2:1b** — Local AI model (free, no API cost)
- **Cloudflare Tunnel** — Free HTTPS external access
- **Jenkins** — CI/CD pipeline (coming soon)
- **Prometheus + Grafana** — Monitoring (coming soon)
- **Terraform** — Infrastructure as Code (coming soon)

## ✨ Features
- 🔐 Two-level password protection (User + Admin)
- 🤖 AI Helpdesk Chatbot powered by Ollama
- 📦 Software package downloads (CrowdStrike, Zscaler)
- 📜 Automation scripts library
- ⌨ Commands reference with search and copy
- 🌙 Dark / Light mode
- 📱 Mobile responsive

## 📁 Project Structure
\`\`\`
it-help-portal/
├── Dockerfile          # Nginx portal container
├── Dockerfile.ai       # FastAPI AI container
├── docker-compose.yml  # Full stack orchestration
├── nginx.conf          # Reverse proxy + auth config
├── html/               # All web pages
│   ├── login.html      # Custom login page
│   ├── index.html      # Main portal
│   ├── packages.html   # Software downloads
│   ├── scripts.html    # Automation scripts
│   └── commands.html   # Commands reference
├── ai/                 # AI backend
│   ├── main.py         # FastAPI app
│   ├── chatbot.py      # Ollama chatbot
│   └── requirements.txt
├── monitoring/         # Prometheus + Grafana
├── terraform/          # Infrastructure as Code
└── jenkins/            # CI/CD pipeline
\`\`\`

## 🏃 Quick Start
\`\`\`bash
git clone https://github.com/SIVASAKTHI-CE/it-help-portal.git
cd it-help-portal
docker compose up -d --build
\`\`\`

## 👤 Author
SIVASAKTHI — DevOps Learning Project 2026
