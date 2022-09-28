print("\nLoop through a simple list:")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\nCompose a message for each item:")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("\nCompose two messages for each item:")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("\nSummarize the operation:")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone.  That was a great magic show!\n")
