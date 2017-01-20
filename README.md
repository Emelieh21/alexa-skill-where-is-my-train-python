# where-is-my-train

An Alexa skill build in Python that tells you when your next train is leaving. This skill is made with the [schiene] python library and also uses BeautifulSoup. 

Inspired by [this Alexa python skill] - the Alexa BART skill.

To make a skill in Alexa you need an Alexa developer account and an aws account, if this is the first time you are making an Alexa skill, [this tutorial] will be a great help.

[schiene]: https://github.com/kennell/schiene
[this Alexa python skill]: https://github.com/simonprickett/alexabart
[this tutorial]: https://github.com/alexa/skill-sample-nodejs-fact

## Step-by-step

1. Go to your developer.amazon.com account, click on the Alexa tab and then on "Get Started" in the Alexa Skills Kit box.

2. Click on add a new skill, fill in the skill information and click "Next".

3. In the `Interaction Model` - add the intent_schema, the **two** custom slot types (LIST_OF_STATIONS_ONE and LIST_OF_STATIONS_TWO) and the example_utterances.

![interaction-model](https://github.com/Emelieh21/where-is-my-train/blob/master/screenshots/interaction-model.png) 

4. If you are planning to use a Lambda function from aws, now is the time to make it. Go to aws.amazon.com, and look for Lambda. Click on `Create a Lambda Function`, select `Blank Function` and continue. Do not forget to configure the trigger! Click on the "clickable" blank box and select "Alexa Skills Kit". 

![configure trigger](https://github.com/Emelieh21/where-is-my-train/blob/master/screenshots/configure_triggers.png) 

In the next section you can give the function a name, description and select "Python 2.7" in the runtime. Do not forget to set a role - `Create a custom role` will do. The rest we can leave it as it is and click "Next". Click "Create Function".

5. For this specific skill to work, we need to upload some Python libraries with the lambda Function. This is actually very easy. Gather the folders of the Python libraries together with the lambda_function.py file and zip everything together:

![adding python libraries](https://github.com/Emelieh21/where-is-my-train/blob/master/screenshots/adding_python_libraries.png) 

6. Now we can upload the zip file to the lambda function:

![upload zip file](https://github.com/Emelieh21/where-is-my-train/blob/master/screenshots/upload_zip_file.png) 

7. Copy the ARN of your lambda function (in the right upper corner, looks somehthing like "ARN - arn:aws:lambda:eu-west-1:XXXXX:function:XXXX"). 

8. Now it is time to go back to the Alexa Skill in the developer account. In the `Configuration` - set the endpoint to "AWS Lambda ARN ...", choose your region and paste the `ARN - arn:aws:lambda:eu-west-1:...` from your lambda function in there. Click "Next".

9. And voila, now you can test your new python skill!


