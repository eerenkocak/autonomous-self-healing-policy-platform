#!/usr/bin/env bash
set -euo pipefail

TARGET_CONTAINER="critical-payment-api"

echo "============================================================"
echo "[CHAOS MONKEY] Initiating controlled fault injection..."
echo "[CHAOS MONKEY] Terminating target service: ${TARGET_CONTAINER}"
echo "============================================================"

docker stop "${TARGET_CONTAINER}" >/dev/null

echo "[CHAOS MONKEY] Fault injected! Service '${TARGET_CONTAINER}' is now DOWN."
echo "[CHAOS MONKEY] Observe the Autonomous Self-Healing Engine recover it within ~5-8 seconds..."
