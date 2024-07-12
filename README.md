


# Jafar Abdollahi

<h2> Discription </h2>
# Early Prediction of Diabetes using Feature Selection and Machine Learning Algorithms 
Highlights
•	A model is proposed for Prediction diabetes based on Feature Selection and Machine Learning Algorithms.
•	The purpose of the study is to enforce Particle Swarm Optimization (PSO) and Machine Learning Algorithms.
•	The proposed method is to evaluate on a set of medical data relating to a diabetes diagnosis challenge.
•	The PSO-RF method delivers greater performance when compared with other models.

Abstract
Diabetes has become one of the most common diseases in middle- and low-income countries. Machine learning (ML) and data mining techniques have recently been used to predict diabetes with a high success rate. As a result, medical professionals seek a dependable method for predicting diagnosis. Of course, the feature selection process may be considered a global combinatorial optimization problem in machine learning. The number of features is reduced, irrelevant, noisy, redundant data is removed, and classification accuracy is acceptable. This work uses particle swarm optimization (PSO) to implement feature selection, followed by performance comparison. After that, three medical datasets are used to compare the performance of several machine learning methods. Standard approaches are used to determine the optimum technique for the three datasets. The best results for three datasets are reported for each scheme. The primary goal is to assess the validity of each algorithm's data classification in terms of efficiency and effectiveness in terms of accuracy, sensitivity, and specificity. Decision Tree, Random Forest, and Naïve Bayes deliver the highest accuracy with the lowest mistake rate, according to the findings of the experiments. Machine learning may classify and determine which instances should be sent to medical for further evaluation and treatment with high accuracy. Using such an algorithm on a global scale could help minimize the number of people diagnosed with diabetes.  

2.2.	PSO Algorithms
Many challenging research issues can be formulated as optimization issues. The emergence of big data technology has also sparked a large-scale increase in the complexity and size of optimization challenges. The development of parallelized optimization techniques has become necessary due to the high computing cost of these issues. One of the most well-known swarm intelligence-based algorithms, particle swarm optimization (PSO), is enhanced with resilience, simplicity, and global search capabilities [33]. It has undergone numerous improvements since it was first introduced in 1995. With more knowledge of the method, researchers have created new iterations that address diverse demands, created new applications in various fields, published theoretical analyses of the consequences of the different parameters, and proposed numerous algorithm variations [34]. Ant colony optimization (ACO), particle swarm optimization (PSO), artificial fish swarm (AFS), bacterial foraging optimization (BFO), and artificial bee colony are just a few of the swarm intelligence techniques that have been developed in recent years (ABC). This paper attempts to pick features using PSO. 


USAGE
Firstly install all dependencies via the following command.

pip3 install -r requirements.txt
Now train the application in you pc as

python3 diabetes.py
Finally run the application :

python3 gui.py


