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

4. If you are planning to use a Lambda function from aws, now is the time to make it. Go to aws.amazon.com, and look for Lambda. Click on `Create a Lambda Function`, select `Blank Function` and continue. Do not forget to configure the trigger! Click on the "clickable" blank box and select "Alexa Skills Kit". 

![configure trigger](https://github.com/Emelieh21/where-is-my-train/blob/master/screenshots/configure_triggers.png) 

In the next section you can give the function a name, description and select "Python 2.7" in the runtime. Do not forget to set a role - `Create a custom role` will do. The rest we can leave it as it is and click "Next". Click "Create Function".



6. In the `Configuration` - set the endpoint. If you use a Lambda function add
