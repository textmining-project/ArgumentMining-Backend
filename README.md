# Identifying Argumentative Discourse Structures in Persuasive Essays
Text mining project at Universitat Passau

# tools
- 1.Python 2.7
- Python libraries
- Pandas
- Numpy
- Scipy
- gensim
- Scikit learn
- nltk library
- Pycharm or suitable IDE tool
- [Brat reader ,Integrated with the project](https://github.com/clips/bratreader.git)
# Datasets Train and Test

- Christian Stab and Iryna Gurevych. 2014. Annotating argument components and relations
   in persuasive essays. In Proceedings of the 25th International Conference on
   Computational Linguistics (COLING 2014), Dublin, Ireland

- Christian Stab and Iryna Gurevych. 2016. Parsing Argumentation Structure in
   Persuasive Essays. arXiv preprint, https://arxiv.org/abs/1604.07370

# Note
- Certain blocks of code has been commented since it needs to be compiled once , if Datasets are changed picklefiles needs to be trained again

# Steps to Load and train your dataset

- Collect corpus which should be annotated as shown below in the link
  
- [Example for annotated data](https://gist.github.com/abhiglobalistic/d7107236b6c40eb946b337abf86b8095)  


- [Bratreader](https://github.com/clips/bratreader.git )
  

- Using the above bratreader to extract each annotated essay as annotated object
  which contains several attributes which are used in Data preprocessing
   * Place the annotated files ".ann" at "ArgumentMining-Backend/bratessays/"

# Usage 
  
   [Usage Instructions](https://gist.github.com/abhiglobalistic/d3b60a5f9d20d1dad22ce598b6cbf615)
        
# Metrics
  
   [Metrics sample](https://gist.github.com/abhiglobalistic/8471f10090ea24f623f5418589985ba1)
   
   
   This project is only for education purpose only !!
     
