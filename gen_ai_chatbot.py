#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, render_template


# In[4]:


from gen_ai import get_llm


# In[ ]:


pdf_path = r"data"


# In[5]:


chatbot=get_llm(pdf_path)


# In[6]:


app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
        
@app.route("/get_answer", methods=["POST"])
def get_answer():
    question =request.form['question']

    response=chatbot.invoke({
        'query':question
    })

    return jsonify({
        "answer": response['result']
    })


if __name__=="__main__":
    app.run(debug=False)


# In[ ]:




