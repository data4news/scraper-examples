# Web Scraping Examples

> Built with [Claude Code](https://claude.com/claude-code) 🤖

A collection of Python web scraping examples demonstrating different approaches to data extraction.

## Overview

This repository contains three different web scraping techniques:

1. **Browser Automation** - Using Playwright to interact with JavaScript-heavy sites
2. **Standard HTML Scraping** - Using requests + BeautifulSoup for static pages
3. **API Extraction** - Directly accessing undocumented JSON endpoints

## Files

- **[scrape_browser.py](scrape_browser.py)** - Automated browser scraping with Playwright
  - Example: Searching for "potato" on Amazon
  - Uses headless Chrome to handle dynamic content
  - Great for sites that require JavaScript rendering

- **[scrape_standard.py](scrape_standard.py)** - Traditional HTML scraping
  - Example: Extracting social media links from a personal website
  - Uses requests + BeautifulSoup with CSS selectors
  - Best for static HTML pages

- **[scrape_undocumented_api.py](scrape_undocumented_api.py)** - Direct API access
  - Example: Querying TRAC immigration reports database
  - Makes GET requests to JSON endpoints
  - Most efficient when APIs are available

## Installation

```bash
pip install -r requirements.txt
```

For Playwright, you'll also need to install browser binaries:

```bash
playwright install chromium
```

## Usage

Run any of the example scripts:

```bash
python scrape_standard.py
python scrape_undocumented_api.py
python scrape_browser.py
```

## Dependencies

- `playwright` - Browser automation
- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing

---

**Note:** This project was created entirely with [Claude Code](https://claude.com/claude-code), an AI-powered coding assistant.
