#!/usr/bin/python3
"""
Define class Base.
"""
import json
import os
import csv
import turtle


class Base:
    """
    Base class to manage id attribute in all
    future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation
        of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all
        attributes already set.
        """
        instance = cls.__new__(cls)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
         Returns a list of instances.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

        if not json_string:
            return []

        json_list = json.loads(json_string)
        instances = [cls.create(**dictionary)
                     for dictionary in json_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.
        """
        from models.rectangle import Rectangle
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif isinstance(obj, Square):
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of objects from a CSV file.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        filename = cls.__name__ + ".csv"
        list_objs = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = Rectangle(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    obj = Square(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                list_objs.append(obj)
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the
        turtle module.
        """
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(10)
        
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
                
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for i in range(4):
                t.forward(square.size)
                t.left(90)
                
        screen.exitonclick()
