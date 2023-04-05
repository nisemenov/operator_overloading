# Operator overloading

Write a class `Snow` according to the following description:

1. In the class constructor, a field containing the number of snowflakes as an integer is initiated.
2. The class includes methods for overloading arithmetic operators: `add()` - addition, `sub()` - subtraction, `mul()` - multiplication, `truediv()` - division. The code of these methods in the class should perform an increase or decrease in the number of snowflakes by a number **n** or by a factor of **n**. The `truediv()` method overloads normal (/) division, not integer (//) division. However, let the method round the value to the nearest integer.
3. The class includes the method `makeSnow()`, which takes the object itself and the number of snowflakes in a row as an argument, and returns a string of the form "\n\n*****...", where the number of snowflakes between '\n' is equal to the passed argument, and the number of rows is calculated based on the total number of snowflakes.
4. Calling an object of the Snow class in function notation with one argument should lead to rewriting the value of the field that stores the number of snowflakes to the passed argument value.

---

Task 8 from the course: <https://younglinux.info/oopython/course>
