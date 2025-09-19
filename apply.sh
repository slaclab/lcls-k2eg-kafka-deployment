#!/usr/bin/env bash

set -euo pipefail

# Kubernetes context to use
CTX="lcls-k2eg"

if ! command -v kubectl >/dev/null 2>&1; then
  echo "Error: kubectl is not installed or not in PATH." >&2
  exit 127
fi

# Verify the context exists
if ! kubectl config get-contexts "$CTX" >/dev/null 2>&1; then
  echo "Error: Kubernetes context '$CTX' not found in your kubeconfig." >&2
  echo "Available contexts:" >&2
  kubectl config get-contexts >&2 || true
  exit 1
fi

echo "Switching Kubernetes context to '$CTX'..."
kubectl config use-context "$CTX" >/dev/null

# Ensure we run from the repo directory containing kustomization
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Running: kubectl apply -k ."
kubectl apply -k . "$@"
