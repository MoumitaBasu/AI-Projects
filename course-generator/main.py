import json, os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env file!")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)
app = FastAPI()

# Request Model
class CourseRequest(BaseModel):
    brief: str
    target_audience: str
    course_duration: str

async def generate_course_structure(brief, audience, duration):
    """Generates course structure with module and lesson titles."""
    system_prompt = f"""
    You are an expert educational AI creating a structured course outline.
    - Design a course based on the following:
      - **Topic**: {brief}
      - **Target Audience**: {audience}
      - **Duration**: {duration}
    - DO NOT write full content. Only return:
      - Course Title
      - 5-6 Modules
      - 2 Lessons per module (just titles)
    - Example format:
    {{
      "course_title": "Your Course Title",
      "modules": [
        {{
          "title": "Module 1 Title",
          "lessons": [
            {{"title": "Lesson 1 Title"}},
            {{"title": "Lesson 2 Title"}}
          ]
        }},
        ...
      ]
    }}
    """

    print("🔹 Generating Course Structure...")
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.5,
        max_tokens=1000
    )

    # ✅ Extract and parse response
    generated_text = response.choices[0].message.content
    print("✅ Raw GPT Response:", generated_text)

    try:
        structure = json.loads(generated_text)
        return structure
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error parsing OpenAI response as JSON")

async def research_lessons(modules):
    """Uses GPT-4 to find detailed research information for each lesson."""
    research_results = {}

    for module in modules:
        for lesson in module["lessons"]:
            prompt = f"""
            Research the topic: "{lesson['title']}" in detail.
            - Explain the key concepts, historical background, and real-world applications.
            - Mention key studies, organizations, or experts related to this topic.
            - Provide case studies or real-life examples where applicable.
            - List useful online resources (e.g., government reports, academic papers, industry sources).
            - The response should be detailed and structured in multiple paragraphs.
            """

            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "system", "content": prompt}],
                temperature=0.5,
                max_tokens=500
            )

            research_results[lesson["title"]] = response.choices[0].message.content.strip()

    return research_results

async def generate_final_course(structure, research_data):
    """Generates the full course content using GPT-4 Turbo."""
    system_prompt = f"""
    You are an expert course creator. Use real research to generate detailed, engaging content.
    - Each lesson should contain:
      - A detailed explanation based on real research
      - A real-life example or analogy
      - An interactive exercise
      - 2-3 resources (from research data)
    - Format:
    {{
      "course_title": "{structure['course_title']}",
      "description": "An engaging introduction to the topic.",
      "modules": [
        {{
          "title": "Module 1",
          "lessons": [
            {{
              "title": "Lesson 1",
              "content": "...",
              "analogy": "...",
              "interactive_exercise": "...",
              "analogy": "Think of this summary as a map that highlights the most important stops in your learning journey.",
              "interactive_exercise": "Write a short reflection on how the topic can impact your local community.",
              "resources": ["Resource 1", "Resource 2"]
            }},
            ...
            "title": "Summary of Key Concepts",
            "content": "This lesson summarizes the key concepts covered in the course, including the definition and importance of the topic, key players in the industry, and its impact on global issues.",
              
          ]
        }}
      ]
    }}
    """
    print("🔹 Generating Final Course...")
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": str(research_data)}
        ],
        temperature=0.7,
        max_tokens=4096
    )

    return response.choices[0].message.content

@app.post("/generate_course/")
async def generate_course_endpoint(request: CourseRequest):
    try:
        print("🔹 Generating Course Structure...")
        structure = await generate_course_structure(request.brief, request.target_audience, request.course_duration)
        print("✅ Structure Generated:", structure)

        print("🔹 Researching Lesson Titles...")
        research_data = await research_lessons(structure["modules"])
        print("✅ Research Data Fetched:", research_data)

        print("🔹 Generating Final Course with Real Research...")
        final_course = await generate_final_course(structure, research_data)
        print("✅ Final Course Ready!")

        # ✅ Parse the returned string into a JSON object
        final_course_json = json.loads(final_course)

        return {"course": final_course_json}  # Return as a valid JSON object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))