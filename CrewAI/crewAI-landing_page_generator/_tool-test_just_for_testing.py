
# excerpt of main.py to test template_tools for debugging

import json
import os
import shutil
from textwrap import dedent

from crewai import Agent, Crew, Task
#from langchain.agents.agent_toolkits import FileManagementToolkit
from langchain_community.agent_toolkits.file_management.toolkit import FileManagementToolkit
from tasks import TaskPrompts

from tools.browser_tools import BrowserTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools
from tools.template_tools import TemplateTools

from dotenv import load_dotenv
load_dotenv()

class LandingPageCrew():
  def __init__(self, idea):
    self.agents_config = json.loads(open("config/agents.json", "r").read())
    self.idea = idea
    self.__create_agents()

  def run(self):
    #ed_idea = self.__expand_idea()
    self.__choose_template()
    #self.__update_components(components, expanded_idea)

 

  def __choose_template(self):
    choose_template_task = Task(
        description=TaskPrompts.choose_template().format(
          idea='Create Landingpage for SaaS Software AI Assistant'
        ),
        agent=self.react_developer
    )
    
    crew = Crew(
      agents=[self.react_developer],
      tasks=[choose_template_task],
      verbose=True
    )
    components = crew.kickoff()
    return components
  

  def __create_agents(self):
    developer_config = self.agents_config["senior_react_engineer"]
    
    toolkit = FileManagementToolkit(
      root_dir='workdir',
      selected_tools=["read_file", "list_directory"]
    )

    self.react_developer = Agent(
      **developer_config,
      verbose=True,
      tools=[
          SearchTools.search_internet,
          BrowserTools.scrape_and_summarize_website,
          TemplateTools.learn_landing_page_options,
          TemplateTools.copy_landing_page_template_to_project_folder,
          FileTools.write_file
      ] + toolkit.get_tools()
    )


if __name__ == "__main__":
  print("Test file copy")
  
  idea = "Create Landingpage for SaaS Software AI Assistant" #input("# Describe what is your idea:\n\n")

  if not os.path.exists("./workdir"):
    os.mkdir("./workdir")

  if len(os.listdir("./templates")) == 0:
    print(
      dedent("""
      Test to copy files
      """)
    )
    exit()

  crew = LandingPageCrew(idea)
  crew.run()
  
  print("\n\n")
  print("==========================================")
  print("DONE!")
  
