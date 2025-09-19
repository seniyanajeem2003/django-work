from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def result(request, student_name):
    
    results = {
       "Seniya Najeem": {
            "grade": "A+",
            "marks": {"Math": 95, "Science": 92, "English": 90},
            "remarks": "Seniya Najeem is Passed."
        },
        "Amaya Raj": {
            "grade": "A+",
            "marks": {"Math": 92, "Science": 95, "English": 93},
            "remarks": "Amaya Raj is Passed."
        },
        "Karthika Indrajith": {
            "grade": "A+",
            "marks": {"Math": 95, "Science": 90, "English": 94},
            "remarks": "Karthika Indrajith is Passed."
        }
    }

    student_data = results.get(student_name)

    return render(request, 'result.html', {
        'student_name': student_name,
        'grade': student_data["grade"],
        'marks': student_data["marks"],
        'remarks': student_data["remarks"]
    })