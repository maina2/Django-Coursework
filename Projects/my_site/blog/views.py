from django.shortcuts import render


all_posts = [
    {
        "slug": "mountain-hiking",
        "image": "picture4.jpg",
        "author": "John Doe",
        "date": "2024-11-21",
        "title": "Mountain Hiking Adventures",
        "excerpt": "Discover the beauty of hiking through breathtaking mountain trails.",
        "content": "Mountain hiking offers a unique experience to connect with nature. The fresh air, challenging climbs, and stunning views make it a favorite activity for adventurers. Always ensure to pack the essentials and check the weather before heading out."
    },
    {
        "slug": "city-night-life",
        "image": "picture6.jpg",
        "author": "Jane Smith",
        "date": "2024-11-20",
        "title": "Exploring City Nightlife",
        "excerpt": "The city comes alive at night with lights, music, and endless entertainment.",
        "content": "From rooftop bars to late-night street food markets, the city's nightlife has something for everyone. Whether you prefer dancing the night away or enjoying a quiet drink with friends, there's no shortage of options."
    },
    {
        "slug": "beach-getaway",
        "image": "picture3.jpg",
        "author": "Alice Johnson",
        "date": "2024-11-19",
        "title": "A Perfect Beach Getaway",
        "excerpt": "Relax and unwind with a perfect day at the beach.",
        "content": "Beaches offer a serene escape from the hustle of daily life. Whether you want to sunbathe, swim, or build sandcastles, a day at the beach is always refreshing. Don't forget your sunscreen!"
    },
    {
        "slug": "tech-trends-2024",
        "image": "picture1.jpg",
        "author": "Mark Brown",
        "date": "2024-11-18",
        "title": "Top Tech Trends for 2024",
        "excerpt": "Stay ahead of the curve with these top tech trends for the coming year.",
        "content": "Artificial intelligence, quantum computing, and 5G technology are just some of the innovations shaping our future. These advancements promise to revolutionize industries and improve everyday life."
    },
    {
        "slug": "culinary-delights",
        "image": "picture5.jpg",
        "author": "Emily Davis",
        "date": "2024-11-17",
        "title": "Exploring Culinary Delights",
        "excerpt": "Embark on a journey through the world's most delicious cuisines.",
        "content": "Food is not just sustenance; it's an art form. From traditional dishes to modern fusion creations, exploring new cuisines can be an adventure for your taste buds."
    },
    {
        "slug": "Night-travels",
        "image": "picture7.jpg",
        "author": "Emily Davis",
        "date": "2024-10-17",
        "title": "Night travellings",
        "excerpt": "Embark on a journey through the world's most delicious cuisines.",
        "content": "Food is not just sustenance; it's an art form. From traditional dishes to modern fusion creations, exploring new cuisines can be an adventure for your taste buds."
    }
]

def get_date(posts):
    return posts['date']



def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts_list" : latest_posts
    })

def posts(request):


    return render(request,"blog/all-posts.html",{
        "whole_list" : all_posts
    })


def post_detail(request, slug):
    # Assuming all_posts is a list of dictionaries with a "slug" key
    for details in all_posts:
        if details['slug'] == slug:  # Check if the slug matches
            return render(request, "blog/post-detail.html", {
                "post": details
            })

    # If no matching post is found, return a 404 page
    return render(request, "404.html", {"message": "Page not found"})

