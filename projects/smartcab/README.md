# Project 4: Reinforcement Learning
## Train a Smartcab How to Drive

## Table of Contents  
- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Install](#install)
- [Files](#files)
- [Definitions](#definitions)
    - [Environment](#environment)
    - [Inputs and Outputs](#inputs-and-outputs)
    - [Rewards and Goal](#rewards-and-goal)
- [Code](#code)
- [Run](#run)
- [Data](#data)


### <a name='project-overview'></a>Project Overview

In the not-so-distant future, taxicab companies across the United States no longer employ human drivers to operate their fleet of vehicles. Instead, the taxicabs are operated by self-driving agents — known as **smartcabs** — to transport people from one location to another within the cities those companies operate. In major metropolitan areas, such as Chicago, New York City, and San Francisco, an increasing number of people have come to rely on **smartcabs** to get to where they need to go as safely and efficiently as possible. Although **smartcabs** have become the transport of choice, concerns have arose that a self-driving agent might not be as safe or efficient as human drivers, particularly when considering city traffic lights and other vehicles. To alleviate these concerns, your task as an employee for a national taxicab company is to use reinforcement learning techniques to construct a demonstration of a **smartcab** operating in real-time to prove that both safety and efficiency can be achieved.

In this project we will apply reinforcement learning techniques for a self-driving agent in a simplified world to aid it in effectively reaching its destinations in the allotted time. We will first investigate the environment the agent operates in by constructing a very basic driving implementation. Once our agent is successful at operating within the environment, we will then identify each possible state the agent can be in when considering such things as traffic lights and oncoming traffic at each intersection. With states identified, we will then implement a Q-Learning algorithm for the self-driving agent to guide the agent towards its destination within the allotted time. Finally, we will improve upon the Q-Learning algorithm to find the best configuration of learning and exploration factors to ensure the self-driving agent is reaching its destinations with consistently positive results.


### <a name='project-highlights'></a>Project Highlights

This project is designed to give you a hands-on experience with reinforcement learning to train an agent to learn self-driving.

Things you will learn by completing this project:

- How to implement Q-learning.
- How to train a self-driving agent with Q-learning.


### <a name='install'></a>Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pygame](https://www.pygame.org/wiki/GettingStarted)
    - Helpful links for installing PyGame:
    - [Google Group](https://groups.google.com/forum/#!forum/pygame-mirror-on-google-groups)
    - [PyGame subreddit](https://www.reddit.com/r/pygame/)

If you have [Anaconda](https://www.continuum.io/downloads) installed, `Pygame` can then be installed using one of the following commands:

Mac:
`conda install -c https://conda.anaconda.org/quasiben pygame`

Windows & Linux:
`conda install -c https://conda.anaconda.org/tlatorre pygame`


### <a name='files'></a>Files

This project contains two directories:
- `/images/`: This folder contains various images of cars to be used in the graphical user interface. You will not need to modify or create any files in this directory.
- `/smartcab/`: This folder contains the Python scripts that create the environment, graphical user interface, the simulation, and the agents. You will not need to modify or create any files in this directory except for `agent.py`.

In `/smartcab/` are the following four files:
- **Modify**:
    - `agent.py`: This is the main Python file where you will be performing your work on the project.
- **Do not modify**:
    - `environment.py`: This Python file will create the smartcab environment.
    - `planner.py`: This Python file creates a high-level planner for the agent to follow towards a set goal.
    - `simulation.py`: This Python file creates the simulation and graphical user interface.


### <a name='definitions'></a>Definitions

#### <a name='environment'></a>Environment
The **smartcab** operates in an ideal, grid-like city (similar to New York City), with roads going in the North-South and East-West directions. Other vehicles will certainly be present on the road, but there will be no pedestrians to be concerned with. At each intersection is a traffic light that either allows traffic in the North-South direction or the East-West direction. U.S. Right-of-Way rules apply:
- On a green light, a left turn is permitted if there is no oncoming traffic making a right turn or coming straight through the intersection.
- On a red light, a right turn is permitted if no oncoming traffic is approaching from your left through the intersection.<br>
To understand how to correctly yield to oncoming traffic when turning left, you may refer to [this official drivers’ education video](https://www.youtube.com/watch?v=TW0Eq2Q-9Ac), or [this passionate exposition](https://www.youtube.com/watch?v=0EdkxI6NeuA).

#### <a name='inputs-and-outputs'></a>Inputs and Outputs
Assume that the **smartcab** is assigned a route plan based on the passengers’ starting location and destination. The route is split at each intersection into waypoints, and you may assume that the **smartcab**, at any instant, is at some intersection in the world. Therefore, the next waypoint to the destination, assuming the destination has not already been reached, is one intersection away in one direction (North, South, East, or West). The **smartcab** has only an egocentric view of the intersection it is at: It can determine the state of the traffic light for its direction of movement, and whether there is a vehicle at the intersection for each of the oncoming directions. For each action, the **smartcab** may either idle at the intersection, or drive to the next intersection to the left, right, or ahead of it. Finally, each trip has a time to reach the destination which decreases for each action taken (the passengers want to get there quickly). If the allotted time becomes zero before reaching the destination, the trip has failed.

#### <a name='rewards-and-goal'></a>Rewards and Goal
The **smartcab** receives a reward for each successfully completed trip, and also receives a smaller reward for each action it executes successfully that obeys traffic rules. The **smartcab** receives a small penalty for any incorrect action, and a larger penalty for any action that violates traffic rules or causes an accident with another vehicle. Based on the rewards and penalties the **smartcab** receives, the self-driving agent implementation should learn an optimal policy for driving on the city roads while obeying traffic rules, avoiding accidents, and reaching passengers’ destinations in the allotted time.


### <a name='code'></a>Code

Template code is provided in the `smartcab/agent.py` python file. Additional supporting python code can be found in `smartcab/enviroment.py`, `smartcab/planner.py`, and `smartcab/simulator.py`. Supporting images for the graphical user interface can be found in the `images` folder. While some code has already been implemented to get you started, you will need to implement additional functionality for the `LearningAgent` class in `agent.py` when requested to successfully complete the project. 


### <a name='run'></a>Run

In a terminal or command window, navigate to the top-level project directory `smartcab/` (that contains this README) and run one of the following commands:

```python smartcab/agent.py```  
```python -m smartcab.agent```

This will run the `agent.py` file and execute your implemented agent code into the environment
