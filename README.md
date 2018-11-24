# Signaling heroes instructions


## The challenge

The challenge is to create an anomaly detection solution to detect attack messages from SS7 signaling traffic. The solution is supposed to include a complete pipeline from the network capture dataset (pcap file) to the result that points out the attacks from the message data and the malicious nodes in the network. Regardless, there will be datasets in both the network capture format (pcap) and the preprocessed format (csv), which enables the teams to start their work by implementing the machine learning algorithm or even work on the data preprocessing and algorithm creation simultaneously.

The main focus should be in generating a machine learning based solution to detect attacks and malicious endpoints from the signaling traffic. The key areas of the implementation are data preprocessing, algorithm creation and model fine-tuning. You are free use any machine learning tools and frameworks you see applicable.


## The data

The relevant datasets can be downloaded from the provided Github repository.

The three datasets (found from [training_data.zip](/docs/training_data.zip)) named *training_* should be used in creating the pipeline and training the model. The teams can choose whether to implement a supervised or an unsupervised model. An unsupervised model will be valued more.

The files *training_data.pcapng* and *training_data.csv* include the same traffic data without any attacks. The file *training_data_attacks.csv* is the same data but enriched with some attack messages and labels. The messages labeled 0 is considered normal and message labeled 1 is considered anomalous.

The datasets folder also includes two more challenging datasets in case the teams want to challenge themselves more and would like to earn additional points.


## SS7 crash course

Please use the provided source material provided in the Github repository to familiarize yourself with the SS7 signaling protocol and the relevant attack material. A good starting points is the [SS7_advanced_attacks.pdf](/docs/SS7_advanced_attacks.pdf). The attack in question is the SMS interception and SS7 firewall bypass.


## Where to start

The best bet might be to start from the training datasets and try to come up with a viable ML solution.


## Asking for help

There are Ericsson mentors present in the challenge areas. Please send your questions to the challenge specific Slack group. You may also ask questions directly from the mentors but please be aware that the mentors will shared those answers in the slack group as well.


## Uploading the results

The test datasets will be provided to the participants at 8:15 on Sunday morning. The same data will be provided both in pcap and csv format. Use your solution to detect the malicious messages from the data. Store your results (malicious messages indeces) to a csv file. The indices should be according to those in the *testing_data.csv* file. Please note that the testing data files do not include any labels.

The uploaded files should at least include the the source code files and the results file (csv).


## Evaluation criteria

The evaluation is done based on the following criteria. Only the first criteria is used. In case the evaluation results in a tie (less than 0.1 difference) between two teams, the second criteria is used and so on.

1. F1 Score
2. Completeness:
  * Has the pipeline been implemented from PCAP or only from CSV?
3. Effectiveness:
  * How long does it take to run the pipeline? (difference of less than a couple of seconds is considered equal)
4. Elegance:
  * The readability of the code
5. Solution to detect anomalies from more challenging datasets


## Links

[SS7 on Wikipedia](https://en.wikipedia.org/wiki/Signalling_System_No._7)

[SS7 attacks presentation](https://www.youtube.com/watch?v=-wu_pO5Z7Pk)

[Wireshark GSM MAP parameters](https://www.wireshark.org/docs/dfref/g/gsm_map.html)


