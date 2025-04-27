Course Generator App
====================

This project is a web-based application designed to generate a structured course outline based on user input. It leverages the power of OpenAI's GPT-4 to create a customized course outline, research lesson content, and generate detailed course material. The application is built using FastAPI and OpenAI's API for advanced natural language processing.

Features
--------

*   **Course Outline Generation**: Generate a structured course outline with modules and lessons based on a given topic, target audience, and course duration.
    
*   **Research Integration**: Use GPT-4 to fetch detailed information for each lesson, including key concepts, real-life examples, and online resources.
    
*   **Final Course Content**: Generate a fully detailed course, including lessons with explanations, analogies, interactive exercises, and resources.
    
*   **Easy API Endpoint**: The course generation process is accessible through a simple POST API endpoint for easy integration.
    

Prerequisites
-------------

*   Python 3.8+
    
*   Virtual environment (optional but recommended)
    
*   Required Python packages: FastAPI, OpenAI, Pydantic, dotenv
    

Installation
------------

1.  git clone cd
    
2.  python3 -m venv venvsource venv/bin/activate # On Windows use \`venv\\Scripts\\activate\`
    
3.  pip install -r requirements.txt
    
4.  OPENAI\_API\_KEY=your\_openai\_api\_key
    
5.  Make sure your OpenAI API key is valid and configured correctly. If the key is missing or incorrect, the app will throw an error.
    

API Usage
---------

### POST /generate\_course/

This endpoint accepts a JSON request with the following fields and returns a full course structure in JSON format.

#### Request Body:
```json
{
    "brief": "Introduction to Python Programming",
    "target_audience": "Beginner programmers",
    "course_duration": "4 weeks"
}
```    

#### Response Body:
```json
{
    "course": {
        "course_title": "Introduction to Python Programming",
        "description": "An engaging introduction to Python programming, designed for beginners.",
        "modules": [
            {
                "title": "Module 1: Basics of Python",
                "lessons": [
                    {
                        "title": "Lesson 1: Variables and Data Types",
                        "content": "In this lesson, we explore the basics of variables and data types in Python. You will learn how to work with strings, integers, and floats.",
                        "analogy": "Think of variables as containers where you store your data, like a box that holds different items.",
                        "interactive_exercise": "Create a Python script that defines variables for your age, name, and favorite color.",
                        "resources": [
                            "https://www.python.org/doc/",
                            "https://realpython.com/python-data-types/"
                        ]
                    },
                    {
                        "title": "Lesson 2: Control Flow",
                        "content": "Learn about conditional statements and loops in Python. You'll explore how to control the flow of your programs using if, elif, and else statements.",
                        "analogy": "Imagine you're at a fork in the road. The condition is like deciding which road to take based on the weather.",
                        "interactive_exercise": "Write a Python script that checks if a number is even or odd.",
                        "resources": [
                            "https://docs.python.org/3/tutorial/controlflow.html",
                            "https://realpython.com/python-conditional-statements/"
                        ]
                    }
                ]
            },
            ...
        ]
    }
}
```

Running the Application
-----------------------

To run the application locally, execute the following command:
```bash
uvicorn main:app --reload
```
This will start the server, and you can interact with the API at http://127.0.0.1:8000.

Error Handling
--------------

The application includes error handling to ensure smooth operation:

*   **Missing API Key**: If the OpenAI API key is missing from the .env file, the app will raise a ValueError.
    
*   **Invalid Response from GPT**: If there is an issue with the response format from OpenAI, the app will raise an HTTPException with a 500 status code.
    

Development Notes
-----------------

*   This app uses FastAPI to serve the API and Pydantic models for request validation.
    
*   OpenAI's GPT-4 is utilized to generate course outlines, lesson plans, and detailed content for each lesson.
    
*   Make sure your OpenAI API key has sufficient quota for the tasks this app performs.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
