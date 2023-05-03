#!/usr/bin/env python
# coding: utf-8

# <a href="https://www.youtube.com/watch?v=iCL1TmRQ0sk&list=PLxqBkZuBynVQEvXfJpq3smfuKq3AiNW-N&index=19"><h1 style="font-size:250%; font-family:cursive; color:#ff6666;"><b>Link YouTube Video - Adding a custom task-specific Layer to a HuggingFace Pretrained Model</b></h1></a>
# 
# [![IMAGE ALT TEXT](https://imgur.com/ZFLzcw9.png)](https://www.youtube.com/watch?v=iCL1TmRQ0sk&list=PLxqBkZuBynVQEvXfJpq3smfuKq3AiNW-N&index=19 "")
# 
# ---------------------------

# ## First What is BERT?
# 
# BERT stands for Bidirectional Encoder Representations from Transformers. The name itself gives us several clues to what BERT is all about.
# 
# BERT architecture consists of several Transformer encoders stacked together. Each Transformer encoder encapsulates two sub-layers: a self-attention layer and a feed-forward layer.
# 
# ### There are two different BERT models:
# 
# - BERT base, which is a BERT model consists of 12 layers of Transformer encoder, 12 attention heads, 768 hidden size, and 110M parameters.
# 
# - BERT large, which is a BERT model consists of 24 layers of Transformer encoder,16 attention heads, 1024 hidden size, and 340 parameters.
# 
# 
# 
# BERT Input and Output
# BERT model expects a sequence of tokens (words) as an input. In each sequence of tokens, there are two special tokens that BERT would expect as an input:
# 
# - [CLS]: This is the first token of every sequence, which stands for classification token.
# - [SEP]: This is the token that makes BERT know which token belongs to which sequence. This special token is mainly important for a next sentence prediction task or question-answering task. If we only have one sequence, then this token will be appended to the end of the sequence.
# 
# 
# It is also important to note that the maximum size of tokens that can be fed into BERT model is 512. If the tokens in a sequence are less than 512, we can use padding to fill the unused token slots with [PAD] token. If the tokens in a sequence are longer than 512, then we need to do a truncation.
# 
# And that’s all that BERT expects as input.
# 
# BERT model then will output an embedding vector of size 768 in each of the tokens. We can use these vectors as an input for different kinds of NLP applications, whether it is text classification, next sentence prediction, Named-Entity-Recognition (NER), or question-answering.
# 
# 
# ------------
# 
# **For a text classification task**, we focus our attention on the embedding vector output from the special [CLS] token. This means that we’re going to use the embedding vector of size 768 from [CLS] token as an input for our classifier, which then will output a vector of size the number of classes in our classification task.
# 
# -----------------------
# 
# ![Imgur](https://imgur.com/NpeB9vb.png)
# 

# # The concept of adding a custom task-specific layer to a HF Model
# 
# ![](1.png)
# 
# 
# When we switch from the pretraining task to the downstream task, we
# need to replace the last layer of the model with one that is suitable for the task.
# This last layer is called the model head; it’s the part that is task-specific. 
# 
# The rest of the model is called the body; it includes the token embeddings and
# transformer layers that are task-agnostic. 
# 
# This structure is reflected in the Transformers code as well: the body of a model is implemented in a class such
# as BertModel or GPT2Model that returns the hidden states of the last layer. 
# 
# ### To get it we do `outputs[0]=last hidden state`
# 
# The hidden states are passed as inputs to a model head to produce the final output. 🤗 Transformers provides a different model head for each task as long as a model supports the task (i.e., you can’t use DistilBERT for a sequence-to-sequence task like translation).
# 
# And then we have Task-specific models such as BertForMaskedLM or BertForSequenceClassification - which usees the base model and add the necessary head on top of the hidden states,
# 
# For example, **`DistilBertForSequenceClassification`** is a base DistilBERT model with a sequence classification head. The sequence classification head is a linear layer on top of the **pooled** outputs.
# 
# For a **question answering task**, you would use the **`DistilBertForQuestionAnswering`** model head. The question answering head is similar to the sequence classification head except it is a linear layer on top of the **hidden states** output.

# ### To get it we do `outputs[0]=last hidden state`

# ### [Dataset link](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection)

