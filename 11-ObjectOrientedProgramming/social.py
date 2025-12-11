class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"\nTimeline for user: {self.username}")
        print("----------------------------")

        number = 1
        for post in self.posts:
            print(f"{number}. {post}")
            number += 1

        print()


def main():
    user = SocialMediaProfile("jhondoe")

    user.add_post("Hello, world!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")

    user.display_timeline()


if __name__ == "__main__":
    main()
