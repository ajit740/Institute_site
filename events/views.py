from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

# Hardcoded events list (should be the same as in events_view)
events = [
    {
        'id': 1,
        'title': 'Cyber Security Awareness',
        'date': '2025-06-01',
        'description': 'Learn the latest in protecting your digital identity, cyber threats, and best security practices.',
        'image': '/static/images/cyber_security.jpg',
    },
    {
        'id': 2,
        'title': 'AI Workshop: Fundamentals & Applications',
        'date': '2025-06-01',
        'description': 'Hands-on workshop on AI concepts, tools, and how AI is transforming industries.',
        'image': '/static/images/ai_workshop.jpg',
    },
    {
        'id': 3,
        'title': 'Data Science Bootcamp',
        'date': '2025-06-15',
        'description': 'Intensive training on data analytics, visualization, and predictive modeling.',
        'image': '/static/images/data_science.jpg',
    },
    {
        'id': 4,
        'title': 'Full Stack Development Seminar',
        'date': '2025-07-05',
        'description': 'Explore modern web development technologies and build your portfolio projects.',
        'image': '/static/images/full_stack.jpg',
    },
]

def events_view(request):
    return render(request, 'events/event_list.html', {'events': events})

def event_register(request, event_id):
    # Find event by id in the hardcoded list
    event = next((e for e in events if e['id'] == event_id), None)
    if event is None:
        raise Http404("Event not found")

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Here you can save registration info or send email, currently just success message
        messages.success(request, f"Thanks {name}, you have successfully registered for {event['title']}!")
        return redirect('events:event_list')

    return render(request, 'events/event_register.html', {'event': event})

from django.shortcuts import render

def news_detail(request, news_id):
    dummy_data = {
        1: {
            "title": "Thinkodex Launch Event",
            "content": """
We are thrilled to announce the grand launch of Thinkodex – a cutting-edge learning platform designed to transform the way students and professionals approach technology education.

The launch event was held at our state-of-the-art campus, bringing together industry leaders, enthusiastic learners, and top-tier educators. The event featured live tech demos, keynote speeches from AI pioneers, and interactive booths showcasing upcoming courses in AI, Full Stack Development, Cybersecurity, and more.

A highlight of the evening was the keynote speech by Mrs. Mitali Muraledharan, a veteran in the Indian tech industry, who emphasized the importance of practical learning and innovation in shaping the workforce of tomorrow. We also hosted a panel discussion with alumni and trainers on the impact of project-based learning in real-world careers.

Guests had the opportunity to network, explore the Thinkodex learning portal, and enroll in our flagship AI Bootcamp. With over 200 attendees and positive feedback pouring in, the launch marked a successful beginning to our journey in redefining tech education.

Stay tuned for upcoming events, workshops, and community initiatives that aim to bridge the gap between learning and industry demand.
""",
            "image": "images/news1.png"
        },

        2: {
            "title": "New AI Workshop",
            "content": """
Our latest AI Workshop was an intensive, hands-on experience designed to equip learners with practical skills in Artificial Intelligence and Machine Learning. Held over three days, the workshop attracted tech enthusiasts, college students, and working professionals eager to explore real-world applications of AI.

The workshop covered essential topics including data preprocessing, supervised and unsupervised learning, neural networks, and deep learning using Python. A special session on Natural Language Processing (NLP) introduced participants to sentiment analysis and chatbot development with tools like NLTK, Scikit-learn, and BERT.

What made this workshop stand out was its project-based approach. Each participant developed a mini-project — from movie recommendation engines to real-time fake news detectors — guided by our expert mentors.

The guest speaker, Mr. Ajit Rawat, an AI Master trainer at Nasscom Foundation, inspired the attendees with a talk on AI in healthcare and ethics in machine learning.

Participants received certificates, project feedback, and exclusive access to Thinkodex's AI learning resources. With overwhelmingly positive reviews and demand for more, we're excited to launch an advanced AI track in the coming months.
""",
            "image": "images/ds_workshop.jpg"
        },

        3: {
            "title": "Student Success Stories",
            "content": """
At Thinkodex, we are proud to celebrate the achievements of our students who have turned their aspirations into success stories through dedication and skill.

One of our shining stars, **Neelam Yadav**, enrolled in our Full Stack Development program during her second year of college. With zero coding background, she quickly picked up front-end and back-end skills. Her final project, a fully functional job portal, was selected for a state-level tech fair. Today, she works as a Software Engineer at **Infosys**, mentoring junior developers and sharing her journey with the Thinkodex community.

Another remarkable story is Milind Negi, who joined our AI Bootcamp with a keen interest in machine learning. He built a fraud detection model using decision trees and neural networks, which he later showcased in a campus hiring drive. He is now working as a Data Analyst at **TCS**, where he contributes to high-impact projects and regularly conducts AI awareness sessions in colleges.

Then there’s **Ekta Sharma**, who came from a teaching background with minimal technical exposure. After completing our Web Development track, she landed a remote internship with a tech startup. Her curiosity, discipline, and design skills helped her grow rapidly, and she now leads the front-end development team at the same company.

These success stories are not just individual achievements—they reflect our commitment to transforming lives through quality education, mentorship, and hands-on experience.

We’re excited to continue nurturing more such journeys. If you're ready to start yours, Thinkodex is the place to be!
""",
            "image": "images/news3.jpg"
        }
    }

    news = dummy_data.get(news_id)
    if not news:
        return render(request, "404.html")  # Or use: raise Http404("News not found")
    return render(request, "events/news_detail.html", {"news": news})