# # import numpy as np
# import pandas as pd
# 
# from datasets import load_dataset,Dataset,DatasetDict
# from transformers import DataCollatorWithPadding,AutoModelForSequenceClassification, Trainer, TrainingArguments,AutoTokenizer,AutoModel,AutoConfig
# from transformers.modeling_outputs import TokenClassifierOutput
# import torch
# import torch.nn as nn
# import pandas as pd
# 
# import os
# for dirname, _, filenames in os.walk('../data'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# Note: You can use any model in this example (not necessarily a model trained for classification) since we will only use that model’s body and leave the head.

# In[1]:


dataset_v2_path = "../data/news-headlines-dataset-for-sarcasm-detection/Sarcasm_Headlines_Dataset_v2.json"


# In[2]:


import pandas as pd
df = pd.read_json(dataset_v2_path, lines=True)
df = df.rename(columns={'is_sarcastic':'label'})

df.head()


# ## Load Dataset with HF's load_dataset

# In[3]:


from datasets import load_dataset
dataset_hf=load_dataset("json", data_files=dataset_v2_path)
dataset_hf = dataset_hf.rename_column(original_column_name='is_sarcastic', new_column_name='label')


# In[4]:


dataset_hf=dataset_hf.remove_columns(['article_link'])

dataset_hf.set_format('pandas')

dataset_hf=dataset_hf['train'][:]


# In[5]:


from datasets import Dataset, DatasetDict
# dataset_hf.drop_duplicates(subset=['headline'],inplace=True)
dataset_hf=dataset_hf.reset_index()[['headline','label']]

dataset_hf=Dataset.from_pandas(dataset_hf)


# Train Test Valid Split
train_testvalid = dataset_hf.train_test_split(test_size=0.2,seed=15)


test_valid = train_testvalid['test'].train_test_split(test_size=0.5,seed=15)

dataset_hf = DatasetDict({
    'train': train_testvalid['train'],
    'test': test_valid['test'],
    'valid': test_valid['train']})

dataset_hf


# In[6]:


from transformers import AutoTokenizer, AutoModel, AutoConfig
checkpoint = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

tokenizer.model_max_len=512


# ## Vector size "distilbert-base-uncased"
# 
# In the model distilbert-base-uncased, each token is embedded into a vector of size 768. The shape of the output from the base model is 
# 
# ### (batch_size, max_sequence_length, embedding_vector_size=768)

# In[7]:


def tokenize(batch):
  return tokenizer(batch["headline"], truncation=True, max_length=512)

tokenized_dataset = dataset_hf.map(tokenize, batched=True)
tokenized_dataset


# In[8]:


from transformers import DataCollatorWithPadding
tokenized_dataset.set_format('torch', columns=["input_ids", "attention_mask", "label"] )

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)



# https://huggingface.co/docs/transformers/main_classes/data_collator
# 
# 
# Data collators are objects that will form a batch by using a list of dataset elements as input. These elements are of the same type as the elements of train_dataset or eval_dataset.
# 
# To be able to build batches, data collators may apply some processing (like padding). Some of them (like DataCollatorForLanguageModeling) also apply some random data augmentation (like random masking) on the formed batch.
# 
# data_collator automatically pads the model inputs in a batch to the length of the longest example. This bypasses the need to set a global maximum sequence length, and in practice leads to faster training since we perform fewer redundant computations on the padded tokens and attention masks.
# 
# 
# ------------

# ## We construct `MyTaskSpecificCustomModel` class that inherits from the nn.Module.

# In[9]:


import torch
import torch.nn as nn
from transformers.modeling_outputs import TokenClassifierOutput
class MyTaskSpecificCustomModel(nn.Module):
    def __init__(self, checkpoint, num_labels ):
        super(MyTaskSpecificCustomModel, self).__init__()
        self.num_labels = num_labels
        
        self.model = model = AutoModel.from_pretrained(checkpoint, config = AutoConfig.from_pretrained(checkpoint, 
                                                                                                       output_attention = True, 
                                                                                                       output_hidden_state = True ) )
        # New Layer
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(768, num_labels )
        
    def forward(self, input_ids = None, attention_mask=None, labels = None ):
        outputs = self.model(input_ids = input_ids, attention_mask = attention_mask  )
        
        last_hidden_state = outputs[0]
        
        sequence_outputs = self.dropout(last_hidden_state)
        
        logits = self.classifier(sequence_outputs[:, 0, : ].view(-1, 768 ))
        
        loss = None
        loss = None
        if labels is not None:
            loss_func = nn.CrossEntropyLoss()
            loss = loss_func(logits.view(-1, self.num_labels), labels.view(-1))
            
            return TokenClassifierOutput(loss=loss, logits=logits, hidden_states=outputs.hidden_states, attentions=outputs.attentions)
        
    