<h2> Dataset </h2>
The National Institute of Diabetes and Digestive and Kidney Diseases (NIDDKD) includes cost information (donated by Peter Turney). The selection of these instances from a larger database was subjected to many constraints. All patients are of Pima Indian heritage, female, and at least 21 years old. This study uses the type 2 diabetes dataset from (https://www.kaggle.com/kumargh/pimaindiansdiabetescsv). There are 768 instances in this data set, divided into two groups: diabetic and non-diabetic, with eight risk factors: number of pregnancies, two-hour plasma glucose concentration in an oral glucose tolerance test, diastolic blood pressure, triceps skin fold thickness, two-hour serum insulin, body mass index, diabetes pedigree function, and age, as shown in Table 8. 70% of the information is for training purposes, while 30% is for testing purposes. The data includes characteristics like Pregnancy, Glucose, Blood-Pressure, Skin-Thickness, Insulin, BMI, Diabetes-Pedigree-Function, Age, and Class.



<h2> Methods </h2>
For effective machine learning model creation. The majority of attributes are typically irrelevant to supervised machine learning categorization. Feature selection and outlier elimination were part of the raw data pre-processing phase. There are several approaches to dealing with outside and inconsistent data. We chose the qualities in our study that had significantly connected data. A feature subset selection based on PSO is proposed in the second stage. After preprocessing and feature selection, the integrated dataset is subjected to classification algorithms.
The project is divided into two halves. The first is the feature selection approach, which focuses on obtaining more relevant This article discusses various approaches and datasets for evaluating the performance of different machine learning algorithms. Figure 1 depicts the study's recommended methodology. This study's methodology is divided into three key steps: data collecting, preprocessing, and classification. The dataset used for the analysis is the diabetes of the study. The proposed method uses data from three different profiles and is based on an integrated methodology. On the other hand, the medical dataset has a lot of missing and irrelevant data that cannot be used for categorization. As a result, the initial phase of the strategy is preparing the dataset using typical imputation techniques in accordance with the data profiles. 
 In machine learning applications, feature engineering is a critical stage. Modern data sets are defined with several property features while discarding the irrelevant for faster and more efficient data classification. The second stage applies the classification algorithms to the collected parts to produce predictions.

<img src="https://github.com/Jafar-Abdollahi/Type-2-diabetes-diagnosis-software-using-artificial-intelligence/blob/main/Picture1.png"> 

So, the objective of this study: Comparison of machine learning algorithms in diagnosing diabetes. Thus, to compare the behavior of LR, NB, KNN, DT, RF, SVM, GB, SGDA, and C4.5, we conducted an experiment evaluating the algorithms' effectiveness and efficiency. Specifically, the research questions we set for the study area: 
1.	Which algorithm is the most effective? 
2.	Which one is the most efficient? 
3.	Which one is the most accurate?



<h2> Conlusion </h2>
Patients' quality of life and life expectancy can benefit from early diabetes diagnosis. Different diabetes detection models [19] have been developed using supervised algorithms. In almost every classification task, the dataset comprises many features. However, because some features are useless and duplicated, they are not required for good classification performance. As a result, classifiers with fewer characteristics but higher classification accuracy are preferred for ease of interpretation. Due to improved representation, the ability to explore huge spaces, being more cost-effective computed, being easier to implement, and requiring fewer parameters, PSO is an excellent technique for feature selection problems. This work compared a particle swarm optimization algorithm and ten machine learning algorithms. The Bayesian information criterion (Accuracy) is proposed as a fitness function. Table 15 shows the feature selection results with the particle swarm algorithm on each data set. All classification techniques were experimented with in "Jupyter Notebook” programming in Python.

<img src="https://github.com/Jafar-Abdollahi/Type-2-diabetes-diagnosis-software-using-artificial-intelligence/blob/main/Picture2.png"> 
<img src="https://github.com/Jafar-Abdollahi/Type-2-diabetes-diagnosis-software-using-artificial-intelligence/blob/main/Picture3.png"> 
<img src="https://github.com/Jafar-Abdollahi/Type-2-diabetes-diagnosis-software-using-artificial-intelligence/blob/main/Picture4.png"> 

Detecting the dangers of diabetes at an early stage is one of the world's most pressing health concerns. Machine learning and deep learning has been successfully utilized in medical image and healthcare [49] analysis like whole-slide pathology [51], X-ray [47], diabetes [1, 2], breast cancer [48], heart [50], time series [57], Medicinal Plants [52], stock market [59], Stroke [74], Maximizing the Impact on Social Networks [76], outcome prediction of bupropion exposure [77], etc. This research aims to develop a framework for predicting the likelihood of developing diabetes. This paper compared the outcomes of nine machine learning classification algorithms with various statistical measures. The dataset collected through the UCI site was subjected to tests. 
There are also many data processing and machine learning strategies for analyzing medical knowledge. Producing accurate and computationally affordable classifiers for medical applications is a significant challenge in data processing and machine learning. On the diabetes datasets, this study used nine primary algorithms: LR, NB, C 4.5, DT, RF, SVM, GB, SGDA, and KNN. To select the best algorithm—classification accuracy, we sought to analyze the efficiency and efficacy of various algorithms in terms of accuracy, sensitivity, and specificity. Random forest and decision trees performed better than all other algorithms. In conclusion, DT, NB, and RF proved their strength in diagnosing and identifying diabetes and achieved the simplest performance, accuracy, and low error rate.  
The findings show that by choosing fewer variables, we could diagnose diabetes illnesses with a higher degree of accuracy. Our method produced more accurate results when the outcomes were compared to the usual feature selection approaches, namely the F-score and the information gain. The accuracy of the suggested method is higher than that of the genetic algorithm for feature selection (99.79% for RF using Holdout - 99.59% for DT using K-fold=5, and 99.86% for NB using K-fold=10). Additionally, the strategy had a superior performance utilizing fewer features than other methods that employed the same data. This work has the potential to be useful in clinical practice and serve as a tool for doctors and other medical professionals. 


<h2> Paper </h2>
https://link.springer.com/article/10.1007/s42979-023-02545-y

<h2> Contact me </h2>
You can reach me at:

Email: ja.abdollahi77@gmail.com
<br>
LinkedIn: https://www.linkedin.com/in/jafar-abdollahi-7647971b3/
<br>
Google Scholar: https://scholar.google.com/citations?user=2dK8kPwAAAAJ&hl=en
<br>
researchgate: https://www.researchgate.net/profile/Jafar-Abdollahi?ev=hdr_xprf&_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6ImxvZ2luIiwicGFnZSI6ImhvbWUiLCJwcmV2aW91c1BhZ2UiOiJsb2dpbiIsInBvc2l0aW9uIjoiZ2xvYmFsSGVhZGVyIn19
<br>
youtube: https://www.youtube.com/@jafarabdollahi/featured
<br>
<img src="https://github.com/Jafar-Abdollahi/cuffless-bp-master-in-python-jupyter-/blob/main/2024-07-07_19-45-22.png"> 
