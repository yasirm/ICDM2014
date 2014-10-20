
The software requires Java version 1.6 or greater and Python version 2.6 or greater.

*********************************************** Executables *****************************************
The software includes three primary files:

- SAMclustering.jar — A JAR file of the SAM modeling. 

- JahmmYah.jar — a modified version of Jahmm libraries to be compatible with Left-right HMMs as well as capable of learning lambda parameters of SAM models that determines the rate of adoptions. 

- clustering_sequences.py — a python file that initially creates random partitions of the dataset in different clusters. This file is for internal usage.
——————————————————————————
——————————————————————————


********************************************** Dataset ***********************************************
The input data should be contained in a file named seq_file.txt. 
Each line of the file should be a sequence that, for example, corresponds to an item. These lines should of of the following format:

%seq_ID [user_1 delay_1] [user_2 delay_2] …. 

As an example, one such input file (i.e. seq_file.txt) can be found in MovieLens directory.
——————————————————————————
——————————————————————————

*********************************************** How to run SAM **********************************

The command to run learn models (and corresponding clusters) as well as the rates of adoptions is as follows:

java -cp SAMclustering.jar:JahmmYah.jar pyramid.comm.init.SAMClustering -p <absPathToDataFolder>  -c <nClusters> -u <nUsers>

here, <absPathToDataFolder> is the absolute path to the directory where the input file resides. 
<nClusters> specifies the number of clusters to be created.
<nUsers>    specifies the total number of users in the dataset. 

As the execution tries different numbers stages/states in parallel to find the best one, it is recommended that one provides the java process at least 3 gigs of RAM. An example command to execute SAM framework using the provided MovieLens dataset, that has 2113 users, in order to learn 5 models from the data is as follows:

java -Xmx4g -cp SAMclustering.jar:JahmmYah.jar pyramid.comm.init.SAMClustering -p /Your/Directory/ICDM2014/MovieLens/ -c 5 -u 2113

here, Java will use 4 gigabytes of RAM at the most. 
———————————————————————————
———————————————————————————


************************************************** Output *******************************************

The output is stored in two folders, namely, FinalModels and FinalClusters, inside at the following location:
<absPathToDataFolder>/mixedClusters/ 

Thus, the learnt models can be found inside <absPathToDataFolder>/mixedClusters/FinalModels/
Each model is a text file, with the naming convention, LRmode_i.txt (i indicates the number of the model). Ignore files called Viterbi*.txt as they are used for other analyses. The model file contains transition probabilities to other states as :

A 0.074 0.373 …

(note that each such line starts with A and first of this line indicates transition probabilities from state 1, the second indicates transitions from state 2, and so on).

and learnt emission and adoption rates of the corresponding states are of the format:

MultiAdoptionOPDF [ [ user1_emission_probability user2_emission_probability …] rateOfAdoption ]


The clusters of sequences corresponding to each model can be found inside <absPathToDataFolder>/mixedClusters/FinalClusters/
These will be available in two formats; for example, the file Clusteri.txt contains just the IDs of sequences in i-th cluster, and Sequencei.txt contains both the ID as well as the actual sequence.

————————————————————————————
————————————————————————————



