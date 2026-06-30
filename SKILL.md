---
name: gemma-web-scraper
description: Fetches live content from a URL and returns the complete cleaned text directly to the model for real-time analysis.
---

# Gemma Web Scraper

Use this skill whenever a user shares a website link/URL and wants you to read, summarize, analyze, or answer questions about its content.

## Execution
Run `main.py` passing the URL as the first argument. The script will scrape the page and output the clean text directly to your context.

## User Interactions
* Use the complete text returned by the script to thoroughly answer the user's questions.
* Since the text is processed directly in memory, do not mention any saved local files.