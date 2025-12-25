# Deployment

This directory contains deployment configurations and artifacts.

## Structure

- `docker/` - Docker configurations and Dockerfiles
- `kubernetes/` - Kubernetes manifests and Helm charts

## Usage

Build Docker image:
```bash
docker build -f deploy/docker/Dockerfile -t pytorch-transformer:latest .
```

Deploy to Kubernetes:
```bash
kubectl apply -f deploy/kubernetes/
```
