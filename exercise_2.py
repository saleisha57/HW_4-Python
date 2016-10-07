strings = ['North Dakota','New York','Washington','Maine']
print [x.upper() if len(x) <= 5 else x.lower() for x in strings]  

