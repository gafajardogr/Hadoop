from starbase import Connection

c = Connection("127.0.0.1", "8000")

ratings = c.table('ratings')

print ("Get back ratings for some users...\n")
print ("Ratings for user ID 6:\n")
print (ratings.fetch("6"))
print ("Ratings for user ID 30:\n")
print (ratings.fetch("30"))