# ## attention_mask
# 
# From Doc - This argument indicates to the model which tokens should be attended to, and which should not.
# 
# ### If the attention_mask is 0, the token id is ignored. For instance if a sequence is padded to adjust the sequence length, the padded words should be ignored hence their attention_mask are 0.
# 
# --------------
# 
# ### torch.nn.Linear(in_features, out_features, bias=True)
# 
# Parameters
# in_features – size of each input sample
# out_features – size of each output sample
# 
# ## Making sense of `nn.Linear`
# 
# #### In your Neural Network, the `self.hidden = nn.Linear(784, 256)` defines a _hidden_ (meaning that it is in between of the input and output layers), _fully connected linear layer_, which takes input `x` of shape `(batch_size, 784)`, where batch size is the number of inputs (each of size 784) which are passed to the network at once (as a single tensor), and transforms it by the linear equation `y = x*W^T + b` into a tensor `y` of shape `(batch_size, 256)`.
# 
# ------------------------

# # Create PyTorch DataLoader

# In[10]:


from torch.utils.data import DataLoader

train_dataloader = DataLoader(
    tokenized_dataset['train'], shuffle = True, batch_size = 32, collate_fn = data_collator
)

eval_dataloader = DataLoader(
    tokenized_dataset['valid'], shuffle = True, collate_fn = data_collator
)


# In[11]:


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_task_specific = MyTaskSpecificCustomModel(checkpoint=checkpoint, num_labels=2 ).to(device)


# In[12]:


from transformers import AdamW, get_linear_schedule_with_warmup

optimizer = AdamW(model_task_specific.parameters(), lr = 5e-5 )

num_epoch = 3

num_training_steps = num_epoch * len(train_dataloader)

# lr_scheduler = get_scheduler(
#     'linear',
#     optimizer = optimizer,
#     num_warmup_step = 0,
#     num_training_steps = num_training_steps,    
# )

lr_scheduler = get_linear_schedule_with_warmup(
    optimizer = optimizer,
    num_training_steps = num_training_steps,
    num_warmup_steps=0
)


# In[13]:


from datasets import load_metric
metric = load_metric("f1")


# # Training

# In[ ]:


from tqdm.auto import tqdm

progress_bar_train = tqdm(range(num_training_steps))
progress_bar_eval = tqdm(range(num_epoch * len(eval_dataloader) ))


for epoch in range(num_epoch):
    model_task_specific.train()
    for batch in train_dataloader:
        batch = { k: v.to(device) for k, v in batch.items() }
        outputs = model_task_specific(**batch)
        loss = outputs.loss
        loss.backward()
        
        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar_train.update(1)
        
    model_task_specific.eval()
    for batch in eval_dataloader:
        batch = { k: v.to(device) for k, v in batch.items() }
        with torch.no_grad():
            outputs = model_task_specific(**batch)
            
        logits = outputs.logits
        predictions = torch.argmax(logits, dim = -1 )
        metric.add_batch(predictions = predictions, references = batch['labels'] )
        progress_bar_eval.update(1)
        
    print(metric.compute()) 
       


# ## Post Training Evaluation

# In[ ]:


model_task_specific.eval()

test_dataloader = DataLoader(
    tokenized_dataset['test'], batch_size = 32, collate_fn = data_collator
)


for batch in test_dataloader:
    batch = { k: v.to(device) for k, v in batch.items() }
    with torch.no_grad():
        outputs = model_task_specific(**batch)
        
    logits = outputs.logits
    predictions = torch.argmax(logits, dim = -1)
    metric.add_batch(predictons = predictions, references=batch['labels'] )
    
metric.compute()  
    

