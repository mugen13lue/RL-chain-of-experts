from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import tensorflow as tf
import numpy as np

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts
import numpy as np 
import os
import json

from experts import (
    ModelingExpert, 
    ProgrammingExpert,
    LPFileGenerator,
    ModelingKnowledgeSupplementExpert,
    ParameterExtractor,
    CodeReviewer,
    ProgrammingExampleProvider,
    TerminologyInterpreter,
)

class RLConductorEnv(py_environment.PyEnvironment):

    def __init__(self):
        model_name = 'gpt-4o-mini-2024-07-18' 
        self.model_name = model_name
        self._all_experts = [
            TerminologyInterpreter(model_name),
            ParameterExtractor(model_name),
            ModelingExpert(model_name),
            ProgrammingExampleProvider(model_name),
            ProgrammingExpert(model_name),
            # LPFileGenerator(model_name),
            ModelingKnowledgeSupplementExpert(model_name),
            CodeReviewer(model_name),
        ]
        self.str_experts = [
                "Terminology Interpreter",
                "Parameter Extractor", 
                "Modeling Expert",
                "Programming Example Provider",
                "Programming Expert",
                "Modeling Knowledge Supplement Expert",
                "Code Reviewer",
        ]
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=6, name='action')
        # what is the observation spec of my model?
        #[expert, problem]
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(2,), dtype=np.int32, minimum=[0,0],maximum=[6, 600], name='observation')
        self._state=[0, 0] #represent the (row, col, frow, fcol) of the player and the finish
        self._episode_ended = False
        #load in the data
        self._comments, self._experts, self._descriptions= self.load_comments_and_experts()
        self._gt = self.load_gt()
        self._current_time_step = 0

    #find ground truth in run_exp
    def load_gt(self):
        codes = []
        directory = "log/run_coe_LPWP_1741681180/"
        for i in range(0,288):
            with open(os.path.join(directory, "prob_{}_original_answer.txt".format(i)), 'r') as f:
                codes.append(f.read())
        return codes
    
    def load_comments_and_experts(self):
        comments = [[] for _ in range(7)]
        experts = set()
        descriptions = []
        desc_path = "dataset/LPWP/"
        directory = "expert_data"
        for file in os.listdir(directory):
            with open(os.path.join(directory, file), 'r') as f:
                j = json.load(f)
                i = 0
                for k, exp in enumerate(self.str_experts):
                    if exp == j["expert"]:
                        #print("FOUND!", str(exp), k, len(comments))
                        i = k
                        break
                prob_i = 0
                for l in range(0,288):
                    with open(os.path.join(desc_path, "prob_{}".format(l), "description.txt"), "r") as g:
                        if g.read()[:10] == file[:10]:
                            prob_i = l
                comments[i].append([j["comment"], l])
                experts.add(j["expert"])
                descriptions.append(l)


        comments[3].append(["", 0])
        return comments, experts, descriptions
    
    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec
    
    def _reset(self):
        self._state=[0, int(np.random.randint(288))]
        self._episode_ended = False
        self._current_time_step = 0
        return ts.restart(np.array(self._state, dtype=np.int32))

    def _step(self, action):
        #self._current_time_step += 1

        if self._episode_ended:
            return self.reset()

        self.move(action)

        if self.game_over():
            self._episode_ended = True

        if self._episode_ended:
            if self.game_over():
                reward = 100
            else:
                reward = 0
            return ts.termination(np.array(self._state, dtype=np.int32), reward)
        else:
            return ts.transition(
                np.array(self._state, dtype=np.int32), reward=0, discount=0.9)

    #Go between the diff experts and get a random response from an expert 
    def move(self, action):
        exp, comment = self._state[0],self._state[1]

        self._state[0] = action
        self._state[1] = np.random.randint(len(self._comments[self._state[0]]))

    def hammingDist(self, str1, str2): 
        i = 0
        count = 0
        length = min(len(str1), len(str2)) 
        while(i < length): 
            if(str1[i] != str2[i]): 
                count += 1
            i += 1
        if length == 0:
            return 0
        return count / length

    def game_over(self):
        #compute hamming distance 
        #fetch the comment
        #fetch the ground truth and compute hamming distance 
        #print(len(self._comments) , [len(i) for i in self._comments])
        #print(self._state[0], [self._state[1]])
        str1 = self._comments[self._state[0]][self._state[1]][0]
        str2 = self._gt[self._comments[self._state[0]][self._state[1]][1]]
        return self.hammingDist(str1, str2) >= 1.0

if __name__ == '__main__':
    env = RLConductorEnv()
    utils.validate_py_environment(env, episodes=5)
