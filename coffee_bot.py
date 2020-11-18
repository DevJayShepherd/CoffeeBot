# Define your functions
def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a " + size + drink_type + "!")
  customer_name = input("Can I get your name please?\n")
  print("Thanks, " + customer_name + "! Your drink will be ready shortly.")

# Get user size
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'Small '
  elif res == 'b':
    return 'Medium '
  elif res == 'c':
    return 'Large '
  else:
    print_message()
    return get_size()

# function for unknown response
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.");

# get user drink type
def get_drink_type():
  res = input("""What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte \n""")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
    
  else:
    print_message()
    return get_drink_type();

# follow up fucntion 
def order_latte():
  res = (input("""And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk
   \n"""));
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte();

coffee_bot();

