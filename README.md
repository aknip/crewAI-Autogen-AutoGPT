# AutoGPT

## Run in Gitpod
https://gitpod.io/#https://github.com/aknip/crewAI-Autogen-AutoGPT

## Install
uv venv
source .venv/bin/activate
uv pip install jupyterlab==4.2.1 pyautogen==0.2.27 crewai==0.30.11 crewai-tools==0.2.6 duckduckgo-search==6.1.4 agentops==0.2.0

# Start:
jupyter lab


Temp:
tasks:
  - name: Open the readme, contract and test
    command: gp open contracts/Token.sol && gp open test/Token.js && gp open README.md
  
  - name: Hardhat server
    init: npm install
    command: npx hardhat node

  - name: Frontend server
    command: npx hardhat --network localhost run scripts/deploy.js && cd frontend && npm install && npm run start
    openMode: split-right