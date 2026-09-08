from app.services.resume_quality import analyze_resume_quality


resume = """
Rishab Singh

Education:
B.Tech Computer Science and Engineering

Skills:
Python
C++
TensorFlow
OpenCV
FastAPI

Projects:
Face Recognition System
Built a face recognition system using Python, OpenCV and TensorFlow.

Plant Disease Detection
Built a plant disease detection system using TensorFlow and Keras.
"""


result = analyze_resume_quality(resume)


print("Overall Score:", result.overall_score)

print("\nStructure:", result.structure_score)
print("Skills:", result.skills_score)
print("Projects:", result.projects_score)
print("Impact:", result.impact_score)
print("Completeness:", result.completeness_score)

print("\nStrengths:")
for item in result.strengths:
    print("-", item)

print("\nWeaknesses:")
for item in result.weaknesses:
    print("-", item)

print("\nRecommendations:")
for item in result.recommendations:
    print("-", item)