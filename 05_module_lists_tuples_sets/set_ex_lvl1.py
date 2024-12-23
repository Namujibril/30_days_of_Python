# sets exercises
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
length_it_companies = (len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Instagram', 'Snapchat'])

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')

### What is the difference between remove and discard?

# remove() will raise an error if the element does not exist in the set

# discard() will not raise an error if the element does not exist in the set
