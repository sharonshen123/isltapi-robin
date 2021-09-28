This API uses Python, Flask, Heroku 
The API will reture json object for flashcard app

Steps:
Create Heroku account
Deploy code to Heroku:
$heroku create isltapi
$git push heroku master

Python versions that are supported by heroku
python-3.9.7 on all supported stacks
python-3.8.12 on all supported stacks
python-3.7.12 on all supported stacks
python-3.6.15 on all supported stacks

api url: https://isltapi.herokuapp.com/?amount=1&category=1

The json object should like https://opentdb.com/api.php/?amount=2&category=10

{
    "response_code":0,
    "results":
    [
        {
            "category":"Entertainment: Books",
            "type":"multiple",
            "difficulty":"medium",
            "question":"What is the make and model of the tour vehicles in &quot;Jurassic Park&quot; (1990)?",
            "correct_answer":"1989 Toyota Land Cruiser",
            "incorrect_answers":["1989 Jeep Wrangler YJ Sahar","1989 Ford Explorer XLT","Mercedes M-Class"]
        },

        {
            "category":"Entertainment: Books",
            "type":"multiple",
            "difficulty":"hard",
            "question":"Which author co-wrote &quot;The Communist Manifesto&quot; alongside Karl Marx?",
            "correct_answer":"Friedrich Engels",
            "incorrect_answers":["Robert Owen","Alexander Kerensky","Paul Lafargue"]
        }
        
    ]
}
