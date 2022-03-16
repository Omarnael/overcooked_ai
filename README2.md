## Installation

- `cd overcooked_ai/`
- `pip install -e .`

## Code Structure Overview

`overcooked_ai_py` contains:

`mdp/`:
- `overcooked_mdp.py`: main Overcooked game logic
- `overcooked_env.py`: environment classes built on top of the Overcooked mdp
- `layout_generator.py`: functions to generate random layouts programmatically

`agents/`:
- `agent.py`: location of agent classes
- `benchmarking.py`: sample trajectories of agents (both trained and planners) and load various models

`planning/`:
- `planners.py`: near-optimal agent planning logic
- `search.py`: A* search and shortest path logic

## Run and test your agents locally
Follow the steps in this notebook `\hacktrick_client\hackathon_tutorial.ipynb`

## Submit your solution
- Implement your agents in `hacktrick_agent.py`.
- In `hacktrick_agent.py` you will find two base classes `MainAgent()` and `OptionalAgent()`. Implement your logic in these classes.
- Run this command `python3 client.py --team_name=TEAM_NAME --password=PASSWORD --mode=MODE --layout=LAYOUT_NAME`.


