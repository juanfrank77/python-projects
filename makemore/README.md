# makemore

makemore takes one text file as input, where each line is assumed to be one training thing, and generates more things like it. For instance, we can feed it a dataset of company names and then it will generate cool new names for a company.
Under the hood, it is an autoregressive character-level language model, with a wide choice of models from bigrams all the way to a Transformer.  

This is made as an experiment to practice building neural networks in PyTorch based on the work of Andrej Karpathy.


