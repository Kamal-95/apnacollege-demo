# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
#
#     def describe(self):
#         print("name=", self.name , "species=", self.species)
#
# a1 = Animal("rabbit","Animal")
# a2 = Animal("bat", "bird")
#
# a1.describe()
# a2.describe()
import time

# class Animal:
#     def speak(self):
#         print("ANIMAL SPEAK")
#     def nose(self):
#         print("animal nose")
#
# class Dog(Animal):
#     def speak(self):
#         print("DOg bark")
#     def nose(self):
#         print("dog nose")
#
# class Cat(Animal):
#     def speak(self):
#         print("Cat meaow")
#     def nose(self):
#         print("cat nose")
#
# a1 = Animal()
# d1 = Dog()
# c1 = Cat()
#
# a1.speak()
# a1.nose()
# d1.speak()
# d1.nose()
# c1.speak()
# c1.nose()



#
# string = "Kamal"
# char_count = {}
#
# for char in string:
#     if char in char_count:
#         char_count[char] +=1
#     else:
#         char_count[char]=1
#
# for char,count in char_count.items():
#     print("character",char, "occurs",count ,"times")


# def count_characters(input_string):
#     # Initialize an empty string to store the result
#     result = ""
#
#     # Initialize a variable to keep track of the current character
#     count = 1
#
#     # Loop through the string, except the last character
#     for i in range(1, len(input_string)):
#         if input_string[i] == input_string[i - 1]:
#             # If the current character is the same as the previous one, increment count
#             count += 1
#         else:
#             # Otherwise, append the character and its count to the result
#             result += input_string[i - 1] + str(count)
#             count = 1  # Reset the count for the new character
#
#     # Add the last character and its count
#     result += input_string[-1] + str(count)
#
#     return result
#
#
# # Test the function
# input_string = "aabbbcccc"
# output_string = count_characters(input_string)
# print(output_string)


# input = "aabbbcccc"   output = "a2b3c4"
#
# def char_count(input_string):
#     count=1
#     result=""
#     for i in range(1,len(input_string)):
#         if input_string[i] == input_string[i-1]:
#             count= count + 1
#
#
#         else:
#             result = result + input_string[i-1] + str(count)
#             count =1
#
#     result = result + input_string[-1] + str(count)
#     return result
#
# output = char_count("aabbbcccc")
# print(output)


# tu = [5,54,7,8,8,43.5]
# print(tu.count(8))


# dict = {
#     "name":"kamal","age": "25","city":"Delhi"
# }
# dict["country"]="India"
# print(dict["age"])




from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.XPATH, '//a[text()="JavaScript Alerts"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href="/upload"]').click()
element = driver.find_element(By.XPATH, '//input[@name="file"]')
element.send_keys('C:\\Users\\Vaibhav\\Desktop\\bugreport.txt')
driver.find_element(By.CLASS_NAME, 'button').click()
# driver.find_element(By.XPATH, '//a[text()="JavaScript Alerts"]').click()
# driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]').click()
# alert = Alert(driver)
# print(alert.text)
# alert.accept()
# alert.dismiss()
# action = ActionChains(driver)
# action.send_keys(Keys.ENTER).perform()
# element = driver.find_element(By.CLASS_NAME, "lnXdpd")
# action = ActionChains(driver)
# action.click(element).perform()
# search_button = driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@aria-label="Google Search"]')
# action.click(search_button).perform()
time.sleep(5)
































