from collections import Counter

likes_data = [10, 20, 15, 10, 25, 20, 15, 30, 10, 25, 25, 15, 20]

likes_distribution = Counter(likes_data)

print("Likes Frequency Distribution:")
for likes, frequency in likes_distribution.items():
    print(f"Likes: {likes}, Frequency: {frequency}")
