#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
# from keras.models import load_model
import joblib

@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        Income = request.form.get("Income")
        model_selection = request.form.get("model")
        print(Age, Loan, Income, model_selection)
        if model_selection == 'Log Regression':
            model = joblib.load("logReg")
            
        elif model_selection == 'Decision Tree':
            model = joblib.load("decTree")
            
        elif model_selection == 'Random Forest':
            model = joblib.load("ranForest")
            
        elif model_selection == 'XGBoost':
            model = joblib.load("XGBoost")
            
        # elif model_selection == 'Neural Network':
        #     model = load_model("neuralNetwork")
        
        pred = model.predict([[float(Income), float(Age), float(Loan)]])
        if pred == [0]:
            pred = 'No'
        if pred == [1]:
            pred = 'Yes'
        s = "The predicted default is : " + pred
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Let's Get it!"))        


# In[ ]:

if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




