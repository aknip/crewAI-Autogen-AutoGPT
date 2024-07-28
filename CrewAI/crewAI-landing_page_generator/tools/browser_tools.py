import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from bs4 import BeautifulSoup

class BrowserTools():

  # Custom tool - read webpage
  @tool("Scrape website content")
  def scrape_and_summarize_website(website: str) -> str:
    """Read the content of a webpage"""
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text() # [:5000]
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing researches and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)