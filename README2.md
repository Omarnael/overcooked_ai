## Installation

- `cd hacktrick_ai/`
- `pip install -e .`

## Code Structure Overview

`hacktrick_ai_py` contains:

`mdp/`:
- `hacktrick_mdp.py`: main Hacktrick game logic
- `hacktrick_env.py`: environment classes built on top of the Hacktrick mdp
- `layout_generator.py`: functions to generate random layouts programmatically

`agents/`:
- `agent.py`: location of agent classes
- `benchmarking.py`: sample trajectories of agents (both trained and planners) and load various models

`planning/`:
- This directory contains some logic that might help you in implementing a rule-based agent.
- You are free to disregard this directory and implement your own functions.
- If you find any functions that make your implementation easier, or even as a guide/starter, feel free to use them. 

## Agents
In `hacktrick_agent.py` you will find two base classes `MainAgent()` and `OptionalAgent()`. Implement according to the following cases. 
- In single mode, implement only one of them but make sure you are testing and submitting the correct agent.
- In collaborative mode, implement both classes if you want to implement different agent logic.
- In collaborative mode, implement one class only if you want to apply the same logic on both agents.

## Run and test your agents locally
Follow the steps in this notebook `\hacktrick_client\hackathon_tutorial.ipynb`

## Submit your solution
- In `hacktrick_agent.py` you will find two base classes `MainAgent()` and `OptionalAgent()`. Implement your logic in these classes.
- Run this command `python3 client.py --team_name=TEAM_NAME --password=PASSWORD --mode=MODE --layout=LAYOUT_NAME`.


