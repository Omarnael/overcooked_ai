![MDP python tests](https://github.com/HumanCompatibleAI/hacktrick_ai/workflows/.github/workflows/pythontests.yml/badge.svg) ![hacktrick-ai codecov](https://codecov.io/gh/HumanCompatibleAI/hacktrick_ai/branch/master/graph/badge.svg) [![PyPI version](https://badge.fury.io/py/hacktrick-ai.svg)](https://badge.fury.io/py/hacktrick-ai) [!["Open Issues"](https://img.shields.io/github/issues-raw/HumanCompatibleAI/hacktrick_ai.svg)](https://github.com/HumanCompatibleAI/minerl/hacktrick_ai) [![GitHub issues by-label](https://img.shields.io/github/issues-raw/HumanCompatibleAI/hacktrick_ai/bug.svg?color=red)](https://github.com/HumanCompatibleAI/hacktrick_ai/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Abug) [![Downloads](https://pepy.tech/badge/hacktrick-ai)](https://pepy.tech/project/hacktrick-ai)

# Hacktrick-AI 🧑‍🍳🤖

<p align="center">
  <!-- <img src="hacktrick_ai_js/images/screenshot.png" width="350"> -->
  <img src="./images/layouts.gif" width="100%"> 
  <i>5 of the available layouts. New layouts are easy to hardcode or generate programmatically.</i>
</p>

## Introduction 🥘

Hacktrick-AI is a benchmark environment for fully cooperative human-AI task performance, based on the wildly popular video game [Hacktrick](http://www.ghosttowngames.com/hacktrick/).

The goal of the game is to deliver solarlabs as fast as possible. Each solarlab requires placing up to 3 ingredients in a construction_site, waiting for the solarlab to cook, and then having an agent pick up the solarlab and delivering it. The agents should split up tasks on the fly and coordinate effectively in order to achieve high reward.

You can **try out the game [here](https://humancompatibleai.github.io/hacktrick-demo/)** (playing with some previously trained DRL agents). To play with your own trained agents using this interface, you can use [this repo](https://github.com/HumanCompatibleAI/hacktrick-demo). To run human-AI experiments, check out [this repo](https://github.com/HumanCompatibleAI/hacktrick-hAI-exp). You can find some human-human and human-AI gameplay data already collected [here](https://github.com/HumanCompatibleAI/human_aware_rl/tree/master/human_aware_rl/static/human_data).

Check out [this repo](https://github.com/HumanCompatibleAI/human_aware_rl) for the DRL implementations compatible with the environment and reproducible results to our paper: *[On the Utility of Learning about Humans for Human-AI Coordination](https://arxiv.org/abs/1910.05789)* (also see our [blog post](https://bair.berkeley.edu/blog/2019/10/21/coordination/)).

For simple usage of the environment, it's worthwhile considering using [this environment wrapper](https://github.com/Stanford-ILIAD/PantheonRL).

## Research Papers using Hacktrick-AI 📑


- Carroll, Micah, Rohin Shah, Mark K. Ho, Thomas L. Griffiths, Sanjit A. Seshia, Pieter Abbeel, and Anca Dragan. ["On the utility of learning about humans for human-ai coordination."](https://arxiv.org/abs/1910.05789) NeurIPS 2019.
- Charakorn, Rujikorn, Poramate Manoonpong, and Nat Dilokthanakul. [“Investigating Partner Diversification Methods in Cooperative Multi-Agent Deep Reinforcement Learning.”](https://www.rujikorn.com/files/papers/diversity_ICONIP2020.pdf) Neural Information Processing. ICONIP 2020.
- Knott, Paul, Micah Carroll, Sam Devlin, Kamil Ciosek, Katja Hofmann, Anca D. Dragan, and Rohin Shah. ["Evaluating the Robustness of Collaborative Agents."](https://arxiv.org/abs/2101.05507) AAMAS 2021.
- Nalepka, Patrick, Jordan P. Gregory-Dunsmore, James Simpson, Gaurav Patil, and Michael J. Richardson. ["Interaction Flexibility in Artificial Agents Teaming with Humans."](https://www.researchgate.net/publication/351533529_Interaction_Flexibility_in_Artificial_Agents_Teaming_with_Humans) Cogsci 2021.
- Fontaine, Matthew C., Ya-Chuan Hsu, Yulun Zhang, Bryon Tjanaka, and Stefanos Nikolaidis. [“On the Importance of Environments in Human-Robot Coordination”](http://arxiv.org/abs/2106.10853) RSS 2021.
- Zhao, Rui, Jinming Song, Hu Haifeng, Yang Gao, Yi Wu, Zhongqian Sun, Yang Wei. ["Maximum Entropy Population Based Training for Zero-Shot Human-AI Coordination"](https://arxiv.org/abs/2112.11701). NeurIPS Cooperative AI Workshop, 2021.
- Sarkar, Bidipta, Aditi Talati, Andy Shih, and Dorsa Sadigh. [“PantheonRL: A MARL Library for Dynamic Training Interactions”](https://iliad.stanford.edu/pdfs/publications/sarkar2022pantheonrl.pdf). AAAI 2022.


## Installation ☑️

### Installing from PyPI 🗜

You can install the pre-compiled wheel file using pip.
```
pip install hacktrick-ai
```
Note that PyPI releases are stable but infrequent. For the most up-to-date development features, build from source


### Building from source 🔧

It is useful to setup a conda environment with Python 3.7 (virtualenv works too):

```
conda create -n hacktrick_ai python=3.7
conda activate hacktrick_ai
```

Clone the repo 
```
git clone https://github.com/HumanCompatibleAI/hacktrick_ai.git
```
Finally, use python setup-tools to locally install

```
pip install -e hacktrick_ai/
```


### Verifying Installation 📈

When building from source, you can verify the installation by running the Hacktrick unit test suite. The following commands should all be run from the `hacktrick_ai` project root directory:

```
python testing/hacktrick_test.py
```

If you're thinking of using the planning code extensively, you should run the full testing suite that verifies all of the Hacktrick accessory tools (this can take 5-10 mins): 
```
python -m unittest discover -s testing/ -p "*_test.py"
```


## Code Structure Overview 🗺

`hacktrick_ai_py` contains:

`mdp/`:
- `hacktrick_mdp.py`: main Hacktrick game logic
- `hacktrick_env.py`: environment classes built on top of the Hacktrick mdp
- `layout_generator.py`: functions to generate random layouts programmatically

`agents/`:
- `agent.py`: location of agent classes
- `benchmarking.py`: sample trajectories of agents (both trained and planners) and load various models

`planning/`:
- `planners.py`: near-optimal agent planning logic
- `search.py`: A* search and shortest path logic


## Python Visualizations 🌠

One can adapt a version of [this file](https://github.com/HumanCompatibleAI/human_aware_rl/blob/master/human_aware_rl/hacktrick_interactive.py) in order to be able to play games in terminal graphics with custom-defined agents.


## Further Issues and questions ❓

If you have issues or questions, don't hesitate to contact either [Micah Carroll](https://micahcarroll.github.io) at mdc@berkeley.edu or [Nathan Miller](https://github.com/nathan-miller23) at nathan_miller23@berkeley.edu

