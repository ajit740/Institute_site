from django.http import JsonResponse

def chatbot_response(request):
    user_message = request.GET.get('message', '').lower().strip()

    main_menu_suggestions = [
        "What courses do you offer?",
        "How to register?",
        "What are the fees?",
        "Where is your institute located?",
        "Contact me"
    ]

    keyword_map = {
        ("courses", "course", "offerings"): {
            "response": "We offer courses in AI, Full Stack Development, Web Development, and Data Science.",
            "suggestions": [
                "How to register?",
                "What are the fees?",
                "Who are the trainers?"
            ]
        },
        ("admission", "apply", "admissions", "enrollment", "register"): {
            "response": "Admissions are currently open. You can apply through our Admissions page on the website.",
            "suggestions": [
                "What are the fees?",
                "How to register?",
                "What are class timings?"
            ]
        },
        ("fees", "cost", "price", "charges"): {
            "response": "Course fees vary: AI Bootcamp is ₹25,000, Full Stack Development is ₹20,000.",
            "suggestions": [
                "Are there any discounts?",
                "What are the payment methods?",
                "How to register?"
            ]
        },
        ("timing", "class timing", "schedule", "class hours", "timings"): {
            "response": "Classes are held from 10 AM to 6 PM, Monday to Friday.",
            "suggestions": [
                "Where is your institute located?",
                "What courses do you offer?",
                "How to contact you?"
            ]
        },
        ("location", "address", "where are you", "campus"): {
            "response": "We are located at MG Road, New Delhi.",
            "suggestions": [
                "What are the class timings?",
                "How to contact you?"
            ]
        },
        ("contact", "phone", "email", "call", "contact me"): {
            "response": "You can contact us at 📞 +91-9876543210 or 📧 info@thinkodex.in.",
            "suggestions": [
                "Where is your institute located?",
                "What are the class timings?"
            ]
        },
        ("certificate", "certification", "certificate"): {
            "response": "Yes, we provide certificates upon successful course completion.",
            "suggestions": [
                "Do you offer placement?",
                "What courses do you offer?"
            ]
        },
        ("placement", "job", "career", "after course"): {
            "response": "We offer placement assistance including mock interviews and resume building support.",
            "suggestions": [
                "Read student success stories",
                "What courses do you offer?"
            ]
        },
        ("workshops", "events", "seminar", "bootcamp"): {
            "response": "Upcoming workshops include AI in Education, Django Bootcamp, and Web3 101.",
            "suggestions": [
                "How to register?",
                "What courses do you offer?"
            ]
        },
        ("trainers", "faculty", "teachers", "instructors"): {
            "response": "Our trainers come from top companies and IIT backgrounds.",
            "suggestions": [
                "What courses do you offer?",
                "How to register?"
            ]
        },
        ("registration", "register", "enroll", "how to register", "sign up"): {
            "response": "To register, visit the course page and click 'Enroll Now'. For assistance, contact us!",
            "suggestions": [
                "What are the fees?",
                "Admissions process",
                "How to contact you?"
            ]
        },
        ("success stories", "alumni", "placements", "results"): {
            "response": "Our students have been placed in Amazon, Flipkart, Infosys. Visit our blog to read their stories.",
            "suggestions": [
                "Do you offer placement?",
                "What courses do you offer?"
            ]
        },
        ("discount", "scholarship", "offer"): {
            "response": "We offer early bird discounts and scholarships based on merit. Check our website for current offers.",
            "suggestions": [
                "What are the fees?",
                "How to register?"
            ]
        },
    }

    if not user_message:
        return JsonResponse({
            "response": "Hello! How can I assist you today? Here are some topics to start with:",
            "suggestions": main_menu_suggestions
        })

    for keywords, data in keyword_map.items():
        if any(k in user_message for k in keywords):
            return JsonResponse({
                "response": data["response"],
                "suggestions": data["suggestions"]
            })

    return JsonResponse({
        "response": "Sorry, I didn't understand that. Please choose from the options below or ask about courses, admission, fees, timings, location, etc.",
        "suggestions": main_menu_suggestions
    })
