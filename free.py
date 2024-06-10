import random
import string

def generate_similar_links(num_links):
    base_url = "https://t.me/giftcode/"
    links = []
    
    for _ in range(num_links):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        links.append(base_url + code)
    
    return links

# Generate 5 similar links
similar_links = generate_similar_links(5)
for link in similar_links:
    print(link)
