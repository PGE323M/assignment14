#!/usr/bin/env python

# Copyright 2018-2020 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest


def cleanup(line):

    return line.strip().strip('\n').split()


class TestSolution(unittest.TestCase):


    def test_cmg_output(self):

        with open('assignment14.out') as f:

            raw_content = f.readlines()


        for line in raw_content:
            clean_line = cleanup(line) 

            if clean_line != []:
                if clean_line[0] == 'Current' and clean_line[1] == 'Fluids':
                    assert abs(float(clean_line[6]) - float(71258)) < 20


    def test_cmg_output_secret(self):

        with open('assignment14.out') as f:

            raw_content = f.readlines()


        for line in raw_content:
            clean_line = cleanup(line) 

            if clean_line != []:
                if clean_line[0] == 'Injection' and clean_line[1] == 'Rates':
                    assert abs(float(clean_line[4]) - float(1.4045)) < 0.2

if __name__ == '__main__':
    unittest.main()









