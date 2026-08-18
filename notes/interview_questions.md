# Python Interview Questions

## Q1. Difference between "5" + "5" and 5 + 5

### Your Answer
The first "5" + "5" are strings, so it will give "55". But 5 + 5 are integers, so it will add and give 10.

### Professional Answer
"5" + "5" performs string concatenation and returns "55". 5 + 5 performs integer addition and returns 10.

---

## Q2. Why use functions?

### Your Answer
So that we can reuse the same code instead of writing it time and again.

### Professional Answer
Functions improve code reusability, readability, maintainability, and reduce duplication. They also help break large problems into smaller manageable pieces.

---

## Q3. What is the purpose of return?

### Your Answer
Return gives the evaluated value in answer.

### Professional Answer
The return statement sends a value back from a function to the caller and ends the function execution.

### Example

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

Output: 8

---

## Q4. What is if __name__ == "__main__":?

### Your Answer
It runs the code only when the file is executed directly.

### Professional Answer
if __name__ == "__main__": ensures that a block of code executes only when the Python file is run directly and not when it is imported as a module into another file.

Think of it as a gate that separates reusable code from executable code.


## Q5. What is the difference between: = AND == .

= is the assignment operator. It assigns a value to a variable.

== is the equality operator. It compares two values and returns True or False.

## Q6. Difference between list and tuple.

Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.


## Q7.  What is JSON?

JSON (JavaScript Object Notation) is a lightweight, text-based data format used to store and exchange structured data

## Q9. Difference between [] and {}

Your answer:

[] is used for lists and {} is used for dictionary.

Interview answer:

[] creates a list, which is an ordered collection of items accessed by index.

{} creates a dictionary, which stores data as key-value pairs and is accessed using keys.

Example:

skills = ["Python", "SQL"]

student = {
    "name": "Arpana",
    "skill": "Python"
}

## Q10.  When should you use a dictionary instead of a list?

Your answer:

Dictionary is preferred when we have to save data in key value pair.

Interview answer:

A dictionary should be used when data has meaningful labels (keys) and we need fast access to values.

For example, student information is better stored in a dictionary because fields like name, age, and skill have specific meanings.

Example:

student = {
    "name": "Arpana",
    "age": 28,
    "skill": "Python"
}

instead of:

student = ["Arpana", 28, "Python"]

because the dictionary is much easier to read and maintain.

## Q11.  .get() vs []

Your answer:

.get() is used when trying to access possible non existing value as it gives none however student["name"] will raise keyerror

✅ Correct.

Interview-quality version:

dictionary.get(key) returns the value if the key exists; otherwise it returns None (or a default value if provided). Using dictionary["key"] raises a KeyError when the key doesn't exist. Therefore, .get() is safer when the presence of a key is uncertain.

Example:

student = {"name": "Arpana"}

print(student.get("age"))      # None
print(student["age"])          # KeyError

## Q12.  What is JSON?

Your answer:

JSON is text-based file where data can be stored

✅ Partially correct.

Interview-quality version:

JSON (JavaScript Object Notation) is a lightweight text-based format used to store and exchange structured data. It is widely used by APIs, web applications, databases, and AI services because it is easy for both humans and machines to read.

Example:

{
  "name": "Arpana",
  "skill": "Python"
}

Important point:

JSON is not just a file format.

It is also a data exchange format.

When you call OpenAI, Gemini, or most APIs, data is sent and received as JSON.

## Q13.  students[0]["skills"][1]

Your answer:

it will go to student then go to its 0th index then go to skills and print the skill in 1st index

✅ Correct.

Interview-quality version:

students[0]["skills"][1] accesses the first student in the list (students[0]), then accesses the skills list inside that student dictionary, and finally returns the second skill ([1]) because list indexing starts at 0.

For:

students = [
    {
        "name": "Arpana",
        "skills": ["Python", "SQL"]
    }
]

it returns:

"SQL"

## Q14.json.load() vs json.loads()

Your answer:

loads is used if the data in file is string as it loads a string and load is used to load a file into python object

✅ Correct.

Interview-quality version:

json.load(file) reads JSON directly from a file object and converts it into a Python object.

json.loads(string) reads JSON from a string and converts it into a Python object.

Example:

with open("student.json") as file:
    data = json.load(file)

vs

json_text = '{"name": "Arpana"}'

data = json.loads(json_text)

## Q15.Why use with open()?

Your answer:

it automatically close file when exited the block

✅ Perfect.

Interview-quality version:

with open() automatically closes the file even if an exception occurs. This prevents resource leaks and is considered the professional way to handle files in Python.

## Q16. What is CSV?

