---
name: gemma-web-scraper
description: Fetches live content from a URL and returns the complete cleaned text directly to the model for real-time analysis.
---

# Gemma Web Scraper

Use this skill whenever a user shares a website link/URL and wants you to read, summarize, or analyze its content.

## Instructions
Call the `run_js` tool with the following parameters:
- script name: index.html
- data: A JSON string with the following field:
  - url: String. The complete website URL to fetch and scrape.