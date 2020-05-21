# Ironhack-Final-Project
Final project for Ironhack bootcamp

**_If you like think about writting the shopping list and what to cook every single week, don't read on_**

# LaComprApp
![alt text](INPUT/imagen.png)

From now on your only worries should be answer some questions and let "LaComprApp" do its job.

### RESUME👨🏻‍💻

The main objective of the project was to develop the structure of a future app that would allow anyone to, only by answering some preferences, have the shopping list and the menu´s recipes of the week done.

  **1.- Answer some questions 🙎🏾‍♀️**
  
    ☞ ⏰ Time of cooking
    
    ☞ ㎉ Kcal of your wished menu
    
    ☞ 🥗 Would you like a veggie menu?
    
    ☞ 🤢 Any ingredient you do not like?
      
  **2.- Based on your answers, the app will create a personalized menu 👨🏻‍🍳**
  
    ☞ 🗓 Here you got the menu
 
  **3.- Some more questions, sorry 🙏**
  
    ☞ Would you like to change some dish?
  
 **4.- Well done, we have created your personalized menu and you shopping list to cook them with its quantities** 👍
  
    ☞ 🥗 📝 Here you got
 
  
### WORK PROCESS 💻 ⚙️

You can find the code I wrote in SRC folder. The file "genera_menu.py"  is the one that runs the code based in the all the others .py files.

From a recipe´s CSV that I had to clean (now located in Input), I have developed a data base in Mongodb from which all the work started. I had to create an user collection as well as a valoration one in Mongodb and after that I made two recommender systems. 
First one filters the recipes returned by user´s answers, after that it makes another filtering by the quantity of each ingridient taking those which the user does not like into account; the second one filters those previusly processed recipes by the valoration of your closest user.

The second part of the project was to generate a shopping list by standardizing all recipes´ ingredients to grams and adding those contained in more than one recipe.

You can also modife de data base by adding users or valorations (SRC files), so it all is dynamic. 

Here you can find the tools I used: 

  - Python 3 (pandas, numpy, request, sklearn, etc)
  - Mongodb 
  - Visual Studio Code


PS: I made the project in spanish because the recipes´ CSV was of spanish dishes.




Hope you like it.

LSG