Your answer:

CSV is used to store data and it is easy to read.

✅ Correct but incomplete.

Interview-quality version:

CSV (Comma-Separated Values) is a simple text format used to store tabular data.

Companies use CSV files to exchange data between systems, store reports, export database records, and work with datasets for analytics and machine learning.

Example:

name,age,skill
Arpana,26,Python
John,30,Java

This is important because most beginner data science projects start with CSV datasets.

## Q17.What does json.dump() do?

Your answer:

transfer data to file

✅ Correct.

Interview-quality version:

json.dump() converts a Python object into JSON format and writes it to a file.

Example:

student = {"name": "Arpana"}

json.dump(student, file)

## Q18.Why save data to a file?

Your answer:

In bigger projects that continue months, it won't be possible to get data from scratch every time.

✅ Excellent reasoning.

That's the real answer.

Interview-quality version:

Saving data to a file provides persistence. Data remains available after the program closes and can be reused later.

For example, a student management system saves student records so they don't disappear when the application is restarted.

## Q19 Why Pandas Matters

Without Pandas:

sales = [
    {"product": "Laptop", "price": 50000},
    {"product": "Phone", "price": 30000}
]

To calculate totals, averages, filtering, grouping, etc., you write lots of loops.

With Pandas:

df["price"].sum()

One line.

This is why companies use Pandas.

## Q20. What is the difference between df["column"] and df[["column"]]?

Answer:

df["column"] returns a Pandas Series (1-dimensional), while df[["column"]] returns a Pandas DataFrame (2-dimensional). Single brackets select a single column as a Series, whereas double brackets treat the column name as a list of columns and therefore return a DataFrame, even if only one column is selected.

Example
type(df["name"])
# pandas.Series


type(df[["name"]])
# pandas.DataFrame

This distinction is important because Series and DataFrames support different operations and have different shapes.

## Q21. What is the difference between: type(data) and type(data["price"]) What types do they return?

Your answer:

type(data["price"]) will return Series and type(data) will return DataFrame

✅ Correct.

A DataFrame is basically a table.

A Series is basically a single column.

Example:

data["price"]

returns:

0    50000
1    30000
2    20000

which is a Pandas Series.

## Q22. What does: data.shape return for your sales dataset?

Your answer:

data.shape will return the shape of data like (3,3)

✅ Correct.

More precisely:

(rows, columns)

For your dataset:

print(data.shape)

should return:

(5, 3)

because:

5 rows
3 columns

After adding:

data["revenue"]

it becomes:

(5, 4)

## Q23. What is the difference between: data["price"] and data[["price"]]

Your answer:

data["price"] returns Series while data[["price"]] returns DataFrame

✅ Perfect.

This distinction is asked surprisingly often in Pandas interviews.

## Q24. Why is this powerful? data["revenue"] = data["price"] * data["quantity"] compared to writing a loop?

Your answer:

because this solves calculation without being messy and takes less time

✅ Correct.

The more professional explanation:

Pandas performs vectorized operations on entire columns at once, making code shorter, faster, and easier to read than manually looping through rows.

## Q25. What does:  df.isnull().sum() do?

Your answer:

df.isnull().sum() gives the total null values in each column

✅ Correct.

Better interview answer:

df.isnull().sum() checks every column for missing values (NaN) and returns the count of missing values in each column.

## Q26. Why remove duplicates?

Duplicates are removed because they can distort analysis, statistics, and machine learning models. For example, duplicate sales records could incorrectly increase revenue calculations.

## Q27. Difference between: fillna() and dropna()

Your answer:

fillna() fill the missing value while dropna() remove that

✅ Correct.

Better interview answer:

fillna() replaces missing values with a specified value (such as mean, median, or "Unknown"), while dropna() removes rows or columns containing missing values.

## Q28. What does: sort_values() do?

Your answer:

it sort data in ascending or decending ording by passing ascending = False or True

✅ Correct.

Better interview answer:

sort_values() sorts a DataFrame by one or more columns in ascending or descending order.

Example:

df.sort_values(by="salary", ascending=False)

sorts employees from highest salary to lowest salary.

## Q29. Why is data cleaning important before machine learning?

Your answer:

Raw data can contain missing values or duplicates records or inconsistent data which can impact on predictions or business decision. To prevent this data cleaning is important.

Score: 8.5/10

Improved Interview Version

Data cleaning is important because raw data often contains missing values, duplicate records, incorrect entries, and inconsistent formats. These issues can lead to inaccurate analysis, poor machine learning model performance, and incorrect business decisions. Cleaning data improves data quality and helps ensure reliable predictions and insights.

## Q30. 

