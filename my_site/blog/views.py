from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "page_title": "kareri-lake",
        "image": "mountains.jpg",
        "author": "Andip Chauhan",
        "date": date(2023, 7, 1),
        "title": "Kareri Lake Trek",
        "excerpt": "A beautiful trek to Kareri Lake, located near Dharamshala in Himachal Pradesh, India. The trek offers stunning views of the Dhauladhar mountain range and lush green forests.",
        "content": """The Kareri Lake trek is a popular trekking route in Himachal Pradesh, India.
        It is known for its scenic beauty, lush green forests, and the serene Kareri Lake.
        The trek usually starts from McLeod Ganj and takes you through beautiful landscapes, offering breathtaking views of the Dhauladhar mountain range.
        The best time to visit is during the summer months when the weather is pleasant and the lake is surrounded by blooming flowers."""
    },
    {
    "page_title": "forest-retreat",
    "image": "woods.jpg",
    "author": "Andip Chauhan",
    "date": date(2023, 8, 15),
    "title": "Forest Retreat in Himachal",
    "excerpt": "An immersive journey into the tranquil woods of Himachal Pradesh. This retreat offers peace, solitude, and a deep connection with nature.",
    "content": """The forest retreat in Himachal Pradesh is perfect for those seeking serenity away from the hustle of city life. 
    Nestled among towering pine trees and misty trails, the experience includes guided nature walks, meditation sessions, and cozy forest cabins.
    The best time to visit is during early autumn when the foliage turns golden and the air is crisp."""
    },
    {
    "page_title": "coding-escape",
    "image": "coding.jpg",
    "author": "Andip Chauhan",
    "date": date(2023, 9, 5),
    "title": "Coding Escape: A Digital Retreat",
    "excerpt": "A unique getaway for tech enthusiasts to code, collaborate, and unwind in a creative environment. Perfect for developers and digital nomads.",
    "content": """The Coding Escape is a retreat designed for programmers and tech creatives. 
    Set in a quiet location with high-speed internet and inspiring workspaces, it blends productivity with relaxation. 
    Participants engage in hackathons, workshops, and fireside tech talks. 
    Ideal during monsoon season when the cozy indoor vibe enhances focus and creativity."""
    }
]

def get_date(post):
    # return post.get('date')
    return post['date']

# Create your views here.
def index(request):
    # sorted_posts = all_posts.sort(key=get_date)   # not using because it modifies the original list
    
    sorted_posts = sorted(all_posts, key=lambda x: x['date'])
    latest_posts = sorted_posts[-3:]  # Get the latest(at last of array) three posts for the index page
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html',{
        "all_posts": all_posts
    })

def post_detail(request, post_title):
    target_post = next(post for post in all_posts if post['page_title'] == post_title)  
    return render(request, 'blog/post-detail.html',{
        "post": target_post
    })