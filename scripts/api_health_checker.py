import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List

TARGET_URLS = [
    "https://api.github.com",
    "https://httpbin.org/get",
    "https://cloudflare.com",
    "https://python.org"
]

def check_endpoint(url: str, timeout: int = 5) -> Dict:
    start_time = time.time()
    result = {"url": url, "status": "UNKNOWN", "latency_ms": 0.0, "code": 0}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HealthChecker/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            result["code"] = response.getcode()
            result["status"] = "HEALTHY" if response.getcode() == 200 else "DEGRADED"
    except urllib.error.HTTPError as e:
        result["code"] = e.code
        result["status"] = f"HTTP_{e.code}"
    except Exception as e:
        result["status"] = f"ERROR: {type(e).__name__}"
    finally:
        result["latency_ms"] = round((time.time() - start_time) * 1000, 2)
    return result

def run_health_checks(urls: List[str], max_workers: int = 4):
    print(f"[*] Probing {len(urls)} target endpoints concurrently...")
    print("-" * 65)
    print(f"{'Endpoint':<35} | {'Status':<12} | {'Latency (ms)':<10}")
    print("-" * 65)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_endpoint, url): url for url in urls}
        for future in as_completed(futures):
            res = future.result()
            print(f"{res['url']:<35} | {res['status']:<12} | {res['latency_ms']:<10}")
    print("-" * 65)

if __name__ == "__main__":
    run_health_checks(TARGET_URLS)
