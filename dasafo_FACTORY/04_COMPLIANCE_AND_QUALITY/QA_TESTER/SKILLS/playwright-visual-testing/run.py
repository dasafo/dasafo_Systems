#!/usr/bin/env python3
"""
Playwright Visual & Interaction Testing (v3.1)
Part of Dasafo Factory QA Department.

Automates UI validation by generating and executing Playwright test suites.
"""

import os
import sys
import argparse
import subprocess

def check_playwright():
    """Checks if playwright is installed in the current environment."""
    try:
        import playwright
        return True, "Playwright is installed."
    except ImportError:
        return False, "Playwright is not installed. Run 'pip install playwright && playwright install'"

def generate_test_template(url, output_path):
    """Generates a basic Playwright test script."""
    template = f"""import asyncio
from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        print(f"Opening {{'{url}'}}...")
        await page.goto('{url}')
        
        # Take a screenshot for visual comparison
        screenshot_path = "latest_screenshot.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {{screenshot_path}}")
        
        # Simple interaction check
        title = await page.title()
        print(f"Page Title: {{title}}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test())
"""
    with open(output_path, 'w') as f:
        f.write(template)
    return True, f"Test template generated at {output_path}"

def main():
    parser = argparse.ArgumentParser(description="Dasafo QA Playwright Tool")
    parser.add_argument("--action", choices=["check", "generate", "run"], required=True)
    parser.add_argument("--url", default="http://localhost:3000", help="Target URL for testing")
    parser.add_argument("--output", default="playwright_test.py", help="Output path for the generated test")

    args = parser.parse_args()

    if args.action == "check":
        success, message = check_playwright()
        if success:
            print(f"✅ {message}")
        else:
            print(f"⚠️ {message}")
            sys.exit(1)

    elif args.action == "generate":
        success, message = generate_test_template(args.url, args.output)
        print(f"✅ {message}")

    elif args.action == "run":
        if not os.path.exists(args.output):
            print(f"ERROR: Test file {args.output} not found. Generate it first.")
            sys.exit(1)
        
        print(f"🚀 Running Playwright test: {args.output}")
        result = subprocess.run([sys.executable, args.output])
        if result.returncode == 0:
            print("✅ Test PASSED.")
        else:
            print("❌ Test FAILED.")
            sys.exit(result.returncode)

if __name__ == "__main__":
    main()
