import pandas as pd


# This is the Original Dataframe
df = pd.DataFrame(columns=['name', 'id number'])


# These are all the Function in the Main Function
def createContact():
  global df
  while True:
    try:
      name = input('Name of Contact: ')
      id = int(input('ID Number of Contact: '))
    except ValueError:
      print("Invalid, Please enter Valid Number")
      continue

    df = df._append({'name': name, 'id number': id}, ignore_index=True)
    print(df)
    break


def deleteContact():
  global df

  if df.empty:
    print('You have no Contacts')
    return
  else:
    print(df)

  while True:
    try:
      remove = int(input('Which contact would you like to remove?(Integer Value Only): '))
    except ValueError:
      print("Invalid, Please enter Valid Number")
      continue

    df = df.drop(remove)
    if df.empty:
      print('You have no more contacts')
    else:
      print(df)
    break


def updateContact():
  global df

  if df.empty:
    print('You have no contacts to update')
  else:
    print(df)
    while True:
      try:
        update = int(input('Which contact would you like to update?(Integer Value Only): '))
        info = input('What would you like to update?(Name/ID Number): ').lower()
        change = input('What would you like to change to? ')
      except ValueError:
        print("Invalid, Please enter Valid Number")
        continue

      if info != 'name' or 'id number':
        print('Invalid')
      else:
        df.at[update, info] = change
        print(df)
      break


def findContact():
  global df

  if df.empty:
    print('You have no contacts to look at')
  else:
    print('Here is your Contact List: ')
    print(df)


# This is the Main Function
def main():
  choice = None
  while choice != 5:
    welcome = '''
Welcome to the Contact Book Application

  1. Look at Contacts
  2. Create a Contact
  3. Update a Contact
  4. Delete a Contact
  5. Leave Application
    '''
    print(welcome)
    choice = (input('What would you like to do?(1/2/3/4/5): '))

    if choice == '1':
      findContact()
    elif choice == '2':
      createContact()
    elif choice == '3':
      updateContact()
    elif choice == '4':
      deleteContact()
    elif choice == '5':
      break
    else:
      print('Invalid')

    cont = input('Would you like to continue?(y/n): ')
    if cont == 'n':
      break
    elif cont == 'y':
      continue
    else:
        print('Invalid')

if __name__ == '__main__':
  main()