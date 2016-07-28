import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator


class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint

        # TODO: Initialize any additional variables here
        # Define all legal actions
        self.allLegalActions = [None, 'forward', 'left', 'right']

        # Initialize Q table
        self.Q_table = {}

        # Initialize learning parameters:
        self.alpha = 1  # leraning rate
        self.gamma = 0.9  # discount rate
        self.epsilon = 1  # exploration probability


    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        # Reset Q table to empty
        self.Q_table = {}


    def getState(self):
        """
        :return: current state
        """
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        # Define state
        self.state = 'deadline: {}, light: {}, left: {}, oncoming: {}, next_waypoint: {}'.\
            format(deadline, inputs['light'], inputs['left'], inputs['oncoming'], self.next_waypoint)
        return self.state


    def computeQ(self, state1, action1, reward1, state2):
        """
        Compute Q value for episode n using the equation:
        Q_n(s, a) = (1 - alpha_n) * Q_n-1(s, a) + alpha_n[r_n + gamma * max on a'{Q_n-1(s', a')}]
                    or Q_n-1(x, a)

        :param state1: current state
        :param action1: action that takes current state to next state
        :param reward1: reward of taking action1
        :param state2: next state
        :return: Q value of (state1, action1)
        """
        prev_Q = self.Q_table.get((state1, action1), None)  # get Q_n-1(s, a) from available Q table
        if prev_Q is None:   # if no value has been recorded, initialize Q value as r_n
            self.Q_table[(state1, action1)] = reward1
        else:  # if Q value has already been recorded in Q table, update the Q value
            Q_s = [self.Q_table.get((state2, a), 0.0) for a in self.allLegalActions]
            self.Q_table[(state1, action1)] = (1 - self.alpha) * prev_Q + self.alpha * (reward1 + self.gamma * max(Q_s))


    def chooseAction(self, state):
        """
        Choose action by balancing exploration and exploitation, i.e. implement epsilon-greedy policy
        :param state: current state
        :return: best action to next state
        """
        if random.random < self.epsilon:
            action = random.choice(self.allLegalActions)    # choose a random action
        else:
            j = self.allLegalActions.index(self.next_waypoint)
            Q_s = [self.Q_table.get((state, action), 0.0) for action in self.allLegalActions]
            maxQ = max(Q_s)
            count = Q_s.count(maxQ)
            if count > 1: # there're multiple actions with max Q value
                best_actions = [i for i in range(len(self.allLegalActions)) if Q_s[i] == maxQ]
                if j in best_actions: # if next way point is in best actions, choose it
                    i = j
                else:
                    i = random.choice(best_actions) # otherwise, choose a random action
                # i = random.choice(best_actions)
            else:
                i = Q_s.index(maxQ)
            action = self.allLegalActions[i]
        return action


    def update(self, t):

        # Adjust learning parameters
        self.alpha = 1.0 / float(t + 1)
        self.gamma = 0.2
        self.epsilon = 1.0 / float(t + 1)

        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        state1 = self.getState()
        # print 'state1: ', state1 # [debug]

        # TODO: Select action according to your policy
        action1 = self.chooseAction(state1)

        # Execute action and get reward
        reward1 = self.env.act(self, action1)

        # TODO: Learn policy based on state, action, reward
        state2 = self.getState()
        # print 'state 2:', state2 # [debug]

        self.computeQ(state1, action1, reward1, state2)

        # print 'Q table:', self.Q_table # [debug]

        print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".\
            format(deadline, inputs, action1, reward1)  # [debug]




def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # set agent to track

    # Now simulate it
    sim = Simulator(e, update_delay=0)  # reduce update_delay to speed up simulation
    sim.run(n_trials=100)


if __name__ == '__main__':
    run()
