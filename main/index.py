import pickle
import random
import tkinter as tk
from re import search
from tkinter import *

import nltk
from PIL import ImageTk, Image

from main.service.impl.CarServiceImpl import CarServiceImpl
from main.service.impl.ContactDetailServiceImpl import ContactDetailServiceImpl

nltk.download("punkt")
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import json

with open("intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = list(out_empty)[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


root = tk.Tk()

root.title("Lambo ChatBot")

root.geometry('400x450')

img = ImageTk.PhotoImage(Image.open("images/cars2.png"))
pic_label = Label(image=img)
pic_label.place(x=50, y=-50)

chatWindow = Text(root, bd=1, bg='white', width=50, height=8)
chatWindow.place(x=6, y=120, height=270, width=370)

messageWindow = Text(root, bg='white', width=30, height=4)
messageWindow.place(x=128, y=400, height=40, width=260)

chatWindow.config(state="disabled")


def btn_send_click():
    carService = CarServiceImpl()
    contactDetailService = ContactDetailServiceImpl()

    chatWindow.config(state="normal")
    inp = messageWindow.get("1.0", 'end-1c')

    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    if inp == "quit":
        quit()

    if inp == "exit":
        quit()

    if results[results_index] > 0.9:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
    else:
        chatWindow.insert(END, '\n')
        chatWindow.insert(END, "You: " + inp + '\n' + '\n')
        messageWindow.delete(1.0, END)

        chatWindow.insert(END, "Bot:Sorry! I didn't get that,Please try again " + '\n')
        return

    chatWindow.insert(END, '\n')
    chatWindow.insert(END, "You: " + inp + '\n' + '\n')
    messageWindow.delete(1.0, END)

    if tag == "car":
        carDtoList = carService.get_car_details()
        chatWindow.insert(END, "Bot: " + random.choice(responses) + '\n')
        for carDto in carDtoList:
            chatWindow.insert(END, carDto.get_car_name() + '\n')
    elif tag == "contact":
        contactDetailDto = contactDetailService.get_email()
        chatWindow.insert(END, "Bot: " + random.choice(responses) + '\n')
        chatWindow.insert(END,
                          "Contact Number: " + contactDetailDto.get__c_number() + " Email Address: " + contactDetailDto.get__c_email() + '\n')
    elif tag == "color":
        carDtoList = carService.get_car_color()
        chatWindow.insert(END, "Bot: " + random.choice(responses) + '\n')
        for carDto in carDtoList:
            chatWindow.insert(END, carDto.get_color() + '\n')
    elif tag == "brand":
        subStrToyota = "toyota"
        subStrMaruti = "maruti"
        subStrHonda = "honda"
        subStrLambo = "Lamborghini Gallardo"

        if search(subStrToyota, inp.casefold()):
            carDtoList = carService.get_car_by_brand(subStrToyota)
        elif search(subStrMaruti, inp.casefold()):
            carDtoList = carService.get_car_by_brand(subStrMaruti)
        elif search(subStrHonda, inp.casefold()):
            carDtoList = carService.get_car_by_brand(subStrHonda)
        elif search(subStrLambo, inp.casefold()):
            carDtoList = carService.get_car_by_brand(subStrLambo)
        else:
            carDtoList = []

        if len(carDtoList) > 0:
            chatWindow.insert(END, "Bot: " + "Yes, " + random.choice(responses) + '\n')
            for carDto in carDtoList:
                chatWindow.insert(END, carDto.get_car_name() + " / Color : " + carDto.get_color() + '\n')
        else:
            chatWindow.insert(END, "Bot: " + "Sorry!, No cars found!" + '\n')
    elif tag == "price":
        carDtoList = carService.get_car_details()
        chatWindow.insert(END, "Bot: " + random.choice(responses) + '\n')
        for carDto in carDtoList:
            chatWindow.insert(END,
                              carDto.get_car_name() + " Price: " + "LKR " + '{:,}'.format(carDto.get_price()) + '\n')
    else:
        chatWindow.insert(END, "Bot: " + random.choice(responses) + '\n')

    chatWindow.config(state="disabled")


button = Button(root, text='Send', bg='light blue', activebackground='blue', width=12, height=5, command=btn_send_click)
button.place(x=6, y=400, height=40, width=120)

scrollbar = Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=375, y=120, height=270)

root.resizable(False, False)

root.mainloop()
