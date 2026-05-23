#!/bin/bash

echo "[+] Starting Automated Mobile Security Scan"

APK=$1

if [ -z "$APK" ]; then
    echo "Usage: ./automated_scan.sh app.apk"
    exit 1
fi

echo "[+] Decompiling APK"
apktool d $APK -o output/

echo "[+] Running JADX"
jadx -d jadx-output $APK

echo "[+] Scan Completed"