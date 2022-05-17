## Practical Work 2 (PW2, Individual): Combining multiple classifiers

## Installation
In order to run the program, first of all we need to install packages.

run the following command:
`pip install -r requirements.txt`

## Usage
you should visit main file to run all algorithms and analyses



## Procedure

1. Implement a Random Forest and a Decision Forest technique.
The base-learner for inducing the trees will be the CART method.

    a. Both the Random Forest (RF) and the Decision Forest (DF) classifier
    must be able to read a dataset in csv file format

    b. Learn the model (the random forest or decision forest) from the 
    training data set, and at the same time produce an ordered list of 
    the features used in the forest, according to its importance. The 
    importance can be estimated as the frequency of its appearance in 
    the random forest/random decision constructed.

    c. The models must have, at least, the hyper-parameter F (number of 
    random features used in the splitting of the nodes in RF or in each 
    tree in DF) and the number of trees (NT) desired.


2. Forest interpreter implemented, with that, is given a random forest 
or a decision forest would be able to classify a test dataset, obtaining 
the corresponding classification accuracy values (or generalization error) 
for different combination of values of F and NT. For instance, try (when 
make sense), being M the total number of features:


    Random Forest
    • Each training set for each tree is a bootstrapped sampling of the 
    original training set
    • NT=1,10,25,50,75,100
    • F=1,3,𝑖𝑖𝑖𝑖𝑖𝑖(log2𝑀𝑀+1),√𝑀𝑀
    Decision Forest
    • Each training set for each tree is the same original training set
    • NT=1,10,25,50,75,100
    • F = 𝑖𝑖𝑖𝑖𝑖𝑖(𝑀𝑀�4) , 𝑖𝑖𝑖𝑖𝑖𝑖(𝑀𝑀�2) , 𝑖𝑖𝑖𝑖𝑖𝑖(3∗𝑀𝑀�4), 𝑅𝑅𝑅𝑅𝑖𝑖𝑖𝑖𝑅𝑅(1,M) for each tree)

